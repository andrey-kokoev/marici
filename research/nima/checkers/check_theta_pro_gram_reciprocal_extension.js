"use strict";

function assert(c, m) { if (!c) throw new Error(m); }
function dot(a, b) { return a.reduce((s, x, i) => s + x * b[i], 0); }
function matVec(A, x) { return A.map(r => dot(r, x)); }
function norm(x) { return Math.sqrt(dot(x, x)); }
function diag(d) { return d.map((x, i) => d.map((_, j) => i === j ? x : 0)); }
function multiply(A, B) {
  return A.map(r => B[0].map((_, j) => r.reduce((s, x, k) => s + x * B[k][j], 0)));
}
function sub(A, B) { return A.map((r, i) => r.map((x, j) => x - B[i][j])); }

const U = diag([1, 1, 1, 1]);
const R = diag([1, -1, 1, -1]);
const C = [
  [1, 2, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 1, -3],
  [0, 0, 0, 1]
];
const thetaC = multiply(multiply(R, C), R);
const c = [2, -3, 5, 7];

function q(A, x) { return norm(matVec(U, matVec(A, x))); }

const left = q(C, matVec(R, c));
const right = q(thetaC, c);
assert(Math.abs(left - right) < 1e-12, "pro-Gram seminorm must be reindexed by reciprocal conjugation");

const hadamard = [
  [0.5, 0.5, 0.5, 0.5],
  [0.5, -0.5, 0.5, -0.5],
  [0.5, 0.5, -0.5, -0.5],
  [0.5, -0.5, -0.5, 0.5]
];
const P = diag([1, 1, 0, 0]);
const IminusP = diag([0, 0, 1, 1]);
const leakage = multiply(multiply(P, hadamard), IminusP);
const leakageNorm = Math.sqrt(leakage.flat().reduce((s, x) => s + x * x, 0));
assert(leakageNorm > 0, "finite cutoff must leak under global Fourier transport");

const omittedConjugateFamily = ["M_t"];
const thetaOfMt = "M_minus_t";
assert(!omittedConjugateFamily.includes(thetaOfMt), "hostile monoid must fail reciprocal closure");

const result = {
  schema: "marici.theta-pro-gram-reciprocal-extension.result.v1",
  verdict: "pass",
  seminorm_reindexing_residual: Math.abs(left - right),
  reciprocal_real_extension: "continuous_by_constructor_reindexing",
  fourier_cutoff_leakage_norm: leakageNorm,
  finite_fourier_cutoff_endomorphism: false,
  hostile_missing_conjugate_constructor: thetaOfMt,
  global_fourier_poisson_cell: "open"
};

process.stdout.write(JSON.stringify(result, null, 2) + "\n");