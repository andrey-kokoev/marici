# All-even linear transport induction

## Result

For every even ambient degree `A>=12`, squared-axis multiplication sends each labelled generator at A to the same family, pole, level, axis or mark at `A+2`, with exponent increased by two and coefficient one.

Domain closure is symbolic:

- IBP: degree at most A maps to degree at most `A+2`;
- K: degree at most `A-4` maps to degree at most `(A+2)-4`;
- q: degree at most `A-1` maps to degree at most `(A+2)-1`;
- columns: degree at most `A+4` maps to degree at most `(A+2)+4`.

The two generators commute because exponent addition in `N²` commutes. Raw K and q rows shift identically; parameter derivatives commute with parameter-independent monomial multiplication; the IBP Leibniz correction is parameter-independent and vanishes under both tangent and `nx` differentiation.

The checker verifies all descriptors for eleven even degrees from 12 through 32, totaling 881,584 mixed-composition checks. A deliberate degree-four shift into a single `A->A+2` step is rejected with boundary overflow two.

Combined with exact A12 words and verified A16 composition, this gives a quantified family of finite source-typed morphisms and transports each parity-orbit word to every even `A>=12`. It does not construct a colimit.

## Claim boundary

No source differential, geometric support, DNC comparison, exceptional localization, horn, or physical period is constructed.

## Verification

- `research/voevodsky/check_cosmology_all_even_linear_transport_induction.py` — exit 0
- `research/voevodsky/results/cosmology_all_even_linear_transport_induction.json`
