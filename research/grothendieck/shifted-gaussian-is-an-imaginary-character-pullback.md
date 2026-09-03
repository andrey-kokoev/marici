# Shifted Gaussian is an imaginary-character pullback

## Correction

The shifted-Gaussian and heat--character kernels are distinct presentations, but their comparison does not require reciprocal-width reparameterization.

Define

\[
\mathcal K(t,z)
=
\langle\mathcal W,e^{-tu^2}e^{izu}\rangle
\]

for complex `z` in the domain authorized by Gaussian smoothing. Since

\[
e^{-t(u-\xi)^2}
=
e^{-t\xi^2}e^{-tu^2}e^{2t\xi u},
\]

one has the exact pullback

\[
\Theta(t,\xi)
=
e^{-t\xi^2}\mathcal K(t,-2it\xi).
\]

Thus the Gaussian center is an imaginary-character section followed by a scalar gauge factor.

## Differential-cell descent

Starting from

\[
\partial_t\mathcal K(t,z)=\partial_z^2\mathcal K(t,z)
\]

and pulling back along `z=-2it xi` with the gauge `e^(-t xi^2)` gives

\[
4t^2\partial_t\Theta
+
\partial_\xi^2\Theta
+
2t\Theta=0.
\]

The different equations are therefore coherent shadows of one holomorphic heat--character kernel. They must not be identified before applying the section and gauge.

## Prime-side check

The Fourier transform of `e^(-tu^2)e^(izu)` evaluated at a prime displacement `L=log n` is proportional to

\[
e^{-(L-z)^2/(4t)}.
\]

Substituting `z=-2it xi` and multiplying by `e^(-t xi^2)` gives

\[
e^{-L^2/(4t)}e^{-i\xi L}.
\]

Pairing `L` and `-L` produces the exact shifted-Gaussian factor

\[
e^{-L^2/(4t)}\cos(\xi L).
\]

This recovers the printed prime term and verifies the comparison normalization.

## Endpoint-side check

Evaluating the shifted Gaussian at the two polar points gives

\[
\frac12\left[e^{-t(i/2-\xi)^2}+e^{-t(-i/2-\xi)^2}\right]
=
e^{t/4-t\xi^2}\cos(t\xi),
\]

matching the source endpoint formula. Hence the same imaginary-character pullback transports the endpoint residual correctly.

## Meta-observer cell

The comparison cell should record

\[
\Theta
=
\iota^*\mathcal K,
\qquad
\iota(t,\xi)=(t,-2it\xi),
\]

with the gauge factor included in `iota*`. Its curvature target is zero for the completed source. At finite arithmetic cutoff, the prime-side cell is exact term by term; only the common omitted tail remains.

## Boundary

The comparison requires holomorphic continuation of `K(t,z)` to the imaginary-character section. Gaussian damping makes each source test entire, but interchange with the completed distribution, gamma integral, and infinite prime sum must be justified uniformly on the selected parameter strata.

## Disposition

Replace the unspecified Fourier/reciprocal-width arrow by the exact imaginary-character pullback with gauge. This provides the first explicit cross-family generator relating the shifted-Gaussian and heat--character observer pyramids.
