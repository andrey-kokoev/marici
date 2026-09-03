# Hankel gamma grows on the moving Laguerre length scale

## Question

How does the finite Hankel \(1/n\) coefficient depend on the tail start \(X=\log q\)?

The degree-eight proxy increases across \(q=3,12,48,192,768\):

\[
0.0492,
0.0892,
0.1228,
0.1529,
0.1808.
\]

A descriptive power fit gives exponent \(0.723\). This is close to the moving Laguerre length exponent

\[
L_X=\frac{X^{1-\beta}}{2a\beta},
\qquad1-\beta=\frac34.
\]

Thus the source-motivated conjecture is

\[
\gamma_X=O(X^{3/4}),
\]

not a uniform constant in the moving start.

## Consequence

Tail movement improves the direct quadrature endpoint prefactor \(q^{-1}\), while the recurrence perturbation coefficient grows only on a logarithmic power scale. If the conjectured law is proved, then

\[
\frac{\gamma_{\log q}}{q}
=O\!\left(\frac{(\log q)^{3/4}}q\right)
\longrightarrow0.
\]

This is compatible with the desired moving-start endpoint decay.

## Disposition

Complete the finite tail-start grid. The next leaf is `hankel-gamma-laguerre-scaling`: derive or falsify \(\gamma_X\asymp X^{3/4}\) from the translated Weibull scaling rather than regression.

## Claim boundary

The fitted exponent is not a theorem, and degree eight need not approximate \(\gamma_X\) uniformly as \(X\) grows.
