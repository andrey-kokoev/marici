# Symmetric-vacuum ratio selector (WP312)

## Source-derived vacuum operation

Complete WP311 with the exchange-invariant potential

\[
V=\lambda(v_1^2+v_2^2-R^2)^2+\kappa(v_1-v_2)^2,
\qquad \lambda,\kappa,R>0.
\]

It is a sum of nonnegative squares. Its unique positive zero is

\[
v_1=v_2=\frac{R}{\sqrt2}.
\]

The Hessian eigenvalues there are $8\lambda R^2$ in the radial channel and
$4\kappa$ in the exchange-odd channel. The vacuum is therefore a strict
minimum throughout the declared positive coefficient family.

## Selector response

The selected ratio $v_1/v_2=1$ has zero response to $\lambda,\kappa,R$.
The physical radius retains rank-one response to $R$. Thus the construction
is a genuine ensemble-stable ratio selector, not a full normalization or
`physical16` point selector.

## Strong hostile consequence

Under WP311's matching,

\[
M_u=v_1Y+v_2Z,
\qquad
M_d=v_2Y+v_1Z,
\]

the symmetric vacuum forces $M_u=M_d$, not merely equal hierarchy ratios.
This makes the candidate sharply falsifiable: any physical packet with unequal
ordered up/down spectra rejects the source completion.

## Classification

WP312 establishes a genuine source-derived dimensionless ratio selector in the
enlarged model. Its stronger spectrum prediction must now be tested on the
complete fitted ensemble. If it fails, exchange breaking must be introduced by
an independent source mechanism rather than fitted to erase the prediction.

Run `uv run --with sympy python
research/flavor/checkers/wp312_symmetric_vacuum_ratio_selector.py` to
regenerate the exact vacuum and response audit.
