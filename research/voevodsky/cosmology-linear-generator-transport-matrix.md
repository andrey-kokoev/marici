# Linear generator transport matrix

## Question

Does squared-axis multiplication define a labelled linear map from every A12 source generator to A14 that commutes with source and target rows?

## Result

The map sends each `T`, `S_K`, or `Q` descriptor to the same descriptor with exponent increased by `(2,0)` or `(0,2)`, with coefficient one. It covers 21,964 `T`, 2,880 `S_K`, and 18,720 `Q` generators. The same descriptor rule acts on all 21,964 `nx` target rows.

Across four exact-reconstruction primes, both axes, all source blocks, and all targets, 524,224 row-commutation tests have zero residual. Linearity extends the basis map uniquely over the rationals.

The constructor derivation is direct: multiplication shifts every column monomial; raw K and q multiplication rows shift identically; parameter differentiation commutes with the parameter-independent monomial; the IBP Leibniz correction is parameter-independent and vanishes under both tangent and `nx` differentiation.

This falsifies the interpretation that prior certificate-word failures show nonexistence of generator transport. They instead expose an origin-decoding or certificate-interface mismatch. The next test applies this verified map to every stored source word and localizes that mismatch.

## Claim boundary

This is a linear map between labelled finite-cutoff relation presentations. It is not yet an A16 coherence theorem, source differential, geometric support map, DNC comparison, or horn consequence.

## Verification

- `research/voevodsky/check_cosmology_linear_generator_transport_matrix.py` — exit 0
- `research/voevodsky/results/cosmology_linear_generator_transport_matrix.json`
