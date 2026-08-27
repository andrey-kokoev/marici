# Gaussian detector-convolution pullback: WP655

## Exact object separation

A Lorentzian source template with mass \(m\) and half-width \(\gamma\) has,
up to normalization, Fourier transform

\[
\widehat L(k)=e^{-\gamma|k|}e^{-imk}.
\]

Gaussian detector resolution of finite width \(\sigma\) multiplies this by

\[
H_\sigma(k)=e^{-\sigma^2k^2/2}.
\]

The transfer is strictly positive at every finite real frequency. It can
therefore be cancelled when testing equality of two convolved templates. For
positive \(k\), their source ratio is

\[
e^{-\delta_\gamma k-i\Delta k}.
\]

Equality for all \(k\) forces its logarithmic derivative at zero to vanish,
so \(\delta_\gamma=0\) and \(\Delta=0\). Gaussian convolution preserves
exact separation of every distinct mass-width pair.

## Completion stability

The inverse is not uniformly stable. As
\((\Delta,\delta_\gamma)\to(0,0)\), the convolved templates coalesce and
the smallest Gram eigenvalue tends to zero. This is completion-stability
failure, not exact object-separation failure.

## Operational target domain

An inequality requiring a positive calibrated Gram-eigenvalue lower bound
defines an operational target domain. It is not evidence that a detector
achieves that bound. Admission still requires detector-derived resolution,
background covariance, efficiencies, and uncertainties.

## Disposition

Gaussian smearing is injective on the declared Lorentzian source family but
has no uniform inverse near coincident mass-width parameters. The smallest
exact falsifier is a finite-frequency zero of the Gaussian transfer or a pair
of distinct Lorentzian parameters with identical convolved templates.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp655_gaussian_convolution_pullback.py

Generated result: results/wp655_gaussian_convolution_pullback.json.
