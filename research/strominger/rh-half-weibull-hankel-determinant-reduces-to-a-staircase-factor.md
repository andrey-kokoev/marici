# The half-Weibull Hankel determinant reduces to a staircase factor

## Question

Can the half-Weibull factorial Hankel determinant be reduced to a standard product whose logarithmic coefficient is accessible?

For \(\beta=1/2\), duplication of the gamma function gives, after removing row, column, and scale constants,

\[
m_k^{(\alpha)}\propto
(a)_k(b)_k,
\qquad
a=\alpha+1,
\quad b=\alpha+\frac32.
\]

Using \((a)_{i+j}=(a)_i(a+i)_j\), the normalized Hankel determinant factors exactly as

\[
\det[(a)_{i+j}(b)_{i+j}]_{i,j=0}^{n-1}
=
\left(\prod_{i=0}^{n-1}(a)_i(b)_i\right)
S_n(a,b),
\]

where

\[
S_n(a,b)=
\det[(a+i)_j(b+i)_j]_{i,j=0}^{n-1}.
\]

The \(j\)-th column of \(S_n\) is a polynomial in \(i\) of degree \(2j\). Thus \(S_n\) is a staircase alternant rather than the ordinary consecutive-degree Vandermonde. The missing odd degrees are the residual obstruction to a direct Selberg product.

## Disposition

Complete the exact algebraic reduction, but do not claim a proof of \(5/9\). The gamma-product factor is explicit; the unresolved logarithmic contribution lies in \(S_n(a,b)\).

The next leaf is `half-weibull-staircase-asymptotic`: derive the relative \(\log n\) coefficient of \(S_n(2,5/2)/S_n(1,3/2)\). Combined with Barnes asymptotics of the explicit product, this decides the five-ninths candidate.

## Claim boundary

Calling \(S_n\) staircase-like does not identify it with an ordinary Schur polynomial or supply a product formula.
