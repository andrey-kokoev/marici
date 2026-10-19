import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { sectors3, counts, pointOnPath, previewSvg, tetrahedralBasis, tetrahedralPoint } from '../demos/minimal-data-packet/model.mjs';

const sectors = sectors3();
test('twelve unique signed sectors, four for each omitted direction', () => {
  assert.equal(sectors.length, 12);
  assert.equal(new Set(sectors.map(s => s.id)).size, 12);
  for (let axis = 0; axis < 3; axis++) {
    const group = sectors.filter(s => s.omitted === axis);
    assert.equal(group.length, 4);
    assert.deepEqual(new Set(group.map(s => s.signs.join(','))), new Set(['-1,-1', '-1,1', '1,-1', '1,1']));
  }
});
test('square boundaries close at the common mark with four unit steps', () => {
  for (const s of sectors) {
    assert.deepEqual(s.boundary[0], [0, 0, 0]);
    assert.deepEqual(s.boundary.at(-1), [0, 0, 0]);
    assert.equal(s.boundary.length, 5);
    for (const point of s.boundary) assert.equal(point[s.omitted], 0);
    for (let i = 0; i < 4; i++) {
      assert.equal(s.boundary[i].reduce((sum, x, j) => sum + Math.abs(x - s.boundary[i + 1][j]), 0), 1);
    }
  }
});
test('two different orders reach the same corner and retain different intermediates', () => {
  for (const s of sectors) {
    assert.deepEqual(s.routes[0][0], s.routes[1][0]);
    assert.deepEqual(s.routes[0].at(-1), s.corner);
    assert.deepEqual(s.routes[1].at(-1), s.corner);
    assert.notDeepEqual(s.routes[0][1], s.routes[1][1]);
  }
  assert.equal(new Set(sectors.map(s => s.corner.join(','))).size, 12);
});
test('path interpolation has exact start, corner and return states', () => {
  for (const s of sectors) {
    assert.deepEqual(pointOnPath(s.boundary, 0), [0, 0, 0]);
    assert.deepEqual(pointOnPath(s.boundary, 0.5), s.corner);
    assert.deepEqual(pointOnPath(s.boundary, 1), [0, 0, 0]);
    assert.deepEqual(pointOnPath(s.routes[0], 1), pointOnPath(s.routes[1], 1));
  }
});
test('codimension-one counts and the three candidate products', () => {
  assert.deepEqual(counts(3), { n: 3, cellDimension: 2, sectors: 12, encounters: 36, terms: [108, 432, 1296], total: 1836 });
  const four = counts(4);
  assert.equal(four.cellDimension, 3); assert.equal(four.sectors, 32);
  assert.deepEqual(four.terms, [512, 4096, 16384]); assert.equal(four.total, 20992);
  for (let n = 1; n <= 12; n++) {
    const c = counts(n);
    assert.equal(c.total, n ** 3 * 2 ** (n - 1) * (1 + (n + 1) * 2 ** (n - 1)));
  }
});
test('unsupported or noninteger dimensions are refused', () => {
  for (const n of [0, -1, 2.5, 13, NaN, '3']) assert.throws(() => counts(n), RangeError);
});
test('authored preview is reproducible from the geometry and has twelve sectors', async () => {
  const saved = await readFile(new URL('../demos/minimal-data-packet/preview.svg', import.meta.url), 'utf8');
  assert.equal(saved, previewSvg());
  assert.equal((saved.match(/data-sector=/g) || []).length, 12);
  assert.equal((previewSvg('2:1:1', true).match(/data-sector=/g) || []).length, 1);
});
test('tetrahedral frame has four equidistant vertex rays with zero barycenter', () => {
  const vertices = [...tetrahedralBasis, tetrahedralPoint([-1, -1, -1])];
  for (const v of vertices) assert.ok(Math.abs(v.reduce((sum, x) => sum + x * x, 0) - 1) < 1e-12);
  for (let j = 0; j < 3; j++) assert.ok(Math.abs(vertices.reduce((sum, v) => sum + v[j], 0)) < 1e-12);
  for (let i = 0; i < 4; i++) for (let j = i + 1; j < 4; j++) {
    const d2 = vertices[i].reduce((sum, x, k) => sum + (x - vertices[j][k]) ** 2, 0);
    assert.ok(Math.abs(d2 - 8 / 3) < 1e-12);
  }
  const [a, b, c] = tetrahedralBasis;
  const determinant = a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0]) + a[2] * (b[0] * c[1] - b[1] * c[0]);
  assert.ok(Math.abs(determinant) > 0.7);
});
test('twelve distinct rhombi preserve endpoints, unit sides and path interpolation', () => {
  const transformed = sectors.map(s => s.boundary.map(tetrahedralPoint));
  assert.equal(new Set(transformed.map(ps => ps.map(p => p.join(',')).join(';'))).size, 12);
  for (const s of sectors) {
    const ps = s.boundary.map(tetrahedralPoint);
    assert.deepEqual(ps[0], [0, 0, 0]); assert.deepEqual(ps.at(-1), [0, 0, 0]);
    for (let i = 0; i < 4; i++) {
      const d2 = ps[i].reduce((sum, x, j) => sum + (x - ps[i + 1][j]) ** 2, 0);
      assert.ok(Math.abs(d2 - 1) < 1e-12);
    }
    const dot = ps[1].reduce((sum, x, j) => sum + x * ps[3][j], 0);
    assert.ok(Math.abs(Math.abs(dot) - 1 / 3) < 1e-12);
    for (const t of [0, 0.125, 0.5, 0.875, 1]) {
      const first = tetrahedralPoint(pointOnPath(s.boundary, t));
      const second = pointOnPath(ps, t);
      first.forEach((x, j) => assert.ok(Math.abs(x - second[j]) < 1e-12));
    }
    assert.deepEqual(tetrahedralPoint(s.routes[0].at(-1)), tetrahedralPoint(s.routes[1].at(-1)));
  }
});
test('tetrahedral SVG is reproducible and keeps twelve sector identities', async () => {
  const saved = await readFile(new URL('../demos/minimal-data-packet/tetra-preview.svg', import.meta.url), 'utf8');
  assert.equal(saved, previewSvg(null, false, true, 'tetrahedral'));
  assert.equal((saved.match(/data-sector=/g) || []).length, 12);
  assert.notEqual(saved, previewSvg());
});
