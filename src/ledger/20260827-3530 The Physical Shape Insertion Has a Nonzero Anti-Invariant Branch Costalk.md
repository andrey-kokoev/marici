---
author: marici.Benincasa
date: 2026-08-27
---

# 3530 — The Physical Shape Insertion Has a Nonzero Anti-Invariant Branch Costalk

## Hard-to-vary claim

At the representative cyclic (A_1) point, the ordered reduction of the two
native triple occurrences has zero marked (s_{12})-residue but a nonzero
anti-invariant Cayley--Menger branch costalk. In the source normalization, its
two sheet values are (-17/6) and (17/6).

## Ordered calculation

Use

\[
x=g_1,qquad y=g_2,qquad z=s_{12}
\]

with the orientation inherited from ((a,b,c)). The coordinate Jacobian is

\[
da\wedge db\wedge dc=\frac12,dx\wedge dy\wedge dz.
\]

Sum the two source occurrences carrying the complete local wall triple before
reduction. Remove the cubic (x)- and (y)-poles by the canonical second
derivatives. The exact remaining coefficient is

\[
\frac{64z^5(z^2+8z+17)}
{3(z-1)(z+4)^3(z^2)^{5/2}}.
\]

The factor (z^5/(z^2)^{5/2}) has opposite values on the two normalized
square-root sheets. Including the coordinate Jacobian gives

\[
c_+=-\frac{17}{6},
\qquad
c_-=\frac{17}{6}.
\]

Thus the anti-invariant difference is (17/3).

## Typing consequence

No (1/z) pole remains after the proper-face reduction. Hence this is not a
ternary marked-wall residue. It is a finite costalk value on the rank-one
anti-invariant (A_1) branch object. This distinction explains why the class
was invisible in the proper marked-wall circuit census.

## Interpretation boundary

The coefficient class is nonzero. A physical observable is not yet proved:
the Bunch--Davies relative cycle has not been specialized to this local
costalk, and no intersection pairing has been computed.

## Next falsifier

Derive the source relative-cycle specialization at the cyclic (A_1) point.
Track orientation and deck character, then pair it with the costalk vector
((-17/6,17/6)). A deck-even cycle gives zero; a source-authorized deck-odd
component activates the class.

## Evidence

- `research/benincasa/compute_shape_branch_mixed_costalk.py`;
- `research/benincasa/results/shape-branch-mixed-costalk.json`.

Allocator claim: `seqclaim-8cdeaf90ab2c0509047f9c04`.
