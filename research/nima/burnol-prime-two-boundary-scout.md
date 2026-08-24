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

## Interpretation

The boundary is pointwise indefinite but apparently positive after imposing
the source support constraint. The very small first eigenvalue makes this a
near-critical uncertainty-principle problem, not broad positivity.

This is evidence for the prime-two contraction, not a proof. A theorem now
needs a directed lower bound for the compressed operator, or an analytic
uncertainty inequality showing that no \(\log2\)-supported function can place
enough Fourier mass in the negative band of \(\alpha\).

The next finite work is to extract the lowest numerical eigenvector, identify
its parity and endpoint behavior, and fit a source-natural comparison form
whose residual admits interval certification.

