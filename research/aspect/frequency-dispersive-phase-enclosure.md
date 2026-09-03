# Frequency-dispersive phase enclosure

## Question

How can analyzer phase variation over a continuous frequency band be certified without treating a finite frequency scan as full coverage?

## Claim boundary

This packet treats measurable two-mode phase multipliers with derivative and curvature bounds on a compact frequency band. It derives essential-supremum operator and SDP margins. It does not derive material dispersion parameters or cover discontinuous spectral response.

## Continuous phase operator

On

\[
H=L^2(\Omega;\mathbb C^2),
\]

a frequency-dependent relative phase acts by

\[
(U_\phi\psi)(\omega)=
\begin{pmatrix}1&0\\0&e^{i\phi(\omega)}\end{pmatrix}
\psi(\omega).
\]

For measurable real \(\phi\), this multiplication operator is unitary. Relative to nominal constant phase \(\phi_0\),

\[
\|U_\phi-U_{\phi_0}\|
=
\operatorname*{ess\,sup}_{\omega\in\Omega}
|e^{i\phi(\omega)}-e^{i\phi_0}|
\le
\operatorname*{ess\,sup}|\phi(\omega)-\phi_0|.
\]

The essential supremum, not values at sampled frequencies, controls the continuous-mode operator.

## Source-derived dispersion enclosure

Let the declared band be

\[
|\omega-\omega_0|\le\Delta.
\]

Suppose source data provide slope \(\beta=\phi'(\omega_0)\) and uniform curvature bound

\[
|\phi''(\omega)|\le\kappa.
\]

Taylor's theorem gives

\[
|\phi(\omega)-\phi_0|
\le
r_\phi:=|\beta|\Delta+rac{\kappa\Delta^2}{2}.
\]

Thus \(r_\phi\) is a rigorous band-wide phase radius.

## Effect and slack transport

For an ideal effect \(E\), define

\[
E_\phi=U_\phi^*EU_\phi.
\]

Using \(\|E\|\le1\),

\[
\|E_\phi-E_{\phi_0}\|
\le2\|U_\phi-U_{\phi_0}\|
\le2r_\phi.
\]

For SDP slack containing analyzer effects with nonnegative weights \(w_j\), a nominal spectral margin \(\gamma\) survives when

\[
2\sum_jw_jr_{\phi,j}<\gamma.
\]

The residual margin is at least the difference. This bound is conservative but source-typed and band-wide.

## Sampling gate

A frequency scan becomes a coverage certificate only with an inter-sample regularity bound. If a scalar residual \(g\) is Lipschitz with constant \(L\) and grid spacing \(h\), then

\[
\sup|g|
\le
\max_{\rm samples}|g|+Lh/2.
\]

Without \(L\), sampled zeros do not bound the continuum: the polynomial

\[
g(x)=4x(1-x)
\]

vanishes at sampled endpoints zero and one but reaches one at the midpoint.

## Exact fixture

With

\[
\Delta=1/10,
\quad |\beta|=1/10,
\quad\kappa=1/5,
\]

the phase radius is \(11/1000\), and the effect radius is at most \(11/500\). A nominal slack margin \(1/20\) retains margin \(7/250\). Enlarging the band to \(1/2\) gives phase radius \(3/40\) and effect radius \(3/20\), exceeding the nominal margin.

## Disposition

Frequency-dispersive analyzer effects admit rigorous continuous-mode bounds from source slope, curvature, and band radius. Essential-supremum effect perturbations preserve SDP certificates when their weighted budget remains below the nominal margin. Finite scans acquire authority only through an admitted regularity bound covering the gaps.
