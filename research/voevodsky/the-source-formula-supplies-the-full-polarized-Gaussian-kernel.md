# The source formula supplies the full polarized Gaussian kernel

## Question

Can the shifted-Gaussian explicit formula supply off-diagonal entries for Gaussian probes of unequal widths?

## Polarized probes

Let

\[
g_{\sigma,a}(x)
=
\exp\left(-\frac{(x-a)^2}{4\sigma}\right),
\qquad
\sigma>0.
\]

Under the fixed Fourier convention, polarization of \(g_{\sigma,a}\) and \(g_{\tau,b}\) gives the spectral test

\[
4\pi\sqrt{\sigma\tau}
\exp\left(-(\sigma+\tau)u^2\right)
\exp\left(-i(a-b)u\right).
\]

Set

\[
t=\sigma+\tau,
\qquad
d=a-b.
\]

Completing the square gives

\[
e^{-tu^2-idu}
=
e^{-d^2/(4t)}
 e^{-t(u+id/(2t))^2}.
\]

Therefore the source-side polarized kernel is

\[
K((\sigma,a),(\tau,b))
=
4\pi\sqrt{\sigma\tau}
 e^{-(a-b)^2/(4(\sigma+\tau))}
 \Theta\left(
 \sigma+\tau,
 -\frac{i(a-b)}{2(\sigma+\tau)}
 \right).
\]

Here \(\Theta\) is evaluated by the endpoint, gamma, and prime source formula through its already-typed imaginary-character continuation.

## Properties

The formula depends on the sum of widths and the difference of centers. Exchanging the probes preserves the total width and reverses the character, giving the Hermitian swap law after complex conjugation.

The equal-width formula is recovered by setting \(\sigma=\tau\).

## What this closes

The polarized jointly regularized gamma-plus-prime kernel is now explicit on the algebraic span of source Gaussian translates. Diagonal values are no longer the only available data.

## Remaining comparison

This does not yet identify the source Gaussian translate span with the heat-Riesz vectors in \(\mathcal H_{\mathrm{ord}}\). Similar Gaussian dependence is insufficient because the two constructions use different source coordinates and norms.

The next required arrow is a typed map sending source Gaussian translates to the order-completion carrier while proving that the displayed kernel is the pullback of a closable form there. Positivity of its finite Gram matrices is also unproved and remains RH-bearing.

## Verification

```text
python research/voevodsky/checkers/check_unequal_width_weil_gaussian_kernel.py
```

The checker verifies 2,000 exact completed-square identities and 400 Hermitian parameter swaps.

Artifacts:

- `research/voevodsky/checkers/check_unequal_width_weil_gaussian_kernel.py`
- `research/voevodsky/results/unequal_width_weil_gaussian_kernel.json`
