# Wilson-flag cyclic-ray gate: WP1086

## Question

Does a source-fixed Wilson \(1+1+1\) flag by itself select a cyclic Krylov ray
and history?

## Krylov criterion

For distinct Wilson eigenvalues

\[
A=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3),
\]

the Krylov determinant factorizes as

\[
\det[x,Ax,A^2x]
=
(\lambda_2-\lambda_1)
(\lambda_3-\lambda_1)
(\lambda_3-\lambda_2)
x_1x_2x_3.
\]

Thus a vector is cyclic exactly when all three eigencomponents are nonzero.

A source-selected eigenline has only one nonzero component, so its Krylov
determinant vanishes. A coherent sum can be cyclic, but the Wilson flag does
not select its amplitude ratios or relative phases. In particular, the
residual \(U(1)\) changes the relative phases of the two Wilson lines.

## Source-supply audit

A source-fixed Wilson flag could supply:

- three distinct eigenlines;
- simple spectrum;
- selected eigenlines.

It does not supply:

- a cyclic eigenline;
- coherent amplitude ratios;
- coherent relative phases;
- a nondestructive history dilation.

## Classification

Conditional flag no-go for the ray. Even after the missing Wilson boundary
condition is supplied, a three-line flag is not yet a Krylov source. A further
coherent-ray preparation is required, followed by history dilation and the
WP1081 reference \(\rho\).

Checker: `research/flavor/checkers/wp1086_wilson_flag_cyclic_ray_gate.py`

Result: `results/wp1086_wilson_flag_cyclic_ray_gate.json`
