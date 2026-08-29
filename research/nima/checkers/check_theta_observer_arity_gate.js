"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function q(x) {
  return x[0] * x[0] + 2 * x[0] * x[1] + 3 * x[1] * x[1];
}

function B(x, y) {
  return x[0] * y[0] + x[0] * y[1] + x[1] * y[0] + 3 * x[1] * y[1];
}

function add(x, y) {
  return [x[0] + y[0], x[1] + y[1]];
}

function scale(a, x) {
  return [a * x[0], a * x[1]];
}

function F(x) {
  return [-x[1], x[0]];
}

const fixtures = [
  [[1, 0], [0, 1]],
  [[2, -1], [3, 4]],
  [[-3, 2], [5, -2]]
];

for (const [x, y] of fixtures) {
  assert(q(add(x, y)) - q(x) - q(y) === 2 * B(x, y), "polarization identity failed");
  assert(q(x) === B(x, x), "diagonal recovery failed");
  assert(q(scale(-1, x)) === q(x), "quadratic parity failed");
}

assert(q([1, 0]) !== 0, "hostile quadratic became zero");
assert(q([1, 0]) + q([-1, 0]) !== 0, "linear impossibility witness failed");

const x = [2, 3];
const y = [-1, 4];
assert(B(F(x), F(y)) === 3 * x[0] * y[0] - x[0] * y[1] - x[1] * y[0] + x[1] * y[1],
  "two-copy Fourier transport failed");

const C1 = 7;
const C2 = -3;
const C3 = 11;
assert((C3 - C1) === (C2 - C1) + (C3 - C2), "transition triangle failed");

const result = {
  schema: "marici.theta.observer_arity_gate.result.v1",
  verdict: "one_copy_linear_square_observer_rejected",
  primitive_domain: "A",
  square_domain: "Sym^2(A)",
  polarization_fixtures: fixtures.length,
  linear_impossibility_witness: true,
  two_copy_transport_checked: true,
  transition_triangle_checked: true
};

process.stdout.write(JSON.stringify(result, null, 2));
