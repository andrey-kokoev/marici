# The weakest certified chord has order-10^-5 average curvature

For a twice differentiable function `H`, put `m=(a+b)/2` and
`d=(b-a)/2`. The midpoint second-difference identity is

\[
 H(a)-2H(m)+H(b)=
 \int_{-d}^{d}(d-|u|)H''(m+u)\,du.
\]

Since the triangular kernel has mass `d^2`, the corresponding weighted average
is

\[
 \langle H''\rangle_{a,b}
 =-\frac{8}{(b-a)^2}
 \left(H(m)-\frac{H(a)+H(b)}2\right).
\]

For the weakest certified central chord `[10^-8,3*10^-8]`, directed interval
propagation gives

\[
 \boxed{\langle H''\rangle\in
 [-3.6213572998\ldots,-3.5928133617\ldots]\times10^{-5}.}
\]

Thus the tiny `10^-21` chord gap is small only because the chord length is
`2*10^-8`; after the correct quadratic normalization, its concavity margin is
macroscopic at roughly `3.6*10^-5`.

## Consequence for continuum certification

The next Taylor-model task does not need twenty digits of pointwise curvature
accuracy. On this shortest cell, it is sufficient to bound the oscillation of
`H''` away from its triangular average by less than `3.59e-5`. Equivalently,
one can bound `H'''` times the cell width strongly enough. This converts the
continuum upgrade from an unspecified interval calculation into a concrete
derivative budget.

The mean-value interpretation assumes `H=1/sqrt(F')` is real and twice smooth
through the chord. A full continuum certificate must establish `F'>0` on each
box simultaneously; pointwise endpoint positivity alone is insufficient.
This result does not prove global concavity or RH.

## Durable verification

- Checker: `checkers/central_chord_average_curvature.py`
- Result: `results/central-chord-average-curvature.json`
