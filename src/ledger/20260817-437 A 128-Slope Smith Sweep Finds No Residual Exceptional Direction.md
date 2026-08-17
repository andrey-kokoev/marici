---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# A 128-Slope Smith Sweep Finds No Residual Exceptional Direction

## Record

Status: bounded intrinsic-support sweep following Entries 421, 423, 426, and 433.

## Hard-to-vary claim

If the exceptional master-image Fitting divisor has support away from the
frozen strict transforms, then a broad test of the intrinsic
minimum-over-minors Smith invariant should encounter a slope where either the
generic rank 10 or generic valuation 66 fails.

A chosen maximal minor is inadmissible after Entry 433.

## Frozen test

Use the ordinary exceptional chart
[
E=t,qquad X_2=ct
]
and the intrinsic invariant
[

u_{m master}
=
delta_{r+10}([E M])-delta_r(E).
]

The computation used the prime field
[
mathbf F_{2305843009213693951},
]
truncation (mathbf F[t]/(t^{12})), and 128 distinct deterministic
pseudorandom slopes generated from seed (mathtt{0x9e3779b97f4a7c15}).
The already classified directions
[
c=0,qquad c=1,qquad c=	frac12
]
were excluded. Eight slopes were independently repeated at exact-form degree
10 after the degree-8 sweep.

## Result

All 128 degree-8 samples satisfy
[
q=10,qquad 
u_{m master}=66.
]

There are no residual samples. All eight degree-10 cross-checks reproduce the
same pair.

Thus
[
oxed{	ext{the bounded 128-slope intrinsic sweep finds no unclassified
exceptional direction}.}
]

## Interpretation

This result is invariant under the minor-chart criticism of Entry 433 because
it uses determinantal minima, not one selected determinant. Together with the
measured tangent excesses, it strengthens the candidate
[
5[c=1]+15[c=	frac12].
]

It does not derive that divisor. A finite pseudorandom sweep cannot exclude a
sparse residual polynomial whose roots miss the sample.

## Classification

- 128 generic sampled directions: existing exceptional coefficient geometry;
- residual sampled support: none;
- frozen strict-transform multiplicities: unchanged at 5 and 15;
- new carrier datum: none;
- saturated Fitting generator: still uncomputed.

## Epistemic boundary

This is a bounded finite-field search sweep, not a symbolic primary
decomposition and not a proof over characteristic zero. The pseudorandom seed,
field, exclusions, truncation, and degree cross-check are frozen in the
certificate.

## Next falsifier

Derive an a priori degree bound for the saturated leading Fitting divisor on
the exceptional (mathbf P^1), or construct the compatible
exact-plus-master quotient determinant directly. Once the degree is bounded
by 20, the already measured multiplicities 5 and 15 exhaust it and force
[
(c-1)^5(2c-1)^{15}
]
up to a unit. Without that degree bound, retain the expression only as a
supported conjecture.

## Evidence

- research/benincasa/dlog-smith-slope-scan-certificate.json
- research/benincasa/marici-gm/src/bin/marked_tangency_support.rs
