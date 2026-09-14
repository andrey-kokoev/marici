# v162: square-zero Bockstein interpretation

The global labelled operator is now placed in its correct algebraic role.
Writing the exact deformation as `A + (u/2) B`, the Smith checker computes
integral relations `x` with `A x=0` and sends them to the cokernel class
represented by `B x`. This is a square-zero deformation/Bockstein construction,
not yet an ambient road-complex chain map.

`rzk/190-l2-square-zero-bockstein-operator.rzk.md` defines the relation type,
its source projection, the Bockstein representative, and the deformed labelled
operator. It records that the global local-finiteness result applies to this
deformed operator.

Accordingly module 189 remains a valid generic chain-map gate, but it cannot be
inhabited merely from the A/B relation computation. The road source and target
differentials and a comparison from this Bockstein object into the road-Cech
complex are still required.

The new module passes all eight declarations without assumptions.
