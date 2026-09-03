# Imaginary-character Weil Gram interface

## Question

Does the materialized shifted-Gaussian explicit formula continue to the character-weighted centered Gaussian required by translated-source Gram pairing?

## Claim boundary

This constructs the interface and verifies its sectorwise algebra. It does not prove matrix positivity.

## Fourier crossing

For source-translate difference \(d=a-b\), the centered spectral Gram test is

\[
4\pi\sigma e^{-2\sigma u^2}e^{-idu}.
\]

Completing the square gives

\[
4\pi\sigma e^{-d^2/(8\sigma)}
 e^{-2\sigma(u+id/(4\sigma))^2}.
\]

Therefore

\[
G_\sigma(a,b)=
4\pi\sigma e^{-(a-b)^2/(8\sigma)}
\Theta\left(2\sigma,-\frac{i(a-b)}{4\sigma}\right).
\]

## Sectorwise continuation

After removing the common positive factor, the endpoint term becomes

\[
e^{\sigma/2}\cosh(d/2).
\]

For a prime logarithmic scale \(L=\log n\),

\[
e^{-d^2/(8\sigma)}e^{-L^2/(8\sigma)}
\cosh\left(\frac{dL}{4\sigma}\right)
=
\frac12\left(
e^{-(L-d)^2/(8\sigma)}+e^{-(L+d)^2/(8\sigma)}
\right).
\]

The gamma Gaussian becomes

\[
e^{-2\sigma u^2-idu}.
\]

The endpoint is entire. On compact character sets, the gamma integral retains Gaussian domination and the prime series retains log-Gaussian domination after completing squares. Thus the imaginary-character continuation is typed sectorwise.

## Disposition

The source Gram interface is now constructed with its Fourier constants and width relation. Positivity for real shifted characters does not imply positivity of these imaginary-character matrices. The sole remaining test is direct positive semidefiniteness of the displayed matrix for every \(\sigma>0\) and every finite real translate family.

## Verification

- `research/voevodsky/imaginary-character-weil-gram-interface-v1.json`
- `research/voevodsky/checkers/check_imaginary_character_weil_gram_interface.py`
- `research/voevodsky/results/imaginary_character_weil_gram_interface.json`
