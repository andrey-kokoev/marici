# Rank-three continuum positivity is a normalized discriminant problem

For three variables define

\[
 D_3(x_1,x_2,x_3)=\det(K_F(x_i,x_j)).
\]

Permuting two variables simultaneously permutes the corresponding rows and
columns, so `D_3` is symmetric. When `x_i=x_j`, two rows and two columns
coalesce. Analyticity therefore forces a double zero. Hence

\[
 D_3=\prod_{i<j}(x_i-x_j)^2\,Q_3(x_1,x_2,x_3),
\]

where `Q_3` extends analytically across every collision diagonal. The
confluent rank-three theorem is exactly positivity of the diagonal extension
of `Q_3`; separated rank-three positivity is `Q_3>=0` off the diagonals.

This quotient is the correct continuum variable. Raw determinants have no
uniform positive lower bound because the Vandermonde factor vanishes at point
collisions.

On all 165 triples of `{0,0.001,...,0.01}`, directed evaluation gives

\[
 1.3924815518\,10^{-20}<Q_3<1.3929433397\,10^{-20}.
\]

Thus the normalized margin varies by less than `0.034%` across the hostile
grid.

The continuum step is now closed by Newton elimination. Applying divided-
difference elimination to rows and columns divides the determinant by one
Vandermonde on each side. Hence `Q_3` is the determinant of the matrix of
mixed divided differences of `K_F` through bidegree `(2,2)`. Each entry is an
average of the corresponding normalized mixed derivative over the node hull.

Directed evaluation of those derivative ranges on the single box
`[0,0.01]^2`, including the Cauchy tail after degree 23, gives

\[
 \boxed{Q_3([0,0.01]^3)\subset
 [1.3413135748,1.4441125285]\times10^{-20}.}
\]

Therefore every three-point Loewner determinant is strictly positive for
distinct central points and nonnegative at collisions. This proves continuum
rank-three positivity on `[0,0.01]`. It does not prove higher ranks, global
Loewner positivity, or RH.

## Durable verification

- Checker: `checkers/central_rank_three_loewner_grid.py`
- Result: `results/central-rank-three-loewner-grid.json`
- Continuum checker: `checkers/central_rank_three_loewner_continuum.py`
- Continuum result: `results/central-rank-three-loewner-continuum.json`

## Next obstruction

The identical one-box construction at rank four is not sharp enough. Its
natural determinant enclosure is approximately `[-1.118e-36,1.124e-36]`,
while midpoint evaluation is positive near `3.020e-39`. This is interval
dependency by a factor around 370, not a negative-minor witness. The next
certificate must preserve correlations through an `LDL*`/Schur complement or
subdivide the ordered simplex; merely extending the source Taylor order does
not address this loss.

- Rank-four probe: `checkers/central_rank_four_natural_box_probe.py`
- Probe result: `results/central-rank-four-natural-box-probe.json`

Exact Newton evaluation repairs that loss on the hostile grid. The divided
difference of a monomial is a complete homogeneous symmetric polynomial in
its nodes, so the normalized rank-four matrix can be evaluated without
subtractions. All 330 quadruples on `{0,0.001,...,0.01}` are directed-positive.
The weakest is `(0.007,0.008,0.009,0.01)`, with normalized determinant in
`[3.0190646591e-39,3.0190702736e-39]`. Rank-four continuum positivity remains
open, but no finite grid falsifier survives.

- Rank-four grid checker: `checkers/central_rank_four_loewner_grid.py`
- Rank-four grid result: `results/central-rank-four-loewner-grid.json`

The grid now upgrades to a continuum theorem. Including repeated nodes gives
1001 nondecreasing anchors; the weakest is the fully confluent endpoint
`(0.01,0.01,0.01,0.01)`, above `3.0187703238e-39`. Explicit derivatives of
the complete homogeneous polynomials bound monotone nearest-grid transport by
`3.6629484668e-41`, leaving

\[
 \boxed{Q_4>2.9821408391\times10^{-39}}
\]

on the full ordered simplex. Hence every distinct rank-four Loewner minor on
`[0,0.01]` is strictly positive, with nonnegative confluent limits.

- Rank-four continuum checker: `checkers/central_rank_four_loewner_continuum.py`
- Rank-four continuum result: `results/central-rank-four-loewner-continuum.json`

## Rank five

A Leibniz determinant box loses nine orders at rank five. Structured `LDL*`
shows that the obstruction was instead the degree-23 tail in the eighth mixed
derivative: it was `2.10e-22`, while the fifth pivot is about `6.67e-26`.
Extending the centered source jet through order 61 and `F` through degree 29
reduces that tail to `1.84e-33`.

With the repaired depth, all 462 distinct quintuple configurations on the
central `0.001` grid have strictly positive directed `LDL*` pivots. The weakest
is `(0.006,0.007,0.008,0.009,0.01)`, whose final pivot is above
`6.6652565650e-26`. Confluent anchors and continuum transport remain open.

