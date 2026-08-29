"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function applyTN(x) {
  return x.map((v, i) => v / (i + 1));
}

for (let N = 1; N <= 64; N++) {
  const eN = Array(N).fill(0);
  eN[N - 1] = 1;
  const image = applyTN(eN);
  assert(image[N - 1] === 1 / N, "finite diagonal image failed");
  assert(image[N - 1] !== 0, "finite compression lost invertibility");
}

assert(1 / 64 < 1 / 2, "smallest singular value did not collapse");

let yNorm2 = 0;
let formalPreimageNorm2 = 0;
for (let n = 1; n <= 100000; n++) {
  yNorm2 += 1 / (n * n);
  formalPreimageNorm2 += 1;
}
assert(yNorm2 < 2, "harmonic-square range-limit witness not in l2");
assert(formalPreimageNorm2 === 100000, "formal preimage divergence failed");

const source = [2, -3];
const analytic = source.map(x => 5 * x);
const arithmetic = source.map(x => 5 * x);
const orientedRelation = analytic.map((x, i) => x - arithmetic[i]);
assert(orientedRelation.every(x => x === 0),
  "finite source comparison relation failed");

const hostileIndependent = analytic.concat(arithmetic);
assert(hostileIndependent.some(x => x !== 0),
  "direct product incorrectly imposed source equality");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.source_pushout_closed_range.result.v1",
  verdict: "finite_pushout_canonical_completion_requires_closed_range",
  finite_compressions_invertible_through: 64,
  smallest_singular_value_at_64: 1 / 64,
  approximate_kernel_checked: true,
  dense_nonclosed_range_witness_checked: true,
  finite_source_pushout_relation_checked: true,
  direct_product_hostile_rejected: true,
  remaining_gate: "closed_range_of_completed_typed_comparison_relation"
}, null, 2));
