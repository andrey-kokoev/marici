# The gap convergence rate is an integrated Christoffel tail

## Question

What exact operator quantity controls convergence of finite gap determinants to the positive fixed-start limit?

Let

\[
A_n=\boldsymbol1_C P_n\boldsymbol1_C,
\qquad
A=\boldsymbol1_C P_{\mathcal H}\boldsymbol1_C,
\qquad
R_n=A-A_n\geq0,
\]

for \(C=[0,X]\). Since \(I-A\) is invertible, determinant factorization gives

\[
\frac{\det(I-A_n)}{\det(I-A)}
=
\det\left(I+(I-A)^{-1}R_n\right).
\]

After similarity by \((I-A)^{-1/2}\), the correction is positive. Therefore

\[
0\leq
\log\frac{\det(I-A_n)}{\det(I-A)}
\leq
\|(I-A)^{-1}\|\operatorname{Tr}R_n.
\]

The trace tail is exactly

\[
\operatorname{Tr}R_n
=
\sum_{j\geq n}
\int_0^X|P_j(x)|^2d\nu(x).
\]

Thus an \(O(1/n)\) integrated Christoffel-tail bound proves the observed gap convergence rate. A matching asymptotic additionally requires control of the quadratic and higher logarithmic terms.

## Disposition

Resolve the Fredholm rate reduction. The next leaf is `integrated-christoffel-tail-rate`: derive or falsify

\[
\sum_{j\geq n}\int_0^X|P_j|^2d\nu=O_X(n^{-1}).
\]

## Claim boundary

Positivity of the limiting determinant gives a finite resolvent constant for each fixed \(X\), not uniformly in moving \(X\). No trace-tail rate is proved here.
