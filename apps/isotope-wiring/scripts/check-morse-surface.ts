import { z } from "zod";
import { createHash } from "node:crypto";
import { readFile, mkdir, writeFile } from "node:fs/promises";
import { MorseSurfaceSchema } from "../src/schemas/morse-surface.js";
import { neon20 } from "../src/examples/neon20.js";
import { DiagramDocumentSchema, type DiagramDocument } from "../src/schemas/document.js";
import { constructMorseSurface, NE20_MINIMUM_CANCELLATIONS } from "../src/domain/morse-surface.js";
function expect(value: boolean, message: string): void {
  if (!value) throw new Error(message);
}
function rejects(document: DiagramDocument, contractions: readonly string[] = []): void {
  let rejected = false;
  try {
    constructMorseSurface(document, contractions);
  } catch {
    rejected = true;
  }
  expect(rejected, "Invalid geometry or non-forest contractions must be rejected");
}
const source = neon20(),
  before = JSON.stringify(source),
  surface = constructMorseSurface(source);
expect(JSON.stringify(source) === before, "Construction mutated source wiring");
expect(
  surface.minima.length === 12 && surface.saddles.length === 26 && surface.darts.length === 52,
  "Crossings were merged or incidences lost",
);
expect(
  surface.components.length === 1 &&
    surface.eulerCharacteristic === -14 &&
    surface.firstBettiNumber === 15,
  "Incorrect graph homotopy invariants",
);
expect(
  2 - 2 * surface.genus - surface.boundaryCount === -14,
  "Surface classification does not match graph",
);
expect(
  surface.genus === 5 && surface.boundaryCount === 6,
  "Authored Ne-20 rotation should produce genus five with six boundaries",
);
const boundaryDarts = surface.components.flatMap((c) => c.boundaries.flat());
expect(
  boundaryDarts.length === 52 && new Set(boundaryDarts).size === 52,
  "Boundary traversal must partition all darts",
);
for (const d of surface.darts)
  expect(
    surface.darts.find((e) => e.id === d.mate)?.mate === d.id,
    "Edge pairing must be a fixed-point-free involution",
  );
for (const m of surface.minima)
  expect(
    m.level.numerator > 0 && m.level.numerator < m.level.denominator,
    "Minimum outside lower level range",
  );
for (const s of surface.saddles)
  expect(
    s.level.numerator > s.level.denominator && s.level.numerator < 2 * s.level.denominator,
    "Saddle outside upper level range",
  );
