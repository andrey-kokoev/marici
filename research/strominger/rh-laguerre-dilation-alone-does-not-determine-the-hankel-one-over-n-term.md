# Laguerre dilation alone does not determine the Hankel one-over-n term

## Question

Does the moving Laguerre length

\[
L_X=\frac{X^{1-\beta}}{2a\beta}
\]

by itself force \(\gamma_X\asymp L_X\) in the compact-truncation determinant ratio?

## Exact dilation law

Under the coordinate dilation \(y=Lz\), moments transform as

\[
\mu_k\mapsto L^{k+1}\mu_k.
\]

Factoring powers from rows and columns gives the exact Hankel law

\[
D_n\mapsto L^{n^2}D_n.
\]

Hence dilation contributes \(n^2\log L\) to \(\log D_n\). It does not create a \(1/n\) term. The coefficient \(\gamma_X\) must come from the dimensionless determinant after dilation, not from dimensional covariance alone.

## Singular local limit

The rescaled shifted Weibull weight converges locally to the Laguerre weight \(e^{-z}\), but the Laguerre moment problem has unbounded endpoint evaluation. The global Weibull problem is indeterminate. Therefore the local limit is singular for precisely the kernel quantity being controlled; convergence on fixed polynomial degrees cannot be promoted uniformly in Hankel size.

The finite proxies make \(\gamma_X/L_X\) nearly constant: the ratio decreases by less than five percent across \(q=3\) through \(768\). This supports proportionality diagnostically, but exact dimensional covariance still does not derive the dimensionless coefficient or control its remainder.

## Disposition

Reject pure Laguerre dilation as a proof of the \(X^{3/4}\) law. Retain `matched-laguerre-weibull-determinant`: a valid derivation must match the local Laguerre window to the far Weibull region while taking Hankel size large.

## Claim boundary

The argument does not falsify \(\gamma_X=O(L_X)\). It shows that such a bound needs global determinant control beyond the exact scaling law.
