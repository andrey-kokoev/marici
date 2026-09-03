# Exact Mellin-Hankel determinants suppress the first shift through degree twenty-two

## Question

Does exact untruncated moment arithmetic preserve the numerical evidence for \(a_1=0\)?

After \(t=2x^{1/4}\), discard the common measure factor and use the integer moments

\[
\mu_k=(4k+3)!.
\]

Let

\[
D_n=\det[\mu_{i+j}]_{i,j=0}^{n-1}.
\]

The monic recurrence coefficient is determined exactly by

\[
a_n^2=\frac{D_{n+1}D_{n-1}}{256D_n^2}.
\]

Fraction-free Bareiss elimination computes positive exact determinants through \(D_{23}\), hence \(a_n\) through degree twenty-two without quadrature or Gram--Schmidt conditioning. Cubic inverse-degree fits on successively later windows give

\[
a_1=-1.21\times10^{-5},
\quad-6.99\times10^{-6},
\quad-4.17\times10^{-6}.
\]

The limiting constant estimate stabilizes near \(A=189.07273\).

## Disposition

Complete the exact finite Mellin-Hankel reduction. It confirms that the near-zero first shift is not a floating quadrature artifact and supplies the canonical determinant ratio whose asymptotics must be proved.

The next leaf is `mellin-hankel-determinant-asymptotic`: prove

\[
\log\frac{D_{n+1}D_{n-1}}{D_n^2}
=\log(256A^2n^8)+O(n^{-2}),
\]

whose absence of a \(1/n\) term is equivalent to \(a_1=0\).

## Claim boundary

Exact finite determinants do not prove their large-degree expansion. Window regression remains diagnostic even when its inputs are exact.
