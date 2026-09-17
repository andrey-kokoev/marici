# Correction: truncated prime translations are not pointwise multipliers after squaring

For a zero-extended test `f`, the quadratic identity

\[
\langle f,T_af\rangle
=\int e^{iua}|\widehat f(u)|^2du
\]

is valid. It identifies the prime contribution to the form with a cosine
multiplier. It does **not** identify the interval operator output
`chi_I T_a chi_I f` with the restriction of the whole-line multiplier output.

This distinction disappears in `Z^*AZ` but matters in `Z^*A^2Z`. Squaring the
pointwise symbol retains translated output lying outside the interval, whereas
the Schur residual uses the compressed interval operator. The failed Parseval
scout made exactly this substitution, explaining why its purported residual
Gram was not positive semidefinite.

The correct complete residual Gram remains

\[
R^*R=\|AZ\|_{L^2(I)}^2-\|P^*AZ\|^2.
\]

It can still be computed finitely: evaluate the interval output

\[
H=(q_RI+P_{2,3}+E)Z
\]

piecewise in physical space, then apply the band multiplier correction using
the actual Fourier transform of the zero extension of `H`, not
`(q_R-\sum c_p\cos(u\log p))\widehat Z`. Since `H` is piecewise polynomial
plus two exponentials, that transform is a finite collection of endpoint
oscillatory integrals and is Arb-certifiable.
