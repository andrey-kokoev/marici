# Beta-displacement acceptance functional: WP709

## Regular marginal ray

Use the first WP708 ray

\[
(x,y,z)=\left(\frac12,\frac12,1\right),
\]

where (x=lambda_n/lambda_x), (y=lambda_m/lambda_x), and
(z=lambda_c/lambda_x). Let independently derived completion terms change
the normalized beta data at this ray by

\[
(N,M,X,C).
\]

Here (N), (M), and (X) correct the two self-quartic and mixed-norm beta
components. The last coordinate corrects (eta_c/lambda_c).

## Exact linear response

The projective-equation Jacobian at the ray is

\[
J=
\begin{pmatrix}
-8&-48&0\\
-48&-8&0\\
-64&-64&8
\end{pmatrix},
\qquad
\det J=-17920.
\]

The implicit-function response therefore exists uniquely. For the radial
stability margin

\[
D=4xy-1,
\]

the exact first-order displacement is

\[
\delta D=\frac{N+M-X}{28}.
\]

The correction (C) changes (z) but cancels from (delta D). A completed
source moves the ray into strict radial stability at first order only if

\[
N+M-X>0.
\]

## Hostile directions

The algebra alone permits every disposition:

- ((N,M,X,C)=(1,1,0,0)) opens the stability margin;
- ((0,0,1,0)) pushes the ray into instability;
- ((0,0,0,1)) moves only the correlation ratio at first order.

These are response probes, not admitted source corrections. Their signs may
not be chosen from the desired outcome.

## Disposition

WP709 supplies the smallest exact acceptance functional for any proposed
gauge, Yukawa, messenger, or new-field completion. It is neither a selector nor
an instrument. A progressive successor must derive (N,M,X,C) from one frozen
source action and scheme, prove (N+M-X>0) with uncertainties, and then recompute
the complete transverse spectrum and finite threshold matching.

The smallest falsifier of a proposed first-order repair is
(N+M-X\leq0). Even a positive value is insufficient if higher-order terms,
another transverse mode, or decoupling removes the stable basin.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp709_beta_displacement_acceptance_functional.py

Generated result: results/wp709_beta_displacement_acceptance_functional.json.
