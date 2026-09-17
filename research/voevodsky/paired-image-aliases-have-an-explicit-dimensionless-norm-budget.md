# Paired finite-interval image aliases have an explicit norm budget

Let `d=x-y`, so `|d|<=ell`. Pair the nonzero translation images:

\[
\frac1{2k\ell+d}+rac1{2k\ell-d}-\frac2{2k\ell}
=
\frac{2d^2}{2k\ell((2k\ell)^2-d^2)}.
\]

Their absolute kernel is bounded by

\[
\frac1{k(4k^2-1)\ell}.
\]

The summed integral-operator norm is therefore at most

\[
\sum_{k\ge1}\frac1{k(4k^2-1)}=2\log2-1.
\]

For reflected aliases, extract the two nearest singular images. Pair the
remaining images with `k>=2`; since `0<=s=x+y<=2ell`, their residual kernel is
bounded by

\[
\frac1{k(k^2-1)\ell}.
\]

Hence their operator norm is at most

\[
\sum_{k\ge2}\frac1{k(k^2-1)}=\frac14.
\]

The total farther-image budget for a coefficient-one logarithmic kernel is

\[
2\log2-\frac34\approx0.6362943611.
\]

For the half-normalized Weil multiplier it is

\[
\log2-\frac38\approx0.3181471806.
\]

Constant subtractions are rank-one kernels. They must be assembled with the
finite block rather than charged to the pure high-mode norm. Once the exact
Poisson/image identity fixes the common prefactor and constants, these bounds
supply the entire repeated-image remainder.
