# The integrated Christoffel tail is dominated by rank-one gap leverage

## Question

Can the integrated kernel tail be reduced to a one-step quantity visible in finite gap determinants?

Let

\[
f_n=\boldsymbol1_C P_n,
\qquad
A_{n+1}=A_n+|f_n\rangle\langle f_n|.
\]

The matrix determinant lemma gives

\[
\frac{G_{n+1}}{G_n}
=1-\ell_n,
\qquad
G_n=\det(I-A_n),
\]

where

\[
\ell_n=
\langle f_n,(I-A_n)^{-1}f_n\rangle.
\]

Because \((I-A_n)^{-1}\succeq I\),

\[
\int_C|P_n|^2d\nu=\|f_n\|^2\leq\ell_n.
\]

Hence

\[
\sum_{j\geq n}
\int_C|P_j|^2d\nu
\leq
\sum_{j\geq n}\ell_j.
\]

The normalized finite gap data determine \(\ell_n\) exactly by

\[
\ell_n=1-\exp(\log G_{n+1}-\log G_n).
\]

At \(X=\log12\), the finite values of \(n^2\ell_n\) approach the same coefficient near \(0.09\) found in the determinant expansion.

## Disposition

Resolve the integrated-tail problem to the rank-one leverage bound. A theorem \(\ell_n=O_X(n^{-2})\) implies the required integrated tail \(O_X(n^{-1})\).

The next leaf is `gap-leverage-n-minus-two`: derive the leverage decay from the endpoint-selected Jacobi/Fredholm structure.

## Claim boundary

The finite leverage grid is not a decay theorem. The inequality is one-sided; integrated mass may be strictly smaller than leverage.
