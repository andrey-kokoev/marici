# RG-completed curvature boundary (WP268)

## Completing the loop packet

Use the \(c=3/2\) one-loop packet from WP267. Write

\[
\ell=\log\frac{\mu}{\mu_0},
\qquad
L_0=\log\frac{M^2}{\mu_0^2}.
\]

The loop curvature is

\[
K_{\mathrm{loop}}(\mu)=2Ak^2(L_0-2\ell).
\]

RG invariance requires the local counterterm coefficient to run as

\[
c_2(\mu)=c_2(\mu_0)+2Ak^2\ell.
\]

The total curvature is then

\[
K_{\mathrm{tot}}
=K_{\mathrm{loop}}+2c_2(\mu)
=2Ak^2L_0+2c_2(\mu_0),
\]

and its derivative with respect to \(\ell\) vanishes exactly.

## What RG does not select

The scale dependence cancels, but the boundary integration constant remains.
At \(A=k=1\), \(M=\mu_0\), and linear selector coefficient one, the two
equally RG-consistent boundaries

\[
c_2(\mu_0)=1,
\qquad
c_2(\mu_0)=2
\]

give total curvatures two and four, and select \(x=1/2\) and \(x=1/4\).

RG completion therefore repairs presentation dependence but does not provide
numerical source authority. It transports whichever boundary packet is
supplied.

## Remaining gate

A UV fixed point, symmetry-breaking threshold, finite matching condition, or
other source law must derive \(c_2(\mu_0)\) before flavor readout. Choosing it
from the observed mixing point is boundary fitting. This theorem does not
exclude a UV completion that fixes the value; it shows that the beta function
and scheme consistency alone cannot.

Run `uv run --with sympy python
research/flavor/checkers/wp268_rg_completed_curvature_boundary.py` for the
exact cancellation, surviving boundary derivative, and hostile selected
points.
