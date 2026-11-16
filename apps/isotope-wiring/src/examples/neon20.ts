import { z } from "zod";
import { DiagramDocumentSchema } from "../schemas/document.js";
import { CountSchema, VertexIdSchema, SafeIntegerSchema } from "../schemas/primitives.js";
import { EdgeColorSchema } from "../schemas/layout.js";

// Authored identities and incidence, never extracted from SVG or merged by coordinates.
const vertices = z.array(z.tuple([VertexIdSchema, SafeIntegerSchema, SafeIntegerSchema])).parse([
  ["vertex.upper-tip", 0, -66],
  ["vertex.upper-left", -50, -16],
  ["vertex.upper-right", 50, -16],
  ["vertex.top-junction", 0, 34],
  ["vertex.middle-left", -50, 84],
  ["vertex.middle-right", 50, 84],
  ["vertex.center", 0, 134],
  ["vertex.bottom-left", -50, 184],
  ["vertex.bottom-right", 50, 184],
  ["vertex.bottom-tip", 0, 234],
  ["vertex.left-tip", -100, 134],
  ["vertex.right-tip", 100, 134],
]);
const edges = z
  .array(z.tuple([CountSchema, VertexIdSchema, VertexIdSchema, EdgeColorSchema]))
  .parse([
    [21, "vertex.middle-left", "vertex.center", "red"],
    [1, "vertex.middle-left", "vertex.top-junction", "blue"],
    [2, "vertex.center", "vertex.middle-right", "blue"],
    [3, "vertex.top-junction", "vertex.middle-right", "red"],
    [4, "vertex.center", "vertex.bottom-right", "red"],
    [6, "vertex.bottom-left", "vertex.bottom-right", "green"],
    [7, "vertex.middle-left", "vertex.middle-right", "green"],
    [8, "vertex.upper-tip", "vertex.upper-left", "red"],
    [9, "vertex.upper-right", "vertex.upper-tip", "blue"],
    [10, "vertex.upper-right", "vertex.top-junction", "red"],
    [11, "vertex.top-junction", "vertex.upper-left", "blue"],
    [12, "vertex.upper-left", "vertex.upper-right", "green"],
    [13, "vertex.bottom-right", "vertex.bottom-tip", "blue"],
    [14, "vertex.bottom-left", "vertex.bottom-tip", "blue"],
    [15, "vertex.bottom-left", "vertex.left-tip", "red"],
    [16, "vertex.left-tip", "vertex.middle-left", "red"],
    [17, "vertex.bottom-left", "vertex.middle-left", "green"],
    [18, "vertex.bottom-left", "vertex.center", "blue"],
    [22, "vertex.bottom-right", "vertex.middle-right", "green"],
    [19, "vertex.right-tip", "vertex.middle-right", "red"],
    [20, "vertex.bottom-right", "vertex.right-tip", "red"],
    [23, "vertex.top-junction", "vertex.center", "green"],
    [24, "vertex.center", "vertex.bottom-tip", "green"],
    [25, "vertex.left-tip", "vertex.center", "green"],
    [26, "vertex.center", "vertex.right-tip", "green"],
    [27, "vertex.upper-tip", "vertex.top-junction", "green"],
  ]);

// Authored incidence is traversable from either endpoint for these segments.
// This declaration is independent of presentation colors.
const undirectedEdges = z.array(CountSchema).parse([6, 7, 12, 17, 22, 23, 24, 25, 26, 27]);

/** New authored diagram, not a claim of recovered legacy identity or scientific review. */
export function neon20() {
  return DiagramDocumentSchema.parse({
    schemaVersion: 1,
    id: "diagram.ne20",
    revision: 20,
    title: "Ne-20 — authored alternating-route diagram",
    isotope: {
      id: "isotope.ne20",
      name: "Neon-20",
      symbol: "Ne",
      protons: 10,
      neutrons: 10,
      electrons: { status: "unspecified" },
      charge: { status: "unspecified" },
      sources: [],
    },
    graph: {
      vertices: vertices.map(([id]) => ({ id })),
      edges: edges.map(([number, from, to]) => ({
        id: `edge.ne20.${number}`,
        from,
        to,
        direction: undirectedEdges.includes(number) ? "undirected" : "from-to",
      })),
      roles: [],
      junctionOrders: [],
      review: {
        status: "unreviewed",
        questions: [
          "New authored diagram, not a scientifically validated nuclear structure.",
          "Duplicate edge 5 was removed by operator instruction; edge 18 retains the bottom-left to center connection and its identity.",
          "Top-shell green 27 joins upper-tip to top-junction; its crossing with green 12 has no junction vertex.",
          "Shell-2 diagonal crossings (7/23, 6/24, 17/25, 22/26) have no junction vertex; only their explicitly named endpoints are incident.",
        ],
      },
    },
    layout: {
      coordinateSystem: "authored-exact-plane",
      viewBox: { x: -150, y: -100, width: 300, height: 370 },
      vertices: vertices.map(([vertexId, x, y]) => ({ vertexId, position: { x, y } })),
      edges: edges.map(([number, , , color]) => ({
        edgeId: `edge.ne20.${number}`,
        color,
        via: [],
        labelPosition: "midpoint",
      })),
      aliases: edges.map(([number]) => ({
        edgeId: `edge.ne20.${number}`,
        number,
        source: "Assigned in the new authored Ne-20 model; not recovered from DOM order",
        review: { status: "unreviewed", questions: [] },
      })),
    },
    policy: {
      status: "alternating",
      version: 14,
      coloredEdges: "visit-once-finish-active-color",
      initialTurn: "left",
      orientation: "authored-plane-y-down",
      straight: "preserve-turn",
      greenContinuation: "straight-before-colored",
      exitSelection: "own-color-first-angular-extreme",
      ambiguity: "stop",
    },
  });
}
