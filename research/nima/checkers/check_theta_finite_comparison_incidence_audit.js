"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function rank(matrix) {
  const a = matrix.map(row => row.slice());
  const rows = a.length;
  const cols = a[0].length;
  let r = 0;
  for (let c = 0; c < cols && r < rows; c++) {
    let pivot = r;
    while (pivot < rows && Math.abs(a[pivot][c]) < 1e-12) pivot++;
    if (pivot === rows) continue;
    [a[r], a[pivot]] = [a[pivot], a[r]];
    const p = a[r][c];
    for (let j = c; j < cols; j++) a[r][j] /= p;
    for (let i = 0; i < rows; i++) {
      if (i === r) continue;
      const f = a[i][c];
      for (let j = c; j < cols; j++) a[i][j] -= f * a[r][j];
    }
    r++;
  }
  return r;
}

const incidence = [
  [1, 1, 1, 1],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
];

const mixing = [
  [1, 1, 1, 1, 1, 1],
  [1,-1, 1,-1, 1,-1],
  [1, 1,-1,-1, 1, 1],
  [1,-1,-1, 1, 1,-1],
  [1, 1, 1, 1,-1,-1],
  [1,-1, 1,-1,-1, 1]
];

function multiply(A, B) {
  return A.map(row => B[0].map((_, j) =>
    row.reduce((s, x, k) => s + x * B[k][j], 0)));
}

assert(rank(incidence) === 1, "source incidence rank fixture failed");
assert(rank(mixing) === 6, "boundary mixing fixture not invertible");
assert(rank(multiply(mixing, incidence)) === 1,
  "invertible mixing incorrectly increased incidence rank");

const fullyRealized = [
  [1,0,0,0,0,0],
  [0,1,0,0,0,0],
  [0,0,1,0,0,0],
  [0,0,0,1,0,0],
  [0,0,0,0,1,0],
  [0,0,0,0,0,1]
];
assert(rank(fullyRealized) === 6, "six-direction positive fixture failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.finite_comparison_incidence_audit.result.v1",
  verdict: "actual_theta_span_blocked_before_completion_parametrix",
  declared_boundary_directions: 6,
  realized_two_prime_rank: 1,
  rank_deficit: 5,
  invertible_mixing_rank_preservation_checked: true,
  abstract_observer_profiles_are_not_source_instantiation: true,
  next_gate: "construct_complete_finite_common_comparison_incidence"
}, null, 2));
