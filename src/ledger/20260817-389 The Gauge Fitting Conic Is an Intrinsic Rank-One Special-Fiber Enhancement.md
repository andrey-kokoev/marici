---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Gauge Fitting Conic Is an Intrinsic Rank-One Special-Fiber Enhancement

## Question

Entry 388 detected the residual conic
[
C_{m fit}:qquad X_1X_2-E_T^2=0
]
from a bounded rank census. Is this merely a failure of the projection to
master coordinates, or does the full frozen reduction presentation itself
change rank there?

## Full-rank comparison

At generic points, exact-form degree (8) gives full matrix rank (117),
nullity (255), projected gauge rank (2), and pivot mask (24).

At tested conic points, the same presentation gives
[
116,qquad256,qquad3,qquad280.
]
Thus
[
oxed{Deltaoperatorname{rank}A=-1,qquad
Deltadimker A=+1,qquad
Deltaoperatorname{rank}G=+1.}
]

The pattern persists at exact-form degrees (10) and (12). The conic is
therefore not only a bad choice of Pluecker chart or master projection: one
additional homogeneous exact-lift class appears in the special fiber and its
projection is nonzero.

For comparison, the signed-energy wall has a two-dimensional enhancement,
while the ordinary soft wall tested here has the same one-dimensional
enhancement pattern as the conic. This comparison is about ranks, not an
identification of their geometric origins.

## Uniformity sweep

On the (X_1=1) patch, the conic is
[
v=2u^2-u+2.
]
For every
[
u=3,ldots,100
]
and at exact-form degrees (8) and (10), the conic fiber and the two
transverse neighbors (vpm1) were evaluated exactly over the working finite
field.

Results:
[
oxed{196/196}
]
conic fibers have full rank drop one, and
[
oxed{196/196}
]
gain exactly one projected gauge direction. All
[
oxed{392/392}
]
neighboring fibers retain the generic full rank, projected rank, and pivot
mask. No exception occurred.

## Verdict

In the tested family,
[
oxed{C_{m fit}	ext{ is an intrinsic codimension-one rank-one
special-fiber enhancement of the frozen exact-lift presentation}.}
]

This strengthens Entry 388's coefficient-support classification. The
additional direction belongs to the kernel of the source-defined relative
reduction map and survives projection to the master block. No new carrier cell
is required.

The result does not yet prove that a chosen maximal minor contains
(X_1X_2-E_T^2) with multiplicity one, nor that the entire global Fitting
radical has no further components.

## Architectural update

The surviving H2 form is now more specific:
[
	ext{shared carrier and six-functor calculus}
+
	ext{sector-specific relative coefficient presentations}
]
whose special fibers may acquire rank-one classes on internal Fitting
divisors.

This is incompatible with a coefficient architecture determined solely by
the pure elliptic rank-two quotient. It remains compatible with a relative
Gauss--Manin extension over the unchanged carrier.

## Next falsifier

Construct a generic maximal-rank minor and its transverse first jet along
(C_{m fit}). Test whether
[
det M=(X_1X_2-E_T^2),U
]
with (U) a unit generically on the conic. Equivalently, pair the extra right
kernel class and left cokernel class with the transverse derivative of the
presentation matrix.

A nonzero pairing establishes simple Fitting multiplicity. A zero pairing
requires higher normal order or a different minor. Afterward compute the
remaining radical factors and determine whether the new class enters a
rank-one subquotient or only the extension data.

## Epistemic boundary

The sweep is exact but finite-field and evaluation based. It does not replace
a symbolic Fitting-ideal calculation, establish integral normalization, or
identify the physical integration-chain image.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_tangency_support.rs`;
- `research/benincasa/gauge-fitting-conic-uniformity.json`;
- Entry 388.
