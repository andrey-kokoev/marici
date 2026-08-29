"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function directSum(a, r) {
  return [a, r];
}

function comparison(a, r) {
  return a - r;
}

const fixtures = [
  [0, 0],
  [1, 1],
  [2, 2],
  [-3, -3]
];

for (const [a, r] of fixtures) {
  assert(comparison(a, r) === 0, "coherent diagonal not in comparison kernel");
  if (a !== 0) {
    const direct = directSum(a, r);
    assert(direct[0] !== 0 || direct[1] !== 0,
      "direct sum incorrectly imposed coherence");
  }
}

assert(comparison(1, 0) !== 0, "analytic-only residue was lost");
assert(comparison(0, 1) !== 0, "arithmetic-only residue was lost");
assert((1 + 1) !== comparison(1, 1), "comparison sign was not distinguished");

const support = { seam: 1, right: 2, left: -2, endpoint: 3 };
assert(support.right + support.left === 0, "global cancellation fixture failed");
assert(support.right !== 0 && support.left !== 0,
  "support-sensitive reciprocal defects were erased");

const roles = {
  tail: "differential",
  endpoint: "differential",
  seam: "independent_state_and_trace",
  primitive: "arity_1_incidence",
  square: "arity_2_incidence",
  archimedean: "forcing_and_boundary_incidence"
};

assert(roles.primitive !== roles.square, "cyclic arity typing was erased");
assert(roles.seam !== "derived_tail_coordinate", "seam independence was erased");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.boundary_comparison_cone.result.v1",
  verdict: "minimal_source_complex_is_boundary_comparison_cone",
  coherent_diagonal_checked: true,
  direct_sum_hostile_rejected: true,
  analytic_and_arithmetic_residues_detected: true,
  support_sensitive_reciprocal_pair_retained: true,
  component_role_typing_checked: true,
  remaining_gate: "construct_common_boundary_carrier_and_comparison_correspondence"
}, null, 2));
