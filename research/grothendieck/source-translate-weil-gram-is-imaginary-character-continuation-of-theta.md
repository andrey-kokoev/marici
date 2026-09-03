# Source-translate Weil Gram is imaginary-character continuation of Theta

## Fourier-normalized source probes

Use

\[
g_{\sigma,a}(x)=e^{-(x-a)^2/(4\sigma)}
\]

and Fourier convention

\[
\widehat f(u)=\int_{\mathbb R}f(x)e^{-iux}\,dx.
\]

Then

\[
\widehat g_{\sigma,a}(u)
=2\sqrt{\pi\sigma}\,e^{-\sigma u^2}e^{-iau},
\]

so the polarized spectral test is

\[
\widehat g_{\sigma,a}(u)
\overline{\widehat g_{\sigma,b}(u)}
=4\pi\sigma e^{-2\sigma u^2}e^{-i(a-b)u}.
\]

## Exact continuation from the shifted Gaussian kernel

Let

\[
\Theta(t,\xi)=\langle\rho,e^{-t(u-\xi)^2}\rangle
\]

for the completed centered spectral distribution `rho`. Put

\[
t=2\sigma,
\qquad d=a-b.
\]

Completing the square gives

\[
e^{-2\sigma u^2-idu}
=
 e^{-d^2/(8\sigma)}
 e^{-2\sigma(u+i d/(4\sigma))^2}.
\]

Therefore the source-translate Weil Gram entry is

\[
G_{ab}
=4\pi\sigma e^{-d^2/(8\sigma)}
\Theta\!\left(2\sigma,-\frac{id}{4\sigma}\right).
\]

This is the missing Fourier crossing: source translation becomes imaginary continuation of the spectral shift parameter, not a real shifted Gaussian.

## Source-side convergence

The continuation is admissible termwise in the explicit formula. The prime factor changes from

\[
e^{-(\log n)^2/(8\sigma)}\cos(\xi\log n)
\]

to a hyperbolic cosine at imaginary `xi`; completing its exponent leaves Gaussian decay in `log n`, so every fixed `sigma>0` and finite `d` remains absolutely convergent. The endpoint cosine likewise becomes a hyperbolic cosine. The digamma Gaussian integral remains convergent after the same finite imaginary shift, subject to the contour convention recorded in the completed explicit formula.

## Matrix form

For a finite source-translate tuple, the common positive factor `4 pi sigma` may be removed. PSD is exactly positivity of

\[
\left[
 e^{-(a_i-a_j)^2/(8\sigma)}
 \Theta\!\left(2\sigma,-\frac{i(a_i-a_j)}{4\sigma}\right)
\right]_{i,j}.
\]

The entries now depend on differences, as required for a translation Gram kernel. Hermitian symmetry follows from reciprocal reality of the analytically continued completed kernel.

## Disposition

The Fourier interface is reduced to analytic continuation of the already materialized two-variable explicit formula from real to imaginary character. Before calling it closed, verify the digamma contour shift and constants against the declared Weil formula. Direct PSD of the displayed difference kernel remains RH-equivalent.
