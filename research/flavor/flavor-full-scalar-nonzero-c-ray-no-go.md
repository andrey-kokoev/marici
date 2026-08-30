# Full scalar nonzero-correlation ray no-go: WP708

## Full projective equations

Use the complete WP662 quartic beta field and normalize by
(lambda_x>0):

\[
x=\frac{\lambda_n}{\lambda_x},
\qquad
y=\frac{\lambda_m}{\lambda_x},
\qquad
z=\frac{\lambda_c}{\lambda_x}.
\]

A projective fixed ray with (z\ne0) requires all four beta components to be
proportional to the corresponding couplings. Exact Gröbner elimination of the
three projective equations gives the necessary polynomial

\[
(2x-1)^3(6x^2-3x+1)(9702x^2-3157x+513)=0.
\]

The two quadratic factors have discriminants (-15) and (-9941855).
Therefore every real nonzero-correlation ray has (x=1/2). Exact
back-substitution then gives

\[
x=y=\frac12,
\qquad
z\in\{1,2\}.
\]

## Stability obstruction

The WP662 radial determinant in these projective coordinates is

\[
D=\lambda_x^2(4xy-1).
\]

Both real rays have (D=0). They lie exactly on the radial-stability boundary,
not in the strictly stable source domain required for the faithful frame.

## Disposition

The second same-field reopening class from WP707 also closes at one loop. The
complete scalar beta field has no strictly stable real projective fixed ray
with nonzero (lambda_c). Together with WP705 and WP707:

- the (lambda_c=0) ray is an infrared saddle and loses angular rigidity;
- every real (lambda_c\ne0) ray is radially marginal.

This result is bounded to the WP662 scalar-only one-loop beta field. Gauge,
Yukawa, messenger, or new-field contributions may shift the projective
polynomials, but must be derived from one completed source before a displaced
stable ray receives selector authority.

The smallest exact falsifier is (4xy-1=0) at both real rays.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp708_full_scalar_nonzero_c_ray_no_go.py

Generated result: results/wp708_full_scalar_nonzero_c_ray_no_go.json.
