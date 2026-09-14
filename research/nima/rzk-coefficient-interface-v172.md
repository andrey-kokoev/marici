# v172: L2 transition detector divisibility

An integral left-annihilator computation at D16 now tests whether the
distinguished transition can map to the primitive logarithmic unit.

The saturated integral left annihilator of the u0 image has rank 31. Evaluating
all of its basis functionals on `3a^3+3a^3b`, their values generate the ideal
`(3)`. Therefore no integral functional annihilating the A-image pairs this
transition to one.

A unit pairing with the primitive log line requires normalization by `1/3`, or
an integral extension/different physical class. This isolates a genuine
3-primary normalization gate and agrees with the 2/3-primary Smith support.

The rank-one readout from module 199 is also clarified: rho is a functional on
the Bockstein image modulo the A-image, not on the cokernel after adjoining the
full Bockstein image.

Evidence is the refreshed `results/L2-bockstein-relation-smith-D16.json`.
`rzk/200-l2-transition-detector-divisibility-d16.rzk.md` passes all eight
declarations without assumptions.
