import { DiagramDocumentSchema } from "../schemas/document.js";

/** Deliberately synthetic geometry, not an isotope model or reviewed legacy mapping. */
export function syntheticExample() {
  return DiagramDocumentSchema.parse({
    schemaVersion: 1,
    id: "diagram.synthetic",
    revision: 0,
    title: "Synthetic crossing and coincident vertices",
    isotope: null,
    graph: {
      vertices: [
        { id: "vertex.a" },
        { id: "vertex.b" },
        { id: "vertex.c" },
        { id: "vertex.d" },
        { id: "vertex.coincident" },
      ],
      edges: [
        { id: "edge.diagonal", from: "vertex.a", to: "vertex.b", direction: "from-to" },
        { id: "edge.crossing", from: "vertex.c", to: "vertex.d", direction: "to-from" },
        { id: "edge.bent", from: "vertex.coincident", to: "vertex.d", direction: "both" },
      ],
      roles: [],
      junctionOrders: [],
      review: { status: "unreviewed", questions: ["Synthetic example only"] },
    },
    layout: {
      coordinateSystem: "authored-exact-plane",
      viewBox: { x: 0, y: 0, width: 400, height: 300 },
      vertices: [
        { vertexId: "vertex.a", position: { x: 60, y: 60 } },
        { vertexId: "vertex.b", position: { x: 340, y: 240 } },
        { vertexId: "vertex.c", position: { x: 60, y: 240 } },
        { vertexId: "vertex.d", position: { x: 340, y: 60 } },
        { vertexId: "vertex.coincident", position: { x: 60, y: 60 } },
      ],
      edges: [
        { edgeId: "edge.diagonal", color: "red", via: [], labelPosition: "midpoint" },
        { edgeId: "edge.crossing", color: "blue", via: [], labelPosition: "midpoint" },
        {
          edgeId: "edge.bent",
          color: "green",
          via: [{ x: 200, y: 25 }],
          labelPosition: "midpoint",
        },
      ],
      aliases: [],
    },
    policy: {
      status: "unresolved",
      questions: ["No traversal semantics are defined for this example"],
    },
  });
}
