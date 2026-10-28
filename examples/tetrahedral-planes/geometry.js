// Pure geometry; importing this module does not create a renderer or access the DOM.
import { Vector3 } from 'three';
export const normals = [[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]]
  .map(n => new Vector3(...n).normalize());
export const basePlanes = distance => normals.map(normal => ({ normal, offset: distance }));
export function repeatPlanes(planes, repeats) {
  return planes.flatMap(plane => Array.from({ length: repeats }, (_, i) => {
    const step = i === 0 ? 0 : i % 2 === 1 ? -(i + 1) / 2 : i / 2;
    return { ...plane, offset: plane.offset + step * 4 * plane.offset };
  }));
}
export function intersectionPoint(a, b, c) {
  const crossBC = new Vector3().crossVectors(b.normal, c.normal);
  const crossCA = new Vector3().crossVectors(c.normal, a.normal);
  const crossAB = new Vector3().crossVectors(a.normal, b.normal);
  const det = a.normal.dot(crossBC);
  if (Math.abs(det) < 1e-9) return null;
  return crossBC.multiplyScalar(a.offset).addScaledVector(crossCA, b.offset)
    .addScaledVector(crossAB, c.offset).divideScalar(det);
}
export function computePolyhedron(planes, epsilon = 1e-6) {
  if (planes.every(p => p.offset === 0)) return { vertices: [new Vector3()], faces: [] };
  const vertices = [];
  for (let i = 0; i < planes.length; i++) for (let j = i + 1; j < planes.length; j++) for (let k = j + 1; k < planes.length; k++) {
    const point = intersectionPoint(planes[i], planes[j], planes[k]);
    if (point && planes.every(p => p.normal.dot(point) <= p.offset + epsilon)) vertices.push({ point, planes: [i, j, k] });
  }
  const faces = planes.flatMap((plane, index) => {
    const points = vertices.filter(v => v.planes.includes(index)).map(v => v.point);
    if (points.length < 3) return [];
    const center = points.reduce((sum, p) => sum.add(p), new Vector3()).divideScalar(points.length);
    const u = points[0].clone().sub(center).normalize();
    const v = new Vector3().crossVectors(plane.normal, u).normalize();
    points.sort((a, b) => Math.atan2(a.clone().sub(center).dot(v), a.clone().sub(center).dot(u))
      - Math.atan2(b.clone().sub(center).dot(v), b.clone().sub(center).dot(u)));
    return [{ index, points }];
  });
  return { vertices: vertices.map(v => v.point), faces };
}
export function diskIntersection(a, b, radius) {
  const axis = new Vector3().crossVectors(a.normal, b.normal);
  const denom = axis.lengthSq();
  if (denom < 1e-12) return null;
  const point = b.normal.clone().multiplyScalar(a.offset).addScaledVector(a.normal, -b.offset).cross(axis).divideScalar(denom);
  const direction = axis.normalize();
  let lo = -Infinity, hi = Infinity;
  for (const plane of [a, b]) {
    const center = plane.normal.clone().multiplyScalar(plane.offset);
    const t = center.clone().sub(point).dot(direction);
    const distanceSquared = point.clone().addScaledVector(direction, t).distanceToSquared(center);
    if (distanceSquared > radius * radius) return null;
    const half = Math.sqrt(Math.max(0, radius * radius - distanceSquared));
    lo = Math.max(lo, t - half); hi = Math.min(hi, t + half);
  }
  return hi - lo > 1e-7 ? [point.clone().addScaledVector(direction, lo), point.clone().addScaledVector(direction, hi)] : null;
}
export function intersectionSegments(planes, radius) {
  const segments = [];
  for (let i = 0; i < planes.length; i++) for (let j = i + 1; j < planes.length; j++) {
    const pair = diskIntersection(planes[i], planes[j], radius);
    if (pair) segments.push(...pair);
  }
  return segments;
}
