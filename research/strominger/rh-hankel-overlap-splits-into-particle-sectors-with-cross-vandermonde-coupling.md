# The Hankel overlap splits into particle sectors with cross-Vandermonde coupling

## Question

What exact determinant object results from cutting the Weibull domain at the Laguerre--Weibull overlap scale?

For a positive weight \(w\), Andréief's identity gives

\[
D_n=\frac1{n!}
\int_{[0,\infty)^n}
\Delta(x)^2\prod_{i=1}^n w(x_i)\,dx_i.
\]

Let \(A=[0,y_*]\) and \(B=[y_*,\infty)\). Partitioning configurations by the number \(k\) of coordinates in \(A\) yields the exact sector decomposition

\[
D_n=
\sum_{k=0}^n
\frac1{k!(n-k)!}
\int_{A^k\times B^{n-k}}
\Delta_A^2\Delta_B^2
\prod_{i\in A,\,j\in B}(x_j-x_i)^2
\prod_iw(x_i)\,dx_i.
\]

The normalization follows by symmetry: the \(\binom nk\) assignments cancel the original \(n!\) denominator to \(1/[k!(n-k)!]\).

## Consequence

The determinant does not factor into a local Laguerre determinant times a far Weibull determinant. The cross-Vandermonde term carries the coherence of one polynomial ensemble across the cut. Dropping it reproduces the independent-region defect already identified at the kernel level.

## Disposition

Construct the exact matched Hankel sector factorization. The next leaf is `cross-vandermonde-interface-asymptotic`: estimate the cross interaction uniformly in the particle number \(k\), rather than fitting independent determinants.

## Claim boundary

This is an exact reorganization of the determinant integral. It supplies no saddle, concentration estimate, dominant sector, or \(1/n\) coefficient.
