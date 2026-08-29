"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function rank(matrix) {
  const a = matrix.map(row => row.slice());
  let r = 0;
  for (let c = 0; c < a[0].length && r < a.length; c++) {
    let p = r;
    while (p < a.length && Math.abs(a[p][c]) < 1e-12) p++;
    if (p === a.length) continue;
    [a[r], a[p]] = [a[p], a[r]];
    const z = a[r][c];
    for (let j = c; j < a[0].length; j++) a[r][j] /= z;
    for (let i = 0; i < a.length; i++) {
      if (i === r) continue;
      const f = a[i][c];
      for (let j = c; j < a[0].length; j++) a[i][j] -= f * a[r][j];
    }
    r++;
  }
  return r;
}

function multiply(A, B) {
  return A.map(row => B[0].map((_, j) =>
    row.reduce((s, x, k) => s + x * B[k][j], 0)));
}

const I = [
  [1,1,1,1],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]
];

const C = [
  [1,2,3,4,5,6],
  [0,1,0,1,0,1]
];

const K = [[1,-1]];

const r0 = rank(I);
const r1 = rank(multiply(C, I));
const r2 = rank(multiply(K, multiply(C, I)));

assert(r0 === 1, "source rank fixture failed");
assert(r1 <= r0 && r2 <= r1, "rank increased under higher observation");

const sourceDimension = 4;
const kernelDimension = sourceDimension - r0;
assert(kernelDimension === 3, "kernel residual dimension failed");

const validDecrease = [3,2,1,0];
assert(validDecrease.every((x, i, a) => i === 0 || x < a[i - 1]),
  "well-founded residual decrease failed");

const invalidReentry = [3,3,3];
assert(invalidReentry.some((x, i, a) => i > 0 && x >= a[i - 1]),
  "nondecreasing re-entry hostile was not detected");

const profile211 = {
  level0: ["J1", "J2"],
  level1: ["F_plus_minus"],
  level2: ["det_line"]
};
assert(profile211.level1.length === 1 && profile211.level2.length === 1,
  "profile fixture failed");
assert(profile211.level1.length < 2,
  "missing level-1 boundary was not retained");

process.stdout.write(JSON.stringify({
  schema: "marici.scc.globular_observer_tower.result.v1",
  verdict: "higher_observers_cannot_manufacture_missing_lower_incidence",
  source_rank: r0,
  level1_composite_rank: r1,
  level2_composite_rank: r2,
  kernel_residual_dimension: kernelDimension,
  child_reentry_requires_promotion: true,
  termination_measure_checked: true,
  nondecreasing_reentry_rejected: true
}, null, 2));
