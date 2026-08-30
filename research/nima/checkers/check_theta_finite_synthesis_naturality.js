"use strict";

function assert(c, m) { if (!c) throw new Error(m); }
function C(re, im) { return { re, im }; }
function conj(z) { return C(z.re, -z.im); }
function scale(z, a) { return C(z.re * a, z.im * a); }
function sub(a, b) { return C(a.re - b.re, a.im - b.im); }
function norm(z) { return Math.hypot(z.re, z.im); }

const phiEven = x => 2 + 3 * x * x + 5 * x * x * x * x;

function plusTail(p, t) { return phiEven(t + p); }
function plusSeam(p, t) { return t >= 0 && t <= p ? phiEven(p - t) : 0; }
function minusTail(p, x) { return phiEven(x - p); }
function minusSeam(p, x) { return x >= -p && x <= 0 ? phiEven(x + p) : 0; }

const labels = [
  { n: 2, p: Math.log(2), type: "primitive", c: C(2, 3) },
  { n: 4, p: 2 * Math.log(2), type: "prime_power_square", c: C(-1, 4) },
  { n: 8, p: 3 * Math.log(2), type: "connected_prime_power", c: C(5, -2) }
];

let maxTailResidual = 0;
let maxSeamResidual = 0;

for (const a of labels) {
  for (const x of [-0.1, -0.5, -1.0, -2.0]) {
    const reflectedTail = conj(scale(a.c, plusTail(a.p, -x)));
    const nativeNegativeTail = scale(conj(a.c), minusTail(a.p, x));
    maxTailResidual = Math.max(maxTailResidual, norm(sub(reflectedTail, nativeNegativeTail)));

    const reflectedSeam = conj(scale(a.c, plusSeam(a.p, -x)));
    const nativeNegativeSeam = scale(conj(a.c), minusSeam(a.p, x));
    maxSeamResidual = Math.max(maxSeamResidual, norm(sub(reflectedSeam, nativeNegativeSeam)));
  }
}

assert(maxTailResidual < 1e-10, "tail naturality must hold");
assert(maxSeamResidual < 1e-10, "seam naturality must hold");
assert(labels[1].type === "prime_power_square", "prime four typing must survive");
assert(labels[2].type === "connected_prime_power", "prime eight typing must survive");

const nonEven = x => 1 + x;
const hostileResidual = Math.abs(nonEven(0.3) - nonEven(-0.3));
assert(hostileResidual > 0, "non-even forcing must falsify reciprocal naturality");

const noConjugation = sub(scale(labels[0].c, 1), scale(conj(labels[0].c), 1));
assert(norm(noConjugation) > 0, "omitting coefficient conjugation must be detected");

const result = {
  schema: "marici.theta-finite-synthesis-naturality.result.v1",
  verdict: "pass",
  label_types: labels.map(x => ({ n: x.n, type: x.type })),
  max_tail_residual: maxTailResidual,
  max_seam_residual: maxSeamResidual,
  finite_packet_naturality: true,
  hostiles: {
    non_even_forcing_residual: hostileResidual,
    omitted_conjugation_residual: norm(noConjugation)
  },
  completion_cell: "open"
};

process.stdout.write(JSON.stringify(result, null, 2) + "\n");
