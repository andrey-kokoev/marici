import { neon20 } from "../src/examples/neon20.js";
import { encodeEdgeEdits, decodeEdgeEditsExact } from "../src/edge-edit-storage.js";
import { DiagramDocumentSchema } from "../src/schemas/document.js";
import { SelectionSchema } from "../src/schemas/inspection.js";
import { DocumentIdSchema } from "../src/schemas/primitives.js";
import { NamedVersionSchema, VersionLibrarySchema } from "../src/schemas/named-versions.js";
import {
  captureNamedVersion,
  restoreNamedVersion,
  namedVersionContent,
} from "../src/domain/named-versions.js";
import { cycleEdgeEdit, emptyEdgeEdits } from "../src/domain/edge-edits.js";
import {
  encodeVersionLibrary,
  decodeVersionLibrary,
  saveVersionLibrary,
} from "../src/named-version-storage.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
function rejects(action: () => void, message: string): void {
  let rejected = false;
  try {
    action();
  } catch {
    rejected = true;
  }
  expect(rejected, message);
}
const base = neon20();
const selection = SelectionSchema.parse({
  kind: "edge",
  edgeId: "edge.ne20.8",
  document: { documentId: base.id, revision: base.revision },
});
const first = cycleEdgeEdit(base, emptyEdgeEdits(base), "edge.ne20.4");
if (first === null) throw new Error("Missing first edit");
const snapshot = captureNamedVersion(
  "  Good λ & draft  ",
  first.document,
  first.edits,
  selection,
  "right",
);
expect(
  snapshot.name === "Good λ & draft" &&
    snapshot.edits.edges.length === 16 &&
    snapshot.startEdge === "edge.ne20.8" &&
    snapshot.initialTurn === "right",
  "Snapshot must capture full colored state and start controls",
);
const second = cycleEdgeEdit(first.document, first.edits, "edge.ne20.4");
if (second === null) throw new Error("Missing reversal");
const third = cycleEdgeEdit(second.document, second.edits, "edge.ne20.3");
if (third === null) throw new Error("Missing other edit");
const restored = restoreNamedVersion(third.document, third.edits, snapshot);
expect(
  JSON.stringify(restored.document.graph) === JSON.stringify(first.document.graph) &&
    JSON.stringify(restored.document.layout) === JSON.stringify(first.document.layout),
  "Load must restore the complete snapshot, not merge partial overrides",
);
expect(
  restored.document.revision > third.document.revision,
  "Load must invalidate the old snapshot revision",
);
expect(
  namedVersionContent(snapshot) ===
    namedVersionContent(
      captureNamedVersion("Different name", restored.document, restored.edits, selection, "right"),
    ),
  "Dirty comparison must ignore snapshot name and revision",
);
for (const changed of [
  NamedVersionSchema.parse({ ...snapshot, initialTurn: "left" }),
  NamedVersionSchema.parse({ ...snapshot, startEdge: "edge.ne20.3" }),
  NamedVersionSchema.parse({
    ...snapshot,
    edits: {
      ...snapshot.edits,
      edges: snapshot.edits.edges.map((edge) =>
        edge.edgeId === "edge.ne20.4" ? { ...edge, nextOperation: "color" } : edge,
      ),
    },
  }),
])
  expect(
    namedVersionContent(changed) !== namedVersionContent(snapshot),
    "Dirty comparison must include controls and click phase",
  );
const persistedWorkingCopy = decodeEdgeEditsExact(encodeEdgeEdits(restored.edits));
expect(
  persistedWorkingCopy.startEdge === "edge.ne20.8" && persistedWorkingCopy.initialTurn === "right",
  "Restored working-copy controls must persist atomically with its colors and arrows",
);
const nextClick = cycleEdgeEdit(restored.document, restored.edits, "edge.ne20.4");
if (nextClick === null) throw new Error("Missing restored edit");
expect(
  nextClick.document.graph.edges.find((edge) => edge.id === "edge.ne20.4")?.direction ===
    "to-from" &&
    nextClick.document.layout.edges.find((edge) => edge.edgeId === "edge.ne20.4")?.color === "blue",
  "Saved next-operation state must be restored",
);
const library = VersionLibrarySchema.parse({
  format: "1",
  documentId: base.id,
  entries: [snapshot],
});
const encoded = encodeVersionLibrary(library);
expect(
  encodeVersionLibrary(decodeVersionLibrary(encoded, base.id)) === encoded,
  "Version library codec must round-trip names and complete snapshots",
);
expect(decodeVersionLibrary(null, base.id).entries.length === 0, "Absent library must be empty");
rejects(
  () =>
    VersionLibrarySchema.parse({
      ...library,
      entries: [snapshot, { ...snapshot, name: snapshot.name.toUpperCase() }],
    }),
  "Case-insensitive duplicate names must be rejected",
);
rejects(
  () => captureNamedVersion("   ", base, emptyEdgeEdits(base), selection, "left"),
  "Blank names accepted",
);
for (const raw of ["corrupt", encoded + "&format=1", encoded.replace("format=1", "format=99")])
  rejects(() => decodeVersionLibrary(raw, base.id), "Malformed library accepted");
rejects(
  () => decodeVersionLibrary(encoded, DocumentIdSchema.parse("diagram.other")),
  "Cross-diagram library accepted",
);
rejects(
  () =>
    restoreNamedVersion(
      third.document,
      third.edits,
      NamedVersionSchema.parse({ ...snapshot, geometry: "wrong" }),
    ),
  "Incompatible geometry accepted",
);
rejects(
  () =>
    restoreNamedVersion(
      third.document,
      third.edits,
      NamedVersionSchema.parse({
        ...snapshot,
        edits: { ...snapshot.edits, edges: snapshot.edits.edges.slice(1) },
      }),
    ),
  "Partial snapshot accepted",
);
const moved = DiagramDocumentSchema.parse({
  ...third.document,
  layout: { ...third.document.layout, viewBox: { ...third.document.layout.viewBox, x: -151 } },
});
rejects(() => restoreNamedVersion(moved, third.edits, snapshot), "Changed geometry accepted");
// Snapshot decoding must not run live-edit color migrations, even for older envelopes.
const exact = VersionLibrarySchema.parse({
  ...library,
  entries: [{ ...snapshot, edits: { ...snapshot.edits, version: "3" } }],
});
expect(
  decodeVersionLibrary(encodeVersionLibrary(exact), base.id).entries[0]?.edits.edges.find(
    (edge) => edge.edgeId === "edge.ne20.4",
  )?.color === "blue",
  "Named snapshots must not be recolored by live-edit migrations",
);
let raw: string | null = null;
let fail = false;
const storage: Pick<Storage, "getItem" | "setItem"> = {
  getItem() {
    return raw;
  },
  setItem(_key, value) {
    if (fail) throw new Error("Quota");
    raw = value;
  },
};
saveVersionLibrary(storage, null, library);
expect(raw === encoded, "Library not persisted");
rejects(() => saveVersionLibrary(storage, null, library), "Stale library write accepted");
fail = true;
rejects(
  () =>
    saveVersionLibrary(storage, encoded, VersionLibrarySchema.parse({ ...library, entries: [] })),
  "Write failure swallowed",
);
expect(raw === encoded, "Failed write altered the library");
expect(
  snapshot.edits.edges.find((edge) => edge.edgeId === "edge.ne20.4")?.direction === "from-to",
  "Restoring/editing mutated the saved snapshot",
);
console.log(
  "PASS: named versions capture/restore, exact codec, click phases, controls, compatibility, duplicates, stale writes and storage errors",
);
