# The existing central mesh has a large estimated continuum safety factor

The continuum upgrade requires an interval bound for `H'''` on each adjacent
cell. Before constructing the fifth-order Xi-log jets, a 90-digit finite-
difference reconnaissance evaluated `H''` and `H'''` at the twelve cell
midpoints of the directed chord mesh.

Every sampled `H''` is negative. On the hardest and shortest cell
`[10^-8,3*10^-8]`,

\[
 H''\approx-3.6065\times10^{-5},\qquad
 H'''\approx3.8208.
\]

Multiplying the estimated `|H'''|` by the full cell width gives only
`7.64e-8`. The certified weighted-curvature margin on that cell is at least
`3.59e-5`, so the estimated oscillation is smaller by a factor of about 470.
No other cell has a larger estimated width-times-`|H'''|` budget.

Equivalently, the first cell only requires a rigorous bound

\[
 \sup|H'''|<\frac{3.59\times10^{-5}}{2\times10^{-8}}
 \approx1.80\times10^3,
\]

whereas the observed value is about `3.82`. The fifth-jet interval model can
therefore be quite coarse and still close the continuum argument.

This is numerical reconnaissance using finite differences, not an interval
bound. It establishes feasibility and selects the existing twelve-cell mesh;
it does not itself prove continuum concavity or RH.

An analytic fourth-order source jet subsequently removes finite differences
and refines the hardest-cell estimate to `H'''~3.76186`, with oscillation
`7.524e-8`. See `central-source-analytic-fourth-jet.md`.

## Durable verification

- Checker: `checkers/central_h_third_derivative_reconnaissance.py`
- Result: `results/central-H-third-derivative-reconnaissance.json`

## Retraction

The `H'''~3.8` finite-difference estimate and its apparent point-jet
confirmation are retracted. High-order subtraction amplified point-evaluation
errors. The cancellation-free reflection-even Xi series instead gives
`H'''(0)~4.47e-7` and passes direct value back-substitution. This packet remains
as a conditioning warning, not derivative evidence.
