# The hard-edge alpha law is relative, not absolute

## Question

What determinant asymptotic is sufficient to derive the fitted hard-edge shift law?

Let \(D_n^{(\alpha)}\) be the Hankel determinant for

\[
x^\alpha e^{-2x^\beta}dx.
\]

The recurrence coefficient obeys

\[
\log a_n^2
=\log D_{n+1}+\log D_{n-1}-2\log D_n.
\]

Suppose the relative free energy has the controlled expansion

\[
\log D_n^{(\alpha)}-\log D_n^{(0)}
=\frac{\alpha}{\beta}n\log n+c_\alpha n+O(\log n),
\]

with a remainder whose centered second difference is \(O(n^{-2})\). Since

\[
\Delta^2(n\log n)=\frac1n+O(n^{-3}),
\]

it follows that

\[
\log\frac{(a_n^{(\alpha)})^2}{(a_n^{(0)})^2}
=\frac{\alpha}{\beta n}+O(n^{-2}),
\]

and therefore

\[
a_1(\alpha)-a_1(0)=\frac{\alpha}{2\beta}.
\]

The \(n\log n\) coefficient is sourced by the hard-edge factor: at the homogeneous scale \(x\asymp n^{1/\beta}\), the contribution \(\alpha\sum_{j=1}^n\log x_j\) has leading term \((\alpha/\beta)n\log n\).

## Disposition

Replace the absolute conjecture by the relative theorem target above. The alpha family cannot prove \(a_1(0)=0\); it only transports a known baseline.

The next leaf is `alpha-relative-determinant-remainder`: prove the relative free-energy expansion with centered-second-difference control. The independent `alpha-zero-baseline` gate must still establish \(a_1(0)=0\).

## Claim boundary

Coulomb-gas power counting identifies the coefficient but not the required remainder regularity. An uncontrolled \(O(n)\) error is insufficient because its second difference need not decay.
