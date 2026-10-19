// Numerical display of the exact, source-bound trial. No physical dynamics.
export const add = (a, b) => [a[0] + b[0], a[1] + b[1]];
export const scale = (s, a) => [s * a[0], s * a[1]];
export const mul = (a, b) => [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]];
export const conjugate = a => [a[0], -a[1]];
export const norm2 = a => a[0] ** 2 + a[1] ** 2;
export const apply = (matrix, z) => matrix.map(row => row.reduce((sum, x, i) => add(sum, mul(x, z[i])), [0, 0]));
export const spinorNorm = z => z.reduce((sum, x) => sum + norm2(x), 0);
export const distance = (a, b) => Math.hypot(...a.flatMap((x, i) => [x[0] - b[i][0], x[1] - b[i][1]]));
const polar = angle => [Math.cos(angle), Math.sin(angle)];
const numeric = x => typeof x === 'number' ? x : x.includes('/') ? Number(x.split('/')[0]) / Number(x.split('/')[1]) : Number(x);
const complex = z => z.map(numeric);
const coefficient = z => z.map(([a, b]) => numeric(a) + numeric(b) * Math.sqrt(3));
const matrix = m => m.map(row => row.map(complex));
export function bloch(z) {
  const off = mul(z[0], conjugate(z[1]));
  return [2 * off[0], -2 * off[1], norm2(z[0]) - norm2(z[1])];
}
export function preparedSpinor(theta, phi, phase = 0) {
  return [scale(Math.cos(theta / 2), polar(phase)), scale(Math.sin(theta / 2), polar(phase + phi))];
}
export function gauge(z) {
  const index = norm2(z[0]) > 1e-12 ? 0 : 1;
  const angle = Math.atan2(z[index][1], z[index][0]);
  return { index, angle, canonical: z.map(x => mul(polar(-angle), x)) };
}
export function relativePhase(initial, z) {
  const overlap = initial.reduce((sum, x, i) => add(sum, mul(conjugate(x), z[i])), [0, 0]);
  return Math.abs(norm2(overlap) - 1) < 1e-9 ? Math.atan2(overlap[1], overlap[0]) : null;
}
export function interpolatedOperation(index, t) {
  const angle = (index < 2 ? 1 : -1) * Math.PI * t / 2;
  if (index % 2 === 0) return [[polar(angle), [0, 0]], [[0, 0], polar(-angle)]];
  const c = Math.cos(angle), s = Math.sin(angle);
  return [[[c, 0], [s, 0]], [[-s, 0], [c, 0]]];
}
export function stateAt(fixture, initial, progress) {
  const clamped = Math.max(0, Math.min(4, progress));
  const steps = Math.floor(clamped);
  let z = initial.map(x => [...x]);
  for (let i = 0; i < steps; i++) z = apply(fixture.operations[i], z);
  if (steps < 4 && clamped !== steps) z = apply(interpolatedOperation(steps, clamped - steps), z);
  return z;
}
export function sourceBlocks(fixture, z) {
  return fixture.projectors.map(p => apply(p, z).map(x => scale(1 / Math.sqrt(2), x)));
}
export function decodeBlocks(fixture, blocks) {
  const result = [[0, 0], [0, 0]];
  for (let j = 0; j < blocks.length; j++) {
    const decoded = apply(fixture.projectors[j], blocks[j]);
    for (let i = 0; i < 2; i++) result[i] = add(result[i], scale(1 / Math.sqrt(2), decoded[i]));
  }
  return result;
}
export function loadFixture(trial, store) {
  if (trial.schema !== 'marici.electron-configuration-dimension-trial.v1' || !trial.verification_passed || !Object.values(trial.checks).every(x => x === true)) throw new Error('The recorded source trial did not pass.');
  const data = trial.display_fixture;
  const expectedLabels = ['U', 'V', 'U inverse', 'V inverse'];
  if (!data || data.steps.length !== 4 || data.steps.some((step, i) => step.label !== expectedLabels[i])) throw new Error('Unsupported source word.');
  const fixture = {
    initial: data.initial_spinor.map(complex), operations: data.steps.map(step => matrix(step.matrix)),
    labels: data.steps.map(step => step.label), prefixes: data.steps.map(step => step.spinor.map(complex)),
    projectors: store.face_projectors.map(p => p.map(row => row.map(coefficient))),
  };
  if (fixture.projectors.length !== 4 || store.arrows.length !== 144 || Math.abs(spinorNorm(fixture.initial) - 1) > 1e-12) throw new Error('Unexpected native fixture.');
  for (let i = 0; i < 4; i++) {
    if (distance(stateAt(fixture, fixture.initial, i + 1), fixture.prefixes[i]) > 1e-12) throw new Error('Source prefix mismatch.');
    if (distance(interpolatedOperation(i, 1).flat(), fixture.operations[i].flat()) > 1e-12) throw new Error('Interpolation does not reach its source endpoint.');
  }
  if (distance(stateAt(fixture, fixture.initial, 4), fixture.initial.map(x => scale(-1, x))) > 1e-12) throw new Error('The source loop is not the expected minus identity.');
  if (distance(decodeBlocks(fixture, sourceBlocks(fixture, fixture.initial)), fixture.initial) > 1e-12) throw new Error('Native face-block recovery failed.');
  return fixture;
}
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const unit = v => { const size = Math.hypot(...v); return v.map(x => x / size); };
export function localDirections(r) {
  const u = unit(cross(Math.abs(r[1]) < 0.9 ? [0, 1, 0] : [1, 0, 0], r));
  return [u, unit(cross(r, u))];
}
export function formatComplex(z) {
  const n = x => Math.abs(x) < 5e-7 ? '0' : Number(x.toFixed(4)).toString();
  return `${n(z[0])} ${z[1] < -5e-7 ? '−' : '+'} ${n(Math.abs(z[1]))}i`;
}
export function electronSvg(fixture, initial = fixture.initial, progress = 0, erased = false) {
  const z = stateAt(fixture, initial, progress), r = bloch(z), r0 = bloch(initial), phase = gauge(z);
  const project = v => [185 + 100 * (v[0] - v[2]) / Math.sqrt(2), 200 - 100 * (-v[0] + 2 * v[1] - v[2]) / Math.sqrt(6)];
  const current = project(r), mark = project(r0), dirs = localDirections(r0);
  let tangent = '';
  dirs.forEach((v, i) => { for (const sign of [-1, 1]) {
    const end = project(r0.map((x, j) => x + sign * 0.36 * v[j]));
    tangent += `<path d="M${mark.join(' ')}L${end.join(' ')}" stroke="${i ? '#ffc179' : '#78d6e8'}" stroke-width="3"/>`;
  } });
  const tip = [475 + 77 * Math.cos(phase.angle), 200 - 77 * Math.sin(phase.angle)];
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 430" role="img" aria-labelledby="title"><title id="title">Two-direction spin-ray base and retained local phase</title><rect width="660" height="430" rx="16" fill="#101827"/><g font-family="system-ui,sans-serif" fill="#edf3fa"><text x="24" y="35" font-size="18">n = 2 base + retained phase / source word ${progress.toFixed(2)} of 4</text><circle cx="185" cy="200" r="100" fill="#78d6e8" fill-opacity=".05" stroke="#526981"/><ellipse cx="185" cy="200" rx="100" ry="30" fill="none" stroke="#526981" stroke-dasharray="5 5"/>${tangent}<path d="M185 200L${current.join(' ')}" stroke="#78d6e8" stroke-width="2"/><circle cx="${current[0]}" cy="${current[1]}" r="6" fill="#78d6e8"/><circle cx="${mark[0]}" cy="${mark[1]}" r="5" fill="#ffe4a0"/><text x="${mark[0] + 8}" y="${mark[1] - 8}" fill="#ffe4a0">l</text><text x="100" y="335">spin-ray base</text><circle cx="475" cy="200" r="77" fill="none" stroke="#526981"/><path d="M475 200L${tip.join(' ')}" stroke="#9bf0bd" stroke-width="4"/><circle cx="${tip[0]}" cy="${tip[1]}" r="6" fill="#9bf0bd"/>${erased ? '<path d="M475 200L552 200" stroke="#bdc5d1" stroke-width="2" stroke-dasharray="5 5"/>' : ''}<text x="403" y="335">${phase.index ? 'β' : 'α'}-chart phase</text><text x="24" y="395" font-size="14" fill="#b8cada">Same ray at return; the retained spinor changes sign.</text></g></svg>\n`;
}
