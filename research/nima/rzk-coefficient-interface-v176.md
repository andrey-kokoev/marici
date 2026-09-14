# v176: selected primitive transition is an order-six direction

The divided-transition Smith calculation now holds at D12, D16, and D20.
Adjoining `v=a^3+a^3b` divides the full relation-lattice saturation index by six
at each cutoff. Adjoining the labelled transition `3v` divides it by two.

Thus the selected class v has exact order six in the tested Bockstein quotient,
while the s11 transition is its order-two triple. The explicit detector rho0
sends v to one and 3v to three, matching the primitive versus index-three log
pairings.

This identifies the minimal derived correction for the selected physical log
line: one `Z/6` cell in direction v. The existing s11 transition supplies only
the `Z/2` subclass and leaves the 3-primary part unresolved.

`rzk/204-l2-order-six-primitive-transition.rzk.md` passes all eight declarations
without assumptions.
