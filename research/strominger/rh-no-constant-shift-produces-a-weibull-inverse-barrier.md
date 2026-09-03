# No constant shift produces a Weibull inverse barrier

## Question

Can a comparison profile \(u_n=(n+\kappa)^{-1}\) repair the failed unshifted Riccati barrier?

A maximin scan over \(0\le\kappa\le1\), using the 520-digit recurrence grid on degrees eight through sixteen, selects

\[
\kappa=0.52.
\]

It reduces the signed defect obstruction by more than an order of magnitude, but does not reverse it. The best slack remains negative at every tested degree, with

\[
n^4(\varepsilon_n^{*,0.52}-\varepsilon_n)
=-0.02850,\ldots,-0.03017.
\]

The stable fourth-order residual shows that a constant index shift can match the first three asymptotic orders but lacks one parameter at the next order.

## Disposition

Reject all tested constant-shift inverse barriers. The next leaf is `weibull-corrected-inverse-barrier`: add one source-tested correction,

\[
u_n^{(\kappa,c)}
=\frac1{n+\kappa}\left(1+\frac{c}{n^2}
ight),
\]

and determine whether its induced fourth-order defect can produce positive signed slack.

## Claim boundary

The maximin scan is finite and discretizes \(\kappa\) in steps of \(0.01\). It does not exclude an isolated continuum value, but the coherent negative \(n^{-4}\) residual rules out claiming success from the sampled optimum.
