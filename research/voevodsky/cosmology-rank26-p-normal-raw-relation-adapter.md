# Rank-26 p-normal raw-relation adapter

## Question

Can the existing complete labelled Laurent relation generator be adapted to the p-normal point and p-normal directions before quotient reduction?

## Claim boundary

This packet checks raw source-row availability and finite-difference consistency only. It does not compute the quotient by the special exact image, does not compute the p-tangent quotient, does not identify a surviving Bockstein line, does not map anything to the \(\tau_p\) horn, and does not construct a physical period.

## Disposition

Yes, at ambient relation degree 8 over \(\mathbb F_{32003}\), the existing labelled relation generator can be evaluated and sampled at the p-normal point

\[
(3,6,-3), \qquad p=x+y+3z=0.
\]

The checker used the two integral unit p-normal directions

\[
n_x=(1,0,0), \qquad n_y=(0,1,0),
\]

and the p-tangent comparison direction

\[
n_x-n_y=(1,-1,0).
\]

It generated 9,780 special labelled relation rows with 8,736 columns. The sampled rows passed the degree-six interpolation check at offset 4 along all three directions.

Derivative support statistics:

- along `nx`: 9,780 rows, 4,596 nonzero derivative rows;
- along `ny`: 9,780 rows, 4,596 nonzero derivative rows;
- along `nx-ny`: 9,780 rows, 8,052 nonzero derivative rows.

The raw tangent identity also passed row-by-row:

\[
D_{n_x}(r)-D_{n_y}(r)=D_{n_x-n_y}(r)
\]

for every labelled relation row. There were zero failures across 9,780 rows.

## Meaning

This removes one materialization gap: the raw rank-26 relation rows and their p-normal finite-difference derivatives are source-computable at the required p-normal point. The remaining obstruction is not raw row generation; it is the quotient-rank step and the comparison map.

The next gate is to stream the special rows, the `nx`/`ny` first derivatives, and the p-tangent derivative rows into a modular quotient-rank engine and test whether a normal-choice-independent surviving line exists. Only after that could one ask whether the line maps to the primitive horn column `(1,1)`.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_rank26_p_normal_raw_relation_adapter.py`

Result:

- `research/voevodsky/results/cosmology_rank26_p_normal_raw_relation_adapter.json`

Command:

- `python research/voevodsky/check_cosmology_rank26_p_normal_raw_relation_adapter.py`
