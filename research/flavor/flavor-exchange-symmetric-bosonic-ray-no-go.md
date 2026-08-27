# Exchange-symmetric bosonic ray no-go: WP714

## Symmetric projective sector

In the RG-closed WP713 theory impose

\[
\lambda_n=\lambda_m,
\qquad
g_n=g_m,
\qquad
\lambda_x>0,
\qquad
\lambda_c\ne0.
\]

Normalize by (lambda_x) and write

\[
x=\frac{\lambda_n}{\lambda_x},
\quad
z=\frac{\lambda_c}{\lambda_x},
\quad
h=\frac{\lambda_\chi}{\lambda_x},
\quad
g=\frac{g_n}{\lambda_x}.
\]

Exact elimination of the four projective equations leaves only the real
correlation-bearing solutions

\[
x=\frac12,
\qquad
g=0,
\qquad
z\in\{1,2}.
\]

For (z=1), (h\in\{0,17/18}); for (z=2),
(h\in\{0,11/9}). The other algebraic (z) factor is a quartic with no real
roots.

## Stability and contrast

Every real solution has

\[
4x^2-1=0.
\]

Moreover (g_n=g_m=0), so the WP712 bosonic contrast vanishes. The boson
self-coupling can run on the ray but cannot move the triplet quartics into the
strict-stability interior.

## Disposition

The exchange-symmetric sector contains no correlation-bearing stable bosonic
ray. Any progressive WP713 ray must break triplet exchange in its portal
couplings and, consistently, be tested in the full asymmetric projective
system. This is a bounded no-go; it does not exclude an asymmetric ray.

The smallest exact falsifier is the common radial margin zero at all four real
symmetric solutions.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp714_exchange_symmetric_bosonic_ray_no_go.py

Generated result: results/wp714_exchange_symmetric_bosonic_ray_no_go.json.
