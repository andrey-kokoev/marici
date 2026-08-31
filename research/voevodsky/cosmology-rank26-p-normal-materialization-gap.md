# Rank-26 p-normal materialization gap

## Question

Does existing rank-26 prior art already materialize the full p-normal relation-module computation needed after the protocol gate?

## Claim boundary

This packet audits source availability. It does not compute the full labelled rank-26 derivative matrix, construct a Bockstein, construct a global contour, or assign a physical period.

## Disposition

The p-normal protocol requires the rank-26 labelled relation rows at

\[
(x,y,z)=(3,6,-3),
\qquad p=x+y+3z=0,
\qquad x+y+z=6.
\]

It then requires first derivatives along

\[
n_x=(1,0,0), \qquad n_y=(0,1,0),
\]

with p-tangent comparison direction

\[
n_x-n_y=(1,-1,0).
\]

Re-reading the available rank-26 artifacts shows that this computation is not yet materialized. The nearest stored Rees packets are total-energy packets at

\[
(3,5,-8),
\]

where total energy is zero and

\[
p(3,5,-8)=-16.
\]

Their connection is `d/dE + A_z at fixed x,y with z=E-x-y`, and their tangent directions are

\[
(1,0,-1), \qquad (0,1,-1).
\]

These are total-energy tangents, not p-tangents, since

\[
dp(1,0,-1)=-2,
\qquad
 dp(0,1,-1)=-2.
\]

The checker scanned 157 Benincasa rank-26 JSON summaries. None materializes the p-normal test point `(3,6,-3)` in the scanned rank-26 corpus, and none advertises a p-normal rank-26 summary field. Therefore the total-energy/gamma rank-26 packets cannot be relabelled as the p-normal computation. Only their algorithmic pattern may be reused.

## Missing materialization

The next real computation must supply:

1. rank-26 labelled relation rows evaluated at `(3,6,-3)` on `p=0`;
2. first derivatives along `nx=(1,0,0)` and `ny=(0,1,0)`;
3. reduction modulo the special exact image and the p-tangent derived span generated from `nx-ny=(1,-1,0)`;
4. a map from any surviving quotient line to the ordered wall/exceptional-face horn column.

No relative Bockstein or physical period follows from the current stored rank-26 packets.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_materialization_gap.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_materialization_gap.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_materialization_gap.py`
