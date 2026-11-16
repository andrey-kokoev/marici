import { neon20 } from "../src/examples/neon20.js";
import { traceRoute } from "../src/domain/route.js";
import { inspectColorBalance } from "../src/domain/color-balance.js";
import { RouteResultSchema } from "../src/schemas/traversal.js";
import { emptyEdgeEdits, cycleEdgeEdit, applyEdgeEdits } from "../src/domain/edge-edits.js";
import { SavedEdgeEditsSchema } from "../src/schemas/edge-edits.js";
import {
  encodeEdgeEdits,
  decodeEdgeEdits,
  readEdgeEdits,
  saveEdgeEdits,
  EDGE_EDITS_PREFIX,
} from "../src/edge-edit-storage.js";
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
const base = neon20(),
  original = JSON.stringify(base);
let document = base,
  edits = emptyEdgeEdits(base);
const values = new Map<string, string>();
let rejectWrites = false;
const storage: Pick<Storage, "getItem" | "setItem"> = {
  getItem(key) {
    return values.get(key) ?? null;
  },
  setItem(key, value) {
    if (rejectWrites) throw new Error("Quota denied");
    values.set(key, value);
  },
};
expect(readEdgeEdits(storage, base).edges.length === 0, "Missing storage must mean no overrides");
for (let i = 0; i < 4; i += 1) {
  const result = cycleEdgeEdit(document, edits, "edge.ne20.4");
  if (result === null) throw new Error("Editable edge rejected");
  const edge = result.document.graph.edges.find((value) => value.id === "edge.ne20.4");
  const style = result.document.layout.edges.find((value) => value.edgeId === "edge.ne20.4");
  expect(style?.color === (i < 2 ? "blue" : "red"), "Color/direction operations must alternate");
  expect(
    edge?.direction === (i === 1 || i === 2 ? "to-from" : "from-to"),
    "Direction operation is out of sequence",
  );
  expect(
    result.document.revision === base.revision + i + 1,
    "Edits must advance the document snapshot",
  );
  saveEdgeEdits(storage, edits, result.edits);
  edits = readEdgeEdits(storage, base);
  document = applyEdgeEdits(base, edits);
  expect(
    JSON.stringify(document) === JSON.stringify(result.document),
    "Reload must reproduce the same model and click phase",
  );
  expect(
    encodeEdgeEdits(decodeEdgeEdits(encodeEdgeEdits(edits))) === encodeEdgeEdits(edits),
    "Storage codec must round-trip",
  );
}
expect(
  JSON.stringify(document.graph) === JSON.stringify(base.graph) &&
    JSON.stringify(document.layout) === JSON.stringify(base.layout),
  "Four clicks must restore the initial colors/directions without rewiring",
);
expect(JSON.stringify(base) === original, "Edits mutated the authored base");
const changed = cycleEdgeEdit(base, emptyEdgeEdits(base), "edge.ne20.4");
if (changed === null) throw new Error("Missing edit");
const independent = cycleEdgeEdit(changed.document, changed.edits, "edge.ne20.2");
if (independent === null) throw new Error("Missing second edit");
expect(
  independent.document.layout.edges.find((edge) => edge.edgeId === "edge.ne20.2")?.color ===
    "red" &&
    independent.document.graph.edges.find((edge) => edge.id === "edge.ne20.2")?.direction ===
      "from-to",
  "Each edge must independently start with color, including initially blue edges",
);
expect(
  independent.edits.edges.every((edge) => edge.nextOperation === "direction"),
  "Per-edge next operations must remain independent",
);
for (const edge of independent.document.graph.edges) {
  const old = base.graph.edges.find((value) => value.id === edge.id);
  expect(old?.from === edge.from && old.to === edge.to, "Editing rewired an endpoint");
}
expect(
  JSON.stringify(independent.document.layout.vertices) === JSON.stringify(base.layout.vertices) &&
    JSON.stringify(independent.document.layout.aliases) === JSON.stringify(base.layout.aliases),
  "Editing moved geometry or changed labels",
);
expect(
  cycleEdgeEdit(base, emptyEdgeEdits(base), "edge.ne20.6") === null &&
    cycleEdgeEdit(base, emptyEdgeEdits(base), "edge.missing") === null,
  "Connectors/missing IDs must not be edited",
);
rejects(
  () => saveEdgeEdits(storage, emptyEdgeEdits(base), changed.edits),
  "Stale editor overwrote newer saved edits",
);
const beforeFailure = values.get(EDGE_EDITS_PREFIX + base.id);
rejectWrites = true;
const next = cycleEdgeEdit(document, edits, "edge.ne20.4");
if (next === null) throw new Error("Missing next edit");
rejects(() => saveEdgeEdits(storage, edits, next.edits), "Write failure was hidden");
expect(
  values.get(EDGE_EDITS_PREFIX + base.id) === beforeFailure,
  "Failed save altered persisted state",
);
rejects(
  () =>
    readEdgeEdits(
      {
        getItem() {
          throw new Error("Security denied");
        },
      },
      base,
    ),
  "Read failure was hidden",
);
for (const raw of [
  "broken",
  encodeEdgeEdits(edits) + "&version=1",
  encodeEdgeEdits(edits) + "&extra=1",
  encodeEdgeEdits(edits).replace("version=2", "version=99"),
])
  rejects(() => decodeEdgeEdits(raw), "Malformed storage accepted");
