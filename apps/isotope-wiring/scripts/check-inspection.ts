import { createPinia, setActivePinia } from "pinia";
import { useInspection } from "../src/vue/stores/inspection.js";
import { useDiagramInspection } from "../src/vue/useDiagramInspection.js";
import { projectDiagram, midpoint, midpointAngle } from "../src/presentation/diagram.js";
import { DiagramDocumentSchema } from "../src/schemas/document.js";
import { SelectionSchema } from "../src/schemas/inspection.js";
import { neon20 } from "../src/examples/neon20.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
setActivePinia(createPinia());
const store = useInspection();
expect(store.state.document?.id === "diagram.ne20", "Ne-20 should be visible on first open");
store.loadExample();
const original = JSON.stringify(store.state.document);
const doc = DiagramDocumentSchema.parse(store.activeDocument);
const projection = projectDiagram(doc);
expect(
  projection.edges.length === 3 && projection.vertices.length === 5,
  "Crossing/coincident identities merged",
);
const reordered = projectDiagram(
  DiagramDocumentSchema.parse({
    ...doc,
    graph: {
      ...doc.graph,
      edges: [...doc.graph.edges].reverse(),
      vertices: [...doc.graph.vertices].reverse(),
    },
    layout: {
      ...doc.layout,
      vertices: [...doc.layout.vertices].reverse(),
      edges: [...doc.layout.edges].reverse(),
    },
  }),
);
for (const edge of projection.edges)
  expect(
    JSON.stringify(edge) === JSON.stringify(reordered.edges.find((value) => value.id === edge.id)),
    "Array ordering changed projection",
  );
expect(
  midpoint([
    { x: 0, y: 0 },
    { x: 0, y: 10 },
    { x: 30, y: 10 },
  ]).x === 10,
  "Polyline midpoint is not half arc-length",
);
expect(
  midpoint([
    { x: 1, y: 2 },
    { x: 1, y: 2 },
  ]).y === 2,
  "Zero-length presentation failed",
);
const behavior = useDiagramInspection();
behavior.selectVertex("vertex.a");
expect(
  store.state.selection.kind === "vertex" && store.state.selection.vertexId === "vertex.a",
  "Wrong vertex selected",
);
behavior.selectEdge("edge.crossing");
expect(
  store.state.selection.kind === "edge" && store.state.selection.edgeId === "edge.crossing",
  "Wrong edge selected",
);
const selection = JSON.stringify(store.state.selection);
store.select(
  SelectionSchema.parse({
    kind: "edge",
    edgeId: "edge.missing",
    document: { documentId: doc.id, revision: doc.revision },
  }),
);
expect(JSON.stringify(store.state.selection) === selection, "Invalid selection committed");
store.toggleLabels();
expect(
  JSON.stringify(store.state.document) === original,
  "Presentation changed authoritative document",
);
store.loadExample();
expect(store.state.selection.kind === "none", "Bundled example reload retained stale selection");
expect(JSON.stringify(store.state.document) === original, "Bundled example changed");
expect(!Object.hasOwn(store, "loadCandidate"), "External project loading API must remain absent");
const neon = neon20();
expect(
  midpointAngle([
    { x: 0, y: 0 },
    { x: 0, y: 10 },
    { x: 30, y: 10 },
  ]) === 0,
  "Bent-edge arrow must use the tangent at half arc length",
);
expect(
  midpointAngle([
    { x: 0, y: 0 },
    { x: 0, y: 0 },
  ]) === null,
  "Degenerate geometry must not invent an arrow direction",
);
for (const direction of ["from-to", "to-from", "both", "undirected", "unresolved"]) {
  const fixture = DiagramDocumentSchema.parse({
    ...neon,
    policy: { status: "unresolved", questions: ["Presentation-only arrow direction fixture"] },
    graph: {
      ...neon.graph,
      edges: neon.graph.edges.map((edge) =>
        edge.id === "edge.ne20.3" ? { ...edge, direction } : edge,
      ),
    },
  });
  const projected = projectDiagram(fixture).edges.find((edge) => edge.id === "edge.ne20.3");
  expect(
    projected?.arrowAngle ===
      (direction === "undirected" || direction === "unresolved"
        ? null
        : direction === "to-from"
          ? 225
          : 45),
    "Midpoint arrows must respect every edge direction mode",
  );
}
const beforeLabels = JSON.stringify(neon);
const packed = projectDiagram(neon);
const reversedLabels = projectDiagram(
  DiagramDocumentSchema.parse({
    ...neon,
    graph: { ...neon.graph, edges: [...neon.graph.edges].reverse() },
  }),
);
for (const edge of packed.edges) {
  expect(
    JSON.stringify(edge) ===
      JSON.stringify(reversedLabels.edges.find((other) => other.id === edge.id)),
    "Label packing must not depend on drawing order",
  );
  expect(
    JSON.stringify(edge.midpoint) === JSON.stringify(midpoint(edge.polyline)),
    "Label packing changed the geometric midpoint",
  );
  for (const other of packed.edges) {
    if (edge.id === other.id) continue;
    expect(
      Math.abs(edge.labelPoint.x - other.labelPoint.x) >=
        (edge.label.length + other.label.length) * 4.5 + 4 ||
        Math.abs(edge.labelPoint.y - other.labelPoint.y) >= 16,
      `Labels overlap: ${edge.label}/${other.label}`,
    );
  }
}
for (const [a, b] of [
  [7, 23],
  [6, 24],
  [17, 25],
  [22, 26],
  [12, 27],
]) {
  const first = packed.edges.find((edge) => edge.id === `edge.ne20.${a}`);
  const second = packed.edges.find((edge) => edge.id === `edge.ne20.${b}`);
  expect(
    first !== undefined &&
      second !== undefined &&
      JSON.stringify(first.midpoint) === JSON.stringify(second.midpoint) &&
      JSON.stringify(first.labelPoint) !== JSON.stringify(second.labelPoint),
    `Coincident labels ${a}/${b} must remain distinct without moving edges`,
  );
}
expect(JSON.stringify(neon) === beforeLabels, "Label packing mutated authoritative data");
console.log(
  "PASS: bundled model validation, identity-based projection/inspection, midpoint, presentation invariance and selection boundaries",
);
