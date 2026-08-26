# UV stability–predictivity tradeoff (WP271)

## Linearized theorem

Let an autonomous RG flow be linearized at a hyperbolic UV fixed point, with
\(t\) increasing toward the UV:

\[
\dot z=Az.
\]

Every eigenmode with eigenvalue \(\lambda<0\) decays as
\(A_\lambda e^{\lambda t}\). Its amplitude is invisible in the UV limit but
remains free at every finite matching scale. Therefore the dimension of the
UV-attractive manifold is exactly the number of finite-scale source
coordinates forgotten by the fixed-point limit.

## Exact rank-two witness

For

\[
A=\operatorname{diag}(-2,-1,3),
\]

reaching the UV fixed point forces the third amplitude to vanish, but leaves

\[
z(t)=\left(A_1e^{-2t},A_2e^{-t},0\right).
\]

Every member has the same UV limit. At \(t=0\), the matching map is
\((A_1,A_2)\mapsto(A_1,A_2,0)\) and has exact rank two. The fixed-point readout
therefore has a two-dimensional trajectory kernel.

## Zero-dimensional alternative

If all eigenvalues are positive in this convention, only the exact fixed
trajectory reaches the UV point and the critical surface is zero-dimensional.
That removes the amplitudes, but it also removes every UV-attractive direction:
physical preparation must land on a measure-zero trajectory by some additional
law.

Thus open-basin UV attraction and unique finite-scale prediction do not follow
from one another. Each attractive direction requires an independent boundary
condition, while a zero-dimensional surface requires a preparation mechanism.

This is a local hyperbolic theorem. Center manifolds, limit cycles,
nonautonomous flows, singular boundaries, and stochastic UV dynamics remain
separate reopening classes.

Run `uv run --with sympy python
research/flavor/checkers/wp271_uv_stability_predictivity_tradeoff.py` for the
exact flow, critical-surface dimension, matching rank, and hostile uniqueness
test.
