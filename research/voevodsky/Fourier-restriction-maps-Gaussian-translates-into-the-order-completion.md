# Fourier restriction maps Gaussian translates into the order completion

## Construction

For

\[
g_{\sigma,a}(x)
=
\exp\left(-\frac{(x-a)^2}{4\sigma}\right),
\]

its Fourier transform is a positive constant times

\[
F_{\sigma,a}(\lambda)
=
e^{-\sigma\lambda^2}e^{-ia\lambda}.
\]

Restrict this function to the ordered arithmetic labels \(\lambda_i\). On a finite zero-sum coefficient packet define

\[
L_{\sigma,a}(c)
=
\sum_i c_iF_{\sigma,a}(\lambda_i).
\]

The adjacent-gap estimate gives

\[
\lVert L_{\sigma,a}\rVert_*^2
\leq
\frac12
\int_0^\infty
|F'_{\sigma,a}(\lambda)|^2d\lambda.
\]

Since

\[
|F'_{\sigma,a}(\lambda)|^2
=
(4\sigma^2\lambda^2+a^2)e^{-2\sigma\lambda^2},
\]

the integral is finite for every positive \(\sigma\) and real \(a\). Explicitly, the bound is

\[
\frac{\sqrt\pi\sqrt\sigma}{2^{5/2}}
+
\frac{a^2\sqrt\pi}{4\sqrt{2\sigma}}.
\]

Therefore each translated source Gaussian has a canonical Riesz representative in the complexified order completion.

## Resulting map

Fourier restriction followed by Riesz representation defines

\[
\mathfrak R:
(\sigma,a)
\longmapsto
r_{\sigma,a}
\in
\mathcal H_{\mathrm{ord}}\otimes\mathbb C.
\]

This is the requested typed observation map from source Gaussian translates to the arithmetic order carrier. It extends the previously constructed centered Gaussian Riesz family by allowing the translation character.

## Remaining descent condition

The polarized source kernel is known explicitly, but it defines a form on the Riesz image only if it respects relations among those images. Precisely, whenever

\[
\sum_jc_jr_{\sigma_j,a_j}=0,
\]

one must prove

\[
\sum_jc_jK((\sigma_j,a_j),(\tau,b))=0
\]

for every \((\tau,b)\).

This radical-containment condition is required before declaring that the source kernel descends to a form on \(\mathcal H_{\mathrm{ord}}\). After descent, closability remains governed by the previously recorded kernel null-sequence criterion.

## Disposition

The source and order presentations are no longer merely similar Gaussian families: a bounded Fourier-restriction/Riesz map now joins them. The live gate has narrowed to kernel descent through this map, followed by closability and positivity.

## Verification

```text
python research/voevodsky/checkers/check_gaussian_translate_to_order_riesz_map.py
```

The checker verifies the exact integral bound numerically in 25 parameter cases.

Artifacts:

- `research/voevodsky/checkers/check_gaussian_translate_to_order_riesz_map.py`
- `research/voevodsky/results/gaussian_translate_to_order_riesz_map.json`
