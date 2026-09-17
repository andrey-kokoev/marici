# The modified-gamma Bernstein budget closes rank-670 quadrature

The established unit-panel Bernstein estimate on `[0,250]`, with ellipse
semiminor `0.2`, bounds every rank-independent normalized gamma matrix entry
by using

\[
|\widehat\phi_n(u)|\le\sqrt{2L}e^{L|\Im u|}.
\]

For the original normalized gamma symbol the uniform integrand majorant was
`3`, and 250 panels at Gauss order 48 had total entry error
`2.544e-13`.

The modified symbol is `q(u)-q(250)`. On the same ellipse, subtracting the
constant adds at most

\[
\frac{q(250)}\pi\,2L e^{2L(0.2)}<0.805
\]

to the integrand majorant. Hence the old remainder scales to at most

\[
2.544\times10^{-13}\frac{3+0.805}{3}
<3.227\times10^{-13}
\]

per matrix entry. The rank-670 calculation uses order 64, so retaining the
larger order-48 remainder is conservative.

A symmetric `670 by 670` error matrix with this entry bound has spectral norm
at most

\[
670(3.227\times10^{-13})<2.163\times10^{-10}.
\]

This is below one percent of the directed-node even midpoint margin
`2.6070751e-8`. Together with the Arb node radius, the rank-670 gamma-floor
matrix is positive definite.
