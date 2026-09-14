# v126: oriented road correction

The unit-column requirement is now oriented relative to the actual Cech
residual. A valid road correction must provide a cell whose boundary is the
negative residual, prove residual-plus-boundary is zero, and pair with the
alternating detector by the negative scalar unit.

This fixes a sign ambiguity in the prior unit-cell interface: a positive unit
column only states transversality to the free cokernel, whereas cancellation of
a residual with positive detector value requires the negative unit orientation.
The interface projects both the cancellation equality and oriented detector
hit for direct use in a candidate-completion assembly.

No geometric cell is asserted. The remaining task is now specifically to
construct a soft nearby-cycle cell with boundary `-residual`, not merely any
cell detected nontrivially.

`rzk/154-soft-d1-oriented-road-correction.rzk.md` passes all six declarations
without assumptions.
