# Transition occupancy is a restricted Christoffel trace problem

## Question

What exact quantity controls the number of polynomial-ensemble particles in the buffered transition region \(C=[y_-,y_+]\)?

The size-\(n\) orthogonal-polynomial ensemble is determinantal with projection kernel

\[
K_n(x,y)=\sum_{j=0}^{n-1}P_j(x)P_j(y).
\]

Let \(\mathsf K_{n,C}\) be the integral operator obtained by restricting this kernel to \(C\) with the Weibull measure. Then

\[
\mathbb E[N_C]
=\operatorname{Tr}\mathsf K_{n,C}
=\int_C K_n(x,x)\,d\nu(x),
\]

and its probability generating function is

\[
\mathbb E[s^{N_C}]
=\det\big(I+(s-1)\mathsf K_{n,C}\big).
\]

In particular,

\[
\Pr(N_C\geq1)
\leq\operatorname{Tr}\mathsf K_{n,C}.
\]

Thus negligible transition occupancy requires a restricted Christoffel-trace estimate, not merely small scalar measure of \(C\).

## Artifact boundary

The current endpoint Christoffel calculations evaluate \(K_n(0,0)\) after translation. They do not bound the integral of the diagonal kernel across a growing interval. The trivial projection bound

\[
0\leq\operatorname{Tr}\mathsf K_{n,C}\leq n
\]

provides no reduction in the cross-pair count.

## Disposition

Resolve the occupancy reduction, but do not claim concentration. The next leaf is `transition-christoffel-trace`: bound or compute the restricted kernel trace on the moving buffered interval. Until then, the earlier \(n^2\) cross-pair remainder cannot be improved by occupancy arguments.

## Claim boundary

The determinantal identities are exact. No asymptotic occupancy law, eigenvalue decay, or transition-sector suppression is established.
