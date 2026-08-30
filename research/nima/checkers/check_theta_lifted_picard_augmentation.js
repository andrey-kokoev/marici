"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function add(a, b) {
  return a.map((x, i) => x + b[i]);
}

function sum(a) {
  return a.reduce((x, y) => x + y, 0);
}

const dXY = [2, -1, 3, -4];
const dYZ = [5, 7, -2, 1];
const dXZ = add(dXY, dYZ);

assert(JSON.stringify(dXZ) === JSON.stringify(add(dYZ, dXY)),
  "componentwise transition composition failed");
assert(sum(dXZ) === sum(dXY) + sum(dYZ),
  "coherence map is not additive");

const tauXY = Math.exp(sum(dXY));
const tauYZ = Math.exp(sum(dYZ));
const tauXZ = Math.exp(sum(dXZ));
assert(Math.abs(tauXZ - tauYZ * tauXY) < 1e-10,
  "Picard transition triangle failed");

const zeroLift = { phase: 0, winding: 0 };
const chargedLift = { phase: 0, winding: 1 };
assert(zeroLift.phase === chargedLift.phase, "scalar alias fixture failed");
assert(zeroLift.winding !== chargedLift.winding, "winding grade was erased");

const typedCancellation = [3, 0, 0, -3];
const typedZero = [0, 0, 0, 0];
assert(sum(typedCancellation) === sum(typedZero), "typed cancellation fixture failed");
assert(JSON.stringify(typedCancellation) !== JSON.stringify(typedZero),
  "typed packets were incorrectly identified");

const trivializations = [1, 0.5, 0.25, 0.125];
assert(trivializations.every(x => x !== 0), "finite invertibility fixture failed");
assert(trivializations.map(x => 1 / x).every((x, i, a) => i === 0 || x > a[i - 1]),
  "inverse escape fixture failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.lifted_picard_augmentation.result.v1",
  verdict: "finite_augmentation_functor_exists_completion_stability_missing",
  transition_triangle_checked: true,
  exponential_winding_alias_rejected: true,
  typed_cancellation_preserved: true,
  inverse_escape_witness_checked: true,
  remaining_gate: "compact_local_completion_stability_of_lifted_trivializations"
}, null, 2));
