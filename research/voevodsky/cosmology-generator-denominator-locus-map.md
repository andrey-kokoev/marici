# Generator denominator-locus map

## Result

Every A12 labelled generator now has a source-derived pole-locus signature:

- `T` applied to IBP rows: `V(K)` together with all five `V(q_i)` loci;
- `T` applied to K rows and every `S_K` row: `V(K)`;
- `T` applied to q rows and every `Q` row: the indexed `V(q_i)`.

The rule covers 43,564 generators. All 87,128 squared-axis transport checks preserve the signature because exponent shifts do not alter family, pole, level, or q index.

## Falsification

Pole locus is not geometric support. None of the 43,564 mapped generators has a cycle constructor, closed-chain witness, or inclusion into a source complex. A fabricated `V(K)` label is rejected. Rational-presentation singularities therefore cannot populate the geometrization contract's support field.

## Disposition

Retain the complete transport-invariant pole-locus map as algebraic provenance. Defer geometric realization at the first missing typed object: a cycle or sheaf object on each locus with a verified inclusion. Its acceptance test is recorded once in the result.

Continue on the independent executable field: construct and test an algebraic source differential. No waiting-only geometric-support leaf is opened.

## Verification

- `research/voevodsky/check_cosmology_generator_denominator_locus_map.py` — exit 0
- `research/voevodsky/results/cosmology_generator_denominator_locus_map.json`
