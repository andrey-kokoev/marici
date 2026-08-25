# Detector derivation chain

Owner: `marici.Figueiredo`.

## Purpose

WP206-WP213 derived the detector constants in stages. This packet closes the
branch by recording the dependency chain and the remaining external gates.

## Chain

The conditional chain is:

`minimal nonzero fault tolerance`
`-> one-bad contract`
`+ strict below-quarter target`
`-> five-copy minimality`
`-> one-fifth safety cap`
`+ width/background exchange symmetry`
`-> width = background = 1/10`.

Strict interval separation is already part of the branch convention and
explains why touching boundaries fail.

## Remaining gates

The checker identifies three external gates:

- minimal nonzero fault tolerance;
- strict below-quarter target;
- width/background exchange symmetry.

Everything else in the detector constant chain follows conditionally from
those gates.

## Disposition

The detector constants are no longer arbitrary, but they are not unconditional.
The next physical task is to derive or admit the three remaining detector gates
from architecture.

## Exact checker

- Checker: `checkers/wp214_detector_derivation_chain.py`
- Result: `results/wp214_detector_derivation_chain.json`

The checker verifies dependency closure, remaining external gates, and
acyclicity.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: do not extend detector arithmetic; derive the three
  remaining architecture gates.

## Report to `marici.Nima`

- Admitted state domain: detector derivation dependencies.
- Faithful quotient coordinate: dependency graph and external gate set.
- Source-authorized probe family: conditional on three remaining gates.
- Contextual partition: one-tenth constants are conditionally derived, not
  unconditional.
- Classification: detector derivation closeout.
- Smallest exact falsifier: remove any remaining gate and the chain no longer
  derives one-tenth constants.
- Remaining physical-instrument gate: derive the three external gates.
