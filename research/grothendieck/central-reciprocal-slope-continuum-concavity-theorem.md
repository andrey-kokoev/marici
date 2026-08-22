# Reciprocal-slope concavity holds on the full central interval

Let

\[
 H(t)=F'(t)^{-1/2}.
\]

The unit-disk theta certificate and the degree-four modulus certificate give
`|F'|>0.0845202` on `|t|<=1/4`. Thus `H` is analytic there and `|H|<3.5`.

A directed centered Xi-log jet through order 61 gives the Taylor coefficients
of `H` through degree 11. Reflection parity is checked internally through
centered degree 60. For `0<=t<=0.01`, the omitted part of `H'''` is bounded by
differentiating the Cauchy majorant

\[
 3.5\sum_{n\ge12}(t/(1/4))^n.
\]

The expansion ratio is at most `0.04`. Directed Horner evaluation of the
degree-eight polynomial for `H'''`, plus that exact geometric tail, upgrades
every one of the 78 certified triangular averages of `H''` to pointwise
negativity on its chord. The weakest residual margin is

\[
 3.5928133608845\ldots\times10^{-5}>0.
\]

The independently certified value `H''(0)<0`, propagated across the remaining
sliver `[0,10^-8]` with the same `H'''` bound, closes the endpoint. Therefore

\[
 \boxed{H''(t)<0\quad\text{for every }0\le t\le10^{-2}.}
\]

Equivalently, the source-derived reciprocal square-root slope is strictly
concave on this full central interval. This is the first universal coupled
positivity theorem in the program: it replaces finitely many chord witnesses
by a continuum statement. It is local in the spectral coordinate and does not
prove RH.

## Durable verification

- Coefficient checker: `checkers/central_H_degree_eleven_interval.py`
- Continuum checker: `checkers/central_all_chords_continuum_upgrade.py`
- Coefficient result: `results/central-H-degree-eleven-interval.json`
- Continuum result: `results/central-all-chords-continuum-upgrade.json`
