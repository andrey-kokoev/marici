# An analytic fourth-order source jet confirms the continuum margin

A truncated Taylor algebra now propagates the central variable `t` through
square root, exponentials, logarithms, inversion, the Euler-transformed eta
pair, and the recurrent gamma sector. The source output contains `F` through
fourth derivative, so `H=(F')^(-1/2)` yields `H''` and `H'''` directly without
finite differences.

On the hardest cell midpoint `t=2*10^-8`, the analytic jet gives

\[
 H''=-3.6065339789\ldots\times10^{-5},\qquad
 H'''=3.7618605991\ldots.
\]

The full-cell oscillation estimate is therefore `7.524e-8`, still roughly 477
times smaller than the certified `3.59e-5` average-curvature margin. All twelve
cell-midpoint values of `H''` are negative, and this first cell remains the
largest estimated oscillation budget.

## Repaired jet defect

The first jet draft failed dramatically because it substituted the composed
`t` derivative of eta where the formula for `zeta'/zeta` requires the partial
`s` derivative `eta_s`. The corrected algebra transports `eta(s(t))` and
`eta_s(s(t))` as separate jets. This distinction is mandatory for any interval
version.

The jet is high-precision numerical arithmetic, not yet a Taylor interval
model. Its value is architectural: all operations needed by the fifth-jet
continuum certificate now exist without numerical differentiation. The next
step is to replace each scalar coefficient by a directed interval and attach
Euler/polygamma tails through the required jet order.

## Durable verification

- Checker: `checkers/central_source_fourth_order_jet.py`
- Result: `results/central-source-fourth-order-jet.json`

## Retraction of the high derivative estimate

The reported `H'''~3.76186` is superseded. The reflection-even Xi series
back-substitutes into independently directed point intervals and gives
`H'''(0)~4.47e-7`; the unreduced point jet amplified central cancellation in
its high coefficients. See `central-xi-log-even-series-construction.md`.
