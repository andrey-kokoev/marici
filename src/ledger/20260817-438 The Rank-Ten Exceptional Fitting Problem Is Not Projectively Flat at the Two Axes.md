---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Rank-Ten Exceptional Fitting Problem Is Not Projectively Flat at the Two Axes

## Record

Status: projective-boundary falsification test following Entries 421, 423, 426, 433, and 437.

## Hard-to-vary claim

The generic rank-ten master-image presentation on the first blow-up might
extend unchanged to both boundary points of the exceptional
(mathbf P^1_{[E:X_2]}). If so, its saturated leading Fitting divisor would
admit a direct global degree count before any further boundary saturation.

The finite falsifier is the intrinsic determinantal difference
[

u_{m master}
=
delta_{r+q}([E M])-delta_r(E)
]
at the two omitted projective directions, using both blow-up charts.

## Frozen test

The ordinary chart is
[
E=t,qquad X_2=ct,
]
whose point (c=0) is ([E:X_2]=[1:0]).

The reciprocal chart is
[
X_2=t,qquad E=ct,
]
whose point (c=0) is ([E:X_2]=[0:1]).

The computation used
(mathbf F_{2305843009213693951}[t]/(t^{12})) and was repeated at
exact-form degrees 8 and 10. No support factor or rank correction was added
after specialization.

## Result

At the ordinary boundary,
[
[E:X_2]=[1:0],
qquad
(q,
u_{m master})=(7,55).
]

At the reciprocal boundary,
[
[E:X_2]=[0:1],
qquad
(q,
u_{m master})=(3,13).
]

Both results agree at exact-form degrees 8 and 10. They differ from the
punctured generic pair
[
(q,
u_{m master})=(10,66).
]

Therefore
[
oxed{
	ext{the unsaturated rank-ten master-image presentation is not flat across
either projective axis.}
}
]

## Interpretation

The two exceptional boundary points are not residual directions:

- ([1:0]) is the strict transform of the frozen soft divisor (X_2=0);
- ([0:1]) is the strict transform of the frozen total-energy divisor (E=0).

Thus the rank loss is supported on existing energy geometry. It supplies no
new carrier incidence.

However, it invalidates the proposed shortcut from the punctured
rank-ten calculation to a global degree bound on
(mathbf P^1). The candidate
[
5[c=1]+15[c=	frac12]
]
lives on the rank-ten open locus only after the two source-derived boundary
components have been saturated. A degree bound for its compactification
cannot be read from the unsaturated presentation.

## Classification

- (X_2=0) boundary: existing soft support;
- (E=0) boundary: existing total-energy support;
- punctured exceptional rank-ten locus: unchanged;
- residual projective boundary support: none;
- new carrier datum: none;
- naive unsaturated projective degree argument: refuted.

## Epistemic boundary

This is a finite-field truncated Smith calculation, not a construction of the
doubly saturated Fitting sheaf. The stable degree-8/10 agreement establishes
the tested presentation behavior, but not its characteristic-zero flat
extension. The result refutes only the unsaturated projective degree route; it
does not refute the two-point divisor candidate on the punctured rank-ten
locus.

## Next falsifier

Construct the rank-ten master-image module after source-derived saturation by
both boundary ideals ((E)) and ((X_2)). Compute its transition function
between the ordinary and reciprocal charts. That transition—not the raw
presentation—determines the compactified Fitting-line degree. Test whether it
has degree 20. If it does, the measured multiplicities 5 and 15 exhaust the
divisor; if it does not, the two-point expression remains non-exhaustive.

## Evidence

- research/benincasa/dlog-smith-projective-infinity-certificate.json
- research/benincasa/marici-gm/src/bin/marked_tangency_support.rs
