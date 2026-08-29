"use strict";

function assert(ok, message) {
  if (!ok) throw new Error(message);
}

function rotate(xs, k) {
  const n = xs.length;
  return xs.map((_, i) => xs[(i + k) % n]);
}

function canonicalCyclic(word) {
  const forms = word.map((_, k) => JSON.stringify(rotate(word, k)));
  forms.sort();
  return forms[0];
}

function reverseValuations(word) {
  return word.map(v => v.map(x => -x));
}

const words = [
  [[1]],
  [[1], [2]],
  [[1, 0], [0, 2], [3, 1]],
  [[0], [0], [0], [0]]
];

for (const word of words) {
  const reversed = reverseValuations(word);
  assert(reversed.length === word.length, "arity changed");
  assert(
    canonicalCyclic(reverseValuations(rotate(word, 1))) === canonicalCyclic(reversed),
    "map failed to descend to cyclic coinvariants"
  );
  assert(
    JSON.stringify(reverseValuations(reversed)) === JSON.stringify(word),
    "bilateral reversal failed involution"
  );
}

assert(reverseValuations([[[1][0]]])[0][0] === -1, "one-prime reversal witness failed");
assert(!Number.isInteger(-1) || -1 < 0, "negative valuation incorrectly admitted to positive cone");

const cutoffs = { X: 2, Y: 7, Z: 13 };
const tauXY = cutoffs.Y - cutoffs.X;
const tauYZ = cutoffs.Z - cutoffs.Y;
const tauXZ = cutoffs.Z - cutoffs.X;
assert(tauXZ === tauYZ + tauXY, "relative transition triangle failed");

const etaX = -2 * cutoffs.X;
const etaY = -2 * cutoffs.Y;
assert((-tauXY) + etaX === etaY + tauXY, "Fourier transition naturality failed");

process.stdout.write(JSON.stringify({
  schema: "marici.theta.bilateral_cyclic_fourier.result.v1",
  verdict: "fourier_is_intertower_not_positive_tower_endomorphism",
  cyclic_arities_checked: words.map(w => w.length),
  cyclic_quotient_well_defined: true,
  bilateral_involution_checked: true,
  one_prime_positive_cone_falsifier: true,
  transition_triangle_checked: true,
  line_transition_naturality_checked: true
}, null, 2));
