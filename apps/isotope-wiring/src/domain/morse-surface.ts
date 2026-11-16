import { z } from "zod";
import { type DiagramDocument } from "../schemas/document.js";
import { type LogicalCoordinate, type LogicalPoint } from "../schemas/layout.js";
import { VertexIdSchema, EdgeIdSchema } from "../schemas/primitives.js";
type VertexId = z.infer<typeof VertexIdSchema>;
type EdgeId = z.infer<typeof EdgeIdSchema>;
import {
  DartIdSchema,
  SurfaceDartSchema,
  MorseSurfaceSchema,
  type DartId,
  type SurfaceDart,
  type SurfaceRotation,
  type SurfaceComponent,
  type MorseSurface,
} from "../schemas/morse-surface.js";
export const NE20_MINIMUM_CANCELLATIONS = z
  .array(EdgeIdSchema)
  .readonly()
  .parse(["edge.ne20.8", "edge.ne20.9"]);
const FractionSchema = z.strictObject({ n: z.bigint(), d: z.bigint().positive() });
const VectorSchema = z.strictObject({ x: z.bigint(), y: z.bigint() });
type Fraction = z.infer<typeof FractionSchema>;
type Vector = z.infer<typeof VectorSchema>;
function fraction(x: LogicalCoordinate): Fraction {
  return typeof x === "number"
    ? { n: BigInt(x), d: 1n }
    : { n: BigInt(x.numerator), d: BigInt(x.denominator) };
}
function difference(a: LogicalCoordinate, b: LogicalCoordinate): Fraction {
  const x = fraction(a),
    y = fraction(b);
  return { n: x.n * y.d - y.n * x.d, d: x.d * y.d };
}
function vector(a: LogicalPoint, b: LogicalPoint): Vector {
  const x = difference(b.x, a.x),
    y = difference(b.y, a.y);
  return { x: x.n * y.d, y: y.n * x.d };
}
function half(v: Vector): number {
  return v.y > 0n || (v.y === 0n && v.x >= 0n) ? 0 : 1;
}
function compare(a: Vector, b: Vector): number {
  if (half(a) !== half(b)) return half(a) - half(b);
  const cross = a.x * b.y - a.y * b.x;
  if (cross === 0n)
    throw new Error(
      "Coincident outgoing tangents require an explicit rotation; no edge-ID tie-break is inferred.",
    );
  return cross > 0n ? -1 : 1;
}
function directedCycle(document: DiagramDocument): EdgeId[] {
  const done = new Set<VertexId>();
  function visit(v: VertexId, vertices: VertexId[], path: EdgeId[]): EdgeId[] {
    for (const edge of document.graph.edges) {
      if (edge.direction !== "from-to" && edge.direction !== "to-from") continue;
      const from = edge.direction === "from-to" ? edge.from : edge.to,
        to = edge.direction === "from-to" ? edge.to : edge.from;
      if (from !== v) continue;
      const index = vertices.indexOf(to);
      if (index >= 0) return [...path.slice(index), edge.id];
      if (!done.has(to)) {
        const found = visit(to, [...vertices, to], [...path, edge.id]);
        if (found.length) return found;
      }
    }
    done.add(v);
    return [];
  }
  for (const vertex of document.graph.vertices)
    if (!done.has(vertex.id)) {
      const found = visit(vertex.id, [vertex.id], []);
      if (found.length) return found;
    }
  return [];
}
/** Oriented ribbon surface, not a planar union of overlapping drawn strips. */
export function constructMorseSurface(
  document: DiagramDocument,
  contractEdges: readonly string[] = [],
): MorseSurface {
  let vertices = [...document.graph.vertices].sort((a, b) =>
    a.id < b.id ? -1 : a.id > b.id ? 1 : 0,
  );
  let edges = [...document.graph.edges].sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
  let darts: SurfaceDart[] = [];
  const tangents = new Map<DartId, Vector>();
  const position = (id: VertexId): LogicalPoint => {
    const p = document.layout.vertices.find((v) => v.vertexId === id)?.position;
    if (p === undefined) throw new Error("Missing vertex position");
    return p;
  };
  for (const edge of edges) {
    const style = document.layout.edges.find((e) => e.edgeId === edge.id);
    if (style === undefined) throw new Error("Missing edge geometry");
    const forward = [position(edge.from), ...style.via, position(edge.to)];
    for (const end of ["from", "to"]) {
      const id = DartIdSchema.parse(`${edge.id}:${end}`),
        mate = DartIdSchema.parse(`${edge.id}:${end === "from" ? "to" : "from"}`);
      const points = end === "from" ? forward : [...forward].reverse(),
        origin = points[0];
      if (origin === undefined) throw new Error("Missing endpoint");
      const tangent = points
        .slice(1)
        .map((p) => vector(origin, p))
        .find((v) => v.x !== 0n || v.y !== 0n);
      if (tangent === undefined) throw new Error("Collapsed edge has no outgoing tangent");
      tangents.set(id, tangent);
      darts.push(
        SurfaceDartSchema.parse({
          id,
          mate,
          edgeId: edge.id,
          vertexId: end === "from" ? edge.from : edge.to,
        }),
      );
    }
  }
  const tangent = (id: DartId): Vector => {
    const value = tangents.get(id);
    if (value === undefined) throw new Error("Missing tangent");
    return value;
  };
  let rotations: SurfaceRotation[] = vertices.map((v) => ({
    vertexId: v.id,
    darts: darts
      .filter((d) => d.vertexId === v.id)
      .map((d) => d.id)
      .sort((a, b) => (a === b ? 0 : compare(tangent(a), tangent(b)))),
  }));
  const sources = new Map(vertices.map((v) => [v.id, [v.id]]));
  const contractedEdges: EdgeId[] = [];
  // Contract a forest in the ribbon graph, never re-sort the surviving ports by geometry.
  for (const requested of contractEdges) {
    const edge = edges.find((e) => e.id === requested);
    if (edge === undefined) throw new Error("Missing or repeated contraction edge");
    if (edge.from === edge.to) throw new Error("A loop cannot cancel a minimum–saddle pair");
    const from = rotations.find((r) => r.vertexId === edge.from),
      to = rotations.find((r) => r.vertexId === edge.to);
    const a = darts.find((d) => d.edgeId === edge.id && d.vertexId === edge.from);
    const b = darts.find((d) => d.edgeId === edge.id && d.vertexId === edge.to);
    if (from === undefined || to === undefined || a === undefined || b === undefined)
      throw new Error("Missing contraction ports");
    function after(rotation: SurfaceRotation, id: DartId): DartId[] {
      const index = rotation.darts.indexOf(id);
      if (index < 0) throw new Error("Port absent from rotation");
      return [...rotation.darts.slice(index + 1), ...rotation.darts.slice(0, index)];
    }
    const merged = [...after(from, a.id), ...after(to, b.id)];
    const fromSources = sources.get(edge.from),
      toSources = sources.get(edge.to);
    if (fromSources === undefined || toSources === undefined)
      throw new Error("Missing minimum provenance");
    sources.set(edge.from, [...fromSources, ...toSources].sort());
    sources.delete(edge.to);
    rotations = rotations.filter((r) => r.vertexId !== edge.from && r.vertexId !== edge.to);
    rotations.push({ vertexId: edge.from, darts: merged });
    vertices = vertices.filter((v) => v.id !== edge.to);
    darts = darts
      .filter((d) => d.edgeId !== edge.id)
      .map((d) => ({ ...d, vertexId: d.vertexId === edge.to ? edge.from : d.vertexId }));
    edges = edges
      .filter((e) => e.id !== edge.id)
      .map((e) => ({
        ...e,
        from: e.from === edge.to ? edge.from : e.from,
        to: e.to === edge.to ? edge.from : e.to,
      }));
    contractedEdges.push(edge.id);
  }
  rotations.sort((a, b) => (a.vertexId < b.vertexId ? -1 : a.vertexId > b.vertexId ? 1 : 0));
  const successor = new Map<DartId, DartId>();
  for (const rotation of rotations)
    for (const [i, id] of rotation.darts.entries()) {
      const next = rotation.darts[(i + 1) % rotation.darts.length];
      if (next === undefined) throw new Error("Missing rotation successor");
      successor.set(id, next);
    }
  const byId = new Map(darts.map((d) => [d.id, d]));
  const visited = new Set<VertexId>(),
    components: SurfaceComponent[] = [];
  for (const vertex of vertices) {
    if (visited.has(vertex.id)) continue;
    const componentVertices: VertexId[] = [],
      pending = [vertex.id];
    while (pending.length) {
      const v = pending.pop();
      if (v === undefined || visited.has(v)) continue;
      visited.add(v);
      componentVertices.push(v);
      for (const edge of edges) {
        if (edge.from === v && !visited.has(edge.to)) pending.push(edge.to);
        if (edge.to === v && !visited.has(edge.from)) pending.push(edge.from);
      }
    }
    const componentEdges = edges.filter((e) => componentVertices.includes(e.from)).map((e) => e.id);
    const componentDarts = darts.filter((d) => componentVertices.includes(d.vertexId));
    const walked = new Set<DartId>(),
      boundaries: DartId[][] = [];
    for (const dart of componentDarts) {
      if (walked.has(dart.id)) continue;
      const cycle: DartId[] = [];
      let current = dart.id;
      do {
        if (walked.has(current)) throw new Error("Boundary permutation did not close at its start");
        walked.add(current);
        cycle.push(current);
        const item = byId.get(current);
        const next = item === undefined ? undefined : successor.get(item.mate);
        if (next === undefined) throw new Error("Missing boundary successor");
        current = next;
      } while (current !== dart.id);
      boundaries.push(cycle);
    }
    // An isolated vertex contributes a disk with one boundary and no darts.
    if (componentDarts.length === 0) boundaries.push([]);
    const chi = componentVertices.length - componentEdges.length,
      genus = (2 - boundaries.length - chi) / 2;
    if (!Number.isSafeInteger(genus) || genus < 0)
      throw new Error("Invalid orientable surface invariant");
    components.push({
      vertices: componentVertices,
      edges: componentEdges,
      boundaries,
      eulerCharacteristic: chi,
      genus,
      firstBettiNumber: 1 - chi,
    });
  }
  return MorseSurfaceSchema.parse({
    documentId: document.id,
    revision: document.revision,
    convention: contractedEdges.length
      ? "clockwise-authored-tangents-untwisted-contracted"
      : "clockwise-authored-tangents-untwisted",
    contractedEdges,
    darts,
    rotations,
    components,
    minima: vertices.map((v, i) => ({
      vertexId: v.id,
      sourceVertices: sources.get(v.id),
      level: { numerator: i + 1, denominator: vertices.length + 1 },
    })),
    saddles: edges.map((e, i) => ({
      edgeId: e.id,
      level: { numerator: edges.length + i + 2, denominator: edges.length + 1 },
    })),
    boundaryLevel: 3,
    maxima: 0,
    eulerCharacteristic: vertices.length - edges.length,
    genus: components.reduce((sum, c) => sum + c.genus, 0),
    boundaryCount: components.reduce((sum, c) => sum + c.boundaries.length, 0),
    firstBettiNumber: components.reduce((sum, c) => sum + c.firstBettiNumber, 0),
    directedCycle: directedCycle(document),
    unresolvedArrows: document.graph.edges
      .filter((e) => e.direction === "unresolved")
      .map((e) => e.id)
      .sort(),
  });
}
