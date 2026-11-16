import { z } from "zod";
import { CountSchema } from "./schemas/primitives.js";
import { SavedEdgeEditsSchema, type SavedEdgeEdits } from "./schemas/edge-edits.js";
import { type DiagramDocument } from "./schemas/document.js";
import { emptyEdgeEdits } from "./domain/edge-edits.js";

export const EDGE_EDITS_PREFIX = "isotope-wiring:edge-edits:v1:";
const RevisionTextSchema = z
  .string()
  .regex(/^(0|[1-9][0-9]*)$/)
  .transform(Number)
  .pipe(CountSchema);
function one(params: URLSearchParams, key: string): string {
  const values = params.getAll(key);
  const value = values[0];
  if (values.length !== 1 || value === undefined)
    throw new Error("Missing or duplicate saved-edit field");
  return value;
}
function fields(params: URLSearchParams, allowed: string[]): void {
  if ([...params.keys()].some((key) => !allowed.includes(key)))
    throw new Error("Unexpected saved-edit field");
}
// Native URLSearchParams is the text codec; all decoded values then cross Zod schemas.
// No unchecked JSON.parse or hand-written JSON parser is introduced.
export function encodeEdgeEdits(value: SavedEdgeEdits): string {
  const edits = SavedEdgeEditsSchema.parse(value);
  const params = new URLSearchParams({
    version: edits.version,
    documentId: edits.documentId,
    revision: String(edits.revision),
  });
  if (edits.startEdge !== undefined) params.set("startEdge", edits.startEdge ?? "");
  if (edits.initialTurn !== undefined) params.set("initialTurn", edits.initialTurn);
  for (const edge of [...edits.edges].sort((a, b) =>
    a.edgeId < b.edgeId ? -1 : a.edgeId > b.edgeId ? 1 : 0,
  )) {
    params.append(
      "edge",
      new URLSearchParams({
        edgeId: edge.edgeId,
        from: edge.from,
        to: edge.to,
        color: edge.color,
        direction: edge.direction,
        nextOperation: edge.nextOperation,
      }).toString(),
    );
  }
  return params.toString();
}
export function decodeEdgeEditsExact(raw: string): SavedEdgeEdits {
  const params = new URLSearchParams(raw);
  fields(params, ["version", "documentId", "revision", "edge", "startEdge", "initialTurn"]);
  return SavedEdgeEditsSchema.parse({
    version: one(params, "version"),
    documentId: one(params, "documentId"),
    revision: RevisionTextSchema.parse(one(params, "revision")),
    ...(params.has("startEdge") ? { startEdge: one(params, "startEdge") || null } : {}),
    ...(params.has("initialTurn") ? { initialTurn: one(params, "initialTurn") } : {}),
    edges: params.getAll("edge").map((rawEdge) => {
      const edge = new URLSearchParams(rawEdge);
      fields(edge, ["edgeId", "from", "to", "color", "direction", "nextOperation"]);
      return {
        edgeId: one(edge, "edgeId"),
        from: one(edge, "from"),
        to: one(edge, "to"),
        color: one(edge, "color"),
        direction: one(edge, "direction"),
        nextOperation: one(edge, "nextOperation"),
      };
    }),
  });
}
export function decodeEdgeEdits(raw: string): SavedEdgeEdits {
  const saved = decodeEdgeEditsExact(raw);
  // Retire duplicate 5; retain the earlier v1 correction. V3 was the rejected
  // three-pair swap: restore its six colors to the verified 28-step configuration.
  // Ordinary v2 overrides remain untouched, including all arrow directions.
  if (saved.documentId !== "diagram.ne20") return saved;
  return SavedEdgeEditsSchema.parse({
    ...saved,
    version: "2",
    edges: saved.edges
      .filter((edge) => edge.edgeId !== "edge.ne20.5")
      .map((edge) => {
        if (saved.version === "3") {
          if (["edge.ne20.4", "edge.ne20.13", "edge.ne20.19"].includes(edge.edgeId))
            return { ...edge, color: "red" };
          if (["edge.ne20.16", "edge.ne20.18", "edge.ne20.20"].includes(edge.edgeId))
            return { ...edge, color: "blue" };
          return edge;
        }
        if (saved.version !== "1") return edge;
        if (edge.edgeId === "edge.ne20.13" || edge.edgeId === "edge.ne20.14")
          return { ...edge, color: "blue" };
        if (edge.edgeId === "edge.ne20.16" || edge.edgeId === "edge.ne20.20")
          return { ...edge, color: "red" };
        return edge;
      }),
  });
}
export function readEdgeEdits(
  storage: Pick<Storage, "getItem">,
  base: DiagramDocument,
): SavedEdgeEdits {
  const raw = storage.getItem(EDGE_EDITS_PREFIX + base.id);
  return raw === null ? emptyEdgeEdits(base) : decodeEdgeEdits(raw);
}
export function saveEdgeEdits(
  storage: Pick<Storage, "getItem" | "setItem">,
  previous: SavedEdgeEdits,
  next: SavedEdgeEdits,
): void {
  if (previous.documentId !== next.documentId) throw new Error("Mismatched edit document");
  const key = EDGE_EDITS_PREFIX + next.documentId;
  const raw = storage.getItem(key);
  if (
    raw === null
      ? previous.revision !== 0
      : encodeEdgeEdits(decodeEdgeEdits(raw)) !== encodeEdgeEdits(previous)
  )
    throw new Error("Saved edits changed elsewhere; reload before editing");
  // Commit storage first. If setItem throws, the caller must retain its old model.
  storage.setItem(key, encodeEdgeEdits(next));
}
