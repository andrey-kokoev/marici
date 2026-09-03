# The moving Weibull weight has a growing Laguerre overlap window

## Question

Is there a source-derived scale on which a local Laguerre model and the global Weibull weight can be matched?

With

\[
L_X=\frac{X^{1-\beta}}{2a\beta},
\qquad y=L_Xz,
\]

the normalized exponent is

\[
\Phi_X(z)=2a[(X+L_Xz)^\beta-X^\beta].
\]

Its expansion is

\[
\Phi_X(z)=z-rac{1-\beta}{4a\beta}X^{-\beta}z^2
+O(X^{-2\beta}z^3).
\]

Choose the explicit moving cut

\[
z_*(X)=X^{\beta/4}.
\]

Then \(z_*\to\infty\), so the local region grows, while

\[
X^{-\beta}z_*^2=X^{-\beta/2}\to0.
\]

Thus the Laguerre approximation is uniformly asymptotic at the matching cut, and the cut still leaves the full region \(z\geq z_*\) for the Weibull tail. More generally, every \(z_*=X^\theta\) with \(0<\theta<\beta/2\) supplies an overlap.

In original coordinates,

\[
y_*(X)=L_Xz_*(X)
=\frac{X^{1-3\beta/4}}{2a\beta}.
\]

For \(\beta=1/4\), this is proportional to \(X^{13/16}\).

## Disposition

Construct the scalar matching window. The next leaf is `matched-hankel-factorization`: determine whether splitting at \(y_*\) admits a determinant identity or controlled operator factorization that preserves one polynomial ensemble across both regions.

## Claim boundary

A uniform scalar-weight approximation on a growing interval is not a Hankel-determinant asymptotic. Polynomial degree and matrix size remain uncontrolled; no \(1/n\) coefficient follows yet.
