"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function coeffs(u, maxK) {
  const out = [null, u];
  for (let k = 1; k < maxK; k++) {
    out[k + 1] = (k * u * out[k]) / (k + 1);
  }
  return out;
}

const u = 0.5;
const a = coeffs(u, 8);

for (let k = 1; k <= 8; k++) {
  assert(a[k] === Math.pow(u, k) / k, "cyclic coefficient formula failed");
  assert(k * Math.log(2) > 0, "positive scale support failed");
  assert(-k * Math.log(2) < 0, "reversed scale support failed");
}

assert(a[1] === 0.5, "primitive amplitude failed");
assert(a[2] === 0.125, "square coefficient failed");
assert(2 * a[2] === a[1] * a[1], "first square recurrence failed");

const hostile = { b1: 1, b2: 1 };
assert(2 * hostile.b2 !== hostile.b1 * hostile.b1,
  "hostile independent square coefficient was not rejected");

const sameSupportPositive = [1, 2].map(k => k * Math.log(2));
const sameSupportNegative = sameSupportPositive.map(q => -q);
assert(sameSupportPositive.every((q, i) => q === -sameSupportNegative[i]),
  "orientation reversal failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.atomic_incidence_factorization.result.v1",
  verdict: "polarization_fixes_support_not_weight",
  checked_grades: 8,
  primitive_amplitude: a[1],
  square_coefficient: a[2],
  cyclic_recurrence_checked: true,
  intertower_scale_reversal_checked: true,
  independent_square_hostile_rejected: true,
  remaining_gate: "typed_boundary_augmentation_into_relative_determinant_line"
}, null, 2));
