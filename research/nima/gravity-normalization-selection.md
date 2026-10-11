# Iteration 3: gravitational normalization is not identifiable in the current model

## Fresh state and inspected sources

This iteration freshly read the iteration-2 local-frame result, the original gravitational checker, `agda/PhysicsConstants.agda`, and the gravity-related formulas/assumptions in the constant table, three-cycle checker and Poisson packet. The old claim-generating scripts were not executed or overwritten.

The current exchange/mixer system is an exact dimensionless record dynamics. No sourced map from its records to gravitational mass, spatial potential, matter coupling or an absolute clock has been provided by these inspected files.

## Calibration freedoms survive the selected dynamics

For the current twenty-dimensional update U:

- Linearity implies U(lambda z)=lambda U(z).
- Orthogonality implies U^T(kappa I)U=kappa I for every positive kappa.
- A six-step numerical return does not select the duration tau of a step.

The checker verifies the exact matrix relations and several rational calibration controls. Their generality follows directly from linearity and scalar multiplication of the orthogonality identity, not from the number of tested values.

Even if the mathematical counting metric is held fixed by the source, identifying its conserved number with physical energy E=kappa*B remains a separate calibration. The test does not claim that changing that calibration changes the formal unit or forces acceptance of a different mathematical metric.

These freedoms alone address absolute scale, not every possible dimensionless prediction. Therefore a second test freezes external units and the weak-scale calibration.

## Dimensionless check: the gap is not merely units

Freeze hbar=c=1, weak scale v=246 in the same external units, and the same reference mass m*=1. Let eta denote the absent physical readout M_Pl/v. The old candidate assigns

    eta0 = 12*11^15 / (1+1/90-1/5280).

Assigning eta=eta0 or eta=2*eta0 leaves the current record update, witness histories and conservation conditions unchanged. Yet the associated G=1/(v eta)^2 and dimensionless alpha_G=G*m*^2 differ by a factor of four.

These are alternative external READOUT ASSIGNMENTS, not two derived gravitational solutions. Their role is to make the missing constraint explicit: the current record laws contain no equation that identifies eta with either assignment. The checker computes the distinction exactly in fixed units. It does not infer it from a fit to observed gravity.

If the old formula is added as an axiom identifying physical masses, it fixes a number by that new assumption. That is not selection by the presently checked WG operations.

## What the older sources actually establish

- `check_gravitational_constant.py` labels an integer expression as 246 GeV, assigns a Planck/weak hierarchy and explicitly calls the carrier's Planck spacing a fundamental input. It supplies no derivation tying the new exchange state to that spacing.
- `PhysicsConstants.agda` proves arithmetic identities, including 11+4=15 and the denominator products. Its physical names do not turn the Nat equalities into mass, length or coupling identification theorems.
- `newton-law-from-poisson.md` explicitly supplies G and the matter/acceleration coupling. It cannot be reused to select a G that it assumes.
- The constant-table/three-cycle proposals supply their numerical formulas. No newly inspected binding connects their coefficients to the selected exchange or frame-covariant hidden readout.

## Overall outcome of the three selection iterations

1. **Mixer:** selected within the stated common-frame-natural, unital algebra-automorphism, one-factor class, with the existing algebra and metric.
2. **Frame:** independent local naturality forbids a fixed unframed hidden mixer. A retained orthogonal edge supplies relative orientation and yields a covariant family, but that self-attachment removes the additional signal in the tested source class. No absolute physical reference has been derived.
3. **Gravity:** neither a physical matter/geometry readout nor its dimensionless normalization is selected. Arithmetic identities, recurrence and conservation do not remove that gap.

## Stopping boundary

The requested objective is not complete. It is blocked relative to the current model and the inspected source laws. Another algebraic rewrite, broader numerical sweep, or fitted old coefficient cannot select a variable that the physical interpretation has not bound to the model.

A substantive continuation would require a new independently justified source construction: a matter/geometry coupling and calibrated observable, or a physical reference/preparation law and dimensionless mass-ratio identification. This note does not assert that no such theory could exist or that every repository source has been exhausted. It records that none has been supplied in the current construction, and does not manufacture one to satisfy the target.

Without that additional source input, further iterations of this selection task would only add assumptions rather than make the present model select the requested physical quantities. Stop this iteration loop at that boundary rather than presenting conditional constructions as a derivation of G.

## Verification

`python research/nima/checkers/check_gravity_normalization_selection.py` passed with exact rational dilation, conservation and fixed-unit readout controls. Results: `results/gravity-normalization-selection.json`, including source digests.

No old result generator, prior dynamics implementation or arithmetic proof was modified. No new formal proof of gravitational physics, ledger entry, commit or publication is claimed.