- Rank-five grid checker: `checkers/central_rank_five_loewner_grid.py`
- Rank-five grid result: `results/central-rank-five-loewner-grid.json`

The confluent audit also passes: all 3003 nondecreasing anchors, including
repeated nodes, have positive directed pivots. The weakest is the fully
confluent upper endpoint `(0.01,...,0.01)`, whose final pivot is above
`6.6651134944e-26`; its normalized determinant is above
`2.0120465530e-64`.

Determinant transport does not close the continuum. A global adjugate bound
costs `3.2836590002e-60` over a half-grid step, about four orders larger than
the determinant margin. This is another representation lesson: the individual
`LDL*` pivots have generous relative margins, while their product is tiny.
The next checker must propagate derivatives through the Newton--`LDL*`
recursion itself rather than differentiate the expanded determinant.

- Confluent-anchor checker: `checkers/central_rank_five_confluent_anchors.py`
- Confluent-anchor result: `results/central-rank-five-confluent-anchors.json`

The differentiated-pivot architecture is now operational at the weakest
anchor. Differentiating the complete-homogeneous Newton matrix and every
`LDL*` recursion step gives a fifth-pivot half-grid linearized cost below
`9.185e-31`, versus pivot margin `6.665e-26`—a safety factor above 72,000.
This is a local derivative certificate; the derivatives must still be
enclosed over each grid cell to justify continuum transport.

This implementation also repaired an execution defect: importing the
rank-five helper previously reran all 462 grid cases. Grid execution is now
confined to the explicit main action, so derivative checkers reuse only the
arithmetic functions.

- Pivot-derivative checker:
  `checkers/central_rank_five_pivot_derivative_probe.py`
- Pivot-derivative result:
  `results/central-rank-five-pivot-derivative-probe.json`

A natural interval extension from the anchor to its endpoint cell
`[0.0095,0.01]^5` is not viable. Although the first four pivots stay positive,
the fifth expands to approximately `[-2.91e-21,1.97e-23]`, versus its true
scale `6.67e-26`; derivative boxes similarly inflate to order `1e-21`.
Straight subdivision would need widths around `1e-8` and is therefore the
wrong representation. The next implementation must retain the five shared
node displacements as affine or centered Taylor symbols through the `LDL*`
recursion, enclosing only the higher-order remainder.

That centered Taylor carrier is now operational through total degree five at
the weakest anchor. Its successive half-grid box budgets are
`8.99e-31, 6.76e-36, 3.75e-41, 1.71e-46, 6.86e-52`. The apparent ratio is
about `5e-6` per degree, and the degree-five polynomial leaves margin
`6.66502e-26`. These coefficients currently use midpoint source data and are
reconnaissance, not directed intervals. The remaining task is to enclose the
Taylor coefficients and prove an all-orders majorant for the rational `LDL*`
remainder.

- Centered Taylor checker: `checkers/central_rank_five_pivot_quadratic_taylor.py`
- Taylor result: `results/central-rank-five-pivot-quadratic-taylor.json`

The midpoint limitation is now removed for the finite source polynomial.
Directed interval coefficients propagated through the full five-variable
degree-five `LDL*` Taylor algebra give polynomial margin
`6.6650237584e-26`; the degree budgets agree with reconnaissance down to the
displayed digits. This certifies the degree-29 source polynomial only. Two
remainders remain deliberately separate: the omitted analytic source tail and
the all-orders rational tail generated by pivot inversions.

- Directed Taylor checker: `checkers/central_rank_five_pivot_taylor_interval.py`
- Directed Taylor result: `results/central-rank-five-pivot-taylor-interval.json`

The omitted analytic source is now injected coefficientwise through Taylor
degree five using unit-disk Cauchy and falling-factorial mixed-derivative
majorants. The coarse allowance raises degree-two-through-five budgets to
`2.4e-32`--`4.3e-32`, still over six orders below the pivot. The rigorous
margin including this source tail is `6.6650083764e-26`. Only the combined
degree-six-and-higher source and rational inversion remainder remains.

That final endpoint-cell remainder is now closed a posteriori. Positive-
coefficient majorants give omitted-source matrix remainder `4.6293e-32` and
known-polynomial remainder `3.4635e-35`; both fit inside a common `1e-30`
entry allowance. Residual bounds for every reciprocal propagate this through
the rational `LDL*` algebra, giving final pivot remainder `1.0167e-30` and

\[
 d_5>6.6649067122\times10^{-26}
\]

on the full endpoint cell `[0.0095,0.01]^5`. The remaining continuum task is
to uniformize the same Taylor-model certificate across the other ordered
cells.

- Taylor-majorant checker:
  `checkers/central_rank_five_pivot_taylor_majorant.py`
- Taylor-majorant result:
  `results/central-rank-five-pivot-taylor-majorant.json`
