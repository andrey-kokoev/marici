import { DiagramDocumentSchema, type DiagramDocument } from "../schemas/document.js";
import {
  SavedEdgeEditsSchema,
  EdgeEditResultSchema,
  type SavedEdgeEdits,
  type EdgeEditResult,
} from "../schemas/edge-edits.js";
import { NamedVersionSchema, type NamedVersion } from "../schemas/named-versions.js";
import { type Selection } from "../schemas/inspection.js";
import { type Turn } from "../schemas/traversal.js";
import { applyEdgeEdits } from "./edge-edits.js";

// Opaque compatibility signature, never decoded as JSON. Editable color/direction
// values and source revisions are deliberately excluded. No graph is reconstructed.
function geometry(document: DiagramDocument): string {
  return JSON.stringify([
    document.id,
    document.graph.vertices,
    document.graph.edges.map((edge) => [edge.id, edge.from, edge.to]),
    document.layout.viewBox,
    document.layout.vertices,
    document.layout.aliases,
    document.layout.edges.map((edge) => [
      edge.edgeId,
      edge.via,
      edge.labelPosition,
      edge.color === "green",
    ]),
  ]);
}
export function captureNamedVersion(
  name: string,
  document: DiagramDocument,
  previous: SavedEdgeEdits,
  selection: Selection,
  initialTurn: Turn,
): NamedVersion {
  if (previous.documentId !== document.id) throw new Error("Wrong edits document");
  const edges = document.graph.edges.flatMap((edge) => {
    const style = document.layout.edges.find((value) => value.edgeId === edge.id);
    if (style === undefined) throw new Error("Missing edge presentation");
    if (style.color === "green") return [];
    if (edge.direction !== "from-to" && edge.direction !== "to-from")
      throw new Error("Unresolved arrow");
    return [
      {
        edgeId: edge.id,
        from: edge.from,
        to: edge.to,
        color: style.color,
        direction: edge.direction,
        nextOperation:
          previous.edges.find((value) => value.edgeId === edge.id)?.nextOperation ?? "color",
      },
    ];
  });
  return NamedVersionSchema.parse({
    name,
    documentId: document.id,
    geometry: geometry(document),
    edits: {
      documentId: document.id,
      version: "2",
      revision: Math.max(previous.revision, edges.length),
      edges,
    },
    startEdge: selection.kind === "edge" ? selection.edgeId : null,
    initialTurn,
  });
}
export function namedVersionContent(snapshot: NamedVersion): string {
  return JSON.stringify([
    snapshot.documentId,
    snapshot.geometry,
    snapshot.startEdge,
    snapshot.initialTurn,
    [...snapshot.edits.edges].sort((a, b) =>
      a.edgeId < b.edgeId ? -1 : a.edgeId > b.edgeId ? 1 : 0,
    ),
  ]);
}
export function restoreNamedVersion(
  document: DiagramDocument,
  previous: SavedEdgeEdits,
  value: NamedVersion,
): EdgeEditResult {
  const snapshot = NamedVersionSchema.parse(value);
  if (
    snapshot.documentId !== document.id ||
    previous.documentId !== document.id ||
    snapshot.geometry !== geometry(document)
  )
    throw new Error("Version no longer matches this diagram");
  const expectedIds = document.layout.edges
    .filter((edge) => edge.color !== "green")
    .map((edge) => edge.edgeId)
    .sort();
  if (
    JSON.stringify(snapshot.edits.edges.map((edge) => edge.edgeId).sort()) !==
    JSON.stringify(expectedIds)
  )
    throw new Error("Incomplete version");
  if (
    snapshot.startEdge !== null &&
    !document.graph.edges.some((edge) => edge.id === snapshot.startEdge)
  )
    throw new Error("Missing start edge");
  const edits = SavedEdgeEditsSchema.parse({
    ...snapshot.edits,
    version: "2",
    startEdge: snapshot.startEdge,
    initialTurn: snapshot.initialTurn,
    revision: Math.max(previous.revision + 1, snapshot.edits.edges.length),
  });
  const restored = applyEdgeEdits(document, edits);
  return EdgeEditResultSchema.parse({
    edits,
    document: DiagramDocumentSchema.parse({
      ...restored,
      revision: document.revision + edits.revision - previous.revision,
    }),
  });
}
