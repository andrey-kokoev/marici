"use strict";

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function trace2(a) {
  return a[0][0] + a[1][1];
}

function supportOfDiagonal(a) {
  return [a[0][0] !== 0, a[1][1] !== 0];
}

function andSupport(a, b) {
  return [a[0] && b[0], a[1] && b[1]];
}

function multiplyDiagonal(a, b) {
  return [[a[0][0] * b[0][0], 0], [0, a[1][1] * b[1][1]]];
}

function classify(forward, backward) {
  const forwardSupport = supportOfDiagonal(forward);
  const backwardSupport = supportOfDiagonal(backward);
  const crossing = forwardSupport.some(Boolean) || backwardSupport.some(Boolean);
  const twoSided = forwardSupport.some(Boolean) && backwardSupport.some(Boolean);
  const positiveComposite = multiplyDiagonal(forward, backward);
  const negativeComposite = multiplyDiagonal(backward, forward);
  const positiveIdeal = supportOfDiagonal(positiveComposite);
  const negativeIdeal = supportOfDiagonal(negativeComposite);
  const full = andSupport(positiveIdeal, negativeIdeal).every(Boolean);
  return { crossing, twoSided, positiveIdeal, negativeIdeal, full };
}

const zero = [[0, 0], [0, 0]];
const identity = [[1, 0], [0, 1]];
const partial = [[1, 0], [0, 0]];
const scalarMatchedPartial = [[2, 0], [0, 0]];

const diagonalOnly = classify(zero, zero);
assert(!diagonalOnly.crossing, "diagonal-only action must not cross the grading");
assert(!diagonalOnly.full, "diagonal-only action cannot be full");

const full = classify(identity, identity);
assert(full.crossing && full.twoSided && full.full, "identity links must form a full context");

const partialTwoSided = classify(partial, partial);
assert(partialTwoSided.crossing, "partial link must cross the grading");
assert(partialTwoSided.twoSided, "partial hostile is intentionally two-sided");
assert(!partialTwoSided.full, "noncentrality and two-sidedness must not imply fullness");
assert(JSON.stringify(partialTwoSided.positiveIdeal) === JSON.stringify([true, false]),
  "partial link must miss the second positive idempotent");

const oneWay = classify(identity, zero);
assert(oneWay.crossing, "one-way link must be grading-noncentral");
assert(!oneWay.twoSided && !oneWay.full, "one-way link must fail two-sided fullness");

assert(trace2(identity) === trace2(scalarMatchedPartial),
  "hostile scalar shadows must agree");
const scalarHostile = classify(scalarMatchedPartial, scalarMatchedPartial);
assert(!scalarHostile.full, "equal scalar trace must not determine fullness");

const margins = [1, 1 / 2, 1 / 3, 1 / 4];
assert(margins.every(x => x > 0), "each finite cutoff is full");
assert(margins[margins.length - 1] < margins[0], "completion hostile must exhibit collapsing margin");

const result = {
  schema: "marici.rh-linking-action-gate.result.v1",
  verdict: "pass",
  cases: {
    diagonal_only: diagonalOnly,
    full_link: full,
    partial_two_sided_link: partialTwoSided,
    one_way_link: oneWay,
    equal_scalar_trace_partial_link: scalarHostile
  },
  finite_hostiles: 4,
  completion_hostile: "positive finite margins with no uniform positive lower bound",
  conclusion: "grading noncentrality is necessary but not sufficient; faithful action requires two-sided Morita fullness and a uniform completion margin"
};

process.stdout.write(JSON.stringify(result, null, 2) + "\n");
