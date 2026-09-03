# The truncated Weibull polynomial grid selects the minus-one branch

## Question

Does the polynomial solution behave like the \(n^{-1}\) branch rather than the minimal \(n^{-2}\) branch?

A 520-digit incomplete-gamma Gram--Schmidt calculation through degree seventeen evaluates the orthonormal polynomial at the exterior point zero. On degrees eight through seventeen, the log--log fit gives

\[
|P_n(0)|\asymp n^{-0.95155}.
\]

More directly,

\[
n|P_n(0)|
=0.16068,\ldots,0.16674
\]

increases slowly toward a nonzero value, whereas

\[
n^2|P_n(0)|
=1.285,\ldots,2.835
\]

grows throughout the grid. This discriminates the \(n^{-1}\) model from \(n^{-2}\) at finite degree and supports

\[
\mathcal W(P,G)\ne0.
\]

## Disposition

Complete finite minimal-solution separation in favor of the \(p=-1\) branch. The next leaf is `weibull-nP-positive-limit`: prove that \(n(-1)^nP_n(0)\) converges to a strictly positive constant using the asymptotic recurrence basis and a uniform remainder estimate.

## Claim boundary

Finite precision and degree do not prove the positive limit or Wronskian nonvanishing. The calculation supplies a discriminating diagnostic, not the required asymptotic theorem.
