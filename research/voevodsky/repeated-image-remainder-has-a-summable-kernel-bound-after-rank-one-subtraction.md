# Repeated-image remainder has a summable bound after rank-one subtraction

Let the interval length be `ell` and put `s=x+y in (0,2ell)`. Beyond the two
nearest reflected kernels `1/s` and `1/(2ell-s)`, pair the repeated images as

\[
r_k(s)=
\left(\frac1{2k\ell+s}-\frac1{2k\ell}\right)
+
\left(\frac1{2(k+1)\ell-s}-\frac1{2(k+1)\ell}\right),
\qquad k\ge1.
\]

The subtracted terms are independent of `x,y`; they form a rank-one constant
kernel and can be adjoined to the finite certified block once its coefficient
is fixed by the logarithmic regularization.

For `0<s<2ell`,

\[
|r_k(s)|
\le
\frac{s}{(2k\ell)^2}
+
\frac{s}{2(k+1)\ell\,[2(k+1)\ell-s]}.
\]

The second denominator becomes small only for the already extracted nearest
right image; reindexing the exterior pairs symmetrically yields a uniform
`O(k^-2/ell)` majorant. Consequently the regularized repeated-image series is
an ordinary bounded integral kernel, with a computable zeta-two norm budget.

This identifies the finite-interval comparison architecture:

1. two singular nearest-image Carleman operators;
2. one regularization-dependent rank-one constant kernel;
3. an absolutely convergent repeated-image remainder.

The remaining exact step is to derive the signed image series and rank-one
constant from the declared Fourier normalization. Once fixed, the repeated
remainder can be bounded directly without an IMS partition.
