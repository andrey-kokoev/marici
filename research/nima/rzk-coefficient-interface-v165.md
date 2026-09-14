# v165: synthetic coefficient-side road cells

The Bockstein realization interface is inhabited canonically on the coefficient
side. Take a synthetic road cell to be an integral A-relation itself, define its
boundary to be Bx, and realize each relation by identity. The boundary
comparison is then definitional reflexivity.

`rzk/193-l2-synthetic-road-cell-realization.rzk.md` implements this construction.
It demonstrates that the global relation/Bockstein system has a coherent cell
model without adding rank assumptions or choices of Smith basis.

The construction intentionally contains no physical road geometry. The final
geometric gate is now a comparison map from these synthetic relation cells to
the actual soft nearby-cycle road cells, preserving their Bx boundaries. This
is more precise than asking for road cells from scratch: the coefficient-side
source and boundary are already fixed.

The module passes all eight declarations without assumptions.
