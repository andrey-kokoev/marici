# Projective-ray transverse saddle: WP705

## Full scalar-domain attack

WP704 restricted the complete WP662 quartic flow to
(lambda_n=lambda_m=a), (lambda_x=b), and (lambda_c=0). Its candidate
ray is

\[
(lambda_n,lambda_m,lambda_x,lambda_c)
=\rho\left(\frac32,\frac32,1,0\right),
\qquad \rho>0.
\]

The full WP662 grammar independently contains the allowed operator
(lambda_c(n\mathbin\cdot m)^2). No declared symmetry forces its coefficient
to vanish.

Use the three projective perturbations

\[
q=\frac{(\lambda_n+\lambda_m)/2}{\lambda_x},
\qquad
u=\frac{\lambda_n-\lambda_m}{\lambda_x},
\qquad
z=\frac{\lambda_c}{\lambda_x}.
\]

Linearizing the exact WP662 flow at the candidate ray gives

\[
\dot{\delta q}=16\rho\,\delta q,
\qquad
\dot u=256\rho\,u,
\qquad
\dot z=-112\rho\,z.
\]

With RG time increasing toward the ultraviolet, the first two modes contract
toward the ray in the infrared. The (z) mode does the opposite: every small
nonzero (lambda_c) grows projectively toward the infrared.

## Stable hostile perturbation

For (epsilon>0), the source perturbation

\[
\lambda_c=\epsilon
\]

adds the nonnegative quartic term
(epsilon(n\mathbin\cdot m)^2). It therefore does not violate boundedness of
the positive WP704 quartic ray. Nevertheless its projective displacement has
the infrared-repulsive exponent above. Arbitrarily close stable source points
do not approach the WP704 ray.

## Corrected classification

The ratio (3/2) is selected only after imposing the invariant condition
(lambda_c=0). On the largest currently source-authorized WP662 scalar
family, the ray is a saddle and has no open infrared basin. The invariant
slice is a presentation or boundary restriction unless a new source symmetry
forbids ((n\mathbin\cdot m)^2) and remains anomaly- and threshold-safe.

WP704 remains a valid conditional asymptotic theorem on its declared slice,
but it does not yet supply a genuine flavor selector. The smallest exact
falsifier is any positive infinitesimal (epsilon) in the allowed
(lambda_c) direction.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp705_projective_ray_transverse_saddle.py

Generated result: results/wp705_projective_ray_transverse_saddle.json.
