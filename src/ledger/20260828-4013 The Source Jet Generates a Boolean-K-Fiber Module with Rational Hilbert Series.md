# 4013 — The Source Jet Generates a Boolean–K-Fiber Module with Rational Hilbert Series

## Status

Established for the frozen source generator graph through (K)-depth four in residue charts (G_{12}) and (G_{31}) at prime (32009). The depth-three orbit was also constructed before this prediction.

## Source generators

A basis label has the form

[
(k;ell_0,ell_1,ell_2,ell_3,ell_4;(a,b)),
]

where:

- (k) is the (K)-pole grade;
- each (ell_iin{1,2}) is a labelled pole level for the (q)-pole and four marked poles;
- ((a,b)) is fibre bidegree.

The source connection has two typed generator families.

The (K)-generator acts by

[
kmapsto k+1
]

and shifts fibre degree by a monomial appearing in an external derivative of (K).

The five occurrence generators act by

[
ell_imapstoell_i+1
]

and shift fibre degree by a monomial appearing in the corresponding external derivative of (q_i).

These generators were extracted from the frozen connection formula, not inferred from failed residuals.

## Orbit census

Starting from the three source numerator monomials, the depth-three reachable graph has rank

[
4800
]

in both charts. Its generator-distance profile is

[
3, 33, 165, 519, 1065, 1383, 1083, 465, 84.
]

The Hilbert census factorizes between (K)-pole and occurrence degree. Through depth three:

[
H_{le3}(s,t)
=
3(1+t)^5
left(
1+6s+15s^2+28s^3
ight).
]

The occurrence coefficients are

[
1,5,10,10,5,1,
]

the Boolean rank profile on five labelled pole occurrences.

The (K)-fibre coefficients are

[
1,6,15,28,
]

which equal

[
(k+1)(2k+1)
]

for (k=0,1,2,3).

This predicted the depth-four coefficient

[
45
]

and total rank

[
3cdot 2^5(1+6+15+28+45)=9120.
]

The independently rerun depth-four graph has rank (9120) in both charts and the predicted (K)-marginal (4320=3cdot2^5cdot45).

## Rational series

The resulting source-generator Hilbert law is

[
H(s,t)
=
3(1+t)^5
sum_{kge0}(k+1)(2k+1)s^k
=
3(1+t)^5\frac{1+3s}{(1-s)^3}.
]

This is a statement about the labelled source-generator module before exact-relation quotienting.

## Narrow conclusion

Finite marked-pole closure failed because it retained the Boolean occurrence factor while truncating the intrinsically unbounded (K)-fibre factor.

The correct next object is therefore a source-derived module or bicomplex with:

- a finite Boolean occurrence algebra on five labels;
- an unbounded filtered (K)-fibre module with cubic-denominator Hilbert growth;
- chart transitions exchanging the two fibre-degree directions.

No new carrier divisor is indicated.

## Next falsifier

Construct the exact-relation submodule inside this factored generator module. Test whether its quotient preserves the Hilbert factorization or introduces genuine coupling between the Boolean and (K)-fibre factors.

The first finite test is at (K)-depths three and four:

1. compute the relation-submodule Hilbert table;
2. compute the quotient Hilbert table;
3. test rank-one factorization in ((k,	ext{occurrence degree}));
4. transport both tables between (G_{12}) and (G_{31}).

## Artifacts

- `research/benincasa/checkers/check_source_generator_trigraded_orbit.py`
- `research/benincasa/checkers/factor_source_generator_trigraded_orbit.py`
- `research/benincasa/results/source-generator-trigraded-orbit-*.json`
- `research/benincasa/results/source-generator-trigraded-orbit-*-factorization.json`

Sequence claim: `seqclaim-7d88ac33f582769632b41685`.