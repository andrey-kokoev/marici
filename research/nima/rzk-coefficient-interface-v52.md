# v52: divisor-complement lift torsor

`rzk/68-divisor-complement-lift-torsor.rzk.md` records the seven principal
charts of the maximal local lifting locus and a local generic-unit lift on each.
It retains twelve separately labelled common-to-branch overlap residues.

The singleton positive-family residue used by the all-degree detector is a
native finite Cech one-cochain. Its evaluation is one. In its detected fine
degree the available Cech zero-cochain has zero coboundary, so an asserted
coboundary equality implies `0_Z=1_Z`. Thus local lifts are represented on all
seven charts while the global-unit-lift status remains negative.

The torsor annihilator reuses the secondary naturality generator type
`(I_plus,I_minus,tau_plus*tau_minus)`, rather than the primary affine lifting
ideal. For original coefficients the represented global lifting ideal changes
from the primary ideal to this secondary ideal but still excludes the unit.
Both endpoint overlap discrepancies are retained as separate polarity-labelled
data.

A fresh 72-file transitive closure passed in 32.31 seconds. Evidence:
`results/68-divisor-complement-lift-torsor.typecheck.json`.

Scope: the seven actual 215-state local cycles, complete 29-term localization
Cech differential, twelve explicit rational residue coefficients, all-degree
cohomology, and exact global image ideal remain certificate-backed. No physical
source or endpoint connector is constructed.
