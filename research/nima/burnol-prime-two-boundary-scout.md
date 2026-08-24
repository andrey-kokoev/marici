# Burnol's prime-two boundary is pointwise indefinite but support-positive in the first Galerkin scout

Status: numerical reconnaissance; no continuum positivity claim

## Exact boundary problem

At the support boundary \(c=\sqrt2\), Burnol's proof exposes the multiplier

\[
\alpha(\tau)=
\frac{8\sqrt2\cos(\tau\log2)}{1+4\tau^2}
-\log\pi
+\Re\psi\!\left(\frac14+\frac{i\tau}{2}\right).
\]

A high-precision scout finds

\[
\min_{0\le\tau\le20}\alpha(\tau)
\approx-1.04068425705481
\]

at

\[
\tau\approx2.06499924367117.
\]

The positive-axis crossings are approximately \(0.89044917\) and
\(6.40634873\). Thus Burnol's argument cannot reach \(c=\sqrt2\) by asserting
pointwise nonnegativity of \(\alpha\).

## Support-constrained compression

The relevant test functions are not arbitrary Fourier densities. Their
logarithmic representatives are confined to an interval of length \(\log2\).
We therefore compressed the Fourier multiplier to that interval and computed
its lowest Galerkin eigenvalues using a unitary padded FFT.

Across spatial resolutions 128, 256, and 512 and padding factors through 128,
the lowest eigenvalue remained positive. The best frequency-resolution pair
at 256 support points gave

\[
\lambda_1\approx0.00132501183043,
\qquad
\lambda_2\approx0.0727802744605,
\qquad
\lambda_3\approx0.660360424836.
\]

The 512-point scout with padding 64 gives

\[
\lambda_1\approx0.00132758094046.
\]

## Shape of the nearly-null mode

The lowest mode is even to numerical precision and has no internal zero. Its
correlation with the first Dirichlet mode is

\[
\left|\left\langle v_1,
\cos\frac{\pi x}{\log2}\right\rangle\right|
\approx0.9992665277.
\]

It places about \(69.6\%\) of its Fourier mass inside the negative multiplier
band. The energy balance is nearly exact:

\[
E_-\approx-0.4663343600,
\qquad
E_+\approx0.4676619409.
\]

The bare cosine has Rayleigh quotient \(0.0026545988\), so it captures the
shape but not the sharp margin. Even Dirichlet subspaces of dimensions
\(1,2,4,8,16,32\) give lowest values

\[
0.00265460, 0.00159014, 0.00157656,
0.00150736, 0.00143449, 0.00138586.
\]

Their slow convergence reveals a boundary layer. The endpoint-to-peak sample
ratio decreases from \(0.0441\) to \(0.0382\) to \(0.0344\) under successive
spatial doubling, rather than behaving like a fixed smooth cosine profile.

## Interpretation

The boundary is pointwise indefinite but apparently positive after imposing
the source support constraint. The very small first eigenvalue makes this a
near-critical uncertainty-principle problem, not broad positivity.

This is evidence for the prime-two contraction, not a proof. A theorem now
needs a directed lower bound for the compressed operator, or an analytic
**logarithmic uncertainty inequality** showing that no \(\log2\)-supported
function can place enough Fourier mass in the negative band of \(\alpha\).

The slow boundary layer makes a small fixed polynomial basis unattractive.
Burnol's native conductor-operator language, \(\log|x|+\log|D|\), is better
matched to the asymptotic symbol and should be the next analytic comparison.

The next finite work is to compare the compressed boundary operator with the
known conductor operator or a Sonine-space restriction, isolate the compact
prime-two correction, and seek a certified lower bound on the resulting
ground-state energy.
