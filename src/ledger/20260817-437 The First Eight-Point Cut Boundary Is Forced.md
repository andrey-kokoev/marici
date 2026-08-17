---
id: 437
date: 2026-08-17
title: The First Eight-Point Cut Boundary Is Forced
---

# The First Eight-Point Cut Boundary Is Forced

The first higher-multiplicity gate can be separated into two logically distinct
questions: what the six-by-four boundary must be, and whether an eight-point
interior class restricts to it.  This entry settles the first question without
pretending that the second has already been posed by an available class.

Fix the octagon diagonal (D_{05}).  It cuts the octagon into the hexagon
((0,1,2,3,4,5)) and quadrilateral ((0,5,6,7)).  The diagonals compatible
with the cut split canonically as
[
9+2=11,
]
so the link of (D_{05}) is exactly the join of the hexagon and quadrilateral
noncrossing-diagonal complexes.  Its face counts by residual diagonal number
are
[
(1,11,39,56,28).
]
This is an explicit bijection, not merely an equality of cardinalities.

Loading every face by a subset of its diagonals gives
[
1075=215\cdot5
]
boundary cells.  With degree (4-|F|+|H|), their chain ranks are
[
(28,168,375,369,135),
]
the convolution of the established six-point ranks
((14,63,93,45)) with the four-point ranks ((2,3)).

There is a mild orientation issue: lexicographic octagon order interleaves the
two factors.  The checker computes the canonical left/right shuffle sign on
every face.  After that reorientation, all 369 admissible radial incidences
agree exactly with the tensor-product incidence signs.  Thus no hidden sign
obstruction occurs at the carrier boundary.

Entry 436 supplies a primitive oriented six-point line, while the oriented
four-point interval supplies its primitive unit.  Their external product is
therefore the forced primitive (+1) line on this boundary.  This is the
right-hand side of the first Cut-naturality square.

The important negative control is equally sharp: no eight-point interior
transform or physical class has yet been constructed.  Consequently this
calculation does **not** prove Cut naturality.  It fixes the unique boundary
target against which such a class can be tested.  The next gate is to construct
the smallest octagon interior carrier compatible with this boundary and ask
whether the forced line extends; failure to extend is now a genuine
obstruction rather than an orientation ambiguity.

The executable audit is
`research/voevodsky/check_n8_six_by_four_cut_boundary.py`.
