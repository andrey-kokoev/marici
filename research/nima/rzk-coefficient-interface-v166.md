# v166: soft D1 realization extends to the full principal road

The support reduction of module 135 is now turned into an actual Rzk extension
theorem. Model the principal road Cech target as the soft-D1 component paired
with all other road components. Since D2, D3, incidences, and corners are zero
by support, embed a soft-D1 value by pairing it with the fixed zero-other value.

Module 194 proves by path application that any boundary comparison on soft D1
extends to an equality on the full principal road target. It also specializes
this to relation-cell boundaries.

Therefore the geometric comparison requested by module 192 does not require
constructing independent cells or homotopies on every road component. A
boundary-preserving realization of the synthetic Bockstein relation cells on
soft D1 alone suffices; all other components extend canonically by zero.

`rzk/194-soft-d1-realization-extends-by-zero.rzk.md` passes all seven
declarations without assumptions.
