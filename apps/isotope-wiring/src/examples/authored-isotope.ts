import { z } from "zod";
import { DiagramDocumentSchema, type DiagramDocument } from "../schemas/document.js";
import { CountSchema, NonEmptyTextSchema, SafeIntegerSchema } from "../schemas/primitives.js";
import { EdgeColorSchema } from "../schemas/layout.js";

// These records declare incidence. Positions never create or merge vertices.
export const AuthoredVertexSchema = z.tuple([
  NonEmptyTextSchema,
  SafeIntegerSchema,
  SafeIntegerSchema,
]);
export const AuthoredEdgeSchema = z.tuple([
  CountSchema,
  NonEmptyTextSchema,
  NonEmptyTextSchema,
  EdgeColorSchema,
  z.array(z.tuple([SafeIntegerSchema, SafeIntegerSchema])),
]);
export const AuthoredDrawingSchema = z.strictObject({
  key: NonEmptyTextSchema,
  name: NonEmptyTextSchema,
  symbol: NonEmptyTextSchema,
  protons: CountSchema,
  neutrons: CountSchema,
  vertices: z.array(AuthoredVertexSchema),
  edges: z.array(AuthoredEdgeSchema),
  undirectedEdges: z.array(CountSchema),
  viewBox: z.tuple([SafeIntegerSchema, SafeIntegerSchema, SafeIntegerSchema, SafeIntegerSchema]),
});
export type AuthoredDrawing = z.infer<typeof AuthoredDrawingSchema>;
export function authoredIsotope(input: AuthoredDrawing): DiagramDocument {
  const seed = AuthoredDrawingSchema.parse(input);
  const vertex = (name: string): string => `vertex.${seed.key}.${name}`;
  const edge = (number: number): string => `edge.${seed.key}.${number}`;
  const [x, y, width, height] = seed.viewBox;
  return DiagramDocumentSchema.parse({
    schemaVersion: 1,
    id: `diagram.${seed.key}`,
    revision: 1,
    title: `${seed.name} — authored wiring`,
    isotope: {
      id: `isotope.${seed.key}`,
      name: seed.name,
      symbol: seed.symbol,
      protons: seed.protons,
      neutrons: seed.neutrons,
      electrons: { status: "unspecified" },
      charge: { status: "unspecified" },
      sources: ["research/matter/isotope-reference.resource.json"],
    },
    graph: {
      vertices: seed.vertices.map(([name]) => ({ id: vertex(name) })),
      edges: seed.edges.map(([number, from, to]) => ({
        id: edge(number),
        from: vertex(from),
        to: vertex(to),
        direction: seed.undirectedEdges.includes(number) ? "undirected" : "from-to",
      })),
      roles: [],
      junctionOrders: [],
      review: {
        status: "unreviewed",
        questions: [
          "Manually authored incidence and aliases using the named legacy drawings as visual reference, not extracted SVG identities or measured nuclear geometry.",
          "H/He colored arrows are new authored choices; the legacy reference supplied only green shapes. All green connectors follow the current undirected convention.",
          "Only declared endpoints join. Crossings and intermediate points on a wrapper are not junctions.",
        ],
      },
    },
    layout: {
      coordinateSystem: "authored-exact-plane",
      viewBox: { x, y, width, height },
      vertices: seed.vertices.map(([name, x, y]) => ({
        vertexId: vertex(name),
        position: { x, y },
      })),
      edges: seed.edges.map(([number, , , color, via]) => ({
        edgeId: edge(number),
        color,
        via: via.map(([x, y]) => ({ x, y })),
        labelPosition: "midpoint",
      })),
      aliases: seed.edges.map(([number]) => ({
        edgeId: edge(number),
        number,
        source: "Assigned in the authored replacement, not legacy DOM order",
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
