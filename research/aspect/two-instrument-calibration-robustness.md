# Two-instrument calibration robustness

Owner: `marici.Aspect`

## Bounded question

Which conclusions of the reciprocal denominator-sewing network and the
directional moving-fiber interferometer survive bounded calibration error,
and which exact features are structurally fragile?

## Source and calibration authority

All perturbations are frozen before evaluating a target residual.  The
denominator network uses the same three calibrated ports and spectrum
`(1/2,1/4,1/5)` as its parent packet.  The moving-fiber instrument uses the
same ordered frame `(k_1,k_2,e_1,e_2)` and forget-marks projection `R`.

The declared amplitude-noise floor is `eta=1/1000`.  It is an instrument
fixture, not a claim about fabricated hardware.

## Robust denominator certificate

The unperturbed static impedance has smallest eigenvalue `1/5`.  A symmetric
calibration perturbation with operator norm strictly below `1/5` preserves
positive definiteness.  Consequently `I+M(z)` remains invertible for
`Re z>0`.  The checker uses the exact hostile perturbation `-(1/10)I`; the
smallest eigenvalue remains `1/10`.

Thus denominator zero-freeness has a finite calibration margin.  The exact
Cayley dark zero does not: adding `(1/100)I` moves the eigenchannel zero from
`z=1/2` to `z=49/100`.  At the old coordinate the numerator is nonzero.  A
dark zero is therefore a movable selected-channel feature, not a protected
consequence of passivity.

Schur determinant factorization remains algebraically exact for every
calibrated matrix whose retained block is invertible.  The physical problem is
estimating its entries and inverse stably, not repairing the identity after a
measurement.

## Robust directional detector

For the forget-marks projection, the horizontal residual is exactly the
lower-left `K -> E` block.  The allowed upper-right extension cannot leak into
this residual.  A single forbidden coupling of size `1/100` is above the
declared `1/1000` noise floor and is detectable.  A coupling of size `1/10000`
is nonzero mathematically but cannot be certified by this instrument.

The same calibration applies to overlap gluing: a lower-left transition
residual must exceed the registered uncertainty before global incompatibility
is claimed.

## Torsion fragility

The exact quarter-turn kernel holonomy satisfies `H^4=I`.  Perturbing one
entry by `1/100` gives a nonzero `H^4-I` residual.  Exact finite-order torsion
is therefore not open under ordinary matrix perturbations.  A laboratory may
bound closeness to torsion, but an exact torsion claim requires discrete source
authority or a symmetry that quantizes the holonomy.

In contrast, nonzero persistent holonomy and forbidden directional leakage
are inequality claims and can carry explicit error margins.

## Constructor order, frame, and detector kernel

Calibrate the common phase frame, estimate the complete transfer matrix,
propagate its covariance to the derived determinant or quotient residual, and
only then compare with the preregistered threshold.  Thresholding intensities
before coherent reconstruction loses signs and can hide cancellation.

One scalar detector cannot distinguish an allowed `E -> K` extension from a
forbidden `K -> E` coupling.  At least the two quotient rows and the prepared
input label must be retained.

## Conserved and dissipated quantities

The robustness margins concern accretivity and coherent transfer residuals.
They do not certify unitary power balance.  Loss and bath ports remain part of
the physical completion contract.

## Smallest hostiles

- a `1/100` isotropic impedance shift moves the exact dark zero while leaving
  the positive denominator certificate intact;
- a forbidden coupling below `eta` exists but is experimentally unresolved;
- a `1/100` holonomy perturbation destroys exact order-four torsion;
- an allowed upper-right extension is nonzero but produces no horizontal
  residual.

## Completion gate

The packet supplies exact finite calibration fixtures, not statistical
coverage, detector covariance, fabrication tolerances, interval arithmetic,
or a physical noise model.  Those must be registered for an experiment.

Run `python research/aspect/checkers/two_instrument_calibration_robustness.py`.
The result is
`research/aspect/results/two_instrument_calibration_robustness.json`.
