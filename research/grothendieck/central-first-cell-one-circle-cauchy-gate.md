# One coarse disk bound would certify the entire first central cell

The weakest chord `[10^-8,3*10^-8]` has certified weighted curvature average
at most `-3.5928133617e-5`. To make `H''` negative everywhere on that cell, it
is enough that

\[
 \sup|H'''|<\frac{3.5928\cdot10^{-5}}{2\cdot10^{-8}}
 \approx1796.4.
\]

This does not require a delicate fifth-order real Taylor remainder. Suppose one
proves the coarse complex-disk gate

\[
 \boxed{|F'(t)|\ge\frac1{16}\quad\text{for }|t|\le\frac14.}
\]

Then the branch `H=(F')^(-1/2)` is analytic on the disk and `|H|<=4` there.
Cauchy's estimate on the inner radius `3*10^-8` gives

\[
 \sup|H'''|\le
 \frac{3!\,4}{(1/4-3\cdot10^{-8})^3}<1536.001.
\]

Multiplying by the first-cell width leaves a strictly positive pointwise
concavity margin about `5.21e-6`. Hence the boxed disk inequality plus the
already certified chord average proves `H''<0` throughout the first cell.

## New attack target

The continuum problem has become a single robust nonvanishing estimate for
`F'` on a fixed disk, rather than a tiny real-axis remainder. The proposed
lower bound `1/16=0.0625` is coarse compared with the central value
`F'(0)~0.09246`. It can be attacked using the centered even Xi series with
interval polynomial/radius bounds, and the quarter-point jet lies exactly on
the disk boundary.

The disk modulus bound has not yet been proved. This packet proves only that it
is sufficient; it does not establish first-cell continuum concavity or RH.

## Durable verification

- Checker: `checkers/central_first_cell_cauchy_gate.py`
- Result: `results/central-first-cell-cauchy-gate.json`
