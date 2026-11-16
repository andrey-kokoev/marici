import { DiagramDocumentSchema, type DiagramDocument } from "../schemas/document.js";
import {
  SavedEdgeEditsSchema,
  EdgeEditResultSchema,
  type SavedEdgeEdits,
  type EdgeEditResult,
} from "../schemas/edge-edits.js";

export function emptyEdgeEdits(document: DiagramDocument): SavedEdgeEdits {
  return SavedEdgeEditsSchema.parse({
    version: "2",
    documentId: document.id,
    revision: 0,
    edges: [],
  });
}

/** Restore only color/direction overrides; never replace incidence or geometry. */
export function applyEdgeEdits(base: DiagramDocument, edits: SavedEdgeEdits): DiagramDocument {
  if (edits.documentId !== base.id) throw new Error("Saved edits belong to another diagram");
  for (const edit of edits.edges) {
    const edge = base.graph.edges.find((value) => value.id === edit.edgeId);
    const style = base.layout.edges.find((value) => value.edgeId === edit.edgeId);
    if (edge === undefined || style === undefined || edge.from !== edit.from || edge.to !== edit.to)
      throw new Error("Saved edge identities or endpoints no longer match the diagram");
    if (style.color === "green" || (edge.direction !== "from-to" && edge.direction !== "to-from"))
      throw new Error("Saved edits cannot convert a connector or unresolved edge");
  }
  return DiagramDocumentSchema.parse({
    ...base,
    revision: base.revision + edits.revision,
    graph: {
      ...base.graph,
      edges: base.graph.edges.map((edge) => {
        const edit = edits.edges.find((value) => value.edgeId === edge.id);
        return edit === undefined ? edge : { ...edge, direction: edit.direction };
      }),
    },
    layout: {
      ...base.layout,
      edges: base.layout.edges.map((style) => {
        const edit = edits.edges.find((value) => value.edgeId === style.edgeId);
        return edit === undefined ? style : { ...style, color: edit.color };
      }),
    },
  });
}

/** Each edge independently alternates color, direction, color, direction. */
export function cycleEdgeEdit(
  document: DiagramDocument,
  edits: SavedEdgeEdits,
  edgeId: string,
): EdgeEditResult | null {
  if (edits.documentId !== document.id) throw new Error("Edit state belongs to another diagram");
  const edge = document.graph.edges.find((value) => value.id === edgeId);
  const style = document.layout.edges.find((value) => value.edgeId === edgeId);
  if (
    edge === undefined ||
    style === undefined ||
    style.color === "green" ||
    (edge.direction !== "from-to" && edge.direction !== "to-from")
  )
    return null;
  const operation = edits.edges.find((value) => value.edgeId === edgeId)?.nextOperation ?? "color";
  const color = operation === "color" ? (style.color === "red" ? "blue" : "red") : style.color;
  const direction =
    operation === "direction"
      ? edge.direction === "from-to"
        ? "to-from"
        : "from-to"
      : edge.direction;
  return EdgeEditResultSchema.parse({
    document: {
      ...document,
      revision: document.revision + 1,
      graph: {
        ...document.graph,
        edges: document.graph.edges.map((value) =>
          value.id === edgeId ? { ...value, direction } : value,
        ),
      },
      layout: {
        ...document.layout,
        edges: document.layout.edges.map((value) =>
          value.edgeId === edgeId ? { ...value, color } : value,
        ),
      },
    },
    edits: {
      ...edits,
      revision: edits.revision + 1,
      edges: [
        ...edits.edges.filter((value) => value.edgeId !== edgeId),
        {
          edgeId: edge.id,
          from: edge.from,
          to: edge.to,
          color,
          direction,
          nextOperation: operation === "color" ? "direction" : "color",
        },
      ],
    },
  });
}
