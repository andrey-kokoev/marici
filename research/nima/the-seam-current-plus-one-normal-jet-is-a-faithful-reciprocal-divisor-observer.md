# The seam current plus one normal jet is a faithful reciprocal-divisor observer

Event 10280 showed that the scalar seam current cancels every off-seam
reciprocal pair. The first normal derivative restores the lost information.

For one reciprocal pair at height \(\gamma\) and distance \(d>0\), let
\(x=t-\gamma\). Its first normal jet is

\[
K_d(x)
=
2\frac{x^2-d^2}{(x^2+d^2)^2}.
\]

Using the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}\,dx,
\]

the Poisson-kernel identity

\[
\widehat{\frac{d}{x^2+d^2}}(\xi)
=
\pi e^{-d|\xi|}
\]

gives

\[
\widehat K_d(\xi)
=
-2\pi|\xi|e^{-d|\xi|}.
\]

A pair centered at height \(\gamma\) contributes

\[
-2\pi|\xi|e^{-d|\xi|}e^{-i\gamma\xi}.
\]

Thus for an off-seam reciprocal divisor with multiplicities \(m_j>0\),

\[
\widehat D_\perp(\xi)
=
-2\pi|\xi|
\sum_j
m_j e^{-d_j|\xi|}e^{-i\gamma_j\xi},
\]

after the seam-zero Poisson jets and the known pole/archimedean terms have
been removed.

The factor after \(-2\pi|\xi|\) is a one-parameter
Fourier–Laplace shadow of the positive off-seam divisor measure. For a
general two-dimensional measure this shadow need not be faithful, so ordinary
transform uniqueness must not be invoked here.

## Conditional faithfulness theorem

For a locally finite divisor, each kernel \(K_d(t-\gamma)\) extends
meromorphically in \(t\), with poles at the displaced locations determined
by \(\gamma\) and \(d\). If the assembled first jet has a source-authorized
meromorphic continuation to a connected neighborhood of the seam, then

\[
D_\perp=0
\]

on the real seam implies that continuation vanishes identically. Its pole
divisor is therefore empty; positivity of multiplicities prevents
same-location cancellation.

Thus first-jet faithfulness is conditional on meromorphic continuation. The
one-dimensional Fourier–Laplace shadow alone is not a sufficient theorem.

Therefore one does not need the entire normal germ as independent data. The
following pair is already faithful:

1. the seam boundary current, which records zeros with \(d=0\);
2. the first normal jet after subtracting the canonical Poisson extension of
   those seam atoms.

Under this meromorphic-continuation gate, RH is equivalent to

\[
D_\perp=0.
\]

## Necessary subtraction order

Critical-line zeros also contribute to the raw normal derivative. Their
one-sided Poisson kernels have \(d=0\), so their Fourier multiplier is the
\(e^{-d|\xi|}=1\) term. Hence the raw first jet cannot be set to zero.

The order must be:

\[
\text{read seam atoms}
\to
\text{form their authorized Poisson extension}
\to
\text{subtract its normal jet}
\to
\text{test the residual }D_\perp.
\]

Subtracting an arbitrary fitted seam measure would be circular. The measure
must be the one independently observed by the scalar boundary current.

## Operator interpretation

The multiplier

\[
|\xi|e^{-d|\xi|}
\]

is a fractional Dirichlet-to-Neumann response damped by the distance \(d\)
from the seam. Off-seam zeros are therefore invisible in boundary value but
visible in boundary flux.

This is exactly the Green/Stokes geometry sought by the programme:

\[
\text{Dirichlet seam trace}
+
\text{Neumann residual}
\]

is faithful for the reciprocal divisor.

The next constructor theorem should identify the arithmetic first normal jet
with this Dirichlet-to-Neumann defect and prove the required transform
uniqueness in the projective exponential rigging.
