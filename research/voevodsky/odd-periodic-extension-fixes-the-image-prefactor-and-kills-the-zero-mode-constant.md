# Odd periodic extension fixes the image prefactor and kills the zero-mode constant

Let `f` be supported on `(0,ell)` and extend it oddly to a `2ell`-periodic
function `F`. Its Fourier frequencies are `n*pi/ell`, exactly the spectral
Dirichlet frequencies. Therefore the spectral principal logarithmic form is
the whole-line logarithmic kernel periodized with period `2ell` and evaluated
on the odd extension.

The half-line transform identity

\[
\frac2\pi\int_0^\infty\log\xi\cos(a\xi)d\xi=-\frac1a
\]

fixes the coefficient-one image kernel. No free common prefactor remains.
The odd image signs give

\[
\sum_{k\in\mathbb Z}
\left[h(x-y+2k\ell)-h(x+y+2k\ell)\right].
\]

Abel regularization may add a constant Fourier mode. The odd periodic
extension has

\[
\int_{-\ell}^{\ell}F(x)dx=0,
\]

so the zero-mode constant has zero quadratic form. Equivalently, the
rank-one constants introduced while pairing translation and reflection images
cancel after pullback through odd extension.

Thus the finite-interval principal boundary budget is the sum of:

1. the two nearest reflected-image operator;
2. paired translation aliases;
3. paired farther reflected aliases.

For the half-normalized Weil multiplier, the available direct bound is

\[
C_{\partial}
\le\frac\pi{\sqrt3}+\log2-\frac38.
\]
