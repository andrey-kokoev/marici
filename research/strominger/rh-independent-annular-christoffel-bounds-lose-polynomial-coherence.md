# Independent annular Christoffel bounds lose polynomial coherence

## Question

Can the entire shifted Weibull tail be retained by summing endpoint-evaluation bounds over all fixed-width far annuli?

Let \(I_j=[jY,(j+1)Y]\), \(j\geq1\). For degree at most \(K\), the unweighted evaluation kernel of \(I_j\) at zero is

\[
\mathcal K_{j,K}(0,0)=\frac1Y\sum_{n=0}^K(2n+1)P_n(2j+1)^2,
\]

where the sign of the exterior coordinate is immaterial after squaring. If \(w_X\) is the translated Weibull weight, monotonicity gives

\[
\int_{I_j}|p|^2w_X
\geq
\frac{w_X((j+1)Y)}{\mathcal K_{j,K}(0,0)}|p(0)|^2.
\]

Summing all disjoint annuli is valid and yields the certificate

\[
C_K(X,Y)=
\sum_{j\geq1}
\frac{w_X((j+1)Y)}{\mathcal K_{j,K}(0,0)}.
\]

## Obstruction

For every fixed \(j\), \(\mathcal K_{j,K}(0,0)\to\infty\), so its summand tends to zero. The summands are dominated by their \(K=1\) values, which are summable because

\[
\mathcal K_{j,1}(0,0)
=Y^{-1}[1+3(2j+1)^2]
\asymp j^2/Y.
\]

Dominated convergence therefore gives

\[
C_K(X,Y)\longrightarrow0.
\]

Thus summing independently optimized annular Christoffel inequalities retains the entire tail but still supplies no uniform-degree endpoint constant.

## Interpretation

The failure is not loss of tail mass; every annulus is present. It is loss of polynomial coherence: each annulus is minimized by a different extremal polynomial, and summing their separate minima forgets that one polynomial must serve all annuli simultaneously.

## Disposition

Reject independent-annulus summation as the entire-tail transfer. The next constructor must preserve a common polynomial across annuli, for example through recurrence transfer matrices or a global Nevanlinna kernel.

## Claim boundary

This does not prove that the true full-tail endpoint kernel is unbounded. It proves only that the sum of independent annular lower certificates degenerates with degree.
