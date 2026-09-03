# The quarter Hankel logarithm splits into Barnes and four-staircase terms

## Question

How much of the required \((3/8)\log n\) coefficient is supplied by explicit gamma products?

The multiplication formula gives, up to moment-scale constants,

\[
(4k+3)!\propto
\prod_{s\in\{1,5/4,3/2,7/4\}}(s)_k.
\]

Factoring \((s)_{i+j}=(s)_i(s+i)_j\) from each row yields

\[
D_n=C_n
\left[
\prod_{i=0}^{n-1}
\prod_s(s)_i
\right]
S_n^{(4)},
\]

where \(C_n\) contains elementary row and column scales and

\[
S_n^{(4)}=
\det\left[
\prod_s(s+i)_j
\right]_{i,j=0}^{n-1}.
\]

The explicit product is a ratio of Barnes \(G\)-functions. For one parameter \(s\), the \(\log n\) coefficient in \(\log G(n+s)\) is

\[
\frac{(s-1)^2}{2}-\frac1{12}.
\]

Summing over \(s=1,5/4,3/2,7/4\) gives

\[
\frac12\left(0^2+\left(\frac14\right)^2+\left(\frac12\right)^2+\left(\frac34\right)^2\right)-\frac4{12}
=\frac5{48}.
\]

Therefore the target \(3/8=18/48\) requires the four-staircase factor to contribute

\[
\frac{13}{48}\log n.
\]

## Disposition

Resolve the explicit Barnes contribution. The next leaf is `quarter-four-staircase-thirteen-forty-eight`: prove the \((13/48)\log n\) coefficient for \(S_n^{(4)}\).

## Claim boundary

Elementary scale factors must be tracked in a full determinant theorem, but their forms are polynomial in \(n\), \(n^2\), and \(n\log c\); they do not supply an additional isolated \(\log n\) term. The staircase coefficient remains unproved.
