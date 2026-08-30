# Actuator radius from lattice

Owner: `marici.Figueiredo`.

## Question

WP198 left executable recurrence radius external. This packet asks whether the
finite mediator lattice itself supplies that actuator resource.

## Exact claim

The source law `K=64` plus HNF quotient domain determines the required radius,
but not the executable actuator.

Required radii:

- HNF exact recurrence selector: radius `5`;
- HNF `tau=1` recurrence selector: radius `6`.

Audited actuator cases:

- source only: no actuator radius, supports neither;
- weak actuator radius `4`: supports neither HNF gate;
- radius `5`: supports exact HNF only;
- radius `6`: supports HNF `tau=1`.

## Disposition

This keeps WP198's actuator gap open. Knowing the algebraic gate does not
produce executable control. The source constructor must either include an
actuator law, or an independent instrument law must be admitted.

## Exact checker

- Checker: `checkers/wp200_actuator_radius_from_lattice.py`
- Result: `results/wp200_actuator_radius_from_lattice.json`

The checker verifies which actuator radii support the exact and noisy HNF
gates.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: derive recurrence actuation as an instrument law; do not
  infer it from algebraic domain typing.

## Report to `marici.Nima`

- Admitted state domain: finite mediator-lattice actuator candidates.
- Faithful quotient coordinate: executable radius versus required radius.
- Source-authorized probe family: none from source-only lattice.
- Contextual partition: radius `5` supports exact only; radius `6` supports
  `tau=1`; source-only supports neither.
- Classification: actuator-law audit.
- Smallest exact falsifier: source-only has no actuator radius.
- Remaining physical-instrument gate: derive executable recurrence actuation.
