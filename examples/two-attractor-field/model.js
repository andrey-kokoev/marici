export const defaults = () => ({ weightA: 1, weightB: 1, damping: 0.3 });
export const attractors = [{ x: -3, y: 0 }, { x: 3, y: 0 }];
export const softening = 0.8;
export function fieldAt(x, y, weights) {
  let vx = 0, vy = 0;
  for (const [i, a] of attractors.entries()) {
    const weight = Number(i ? weights.weightB : weights.weightA);
    if (!Number.isFinite(weight) || weight < 0 || weight > 5) throw new RangeError('Weights must be between 0 and 5');
    const dx = a.x - x, dy = a.y - y;
    const scale = weight / (dx * dx + dy * dy + softening * softening) ** 1.5;
    vx += dx * scale; vy += dy * scale;
  }
  return { x: vx, y: vy, magnitude: Math.hypot(vx, vy) };
}
// Unit-mass dynamics: dx/dt = v, dv/dt = F(x) - damping*v.
// Symmetric drag/kick/drift/kick/drag splitting, fixed simulation timestep.
export function stepParticle(p, weights, damping, dt) {
  if (!Number.isFinite(damping) || damping < 0 || damping > 3 || !Number.isFinite(dt) || dt < 0 || dt > 0.05)
    throw new RangeError('Invalid damping or timestep');
  const drag = Math.exp(-damping * dt / 2);
  const a = fieldAt(p.x, p.y, weights);
  let vx = p.vx * drag + a.x * dt / 2, vy = p.vy * drag + a.y * dt / 2;
  const x = p.x + vx * dt, y = p.y + vy * dt;
  const b = fieldAt(x, y, weights);
  vx = (vx + b.x * dt / 2) * drag; vy = (vy + b.y * dt / 2) * drag;
  return { x, y, vx, vy };
}
export const passRadius = 0.6;
export function targetWeights(weights, target) {
  return { weightA: target === 0 ? weights.weightA : 0, weightB: target === 1 ? weights.weightB : 0 };
}
export function initialTarget(x, y) {
  const distances = attractors.map(a => Math.hypot(x - a.x, y - a.y));
  const nearest = distances[0] <= distances[1] ? 0 : 1;
  return distances[nearest] < 1e-8 ? 1 - nearest : nearest;
}
// A pass is a local minimum of distance within the pole's capture neighborhood.
// Switch the force, not the velocity; no teleporting or instantaneous reversal.
export function stepShuttle(p, weights, damping, dt, target) {
  const next = stepParticle(p, targetWeights(weights, target), damping, dt);
  const a = attractors[target];
  const before = (p.x - a.x) * p.vx + (p.y - a.y) * p.vy;
  const after = (next.x - a.x) * next.vx + (next.y - a.y) * next.vy;
  const close = Math.min(Math.hypot(p.x - a.x, p.y - a.y), Math.hypot(next.x - a.x, next.y - a.y)) <= passRadius;
  const switched = before < 0 && after >= 0 && close;
  return { particle: next, target: switched ? 1 - target : target, switched };
}
export function sampleField(weights) {
  const samples = [];
  for (let y = -5; y <= 5; y += 0.5) for (let x = -8; x <= 8; x += 0.5) {
    const vector = fieldAt(x, y, weights);
    samples.push({ x, y, vx: vector.x, vy: vector.y, magnitude: vector.magnitude });
  }
  return samples;
}
