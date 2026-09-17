# Distributional odd periodization closes the full image-kernel audit

Let `f in C_c^infty(0,ell)` and let `F` be its odd `2ell`-periodic
extension. Abel-regularize the principal multiplier by `r^n`, `0<r<1`, in
the sine series. For every fixed `r`, all image rearrangements are absolutely
convergent. Pair `k` with `-k` before taking `r up to 1`.

With the cosine-transform convention

\[
\frac2\pi\int_0^\infty\log\xi\cos(t\xi)d\xi=-\frac1{|t|},
\]

the off-diagonal finite-part identity is

\[
K_D(x,y)-K_0(x,y)=
-\sum_{k\ne0}\frac1{|x-y+2k\ell|}
+\sum_{k\in\mathbb Z}\frac1{|x+y+2k\ell|}.
\]

The comparison needed for a lower bound is the negative of this identity.
Pairing translation and reflection images produces:

- the two nearest reflected Carleman kernels;
- translation residuals bounded in norm by `2 log 2-1`;
- farther reflected residuals bounded in norm by `1/4`;
- a constant kernel `1/(2ell)`, positive in `K_0-K_D`.

The constant Fourier mode cancels before restriction because `F` is odd. The
rank-one term above is not an arbitrary Fourier zero mode: it is the finite
telescoping residue created by the paired interval reduction. Its sign is
positive in the required comparison, so it is discarded rather than charged.

Consequently, for the half-normalized principal Weil logarithm,

\[
K_0-K_D\ge-
\left(\frac\pi{\sqrt3}+\log2-\frac38\right)I
\]

as a quadratic-form inequality on `C_c^infty(0,ell)`. Density extends it to
the common logarithmic form domain. This statement includes translation
aliases, all reflected aliases, the finite-part constant, orientation, and the
factor `1/2`.
