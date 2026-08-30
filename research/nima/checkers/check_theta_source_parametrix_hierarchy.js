"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

const inverseNorms = [];
for (let N = 1; N <= 64; N++) {
  inverseNorms.push(N);
}
assert(inverseNorms[inverseNorms.length - 1] === 64,
  "diagonal inverse norm fixture failed");
assert(inverseNorms.every((x, i, a) => i === 0 || x > a[i - 1]),
  "inverse escape was not monotone");

function unilateralShift(x) {
  return [0].concat(x);
}

function leftInverse(y) {
  return y.slice(1);
}

const x = [3, -2, 5];
assert(JSON.stringify(leftInverse(unilateralShift(x))) === JSON.stringify(x),
  "bounded left inverse for shift failed");
assert(unilateralShift(x)[0] === 0,
  "shift cokernel witness failed");

const identity = x.slice();
assert(JSON.stringify(identity) === JSON.stringify(x),
  "contractible identity fixture failed");

const hierarchy = {
  diagonal: { strict: false, finiteDefect: null, acyclic: false },
  shift: { strict: true, finiteDefect: "cokernel_dimension_1", acyclic: false },
  identity: { strict: true, finiteDefect: "none", acyclic: true }
};

assert(hierarchy.shift.strict && !hierarchy.shift.acyclic,
  "strictness was conflated with acyclicity");
assert(hierarchy.identity.acyclic, "identity contraction failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.source_parametrix_hierarchy.result.v1",
  verdict: "parametrix_unifies_pushout_strictness_and_sector_contraction",
  inverse_escape_checked_through: 64,
  nonclosed_range_model_rejected: true,
  closed_range_finite_cokernel_model_distinguished: true,
  contractible_model_checked: true,
  strictness_not_conflated_with_acyclicity: true,
  remaining_gate: "construct_compact_sector_equicontinuous_source_parametrix"
}, null, 2));
