import { type DiagramDocument } from "../schemas/document.js";
import { type LogicalCoordinate, type LogicalPoint } from "../schemas/layout.js";
import {
  DiagramProjectionSchema,
  type DiagramProjection,
  type ScreenPoint,
} from "../schemas/inspection.js";

function scalar(value: LogicalCoordinate): number {
  return typeof value === "number" ? value : value.numerator / value.denominator;
}
function point(value: LogicalPoint): ScreenPoint {
  return { x: scalar(value.x), y: scalar(value.y) };
}
/** Presentation-only interpolation; never establishes incidence or chooses a route. */
export function pointAtFraction(points: ScreenPoint[], fraction: number): ScreenPoint {
  const first = points[0];
  if (first === undefined) throw new Error("Polyline must have a point");
  let total = 0;
  for (let i = 1; i < points.length; i += 1) {
    const a = points[i - 1];
    const b = points[i];
    if (a !== undefined && b !== undefined) total += Math.hypot(b.x - a.x, b.y - a.y);
  }
  let remaining = total * Math.max(0, Math.min(1, fraction));
  for (let i = 1; i < points.length; i += 1) {
    const a = points[i - 1];
    const b = points[i];
    if (a === undefined || b === undefined) continue;
    const length = Math.hypot(b.x - a.x, b.y - a.y);
    if (length > 0 && remaining <= length)
      return {
        x: a.x + ((b.x - a.x) * remaining) / length,
        y: a.y + ((b.y - a.y) * remaining) / length,
      };
    remaining -= length;
  }
  return points.at(-1) ?? first;
}
export function midpoint(points: ScreenPoint[]): ScreenPoint {
  return pointAtFraction(points, 0.5);
}
// Direction of the nonzero segment containing the half arc-length point.
export function midpointAngle(points: ScreenPoint[]): number | null {
  let total = 0;
  for (let i = 1; i < points.length; i += 1) {
    const a = points[i - 1],
      b = points[i];
    if (a !== undefined && b !== undefined) total += Math.hypot(b.x - a.x, b.y - a.y);
  }
  let remaining = total / 2;
  for (let i = 1; i < points.length; i += 1) {
    const a = points[i - 1],
      b = points[i];
    if (a === undefined || b === undefined) continue;
    const length = Math.hypot(b.x - a.x, b.y - a.y);
    if (length > 0 && remaining <= length)
      return (Math.atan2(b.y - a.y, b.x - a.x) * 180) / Math.PI;
    remaining -= length;
  }
  return null;
}
export function projectDiagram(document: DiagramDocument): DiagramProjection {
  const positions = new Map(
    document.layout.vertices.map((value) => [value.vertexId, point(value.position)]),
  );
  const styles = new Map(document.layout.edges.map((value) => [value.edgeId, value]));
  const aliases = new Map(document.layout.aliases.map((value) => [value.edgeId, value.number]));
  const box = document.layout.viewBox;
  const projection = DiagramProjectionSchema.parse({
    viewBox: `${box.x} ${box.y} ${box.width} ${box.height}`,
    vertices: document.graph.vertices.map((vertex) => {
      const position = positions.get(vertex.id);
      if (position === undefined) throw new Error("Missing authored vertex placement");
      return { id: vertex.id, point: position };
    }),
    edges: document.graph.edges.map((edge) => {
      const from = positions.get(edge.from);
      const to = positions.get(edge.to);
      const style = styles.get(edge.id);
      if (from === undefined || to === undefined || style === undefined)
        throw new Error("Missing authored edge presentation");
      const points = [from, ...style.via.map(point), to];
      const alias = aliases.get(edge.id);
      const middle = midpoint(points);
      const angle = midpointAngle(points);
      return {
        id: edge.id,
        direction: edge.direction,
        color: style.color,
        points: points.map((value) => `${value.x},${value.y}`).join(" "),
        polyline: points,
        midpoint: middle,
        arrowAngle:
          edge.direction === "undirected" || edge.direction === "unresolved" || angle === null
            ? null
            : angle + (edge.direction === "to-from" ? 180 : 0),
        labelPoint: { x: middle.x, y: middle.y - 9 },
        label: alias === undefined ? edge.id : String(alias),
      };
    }),
  });
  // Presentation-only packing, stable by ID rather than SVG/array drawing order.
  // Conservative bounds for the shared 9px sans-serif labels, including their halo.
  const placed: DiagramProjection["edges"] = [];
  for (const edge of [...projection.edges].sort((a, b) =>
    a.id < b.id ? -1 : a.id > b.id ? 1 : 0,
  )) {
    const collides = (candidate: ScreenPoint) =>
      placed.some(
        (other) =>
          Math.abs(candidate.x - other.labelPoint.x) <
            (edge.label.length + other.label.length) * 4.5 + 4 &&
          Math.abs(candidate.y - other.labelPoint.y) < 16,
      );
    let candidate = edge.labelPoint;
    // Prefer another point on this same edge, keeping the label visibly associated
    // with its segment. This also separates labels on coincident directed channels.
    for (const fraction of [0.3, 0.7, 0.2, 0.8]) {
      if (!collides(candidate)) break;
      const anchor = pointAtFraction(edge.polyline, fraction);
      candidate = { x: anchor.x, y: anchor.y - 9 };
    }
    // Crowded/degenerate polylines still get distinct labels; no IDs are suppressed.
    let offset = 1;
    while (collides(candidate)) {
      candidate = {
        x: edge.midpoint.x,
        y: edge.midpoint.y - 9 + (offset % 2 === 1 ? -1 : 1) * Math.ceil(offset / 2) * 16,
      };
      offset += 1;
    }
    edge.labelPoint = candidate;
    placed.push(edge);
  }
  return projection;
}
