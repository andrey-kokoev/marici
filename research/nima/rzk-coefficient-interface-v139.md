# v139: contractible unit-cone road cell

An explicit algebraic road-cell extension now realizes the required unit
boundary. Adjoin the two-term complex `Z<c>[1] --id--> Z<1>[0]`, with
`d(c)=1` and contraction `h(1)=c`. Both contraction identities hold and the
identity differential is an integral unit Smith pivot.

The oriented cell `-c` has boundary `-1`, so it cancels a positive unit residual
with the detector sign required by module 154. Unlike merely adding a target
column, this supplies a genuine chain-level source cell and is contractible, so
it introduces no new cohomology.

This is still algebraic: identifying this cone cell with an actual soft nearby-
cycle road attachment remains open. The geometric task is now to realize a
specific contractible unit cone, not to discover an unspecified correction.

Evidence is `results/soft-axis-unit-cone-cell.json` from
`checkers/check_soft_axis_unit_cone_cell.py`.
`rzk/167-soft-d1-contractible-unit-cone.rzk.md` passes all eight declarations
without assumptions.
