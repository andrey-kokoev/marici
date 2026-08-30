# Threshold multiplicity probe

Owner: `marici.Figueiredo`.

## Question

WP194 added a composite hidden mediator that collides with the frozen mediator
under binary threshold detection and `epsilon` response. This packet tests the
next probe:

Can resolved threshold multiplicity separate the composite rival?

## Exact claim

Binary threshold detection is not enough:

- frozen nonzero mediator: threshold present, epsilon trace `hnf`;
- composite hidden mediator: threshold present, epsilon trace `hnf`.

Resolved threshold multiplicity separates them:

- frozen nonzero mediator: multiplicity `1`;
- composite hidden mediator: multiplicity `2`.

On the four-origin domain

`{local, frozen mediator, zero-accessible mediator, composite hidden mediator}`,

the pair `(threshold_multiplicity, epsilon_trace)` is discrete.

## Disposition

This repairs the WP194 open-world rival, but only conditionally. Multiplicity
is a stronger threshold instrument than binary detection. It must be physically
typed and resolved; it cannot be inferred from the binary threshold result.

## Exact checker

- Checker: `checkers/wp195_threshold_multiplicity_probe.py`
- Result: `results/wp195_threshold_multiplicity_probe.json`

The checker verifies that binary threshold detection leaves the frozen/composite
collision, while threshold multiplicity plus epsilon trace separates all four
origins.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: do not promote binary threshold detection to multiplicity
  resolution without an instrument contract.

## Report to `marici.Nima`

- Admitted state domain: four-origin class including composite hidden mediator.
- Faithful quotient coordinate: threshold multiplicity plus epsilon trace.
- Source-authorized probe family: multiplicity-resolved threshold spectroscopy
  and epsilon intervention, if admitted.
- Contextual partition: binary threshold has a frozen/composite collision;
  multiplicity resolves it on this domain.
- Classification: conditional multiplicity probe.
- Smallest exact falsifier to binary faithfulness: frozen and composite
  mediators share threshold presence and epsilon trace.
- Remaining physical-instrument gate: derive multiplicity resolution and its
  detector error model.
