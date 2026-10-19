import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { loadFixture, stateAt, spinorNorm, preparedSpinor, bloch, gauge, relativePhase, distance, scale,
  sourceBlocks, decodeBlocks, localDirections, electronSvg } from '../demos/minimal-data-packet/electron-model.mjs';

const trial = JSON.parse(await readFile(new URL('../results/electron-configuration-dimension-trial-v1.json', import.meta.url), 'utf8'));
const store = JSON.parse(await readFile(new URL('../results/electron_tetrahedral_spinor_store.json', import.meta.url), 'utf8'));
const fixture = loadFixture(trial, store);
const close = (a, b, epsilon = 1e-12) => assert.ok(Math.abs(a - b) < epsilon, `${a} != ${b}`);

test('all four discrete display prefixes match the exact source export', () => {
  for (let i = 0; i < 4; i++) close(distance(stateAt(fixture, fixture.initial, i + 1), fixture.prefixes[i]), 0);
});
test('supplied interpolation stays normalized and preserves native face-block recovery', () => {
  const seeds = [fixture.initial, preparedSpinor(0, 0), preparedSpinor(Math.PI, 1.2), preparedSpinor(1.3, 2.1, 0.7)];
  for (const initial of seeds) for (let i = 0; i <= 80; i++) {
    const z = stateAt(fixture, initial, i / 20);
    close(spinorNorm(z), 1); close(Math.hypot(...bloch(z)), 1);
    const blocks = sourceBlocks(fixture, z);
    close(blocks.flat().reduce((sum, x) => sum + x[0] ** 2 + x[1] ** 2, 0), 1);
    close(distance(decodeBlocks(fixture, blocks), z), 0);
  }
});
test('completed loop preserves the base while reversing the retained amplitude', () => {
  for (const initial of [fixture.initial, preparedSpinor(0, 0), preparedSpinor(1.3, 2.1, 0.7)]) {
    const end = stateAt(fixture, initial, 4);
    close(distance(end, initial.map(x => scale(-1, x))), 0);
    bloch(end).forEach((x, i) => close(x, bloch(initial)[i]));
    close(Math.abs(relativePhase(initial, end)), Math.PI);
    close(distance(gauge(initial).canonical, gauge(end).canonical), 0);
  }
});
test('phase chart switches at the missing pole without losing the native state', () => {
  const south = preparedSpinor(Math.PI, 1.2, 0.4), g = gauge(south);
  assert.equal(g.index, 1);
  close(g.canonical[1][0], 1); close(g.canonical[1][1], 0);
  close(distance(decodeBlocks(fixture, sourceBlocks(fixture, south)), south), 0);
  assert.equal(gauge(fixture.initial).index, 0);
});
test('local two-direction frame is orthonormal and tangent to the ray sphere', () => {
  for (const seed of [fixture.initial, preparedSpinor(0, 0), preparedSpinor(Math.PI, 0), preparedSpinor(1.1, 2.7)]) {
    const r = bloch(seed), [u, v] = localDirections(r);
    close(Math.hypot(...u), 1); close(Math.hypot(...v), 1);
    close(u.reduce((sum, x, i) => sum + x * v[i], 0), 0);
    for (const tangent of [u, v]) close(tangent.reduce((sum, x, i) => sum + x * r[i], 0), 0);
  }
});
test('mismatched source matrices and face projectors are rejected', () => {
  const changed = structuredClone(trial); changed.display_fixture.steps[0].matrix[0][0] = ['2', '0'];
  assert.throws(() => loadFixture(changed, store), /mismatch|Interpolation/);
  const changedStore = structuredClone(store); changedStore.face_projectors[0][0][0] = [['0', '0'], ['0', '0']];
  assert.throws(() => loadFixture(trial, changedStore), /recovery/);
});
test('electron SVG preview is reproducible from the recorded fixture', async () => {
  const saved = await readFile(new URL('../demos/minimal-data-packet/electron-preview.svg', import.meta.url), 'utf8');
  assert.equal(saved, electronSvg(fixture));
  assert.notEqual(saved, electronSvg(fixture, fixture.initial, 4, true));
});
