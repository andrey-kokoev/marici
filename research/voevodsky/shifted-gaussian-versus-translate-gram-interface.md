# Shifted Gaussian versus translate-Gram interface

## Question

Is the materialized probe \(e^{-t(u-\xi)^2}\) already a translate Gram entry under the fixed Fourier convention?

## Claim boundary

The audit distinguishes the two probe types. It does not deny the explicit formula for the shifted Gaussian.

## Translate polarization

Use

\[
\widehat f(u)=\int_{\mathbb R}f(x)e^{-iux}\,dx
\]

and let

\[
g_\sigma(x)=e^{-x^2/(4\sigma)}.
\]

A source translation contributes a Fourier phase:

\[
\widehat{T_ag_\sigma}(u)=e^{-iau}\widehat g_\sigma(u).
\]

Therefore a polarized translate Gram entry has spectral test

\[
\widehat{T_ag_\sigma}(u)
\overline{\widehat{T_bg_\sigma}(u)}
=
4\pi\sigma e^{-2\sigma u^2}e^{-i(a-b)u}.
\]

The width doubles, and the translate coordinate appears as a character depending on \(a-b\).

## Materialized shifted probe

The current explicit-formula packet instead starts from

\[
h_{t,\xi}(u)=e^{-t(u-\xi)^2}.
\]

Its inverse Fourier shape is proportional to

\[
e^{-x^2/(4t)}e^{i\xi x}.
\]

Thus spectral shift corresponds to source modulation, not source translation. For nonzero \(\xi\), the shifted Gaussian is not a constant multiple of a centered Gaussian times a character.

## Disposition

The materialized scalar family and the translate Gram family are Fourier-dual but not identical as written. Before importing the Gaussian density theorem, one must derive the character-weighted centered-Gaussian explicit formula and prove that it equals the completed Weil translate pairing, including the width relation \(t=2\sigma\) and every normalization constant.

This is an interface defect, not a positivity residual. All-translate positivity remains unproved.

## Verification

- `research/voevodsky/shifted-gaussian-versus-translate-gram-interface-v1.json`
- `research/voevodsky/checkers/check_shifted_gaussian_versus_translate_gram_interface.py`
- `research/voevodsky/results/shifted_gaussian_versus_translate_gram_interface.json`
