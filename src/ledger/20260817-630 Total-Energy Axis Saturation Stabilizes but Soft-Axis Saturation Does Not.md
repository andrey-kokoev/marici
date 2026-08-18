---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Total-Energy Axis Saturation Stabilizes but Soft-Axis Saturation Does Not

## Record

Status: transverse-axis Smith test following Entry 438.

## Hard-to-vary claim

After identifying the two lower-rank boundary points of the exceptional
(mathbf P^1), the generic rank-ten module might admit finite
source-derived elementary transforms at both axes. If so, a generic
second-order transverse arc should produce a cutoff-independent excess over
the generic valuation 66.

## Frozen arcs

Use the nonzero transverse unit (d=3), avoiding the frozen algebraic
branches (X_2=pm E^2).

At the soft axis:
[
E=t,qquad X_2=3t^2.
]

At the total-energy axis:
[
X_2=t,qquad E=3t^2.
]

The intrinsic determinantal difference was computed in
(mathbf F_{2305843009213693951}[t]/(t^{24})) at exact-form degrees
8, 10, and 12.

The initially tested arc (X_2=E^2) was rejected as a saturation probe
because it is exactly the already frozen algebraic branch (D_-).

## Result

Both generic transverse arcs recover master-image rank ten.

At (E=0), the valuation is stable:
[

u_{m master}=93
]
at all three exact-form degrees. Relative to the generic value 66, the
stable transverse excess is
[
oxed{27}.
]

At (X_2=0), the valuations are
[
89,qquad92,qquad95
]
at exact-form degrees (8,10,12). The value increases by 3 whenever the
cutoff increases by 2. Thus no cutoff-independent soft-axis excess is
defined by the present polynomial exact-form presentation.

Therefore
[
oxed{
	ext{the current truncation defines a stable total-energy transform but not
a stable soft-axis transform.}
}
]

## Interpretation

Entry 438 showed that both axes require saturation before a global rank-ten
Fitting line can be discussed. The present test supplies one stable local
number, 27, but it prohibits assigning a second number at the soft axis from
the same truncated presentation.

The drift is presentation dependence, not residual support. Every tested arc
is attached to an already frozen boundary divisor, and no new direction is
introduced. The failure is that the polynomial exact-form tower has not yet
been replaced by a degree-independent completed or graded quotient at the
soft boundary.

Consequently the proposed transition-degree calculation cannot yet be
performed, and no degree-20 conclusion follows.

## Classification

- (E=0) transverse excess 27: stable coefficient-boundary datum;
- (X_2=0) transverse excess: cutoff dependent in the tested presentation;
- algebraic branch (X_2=E^2): existing coefficient support, excluded;
- new carrier datum: none;
- compactified rank-ten Fitting transition: uncomputed.

## Epistemic boundary

The stable (E=0) value is established only in the tested finite-field,
order-24 model. The soft-axis sequence (89,92,95) demonstrates
nonstabilization through degree 12; it does not prove divergence of an
appropriately completed exact-form complex. No extrapolated limiting soft
weight is admissible.

## Next falsifier

Replace the raw polynomial exact-form truncation near (X_2=0) by a
degree-independent graded or completed exact-form quotient, predeclaring the
completion and admissible saturation. Recompute the transverse Smith
difference and test whether it stabilizes. Only after both axis transforms
are canonical may their ordinary/reciprocal transition be used to test a
degree-20 Fitting line.

## Evidence

- research/benincasa/dlog-smith-axis-saturation-certificate.json
- research/benincasa/marici-gm/src/bin/marked_tangency_support.rs
