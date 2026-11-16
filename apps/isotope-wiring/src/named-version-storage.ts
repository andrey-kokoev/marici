import { VersionLibrarySchema, type VersionLibrary } from "./schemas/named-versions.js";
import { type DiagramDocument } from "./schemas/document.js";
import { encodeEdgeEdits, decodeEdgeEditsExact } from "./edge-edit-storage.js";

export const VERSION_LIBRARY_PREFIX = "isotope-wiring:named-versions:v1:";
function one(params: URLSearchParams, key: string): string {
  const values = params.getAll(key),
    value = values[0];
  if (values.length !== 1 || value === undefined)
    throw new Error("Missing or duplicate version field");
  return value;
}
function fields(params: URLSearchParams, allowed: string[]): void {
  if ([...params.keys()].some((key) => !allowed.includes(key)))
    throw new Error("Unexpected version field");
}
export function encodeVersionLibrary(value: VersionLibrary): string {
  const library = VersionLibrarySchema.parse(value);
  const params = new URLSearchParams({ format: library.format, documentId: library.documentId });
  for (const entry of library.entries)
    params.append(
      "entry",
      new URLSearchParams({
        name: entry.name,
        documentId: entry.documentId,
        geometry: entry.geometry,
        edits: encodeEdgeEdits(entry.edits),
        startEdge: entry.startEdge ?? "",
        initialTurn: entry.initialTurn,
      }).toString(),
    );
  return params.toString();
}
export function decodeVersionLibrary(
  raw: string | null,
  documentId: DiagramDocument["id"],
): VersionLibrary {
  if (raw === null) return VersionLibrarySchema.parse({ format: "1", documentId, entries: [] });
  const params = new URLSearchParams(raw);
  fields(params, ["format", "documentId", "entry"]);
  const library = VersionLibrarySchema.parse({
    format: one(params, "format"),
    documentId: one(params, "documentId"),
    entries: params.getAll("entry").map((rawEntry) => {
      const entry = new URLSearchParams(rawEntry);
      fields(entry, ["name", "documentId", "geometry", "edits", "startEdge", "initialTurn"]);
      return {
        name: one(entry, "name"),
        documentId: one(entry, "documentId"),
        geometry: one(entry, "geometry"),
        edits: decodeEdgeEditsExact(one(entry, "edits")),
        startEdge: one(entry, "startEdge") || null,
        initialTurn: one(entry, "initialTurn"),
      };
    }),
  });
  if (library.documentId !== documentId) throw new Error("Wrong version library");
  return library;
}
export function saveVersionLibrary(
  storage: Pick<Storage, "getItem" | "setItem">,
  expectedRaw: string | null,
  library: VersionLibrary,
): void {
  const encoded = encodeVersionLibrary(library);
  const key = VERSION_LIBRARY_PREFIX + library.documentId;
  if (storage.getItem(key) !== expectedRaw) throw new Error("Version library changed elsewhere");
  storage.setItem(key, encoded);
}
