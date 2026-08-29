"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function rank(matrix) {
  const a = matrix.map(row => row.slice());
  let r = 0;
  for (let c = 0; c < a[0].length && r < a.length; c++) {
    let p = r;
    while (p < a.length && Math.abs(a[p][c]) < 1e-10) p++;
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

const evenRows = [
  [1,0,0,1,0,0],
  [0,1,0,0,1,0],
  [0,0,1,0,0,1]
];

const J = [1,1,1,-1,-1,-1];
const lambdas = [Math.log(2),Math.log(3),Math.log(5),
                 Math.log(2),Math.log(3),Math.log(5)];

function afterPower(row, power) {
  return row.map((x, i) => x * Math.pow(lambdas[i], power));
}

const staticPacket = evenRows.concat([J]);
assert(rank(staticPacket) === 4, "static packet rank was not four");

const fullObservability = evenRows.concat([
  afterPower(J,0),
  afterPower(J,1),
  afterPower(J,2)
]);
assert(rank(fullObservability) === 6,
  "Krylov seam observations did not reach full rank");

const v1 = [1,-1,0,-1,1,0];
const v2 = [1,0,-1,-1,0,1];

function dot(a,b) {
  return a.reduce((s,x,i) => s + x*b[i],0);
}

for (const v of [v1,v2]) {
  assert(staticPacket.every(row => Math.abs(dot(row,v)) < 1e-10),
    "static kernel witness failed");
  assert(Math.abs(dot(afterPower(J,1),v)) > 1e-10 ||
         Math.abs(dot(afterPower(J,2),v)) > 1e-10,
    "dynamic observation failed to expose hidden mode");
}

const oddVandermonde = [
  [1,1,1],
  [Math.log(2),Math.log(3),Math.log(5)],
  [Math.log(2)**2,Math.log(3)**2,Math.log(5)**2]
];
assert(rank(oddVandermonde) === 3, "odd Vandermonde rank failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.rank_four_dynamic_observability.result.v1",
  verdict: "rank_four_static_packet_is_fully_observable_under_prime_scale_action",
  static_rank: 4,
  static_kernel_dimension: 2,
  odd_krylov_rank: 3,
  full_observability_rank: 6,
  hidden_basis_vectors_exposed: 2,
  static_isomorphism_still_false: true,
  remaining_gate: "uniform_observability_under_arithmetic_completion"
}, null, 2));
