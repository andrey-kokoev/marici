# Dimensional-transmutation normalization (WP304)

## RG-generated scale

Consider the source-derived running law

\[
\frac{dg}{d\log\mu}=-b g^2,
\qquad b>0.
\]

For boundary coupling $g_0$ at reference scale $\mu_0$, the exact solution
defines

\[
\Lambda
=\mu\exp\left[-\frac1{b g(\mu)}\right]
=\mu_0\exp\left[-\frac1{b g_0}\right].
\]

The checker verifies that $\Lambda$ is invariant along the RG trajectory.
This supplies a mathematically valid normalization relation for lifting a
projective direction.

## Boundary-authority kernel

The numerical scale still depends on $g_0$. With the same $b=1$ and
$\mu_0=1$, boundary values $g_0=1$ and $g_0=1/2$ give
$\Lambda=e^{-1}$ and $\Lambda=e^{-2}$. Conversely, a desired radius can be
installed through

\[
g_0=-\frac1{b\log(\Lambda/\mu_0)}.
\]

Dimensional transmutation moves scale authority into a dimensionless boundary
condition; it does not remove it.

## Classification

The operation is an RG-invariant normalization carrier, conditional on a
source-derived boundary coupling and frozen reference normalization. It is not
yet a numerical `physical16` selector. Threshold matching, scheme contracts,
and uncertainty propagation must join the RG scale to the selected projective
flavor ray in one common frame.

Run `uv run --with sympy python
research/flavor/checkers/wp304_dimensional_transmutation_normalization.py` to
regenerate the exact RG audit.
