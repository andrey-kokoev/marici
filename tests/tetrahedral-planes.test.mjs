import test from 'node:test';
import assert from 'node:assert/strict';
import { basePlanes, repeatPlanes, computePolyhedron, diskIntersection } from '../examples/tetrahedral-planes/geometry.js';
import { usePlanesModel } from '../examples/tetrahedral-planes/usePlanesModel.js';
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} != ${b}`);

test('half-space tetrahedron and zero-distance collapse', () => {
  const planes = basePlanes(0.67), region = computePolyhedron(planes);
  assert.equal(region.vertices.length, 4); assert.equal(region.faces.length, 4);
  for (const p of region.vertices) for (const plane of planes) assert.ok(plane.normal.dot(p) <= plane.offset + 1e-9);
  for (const face of region.faces) {
    assert.equal(face.points.length, 3);
    for (const p of face.points) near(planes[face.index].normal.dot(p), 0.67);
  }
  const [a, b, c, d] = region.vertices;
  const volume = Math.abs(a.clone().sub(d).dot(b.clone().sub(d).cross(c.clone().sub(d)))) / 6;
  near(volume, 8 * Math.sqrt(3) * 0.67 ** 3);
  const collapsed = computePolyhedron(basePlanes(0));
  assert.equal(collapsed.vertices.length, 1); assert.equal(collapsed.vertices[0].length(), 0);
  assert.equal(collapsed.faces.length, 0);
});

test('repeat pitch and finite disk intersections preserve original semantics', () => {
  const planes = basePlanes(0.67);
  const repeated = repeatPlanes(planes, 5);
  assert.equal(repeated.length, 20);
  repeated.slice(0, 5).forEach((p, i) => near(p.offset, [1, -3, 5, -7, 9][i] * 0.67));
  assert.equal(diskIntersection(planes[0], planes[0], 2.5), null);
  assert.equal(diskIntersection(planes[0], planes[1], 0.01), null);
  const segment = diskIntersection(planes[0], planes[1], 2.5);
  assert.equal(segment.length, 2);
  for (const point of segment) for (const plane of planes.slice(0, 2)) {
    near(plane.normal.dot(point), plane.offset);
    assert.ok(point.distanceTo(plane.normal.clone().multiplyScalar(plane.offset)) <= 2.5 + 1e-9);
  }
});

test('Vue derived graph keeps opacity/radius/repeats separate from region constraints', () => {
  const model = usePlanesModel(), independent = usePlanesModel();
  const geometry = model.geometry.value, region = model.region.value;
  model.state.opacity = 0.5;
  assert.equal(model.geometry.value, geometry);
  model.state.radius = 20;
  assert.equal(model.region.value, region);
  model.state.repeats = 15;
  assert.equal(model.repeated.value.length, 60);
  assert.equal(model.region.value, region);
  assert.match(model.summary.value, /60 disks/);
  model.state.intersections = false;
  assert.equal(model.segments.value.length, 0);
  model.state.distance = 0;
  assert.equal(model.volume.value, 0);
  assert.match(model.summary.value, /collapsed to a point/);
  assert.equal(independent.state.distance, 0.67);
});
