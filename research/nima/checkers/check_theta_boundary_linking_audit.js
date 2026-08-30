"use strict";

function assert(c, m) { if (!c) throw new Error(m); }

function support(v) { return v.map(x => x !== 0); }
function product(a, b) { return a.map((x, i) => x * b[i]); }
function classify(forward, backward) {
  const forwardSupport = support(forward);
  const backwardSupport = support(backward);
  const positive = support(product(forward, backward));
  const negative = support(product(backward, forward));
  return {
    crossing: forwardSupport.some(Boolean) || backwardSupport.some(Boolean),
    globally_two_sided: forwardSupport.some(Boolean) && backwardSupport.some(Boolean),
    portwise_two_sided: forwardSupport.map((x, i) => x && backwardSupport[i]),
    positive_image_support: positive,
    negative_image_support: negative,
    full: positive.every(Boolean) && negative.every(Boolean)
  };
}

const arithmetic = classify([1, 1, 0], [1, 1, 0]);
assert(arithmetic.crossing && arithmetic.globally_two_sided, "arithmetic sublink must be two-sided");
assert(!arithmetic.full, "arithmetic sublink must miss the seam port");
assert(arithmetic.positive_image_support[2] === false, "seam idempotent is the proper-ideal witness");

const completed = classify([1, 1, 1], [1, 1, 1]);
assert(completed.full, "adding the seam passage must fill the declared diagonal model");

const oneWaySeam = classify([1, 1, 1], [1, 1, 0]);
assert(oneWaySeam.globally_two_sided, "arithmetic ports remain two-sided");
assert(oneWaySeam.portwise_two_sided[2] === false, "seam port must lack its backward passage");
assert(!oneWaySeam.full, "forward seam transport without a backward seam pairing is not full");

const sameTracePartial = classify([1.5, 1.5, 0], [1.5, 1.5, 0]);
assert(1 + 1 + 1 === 1.5 + 1.5 + 0, "scalar traces must match");
assert(!sameTracePartial.full, "same scalar trace must not repair the missing seam ideal");

const result = {
  schema: "marici.theta-boundary-linking-audit.result.v1",
  verdict: "pass",
  arithmetic_sublink: arithmetic,
  completed_diagonal_model: completed,
  one_way_seam_hostile: oneWaySeam,
  same_trace_hostile: sameTracePartial,
  decisive_witness: "continuum seam idempotent outside both arithmetic composite image ideals",
  current_profile: "typed_not_faithful"
};

process.stdout.write(JSON.stringify(result, null, 2) + "\n");
