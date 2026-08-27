# The two RH sectors carry opposite half-spinor parity

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite Clifford typing theorem

## New identification

The rank-three source carrier does more than produce a six-dimensional
hyperbolic double. Its odd rank gives the exterior spin module a canonical
two-sheet grading:

\[
\mathcal S
=
\Lambda^\bullet V^*
=
\mathcal S^+\oplus\mathcal S^-.
\]

Here

\[
\mathcal S^+=\Lambda^{\mathrm{even}}V^*,
\qquad
\mathcal S^-=\Lambda^{\mathrm{odd}}V^*.
\]

For \(\dim V=3\), both half-spinor sectors have dimension four.

The product-formula charge spinor \(\varepsilon\in\Lambda^1V^*\) is odd.
The polarization-exchange or Hodge operation sends degree \(k\) to degree
\(3-k\). Because three is odd, it reverses parity. In particular,

\[
\varepsilon\in\mathcal S^-
\quad\longmapsto\quad
*\varepsilon\in\Lambda^2V^*\subset\mathcal S^+.
\]

Thus the reciprocal quarter-turn exchanges two differently typed
half-spinor sectors. It is not merely a sign change inside one scalar space.

## Relation to the rigged charts

The earlier two-chart architecture distinguishes

\[
\mathcal C_+=E\oplus E',
\qquad
\mathcal C_-=E'\oplus E.
\]

The new result adds a finite Clifford grading to that analytic distinction.
The source and reciprocal boundary spinors occupy opposite parity sectors
before their scalar comparison is formed.

The two labels must not be conflated:

- chart type records which current or covector component is test-like or
  distributional;
- chirality records even or odd exterior degree in the spin representation.

Fourier exchange affects both. A completed correspondence must therefore
transport the rigging and the parity together.

## The discrete local system

The parity label is a canonical \(C_2\) local system over the continuous
hyperbolic carrier. It is not another linear channel. This matches the
post-\(D_5\) Flavor typing, where continuous constructor--observer geometry
is accompanied by a discrete relative-orientation sheet.

In both cases:

- infinitesimal response covectors cannot recover the sheet label;
- a cross-sector coherent operation is required to compare sheets;
- squaring a cross-sector readout may preserve magnitude while erasing its
  orientation type.

This does not identify Flavor CP sign with RH chirality. It identifies their
categorical role: each is discrete relation data over a continuous dual
geometry.

## Why this does not prove RH

Parity constrains which morphisms can connect the two sectors, but it does not
force a nonzero scalar comparison. An odd correspondence can map a nonzero
odd spinor to an even spinor whose terminal pairing still vanishes.

Likewise, the reciprocal-even Maslov hostile can be installed separately on
each parity-compatible block. Therefore chirality rejects type-erasing
models, but not all off-seam intersections.

The theta smoothing kernel must now satisfy two independent gates:

1. it has the source-required parity and chart variance;
2. its induced Lagrangian transport avoids the Maslov divisor in each open
   half-plane.

The first is a typing theorem. The second remains the RH-bearing theorem.

## A parity-sensitive falsifier

In odd rank, any proposed polarization exchange that preserves exterior
parity is incorrectly typed. In even rank, Hodge exchange preserves parity,
so the same argument cannot manufacture the required two-sheet grading.

This gives a finite hostile comparison:

- rank three: every complement map sends even subsets to odd subsets and
  odd subsets to even subsets;
- rank two: every complement map preserves subset parity.

The parity reversal is therefore forced by the source rank, not by a chosen
phase convention.

## Consequence for the categorical object

The deeper RH object is now refined to:

> A two-chart rigged hyperbolic correspondence carrying a product-formula
> pure-spinor line and an odd-rank half-spinor local system, whose theta
> comparison must be both parity-correct and Maslov-transverse off seam.

The remaining construction problem is to derive the parity degree of the
actual theta smoothing correspondence and then test its transverse chamber.

## Verification

The checker enumerates the exterior basis in ranks two and three. It verifies
the half-spinor dimensions, the parity of the charge one-form, complement
degree under Hodge exchange, parity reversal in rank three, and parity
preservation in the even-rank hostile.

