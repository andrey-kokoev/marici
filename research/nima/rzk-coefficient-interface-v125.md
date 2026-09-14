# v125: road unit-cell realization interface

The algebraic constant-unit extension is now exposed as the exact remaining
road-chain datum.

`rzk/153-soft-d1-road-unit-cell-interface.rzk.md` defines a realization as a
road cell whose boundary is the target unit and whose alternating detector
pairing is the scalar unit. It provides checked projections for the cell,
boundary equality, and detector hit.

This separates two statements that were previously easy to conflate: module
152 proves that a unit column kills the all-degree free cokernel; module 153
requires an actual global road cell realizing that column. No such inhabitant
is asserted yet. Constructing it from the soft nearby-cycle geometry is now the
precise road-Cech gate.

The Rzk module passes all seven declarations without assumptions.
