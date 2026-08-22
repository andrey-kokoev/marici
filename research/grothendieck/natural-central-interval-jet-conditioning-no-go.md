# The unreduced central interval jet is unusable on the first cell

A directed interval Taylor jet was propagated through the unreduced source
formula on the hardest cell `[10^-8,3*10^-8]`. Analytic tails were deliberately
omitted from this conditioning probe; they are negligible compared with the
effect observed.

Although point evaluation gives `F'~0.09246`, the natural interval extension
of the singular-prefactor times vanishing-source formula produces

\[
 F'([10^{-8},3\cdot10^{-8}])\subset
 [-1.84\cdot10^{10},1.90\cdot10^{10}].
\]

It therefore cannot even establish `F'>0`, much less form
`H=(F')^(-1/2)`. Raising precision or adding the already tiny eta/gamma tail
bounds cannot repair a dependency enclosure spanning eleven orders of
magnitude.

This is a structural no-go for the unreduced interval implementation. The
continuum certificate must construct the analytic even function

\[
 \ell(t)=\log\Xi(1/2+\sqrt t)
\]

directly and use `F=(4t-1)ell'`, so the square-root cancellation occurs before
interval variables are introduced. Subdividing the existing cell without that
reduction would address the symptom, not the dependency source.

No mathematical positivity conjecture is falsified; only a numerical interval
representation is ruled out. RH remains open.

## Durable verification

- Checker: `checkers/central_interval_jet_first_cell_probe.py`
- Result: `results/central-interval-jet-first-cell-probe.json`