const first = changed.edits.edges[0];
if (first === undefined) throw new Error("Missing saved edit");
rejects(
  () => SavedEdgeEditsSchema.parse({ ...changed.edits, revision: 2, edges: [first, first] }),
  "Duplicate overrides accepted",
);
rejects(
  () =>
    applyEdgeEdits(
      base,
      SavedEdgeEditsSchema.parse({
        ...changed.edits,
        edges: [{ ...first, from: "vertex.missing" }],
      }),
    ),
  "Changed endpoint identity was silently accepted",
);
rejects(
  () =>
    applyEdgeEdits(
      base,
      SavedEdgeEditsSchema.parse({
        ...changed.edits,
        edges: [
          {
            ...first,
            edgeId: "edge.ne20.6",
            from: "vertex.bottom-left",
            to: "vertex.bottom-right",
          },
        ],
      }),
    ),
  "Storage converted a green connector",
);
const legacy = SavedEdgeEditsSchema.parse({
  ...changed.edits,
  revision: 3,
  edges: [
    ...changed.edits.edges,
    {
      edgeId: "edge.ne20.5",
      from: "vertex.bottom-left",
      to: "vertex.center",
      color: "red",
      direction: "from-to",
      nextOperation: "direction",
    },
    {
      edgeId: "edge.ne20.18",
      from: "vertex.bottom-left",
      to: "vertex.center",
      color: "red",
      direction: "from-to",
      nextOperation: "direction",
    },
  ],
});
rejectWrites = false;
values.set(EDGE_EDITS_PREFIX + base.id, encodeEdgeEdits(legacy));
const migrated = readEdgeEdits(storage, base);
const restored = applyEdgeEdits(base, migrated);
expect(
  !restored.graph.edges.some((edge) => edge.id === "edge.ne20.5") &&
    restored.layout.edges.find((edge) => edge.edgeId === "edge.ne20.18")?.color === "red",
  "Retiring duplicate 5 must preserve saved edge 18 edits",
);
const continued = cycleEdgeEdit(restored, migrated, "edge.ne20.18");
if (continued === null) throw new Error("Surviving edge not editable");
expect(
  continued.document.graph.edges.find((edge) => edge.id === "edge.ne20.18")?.direction ===
    "to-from",
  "Migration lost edge 18 next-operation state",
);
saveEdgeEdits(storage, migrated, continued.edits);
expect(
  !values.get(EDGE_EDITS_PREFIX + base.id)?.includes("edge.ne20.5"),
  "Next save must retire only duplicate 5",
);
// Reconstruct the operator's saved closed path, then apply the approved swap.
const operatorReds = [8, 10, 1, 21, 15, 4, 19, 13, 14];
const reversed = [1, 4, 15, 14, 2, 18, 3];
const operatorSaved = SavedEdgeEditsSchema.parse({
  version: "1",
  documentId: base.id,
  revision: 16,
  edges: base.graph.edges
    .filter(
      (edge) => base.layout.edges.find((style) => style.edgeId === edge.id)?.color !== "green",
    )
    .map((edge) => {
      const number = base.layout.aliases.find((alias) => alias.edgeId === edge.id)?.number;
      if (number === undefined) throw new Error("Missing fixture label");
      return {
        edgeId: edge.id,
        from: edge.from,
        to: edge.to,
        color: operatorReds.includes(number) ? "red" : "blue",
        direction: reversed.includes(number) ? "to-from" : "from-to",
        nextOperation: "color",
      };
    }),
});
const beforeSwap = applyEdgeEdits(base, operatorSaved);
const unbalancedClosed = traceRoute(beforeSwap, "edge.ne20.8");
expect(
  unbalancedClosed.status === "invalid-color-balance" &&
    unbalancedClosed.remainingColoredEdges.length === 0 &&
    unbalancedClosed.steps.at(-1)?.to === unbalancedClosed.steps[0]?.from,
  "A closed traversal covering every colored edge is still invalid with unequal counts",
);
values.set(EDGE_EDITS_PREFIX + base.id, encodeEdgeEdits(operatorSaved));
const approved = readEdgeEdits(storage, base);
const afterSwap = applyEdgeEdits(base, approved);
const approvedRoute = traceRoute(afterSwap, "edge.ne20.8");
expect(
  approvedRoute.colorBalance.red === 9 &&
    approvedRoute.colorBalance.blue === 7 &&
    !approvedRoute.colorBalance.balanced &&
    approved.edges
      .filter((edge) => ["edge.ne20.13", "edge.ne20.14"].includes(edge.edgeId))
      .every((edge) => edge.color === "blue") &&
    approved.edges
      .filter((edge) => ["edge.ne20.16", "edge.ne20.20"].includes(edge.edgeId))
      .every((edge) => edge.color === "red"),
  "Swap migration must apply the four approved colors and preserve the imbalance diagnostic",
);
expect(
  JSON.stringify(beforeSwap.graph) === JSON.stringify(afterSwap.graph) &&
    approved.edges.every((edge) => edge.nextOperation === "color") &&
    approved.version === "2",
  "Swap migration must preserve arrows, topology and click phases",
);
expect(
  !RouteResultSchema.safeParse({ ...approvedRoute, status: "completed" }).success,
  "Result validation must reject a false completion for unequal color counts",
);
const repaired = cycleEdgeEdit(afterSwap, approved, "edge.ne20.4");
if (repaired === null) throw new Error("Missing balancing edit");
expect(
  inspectColorBalance(repaired.document).balanced &&
    inspectColorBalance(repaired.document).red === 8 &&
    inspectColorBalance(repaired.document).blue === 8,
  "Single-edge editing must remain available to repair an invalid draft",
);
const laterEdit = cycleEdgeEdit(afterSwap, approved, "edge.ne20.13");
if (laterEdit === null) throw new Error("Migrated edge not editable");
saveEdgeEdits(storage, approved, laterEdit.edits);
expect(
  readEdgeEdits(storage, base).edges.find((edge) => edge.edgeId === "edge.ne20.13")?.color ===
    "red",
  "Migration must run only once, never overwrite later color edits",
);
// The rejected v3 swap must roll back without touching ordinary v2 saves.
const currentSaved = SavedEdgeEditsSchema.parse({
  ...operatorSaved,
  version: "2",
  edges: operatorSaved.edges.map((edge) => ({
    ...edge,
    color: [8, 10, 3, 21, 15, 4, 19, 13].some((n) => edge.edgeId === `edge.ne20.${n}`)
      ? "red"
      : "blue",
    direction: [4, 14, 15].some((n) => edge.edgeId === `edge.ne20.${n}`) ? "to-from" : "from-to",
  })),
});
const currentRoute = traceRoute(applyEdgeEdits(base, currentSaved), "edge.ne20.8");
expect(
  currentRoute.status === "completed" && currentRoute.steps.length === 28,
  "The latest migration fixture must reproduce the verified balanced starting configuration",
);
expect(
  encodeEdgeEdits(decodeEdgeEdits(encodeEdgeEdits(currentSaved))) === encodeEdgeEdits(currentSaved),
  "Rollback must not change an existing v2 configuration",
);
const rejectedSwap = SavedEdgeEditsSchema.parse({
  ...currentSaved,
  version: "3",
  edges: currentSaved.edges.map((edge) => ({
    ...edge,
    color: [4, 13, 19].some((n) => edge.edgeId === `edge.ne20.${n}`)
      ? "blue"
      : [16, 18, 20].some((n) => edge.edgeId === `edge.ne20.${n}`)
        ? "red"
        : edge.color,
  })),
});
values.set(EDGE_EDITS_PREFIX + base.id, encodeEdgeEdits(rejectedSwap));
const threePair = readEdgeEdits(storage, base);
const threePairModel = applyEdgeEdits(base, threePair);
const shortest = traceRoute(threePairModel, "edge.ne20.8");
expect(
  shortest.status === "completed" &&
    shortest.colorBalance.red === 8 &&
    shortest.colorBalance.blue === 8 &&
    shortest.steps.at(-1)?.to === shortest.steps[0]?.from &&
    shortest.steps.map((step) => step.edgeId.replace("edge.ne20.", "")).join(",") ===
      "8,12,10,3,7,21,25,15,6,4,26,19,7,17,6,13,14,18,2,22,20,26,25,16,1,11,12,9",
  "Rollback must restore the verified balanced 28-step closed route",
);
expect(
  threePair.edges.every((edge) => {
    const before = currentSaved.edges.find((old) => old.edgeId === edge.edgeId);
    return before?.direction === edge.direction && before.nextOperation === edge.nextOperation;
  }),
  "Three-pair migration changed arrows or click phases",
);
const manualAfterSwap = cycleEdgeEdit(threePairModel, threePair, "edge.ne20.4");
if (manualAfterSwap === null) throw new Error("Migrated edge not editable");
saveEdgeEdits(storage, threePair, manualAfterSwap.edits);
expect(
  readEdgeEdits(storage, base).edges.find((edge) => edge.edgeId === "edge.ne20.4")?.color ===
    "blue",
  "Rollback must never overwrite subsequent manual changes",
);
console.log(
  "PASS: persisted edge cycles, reload, independent phases, unchanged incidence/geometry, invalid storage, stale editors and storage failures",
);
