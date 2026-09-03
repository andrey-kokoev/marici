# The quarter pivot amplitude is a convergent renormalized product

## Question

How can the amplitude \(C\) be separated from the universal \(m^2\) growth?

With

\[
R_m=\prod_{j=1}^m c_j,
\]

define

\[
\rho_j=\frac{c_j}{1+2/j}.
\]

The reference product telescopes exactly:

\[
\prod_{j=1}^m\left(1+\frac2j\right)
=\frac{(m+1)(m+2)}2.
\]

Therefore

\[
\frac{2R_m}{(m+1)(m+2)}
=\prod_{j=1}^m\rho_j.
\]

If \(c_j=1+2/j+O(j^{-2})\), then \(\rho_j=1+O(j^{-2})\). Absolute summability of \(\rho_j-1\), together with positivity, gives a finite positive product, and

\[
C=\lim_{m\to\infty}\frac{R_m}{m^2}
=\frac12\prod_{j=1}^{\infty}\rho_j.
\]

The amplitude conjecture becomes the exact product target

\[
\prod_{j=1}^{\infty}\rho_j
=rac{208}{1575}.
\]

## Disposition

Resolve the renormalization step. The next leaf is `quarter-renormalized-pivot-product-evaluation`: find a closed formula or telescoping factorization for \(\rho_j\) whose infinite product is \(208/1575\).

## Claim boundary

The product representation does not establish the local \(O(j^{-2})\) bound or evaluate the product. Numerical partial products remain downstream of the determinant grid and cannot prove the rational target.
