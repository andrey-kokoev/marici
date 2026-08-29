"use strict";

function assert(c, m) { if (!c) throw new Error(m); }
function matVec(A, x) { return A.map(r => r.reduce((s, a, i) => s + a * x[i], 0)); }
function multiply(A, B) {
  return A.map(r => B[0].map((_, j) => r.reduce((s, a, k) => s + a * B[k][j], 0)));
}
function equal(A, B) { return JSON.stringify(A) === JSON.stringify(B); }

const F = [[0, 1], [1, 0]];
const scalarJ = [[1, 1]];
const scalarFB = [[1]];
assert(equal(multiply(scalarJ, F), multiply(scalarFB, scalarJ)),
  "scalar comb observer must be natural");

const odd = [1, -1];
const scalarOdd = matVec(scalarJ, odd);
assert(scalarOdd[0] === 0, "scalar observer must kill the odd sector");
assert(JSON.stringify(matVec(F, odd)) !== JSON.stringify(odd),
  "the invisible odd sector must carry nontrivial action");

const fullJ = [[1, 0], [0, 1]];
const fullFB = F;
assert(equal(multiply(fullJ, F), multiply(fullFB, fullJ)),
  "full observer lift must retain naturality");
assert(matVec(fullJ, odd).some(x => x !== 0), "full observer must separate the odd mode");

const badPrimitive = [[1, 0]];
const badSquare = [[0, 1]];
const primitiveResidual = multiply(badPrimitive, F);
const squareResidual = multiply(badSquare, F);
assert(!equal(primitiveResidual, badPrimitive), "gradewise hostile must expose primitive residual");
assert(!equal(squareResidual, badSquare), "gradewise hostile must expose square residual");

const result = {
  schema: "marici.theta-global-action-observer-lift.result.v1",
  verdict: "pass",
  scalar_naturality: true,
  scalar_observer_odd_kernel_dimension: 1,
  full_observer_naturality: true,
  full_observer_kernel_dimension: 0,
  global_additive_action: "exact",
  boundary_observer_lift: "missing",
  next_residuals: ["primitive_grade", "square_grade"]
};

process.stdout.write(JSON.stringify(result, null, 2) + "\n");
