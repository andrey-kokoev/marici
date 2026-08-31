# The gradient-pivot tau-p candidate fails fixed-fiber typing

The physical normal-adapter prior art uses three pivots `(a,b,c)`. The target
triple-wall fiber has only coordinates `(a,b)`; `c=-(x+y+z)` is a base-dependent
parameter. Restricting the adapter to the fixed fiber therefore leaves two
charts, one overlap, and no Čech triple face. It cannot supply the ordered
exceptional `sigma123` cell.

Retaining the `c` pivot would require a new relative base–fiber comparison,
including a section of the residue exact sequence that fixes its invisible
kernel component. Residue monicity alone cannot provide this because the
residue functor has kernel rank one.

Thus the prior Cartan/second-Čech construction remains a useful pattern but is
not directly transportable to the target. A valid lift now requires either a
source comparison allowing the base direction in the relative total space or
a different native three-chart cover of the two-dimensional marked fiber.
