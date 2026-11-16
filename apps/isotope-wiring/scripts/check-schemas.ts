import * as s from "../src/schemas/index.js";
import { syntheticExample } from "../src/examples/synthetic.js";
function expect(condition: boolean, message: string): void {
  if (!condition) throw new Error(message);
}
const document = syntheticExample();
const edge = document.graph.edges[0];
if (edge === undefined) throw new Error("Fixture requires an edge");
expect(s.DiagramDocumentSchema.safeParse(document).success, "Bundled diagram rejected");
expect(document.isotope === null, "Synthetic geometry must not invent isotope facts");
expect(
  !s.DiagramDocumentSchema.safeParse({ ...document, unexpected: true }).success,
  "Unexpected field accepted",
);
expect(
  !s.DiagramDocumentSchema.safeParse({ ...document, schemaVersion: 2 }).success,
  "Unsupported model version accepted",
);
expect(
  !s.DiagramDocumentSchema.safeParse({ ...document, revision: -1 }).success,
  "Invalid revision accepted",
);
expect(
  !s.DiagramGraphSchema.safeParse({ ...document.graph, edges: [edge, edge] }).success,
  "Duplicate edge accepted",
);
expect(
  !s.DiagramGraphSchema.safeParse({
    ...document.graph,
    vertices: [{ id: edge.from }, { id: edge.from }],
  }).success,
  "Duplicate vertex accepted",
);
expect(
  !s.DiagramGraphSchema.safeParse({ ...document.graph, edges: [{ ...edge, to: "vertex.missing" }] })
    .success,
  "Missing endpoint accepted",
);
expect(
  !s.DiagramGraphSchema.safeParse({
    ...document.graph,
    edges: [{ ...edge, roleId: "role.missing" }],
  }).success,
  "Missing role accepted",
);
expect(
  !s.DiagramGraphSchema.safeParse({
    ...document.graph,
    junctionOrders: [
      {
        vertexId: edge.from,
        status: "specified",
        orientation: "clockwise",
        ends: [{ edgeId: edge.id, end: "to" }],
        review: { status: "unreviewed", questions: [] },
      },
    ],
  }).success,
  "Nonincident junction end accepted",
);
expect(
  !s.DiagramDocumentSchema.safeParse({ ...document, layout: { ...document.layout, vertices: [] } })
    .success,
  "Missing placements accepted",
);
expect(
  !s.DiagramDocumentSchema.safeParse({ ...document, layout: { ...document.layout, edges: [] } })
    .success,
  "Missing edge styles accepted",
);
expect(
  !s.DiagramDocumentSchema.safeParse({
    ...document,
    layout: {
      ...document.layout,
      vertices: [
        ...document.layout.vertices,
        { vertexId: "vertex.missing", position: { x: 0, y: 0 } },
      ],
    },
  }).success,
  "Unknown placement accepted",
);
const alias = {
  edgeId: edge.id,
  number: 8,
  source: "Synthetic alias only",
  review: { status: "unreviewed", questions: [] },
};
expect(
  s.DiagramDocumentSchema.safeParse({
    ...document,
    layout: { ...document.layout, aliases: [alias] },
  }).success,
  "Authored alias rejected",
);
expect(
  !s.DiagramDocumentSchema.safeParse({
    ...document,
    layout: { ...document.layout, aliases: [alias, alias] },
  }).success,
  "Ambiguous alias accepted",
);
const coincident = s.DiagramDocumentSchema.parse({
  ...document,
  layout: {
    ...document.layout,
    vertices: document.layout.vertices.map((value) => ({ ...value, position: { x: 0, y: 0 } })),
  },
});
expect(
  coincident.graph.vertices.length === document.graph.vertices.length &&
    coincident.graph.edges.length === document.graph.edges.length,
  "Coincidence changed identities",
);
expect(
  s.LogicalPointSchema.safeParse({ x: { numerator: 1, denominator: 3 }, y: 0 }).success,
  "Exact rational rejected",
);
expect(
  !s.LogicalPointSchema.safeParse({ x: { numerator: 1, denominator: 0 }, y: 0 }).success,
  "Zero denominator accepted",
);
expect(
  !s.LogicalPointSchema.safeParse({ x: 0.5, y: 0 }).success,
  "Inexact authored coordinate accepted",
);
const isotope = s.IsotopeRecordSchema.parse({
  id: "isotope.hydrogen",
  name: "Hydrogen-1",
  symbol: "H",
  protons: 1,
  neutrons: 0,
  electrons: { status: "unspecified" },
  charge: { status: "unspecified" },
  sources: [],
});
expect(
  !s.IsotopeRecordSchema.safeParse({ ...isotope, neutrons: 1.5 }).success,
  "Fractional count accepted",
);
expect(
  !s.IsotopeRecordSchema.safeParse({ ...isotope, protons: Number.MAX_SAFE_INTEGER, neutrons: 1 })
    .success,
  "Inexact mass number accepted",
);
expect(
  !s.IsotopeRecordSchema.safeParse({
    ...isotope,
    electrons: { status: "specified", value: 1 },
    charge: { status: "specified", value: 1 },
  }).success,
  "Inconsistent charge accepted",
);
expect(
  s.DiagramDocumentSchema.safeParse({ ...document, isotope }).success,
  "Basic isotope facts rejected",
);
expect(
  !s.IsotopeRecordSchema.safeParse({ ...isotope, validation: { status: "validated" } }).success,
  "Removed attestation machinery accepted",
);
expect(
  !s.TraversalPolicySchema.safeParse({ status: "resolved", questions: [] }).success,
  "Invented resolved traversal accepted",
);
expect(
  !s.TraversalPolicySchema.safeParse({ status: "unresolved", questions: [], transitions: [] })
    .success,
  "Empty/pretend traversal policy accepted",
);
const state = s.InspectionStateSchema.parse({
  document,
  selection: { kind: "none" },
  showEdgeLabels: true,
  route: null,
  playback: { elapsedMs: 0, playing: false },
});
const selection = {
  kind: "edge",
  edgeId: edge.id,
  document: { documentId: document.id, revision: document.revision },
};
expect(
  s.InspectionStateSchema.safeParse({ ...state, selection }).success,
  "Valid selection rejected",
);
expect(
  !s.InspectionStateSchema.safeParse({
    ...state,
    selection: { ...selection, edgeId: "edge.missing" },
  }).success,
  "Missing selection accepted",
);
expect(
  !s.InspectionStateSchema.safeParse({
    ...state,
    selection: { ...selection, document: { ...selection.document, revision: 1 } },
  }).success,
  "Stale selection accepted",
);
expect(
  !s.InspectionStateSchema.safeParse({ ...state, document: null, selection }).success,
  "Selection without document accepted",
);
console.log(
  "PASS: diagram/reference integrity, exact layout, basic isotope consistency, selection and unresolved-policy regressions",
);
