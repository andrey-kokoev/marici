# Theta Two-Copy Labels Collapse to Divisor-Variance Blocks

## Translation-orbit source

Write the completed theta source as translated copies of one primitive
profile:

\[
\Phi(u)
=
\sum_{n\ge1}n^{-1/2}\phi(u+\log n).
\]

Let

\[
P(z)=\int_{\mathbb R}\phi(U)e^{zU}\,dU.
\]

In the initial convergence sector, translation gives

\[
F(z)
=
\int_{\mathbb R}\Phi(u)e^{zu}\,du
=
P(z)\zeta\left(z+\frac12\right).
\]

Set \(w=z+1/2\).

## Exact two-label block

The logarithmic-curvature numerator is

\[
\mathscr C_F(z)=F(z)F''(z)-F'(z)^2.
\]

Its source representation is

\[
\mathscr C_F(z)
=
\frac12
\iint
(u-v)^2\Phi(u)\Phi(v)e^{z(u+v)}\,du\,dv.
\]

For labels \(m,n\), substitute

\[
U=u+\log m,
\qquad
V=v+\log n.
\]

Then

\[
u-v
=
U-V-\log(m/n).
\]

The term linear in \(\log(m/n)\) vanishes because the primitive product and
the sum-coordinate character are invariant under \(U\leftrightarrow V\).
Consequently every \((m,n)\) block is a sum of only two primitive channels:

\[
(mn)^{-w}
\left(
\mathscr C_P(z)
+
\frac12P(z)^2\log^2(m/n)
\right).
\]

No third two-copy representation survives.

## Divisor grouping

Group label pairs by \(k=mn\). Define

\[
V(k)
=
\sum_{d\mid k}
\left(2\log d-\log k\right)^2.
\]

Then the complete two-copy curvature becomes

\[
\mathscr C_F(z)
=
\sum_{k\ge1}k^{-w}
\left(
d(k)\mathscr C_P(z)
+
\frac12V(k)P(z)^2
\right).
\]

The coefficients satisfy

\[
d(k)>0,
\qquad
V(k)\ge0.
\]

Their Dirichlet generating functions are

\[
\sum_{k\ge1}\frac{d(k)}{k^w}
=
\zeta(w)^2,
\]

\[
\frac12
\sum_{k\ge1}\frac{V(k)}{k^w}
=
\zeta(w)\zeta''(w)-\zeta'(w)^2.
\]

Hence the block decomposition is exactly the product-curvature identity

\[
\mathscr C_F
=
\zeta(w)^2\mathscr C_P
+
P^2\mathscr C_\zeta(w).
\]

## Meaning

The labelled two-copy obstruction is not an uncontrolled matrix over
\((m,n)\). Unique factorization and translation covariance compress it to:

1. primitive-profile curvature, weighted by the divisor count;
2. arithmetic log-ratio variance, weighted by \(V(k)\).

In the Dirichlet chamber the arithmetic channel is manifestly nonnegative.
It is literally the variance of the logarithmic split of \(k\) across two
factors.

This is a stronger reduction than scalar product differentiation because it
identifies the source meaning of both terms and proves representation
completeness before aggregation.

## Remaining obstruction

After analytic continuation to the RH sector, positivity of the Dirichlet
coefficients does not orient their oscillatory transform. The decomposition
therefore does not prove RH.

It does isolate the only possible cancellation:

- primitive archimedean curvature;
- versus arithmetic divisor-split variance.

Any successful modular-current identity must act on these two channels. There
is no hidden third labelled bulk available to repair their sign.

## Falsifier

The reduction fails if the theta summands are not exact translates of one
primitive profile with weight \(n^{-1/2}\), or if a proposed completion
operation mixes labels in a way not compatible with grouping by \(mn\).

A proposed positivity proof fails if it treats \(V(k)\ge0\) in the Dirichlet
chamber as positivity of its analytically continued oscillatory transform.
