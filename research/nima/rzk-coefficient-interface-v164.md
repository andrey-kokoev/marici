# v164: L2 Bockstein-to-road-Cech realization target

The gap between the global coefficient Bockstein and geometric road descent is
now represented by one dependent type.

A realization must assign a global road cell to every integral A-relation and
prove that its road boundary equals the Cech image of the corresponding
Bockstein representative Bx. Modules 190--191 already supply the relation and
representative side as a globally natural filtered system; module 192 exposes
the missing coefficient-to-Cech map, cell realizer, and boundary comparison.

This target is stronger than matching ranks or Smith factors and avoids the
incorrect unit-residual shortcut corrected in module 169. An inhabitant would
turn the actual relation-derived L2 data into road cells uniformly, after which
orientation/cancellation can be applied to the specific physical residual.

`rzk/192-l2-bockstein-to-road-cech-realization.rzk.md` passes all seven
declarations without assumptions. No realization inhabitant is claimed.
