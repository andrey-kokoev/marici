# v161: global L2 operator/chain-map correction

A proof audit corrected the wording of module 188. Positive degree shifts and
strict cutoff compatibility construct one global locally finite labelled
operator, but do not by themselves prove commutation with ambient chain
differentials. The module and checker now say operator rather than chain map.

`rzk/189-l2-global-chain-map-gate.rzk.md` defines the missing witness exactly:
for every source element,
`dTarget (L2operator x) = L2operator (dSource x)`. The remaining executable
step is to model the global source and target differentials used by the road
complex and verify this identity on labelled generators. Local finiteness then
extends the generator calculation termwise.

This correction preserves the all-degree operator and projection results while
preventing them from being promoted prematurely to global road-Cech closure.

Modules 188 and 189 jointly typecheck; module 189 passes all six declarations
without assumptions.