const reduced = constructMorseSurface(source, NE20_MINIMUM_CANCELLATIONS);
expect(
  reduced.minima.length === 10 && reduced.saddles.length === 24 && reduced.darts.length === 48,
  "Two cancellations must remove two minima and two saddles",
);
expect(
  reduced.genus === 5 &&
    reduced.boundaryCount === 6 &&
    reduced.eulerCharacteristic === -14 &&
    reduced.firstBettiNumber === 15 &&
    reduced.components.length === 1,
  "Contraction changed the surface",
);
function cycleKey(cycle: readonly string[]): string {
  return cycle.map((_, i) => [...cycle.slice(i), ...cycle.slice(0, i)].join("|")).sort()[0] ?? "";
}
const deleted = new Set(
  surface.darts.filter((d) => NE20_MINIMUM_CANCELLATIONS.includes(d.edgeId)).map((d) => d.id),
);
expect(
  JSON.stringify(
    surface.components
      .flatMap((c) => c.boundaries.map((b) => cycleKey(b.filter((d) => !deleted.has(d)))))
      .sort(),
  ) === JSON.stringify(reduced.components.flatMap((c) => c.boundaries.map(cycleKey)).sort()),
  "Boundary words changed beyond removal of contracted ports",
);
const merged = reduced.minima.find((m) => m.sourceVertices.length > 1);
expect(
  merged !== undefined &&
    merged.sourceVertices.join(",") ===
      ["vertex.upper-left", "vertex.upper-right", "vertex.upper-tip"].join(","),
  "Lost merged-vertex provenance",
);
expect(
  reduced.minima
    .flatMap((m) => m.sourceVertices)
    .sort()
    .join(",") ===
    source.graph.vertices
      .map((v) => v.id)
      .sort()
      .join(","),
  "Original vertices were lost or duplicated",
);
expect(
  reduced.darts
    .filter((d) => d.edgeId === "edge.ne20.12")
    .every((d) => d.vertexId === merged?.vertexId) &&
    reduced.darts.filter((d) => d.edgeId === "edge.ne20.12").length === 2,
  "The surviving loop was lost",
);
for (const id of ["edge.ne20.10", "edge.ne20.11", "edge.ne20.27"]) {
  const ports = reduced.darts.filter((d) => d.edgeId === id);
  expect(
    ports.length === 2 &&
      ports.some((d) => d.vertexId === merged?.vertexId) &&
      ports.some((d) => d.vertexId === "vertex.top-junction"),
    "A parallel band was lost",
  );
}
expect(
  !reduced.saddles.some((s) => NE20_MINIMUM_CANCELLATIONS.includes(s.edgeId)),
  "Cancelled saddles remain",
);
rejects(source, ["edge.ne20.8", "edge.ne20.9", "edge.ne20.12"]);
rejects(source, ["edge.ne20.8", "edge.ne20.8"]);
rejects(source, ["edge.ne20.5"]);
const reducedUnresolved = constructMorseSurface(
  DiagramDocumentSchema.parse({
    ...source,
    policy: { status: "unresolved", questions: ["Fixture"] },
    graph: {
      ...source.graph,
      edges: source.graph.edges.map((e) => ({ ...e, direction: "unresolved" })),
    },
  }),
  NE20_MINIMUM_CANCELLATIONS,
);
expect(
  reducedUnresolved.unresolvedArrows.length === 26,
  "Cancellation must not hide unresolved arrows of the original wiring",
);
expect(JSON.stringify(source) === before, "Cancellation modified original wiring");
function subgraph(numbers: number[], isolated: string[] = []): DiagramDocument {
  const edges = source.graph.edges.filter((e) => numbers.some((n) => e.id === `edge.ne20.${n}`));
  const ids = new Set([...edges.flatMap((e) => [e.from, e.to]), ...isolated]);
  return DiagramDocumentSchema.parse({
    ...source,
    id: "diagram.fixture",
    isotope: null,
    graph: { ...source.graph, vertices: source.graph.vertices.filter((v) => ids.has(v.id)), edges },
    layout: {
      ...source.layout,
      vertices: source.layout.vertices.filter((v) => ids.has(v.vertexId)),
      edges: source.layout.edges.filter((e) => edges.some((g) => g.id === e.edgeId)),
      aliases: source.layout.aliases.filter((e) => edges.some((g) => g.id === e.edgeId)),
    },
  });
}
const tree = constructMorseSurface(subgraph([8, 9]));
expect(
  tree.genus === 0 && tree.boundaryCount === 1 && tree.eulerCharacteristic === 1,
  "Tree must thicken to disk",
);
const disk = constructMorseSurface(subgraph([8, 9]), NE20_MINIMUM_CANCELLATIONS);
expect(
  disk.minima.length === 1 &&
    disk.saddles.length === 0 &&
    disk.boundaryCount === 1 &&
    disk.components[0]?.boundaries[0]?.length === 0,
  "Contracting a whole tree must leave a disk",
);
const ring = subgraph([8, 9, 12]),
  annulus = constructMorseSurface(ring);
