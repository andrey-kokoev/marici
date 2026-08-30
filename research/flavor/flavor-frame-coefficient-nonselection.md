# Faithful-frame coefficient nonselection: WP650

## Question

Does WP649's source-derived faithful frame also select the scalar coefficients
that couple its words to the two quark sectors?

## Exact contextual partition

The admitted family is

\[
Y_s=a_sI+b_sJ_n+c_sJ_m,
\qquad s\in\{u,d\},
\]

with six complex scalar coefficients, hence twelve real controls. These
coefficients are (SO(3)) singlets: frame covariance does not relate or fix
them. At WP646's exact nondegenerate CP witness, their weak-basis-invariant
response has rank eight. The local contextual partition therefore has a
four-dimensional control kernel.

The freedom is physical, not merely presentational. In one sector, the two
equally legal packets \(Y=I\) and \(Y=I+J_n\) obey

\[
\operatorname{Tr}(YY^\dagger)=3,
\qquad
\operatorname{Tr}(YY^\dagger)=5,
\]

respectively. Thus the frame action does not select even this basic
weak-basis invariant.

## Classification

WP649 supplies a faithful presentation rigidifier and WP650 supplies a
constrained rank-eight carrier. Neither selects coefficient values or
identifies a source. The smallest exact falsifier is an equation derived from
the existing (SO(3)) source that fixes a scalar sector coefficient without
introducing another invariant or field.

The physical-instrument gate is later still: derive messenger vertices and
calibrated observations sensitive to the rank-eight image. Such an instrument
would read the coefficients; it would not by itself explain their values.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp650_frame_coefficient_nonselection.py
```

Generated result: `results/wp650_frame_coefficient_nonselection.json`.
