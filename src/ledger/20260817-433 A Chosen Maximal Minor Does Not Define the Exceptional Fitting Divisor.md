---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# A Chosen Maximal Minor Does Not Define the Exceptional Fitting Divisor

## Record

Status: negative determinant-reconstruction test following Entries 421, 423, and 426.

## Hard-to-vary claim

After dividing the master-image determinant by its generic exceptional order
(t^{66}), a single fixed maximal-minor quotient chart should recover the
intrinsic exceptional support polynomial. If true, its leading coefficient
would have zeros only at the frozen strict-transform directions
(c=1) and (c=	frac12).

## Frozen chart

Use
[
E=t,qquad X_2=ct.
]
The intrinsic Smith difference is
[

u_{m master}
=
delta_{r+10}([E M])-delta_r(E),
]
where (delta_k) is the minimum valuation of the (k)-minors, (E) is the
exact-form block, and (M) is the twelve-master block.

For comparison, numerator and denominator maximal minors were selected at a
generic base slope and then held fixed as functions of (c).

## Result

The intrinsic Smith valuation remains
[

u_{m master}=66
]
at the generic tested slopes, including (c=5).

The fixed-minor quotient instead has valuation 67 at (c=5). Permuting the
ambient row and column order before deterministic pivot selection did not
remove this extra zero: the tested selections still landed in the same
non-generating minor chart.

Therefore
[
oxed{	ext{a chosen maximal-minor ratio is not an intrinsic generator of
the exceptional Fitting line}.}
]

The (c=5) zero is a minor-chart artifact, not coefficient support, because
the minimum-over-all-minors Smith invariant does not jump there.

## Surviving invariant statement

Entries 421 and 426 still give the valuation-divisor candidate
[
5[c=1]+15[c=	frac12].
]
On the ordinary exceptional chart this has principal representative
[
(c-1)^5(2c-1)^{15}
]
up to a unit. This is supported by the exhaustive first-direction census and
the measured tangent excesses, but it is not yet an explicitly derived
global Fitting generator.

## Classification

- (c=5): noncanonical minor-chart artifact;
- (c=1): frozen (E-X_2) strict-transform support, excess 5;
- (c=	frac12): frozen (E-2X_2) strict-transform support, excess 15;
- new carrier datum: none;
- explicit exceptional Fitting generator: not yet derived.

## Epistemic boundary

This result refutes the proposed single-minor reconstruction method, not the
valuation-divisor candidate. Deterministic pivot permutations do not prove a
gcd over all maximal minors. No zero of one chosen minor may be promoted to
coefficient support without checking the determinantal minimum.

## Next falsifier

Compute the leading (t^{66}) Fitting ideal itself: either obtain the gcd of
the leading coefficients of sufficiently many certified maximal minors, or
construct a compatible exact-plus-master quotient presentation whose
determinant generates the saturated Fitting line. Test whether its
exceptional divisor is exactly
[
5[c=1]+15[c=	frac12].
]
Any surviving zero away from the frozen strict transforms is the first
candidate for new coefficient support; it is not a carrier stratum unless
independent incidence data require it.

## Evidence

- research/benincasa/marici-gm/src/bin/marked_tangency_support.rs
- Entry 421: first-direction census
- Entry 423: intrinsic Smith-length formula
- Entry 426: quadratic tangent excesses