expect(
  annulus.genus === 0 && annulus.boundaryCount === 2 && annulus.firstBettiNumber === 1,
  "Circle must thicken to annulus",
);
const isolated = constructMorseSurface(subgraph([], ["vertex.center"]));
expect(
  isolated.boundaryCount === 1 && isolated.minima.length === 1 && isolated.saddles.length === 0,
  "Isolated vertex must be a disk",
);
const forest = constructMorseSurface(subgraph([8, 9, 13], ["vertex.center"]));
expect(
  forest.components.length === 3 && forest.boundaryCount === 3 && forest.genus === 0,
  "Disconnected components were merged",
);
const recolored = constructMorseSurface(
  DiagramDocumentSchema.parse({
    ...source,
    layout: {
      ...source.layout,
      edges: source.layout.edges.map((e) => ({
        ...e,
        color: e.color === "red" ? "blue" : e.color === "blue" ? "red" : "green",
      })),
    },
    graph: {
      ...source.graph,
      edges: source.graph.edges.map((e) => ({
        ...e,
        direction:
          e.direction === "from-to"
            ? "to-from"
            : e.direction === "to-from"
              ? "from-to"
              : e.direction,
      })),
    },
  }),
);
expect(
  JSON.stringify(recolored.components) === JSON.stringify(surface.components) &&
    JSON.stringify(recolored.rotations) === JSON.stringify(surface.rotations),
  "Color/arrow edits changed surface topology",
);
const fractional = constructMorseSurface(
  DiagramDocumentSchema.parse({
    ...source,
    layout: {
      ...source.layout,
      vertices: source.layout.vertices.map((v) => ({
        ...v,
        position: {
          x:
            typeof v.position.x === "number"
              ? { numerator: 2 * v.position.x, denominator: 2 }
              : v.position.x,
          y:
            typeof v.position.y === "number"
              ? { numerator: 2 * v.position.y, denominator: 2 }
              : v.position.y,
        },
      })),
    },
  }),
);
expect(
  JSON.stringify(fractional.rotations) === JSON.stringify(surface.rotations),
  "Equivalent rational coordinates changed exact rotations",
);
const reflected = constructMorseSurface(
  DiagramDocumentSchema.parse({
    ...source,
    layout: {
      ...source.layout,
      vertices: source.layout.vertices.map((v) => ({
        ...v,
        position: {
          x: v.position.x,
          y:
            typeof v.position.y === "number"
              ? -v.position.y
              : { numerator: -v.position.y.numerator, denominator: v.position.y.denominator },
        },
      })),
    },
  }),
);
expect(
  reflected.genus === surface.genus && reflected.boundaryCount === surface.boundaryCount,
  "Global orientation reversal changed surface type",
);
const cycle = constructMorseSurface(
  DiagramDocumentSchema.parse({
    ...ring,
    graph: { ...ring.graph, edges: ring.graph.edges.map((e) => ({ ...e, direction: "from-to" })) },
  }),
);
expect(cycle.directedCycle.length === 3, "Directed triangular cycle was not detected");
expect(tree.directedCycle.length === 0, "Acyclic arrows falsely rejected");
const unresolved = constructMorseSurface(
  DiagramDocumentSchema.parse({
    ...ring,
    policy: { status: "unresolved", questions: ["Fixture"] },
    graph: {
      ...ring.graph,
      edges: ring.graph.edges.map((e) => ({ ...e, direction: "unresolved" })),
    },
  }),
);
expect(unresolved.unresolvedArrows.length === 3, "Missing arrows must remain explicit");
rejects(
  DiagramDocumentSchema.parse({
    ...source,
    layout: {
      ...source.layout,
      vertices: source.layout.vertices.map((v) => ({ ...v, position: { x: 0, y: 0 } })),
    },
  }),
);
const tied = subgraph([8, 9]);
rejects(
  DiagramDocumentSchema.parse({
    ...tied,
    layout: {
      ...tied.layout,
      vertices: tied.layout.vertices.map((v) =>
        v.vertexId === "vertex.upper-right" ? { ...v, position: { x: -100, y: 34 } } : v,
      ),
    },
  }),
);
const ReceiptSchema = z.strictObject({
  schema: z.literal("marici.ne20-morse-surface.v2"),
  sourceHash: z.string().length(64),
  constructorHash: z.string().length(64),
  document: DiagramDocumentSchema,
  surface: MorseSurfaceSchema,
  reduced: MorseSurfaceSchema,
});
const receipt = ReceiptSchema.parse({
  schema: "marici.ne20-morse-surface.v2",
  sourceHash: createHash("sha256")
    .update(await readFile("src/examples/neon20.ts"))
    .digest("hex"),
  constructorHash: createHash("sha256")
    .update(await readFile("src/domain/morse-surface.ts"))
    .digest("hex"),
  document: source,
  surface,
  reduced,
});
await mkdir("../../research/strominger/results", { recursive: true });
await writeFile(
  "../../research/strominger/results/ne20-morse-surface.json",
  JSON.stringify(receipt, null, 2) + "\n",
);
console.log(
  JSON.stringify({
    reducedCounts: {
      minima: reduced.minima.length,
      saddles: reduced.saddles.length,
      genus: reduced.genus,
      boundaries: reduced.boundaryCount,
    },
    vertices: surface.minima.length,
    edges: surface.saddles.length,
    components: surface.components.length,
    chi: surface.eulerCharacteristic,
    genus: surface.genus,
    boundaries: surface.boundaryCount,
    betti1: surface.firstBettiNumber,
    boundaryCycles: surface.components.map((c) => c.boundaries),
    directedCycle: surface.directedCycle,
  }),
);
console.log(
  "PASS: Morse ribbon construction, exact rotations, boundary partition, tree/circle/isolated/disconnected controls, color/arrow invariance, reflection, directed-cycle obstruction and ambiguous-geometry rejection",
);
