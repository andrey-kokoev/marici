# Constructor-coupled instrument law

Owner: `marici.Figueiredo`.

## Question

WP202 showed that WP201 is not hard to vary if the instrument law is external.
This packet tests the stronger candidate:

What if the constructor itself entails the sharp radius-six instrument law?

## Candidate

`self_reading_finite_two_port_mediator_lattice`

It entails:

- `K=64`;
- HNF quotient domain;
- epsilon, threshold, and multiplicity probes;
- detector bounds `width=1/10`, `background=1/10`;
- actuator radius `6`.

## Exact claim

Within the frozen toy domain, this blocks the WP202 rival-instrument kernel.
The borderline detector and weak actuator variations are incompatible with the
constructor law.

The selector gate closes:

`width + background = 1/5 < 1/2`, and radius `6` supports HNF `tau=1`.

## Disposition

This is the first hard-to-vary candidate within the toy domain. It is still not
a physical derivation. The remaining gate is to derive the self-reading
instrument law from actual flavor dynamics rather than declaring it.

## Exact checker

- Checker: `checkers/wp203_constructor_coupled_instrument_law.py`
- Result: `results/wp203_constructor_coupled_instrument_law.json`

The checker verifies the source fields, instrument fields, selector margin, and
incompatibility of the WP202 rival instruments with the constructor-coupled
law.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: the next attack must target physical derivation of the
  self-reading law, not its formal consistency.

## Report to `marici.Nima`

- Admitted state domain: frozen toy constructor with coupled instrument law.
- Faithful quotient coordinate: full source+instrument tuple.
- Source-authorized probe family: candidate self-reading recurrence/threshold
  family.
- Contextual partition: WP202 rival instruments are incompatible with the
  constructor-coupled law.
- Classification: hard-to-vary candidate within frozen toy domain.
- Smallest exact falsifier: absent physical derivation of the self-reading law.
- Remaining physical-instrument gate: derive self-reading detector and actuator
  bounds from flavor dynamics.
