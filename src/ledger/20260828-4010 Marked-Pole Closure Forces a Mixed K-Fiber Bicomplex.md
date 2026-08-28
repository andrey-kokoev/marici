# 4010 — Marked-Pole Closure Forces a Mixed K–Fiber Bicomplex

## Status

Established in the tested finite-field source-jet models at primes (32009) and (32003), in residue charts (G_{12}) and (G_{31}).

## Frozen objects

Start with the repaired simple-pole quotient (Q_{26}), obtained from the 36 simple-pole monomials by the ten relations internal to that sector.

Entry 4007 identified the first source-covariant-jet residual outside (Q_{26}):

[
(0,1,2,1,2,1;(0,0)).
]

No ambient truncation or fitted projection is allowed.

## Finite falsifiers

First adjoin only that class, producing a rank-27 candidate. It is not jet-closed. At the sixth evaluated jet call:

- (G_{12}) requires ((0,2,2,1,1,1;(0,0)));
- (G_{31}) requires that class together with
  ((0,1,1,2,2,1;(0,0))) and
  ((0,1,2,2,1,1;(0,0))).

The result is identical at both primes.

Occurrence closure then forces the square-free degree-two layer in the five labelled pole factors: the (q)-pole and four marked poles. This layer has dimension

[
inom52=10,
]

giving a rank-36 candidate over (Q_{26}).

The rank-36 candidate is still not jet-closed. At the fourteenth evaluated jet call the first forbidden residuals are

[
(2,1,2,1,1,1;(0,0))
]

and, chart-dependently,

[
(2,1,2,1,1,1;(0,1))
quad	ext{or}quad
(2,1,2,1,1,1;(1,0)).
]

Thus the next required target changes three grades simultaneously:

- the (K)-pole order rises;
- a marked occurrence remains doubled;
- a fibre-degree direction appears and is exchanged between occurrence charts.

## Narrow conclusion

The covariant-jet operation does not close on:

1. the repaired simple-pole quotient;
2. a one-class doubled-pole extension;
3. the complete square-free degree-two marked-pole layer.

Therefore the missing constructor is not a finite marked-pole summand. It must couple marked occurrence grade, (K)-pole filtration, and fibre degree in one source-derived relative bicomplex.

This is the extension obstruction port. It is distinct from the descent obstruction port, which asks whether an operation coequalizes the ten-relation kernel pair.

No new carrier divisor is indicated.

## Next falsifier

Derive the smallest source-defined trigraded target complex containing

[
	ext{marked occurrence degree}
oplus
	ext{(K)-pole filtration}
oplus
	ext{fibre degree},
]

including its chart transition and differential. Then test whether the covariant jet is a morphism of that complex. Do not form closure by iteratively adjoining ambient residual columns.

## Artifacts

- `research/benincasa/checkers/check_rank27_doubled_pole_adapter_closure.py`
- `research/benincasa/checkers/check_rank30_doubled_pole_occurrence_adapter_closure.py`
- `research/benincasa/checkers/check_rank32_pairwise_doubled_pole_adapter_closure.py`
- `research/benincasa/checkers/check_rank36_degree2_boolean_adapter_closure.py`
- `research/benincasa/results/rank27-doubled-pole-adapter-*.json`
- `research/benincasa/results/rank30-doubled-pole-adapter-*.json`
- `research/benincasa/results/rank32-pairwise-doubled-pole-adapter-*.json`
- `research/benincasa/results/rank36-degree2-boolean-adapter-*.json`

Sequence claim: `seqclaim-8e7e1c1d9588d93d2e1b1fce`.
