# Wavefunction running is radially null: WP710

## Exact normalization action

Let independent positive field-normalization factors act on the two triplets as

\[
n\mapsto s_n n,
\qquad
m\mapsto s_m m.
\]

The quartic coefficients transform by their leg counts:

\[
\lambda_n\mapsto s_n^4\lambda_n,
\qquad
\lambda_m\mapsto s_m^4\lambda_m,
\]

\[
\lambda_x\mapsto s_n^2s_m^2\lambda_x,
\qquad
\lambda_c\mapsto s_n^2s_m^2\lambda_c.
\]

Consequently both projective quantities relevant to WP708 are exactly
invariant:

\[
\frac{\lambda_n\lambda_m}{\lambda_x^2}
\mapsto
\frac{\lambda_n\lambda_m}{\lambda_x^2},
\qquad
\frac{\lambda_c}{\lambda_x}
\mapsto
\frac{\lambda_c}{\lambda_x}.
\]

Pure wavefunction running therefore cannot move a marginal ray into the
strict-stability interior at any finite normalization.

## Infinitesimal WP709 interface

For anomalous dimensions (gamma_n,gamma_m), the leg-count contributions at
the regular WP708 ray are

\[
N=2\gamma_n,
\qquad
M=2\gamma_m,
\qquad
X=2(\gamma_n+\gamma_m),
\qquad
C=2(\gamma_n+\gamma_m).
\]

Hence

\[
N+M-X=0.
\]

Unequal anomalous dimensions can shear the individual coordinates (x) and
(y), but their product and the radial margin remain fixed.

## Classification

Wavefunction and common multiplicative beta contributions are normalization
transport. They descend as reparameterizations of the same scalar source and
are neither selectors nor physical instruments. They lie exactly in WP709's
radial kernel.

Opening stability requires genuine vertex corrections whose self-versus-mixed
combination is not reducible to external-leg weights. Such corrections must be
derived from a frozen gauge, Yukawa, messenger, or new-field interaction; an
algebraically chosen positive (N+M-X) has no authority.

The smallest exact falsifier of a wavefunction-only repair is the identity
(N+M-X=0), equivalently invariance of
(4\lambda_n\lambda_m/\lambda_x^2-1).

Reproduce with: uv run --with sympy python research/flavor/checkers/wp710_wavefunction_running_radial_null.py

Generated result: results/wp710_wavefunction_running_radial_null.json.
