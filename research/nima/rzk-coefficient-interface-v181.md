# v181: supported residue law localized to the selected physical point

Module 131 requires the three-detector residue formula for every class in the
ambient supported carrier. That is stronger than needed to construct and
evaluate one physical amplitude witness.

The localized interface retains three genuine supported functionals—primary,
reciprocal, and relation—but requires

`residue(gysin(physical)) = calibrate(primary,reciprocal,relation)`

only on the Gysin class of the selected decorated physical point. This is
sufficient to prove its amplitude calibrated. The relation functional is the
explicit rho0 selector; the endpoint and reflection comparisons supply the
other two candidate functionals.

The remaining supported law is now one equality on one class, rather than a
global theorem over all supported classes.

`rzk/209-point-supported-three-detector-law.rzk.md` passes all nine declarations
without assumptions.
