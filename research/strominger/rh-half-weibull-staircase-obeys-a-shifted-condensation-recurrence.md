# The half-Weibull staircase obeys a shifted condensation recurrence

## Question

Does the staircase determinant admit a closed recurrence compatible with the parameter shift needed for \(\alpha=0\) versus \(\alpha=1\)?

Let

\[
S_n(a,b)=\det[(a+i)_j(b+i)_j]_{i,j=0}^{n-1}
\]

and \(q_i=(a+i)(b+i)\). Applying the Desnanot--Jacobi identity to the first and last rows and columns, then factoring the first Pochhammer term from shifted columns, gives

\[
S_n(a,b)S_{n-2}(a+2,b+2)
=
q_{n-1}S_{n-1}(a,b)S_{n-1}(a+2,b+2)
-q_0S_{n-1}(a+1,b+1)^2.
\]

The two terms have distinct origins. The first-row/first-column minor contributes

\[
\prod_{i=1}^{n-1}q_i\,S_{n-1}(a+2,b+2),
\]

while the two cross minors are shifted copies of \(S_{n-1}(a+1,b+1)\); cancellation against the central minor leaves exactly \(q_{n-1}\) and \(q_0\).

## Disposition

Resolve the exact structured recurrence. It couples the required relative staircase factor to adjacent parameter shifts without assuming a product formula.

The next leaf is `half-weibull-condensation-dominant-balance`: insert a logarithmic asymptotic ansatz into this recurrence and determine whether it forces the relative \(5/9\) coefficient.

## Claim boundary

The subtraction can involve cancellation between terms of comparable size. Taking logarithms or discarding the second term requires a separately proved dominance estimate.
