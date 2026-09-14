# v183: physical road comparison is blocked before the selected equality

The current physical chart assembly does not supply a global Cech cover of the
three cut sectors. The sectors form a C3-equivariant labelled direct sum because
the source has no double pole involving two distinct cut denominators. Thus the
road-Cech target must be local to one wall sector; it cannot be identified with
the unsupported global three-chart Cech differential.

At the qG12 wall, the actual grades are `(-1,-2,-1)`. No source epsilon or
conductor map transports the qg2 grade-minus-two logarithmic class into the
sewn grade-minus-one wall carrier. Multiplication by x has the desired shift but
would be selected from the target grade and is therefore fitted.

Consequently the first physical equality from module 206—raw physical Cech
residual equals `Cech(v)`—is not currently well typed. Before attempting it one
must construct the source normalization `N_epsilon`, retain occurrence labels
and Jacobians, then identify the normalized qg2 wall class with the selected
order-six vector `v=a^3+a^3b`. Only afterward can the local log-road boundary
comparison be tested.

`rzk/211-physical-road-comparison-typing-obstruction.rzk.md` passes all eight
declarations without assumptions.
