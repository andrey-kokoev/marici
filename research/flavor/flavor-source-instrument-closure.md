# Source-instrument closure

Owner: `marici.Figueiredo`.

## Question

WP198 gives a source-side constructor law. WP199 and WP200 show that detector
and actuator laws remain external. This packet asks:

If an explicit instrument law is admitted, does the combined package close the
conditional selector gate?

## Source law

`finite two-port mediator lattice` supplies:

- `K=64`;
- coupled port law;
- HNF quotient domain;
- epsilon, threshold, and multiplicity probes.

## Instrument law candidates

1. `sharp_radius6`: `width=1/10`, `background=1/10`, actuator radius `6`.
2. `borderline_radius6`: `width=1/4`, `background=1/4`, actuator radius `6`.
3. `sharp_radius5`: `width=1/10`, `background=1/10`, actuator radius `5`.

## Exact claim

Only `sharp_radius6` closes the gate:

- detector margin: `1/10 + 1/10 = 1/5 < 1/2`;
- actuator margin: radius `6`, sufficient for HNF `tau=1`.

The borderline detector fails by touching intervals. The radius-five actuator
fails the noisy HNF gate.

## Disposition

This is the strongest current positive result, but it is conditional:

`source law + independently admitted instrument law -> conditional selector`.

It is not a source-only explanation. Deutsch's demand is only met if the
instrument law is itself derived from the same constructor or independently
admitted as part of the physical experiment.

## Exact checker

- Checker: `checkers/wp201_source_instrument_closure.py`
- Result: `results/wp201_source_instrument_closure.json`

The checker verifies the source fields and the three instrument-law cases.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: this is the conditional closure theorem; next work should
  attack whether the instrument law is constructor-derived.

## Report to `marici.Nima`

- Admitted state domain: finite mediator-lattice source plus instrument-law
  candidates.
- Faithful quotient coordinate: source/instrument field satisfaction.
- Source-authorized probe family: conditional on instrument law.
- Contextual partition: sharp radius-six closes; detector-borderline and
  radius-five packages fail.
- Classification: conditional source+instrument closure.
- Smallest exact falsifiers: `width+background=1/2` and actuator radius `5`.
- Remaining physical-instrument gate: derive or independently admit the
  sharp radius-six instrument law.
