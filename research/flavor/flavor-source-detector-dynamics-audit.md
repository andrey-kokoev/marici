# Source detector dynamics audit

Owner: `marici.Figueiredo`.

## Question

WP218 left source-derived detector dynamics as the strongest original-selector
route. This packet asks what would make that route genuine rather than a
renamed detector declaration.

## Gate

A source detector law must independently entail both layers:

- WP215 detector features:
  - strict interval comparator;
  - single-fault sentinel;
  - exchangeable width/background channels.
- WP216 realization fields:
  - executable operation;
  - calibrated error contract;
  - source coupling/descent.

Renaming the WP215 architecture as a source law is not enough. A source action
that couples to the quotient but does not produce detector outputs is also not
enough. A source action that produces detector outputs but lacks calibration is
still not enough.

## Disposition

The live route is narrower now: construct an independent source action whose
equations entail the full detector tuple, including calibration. Without that,
the programme has a coherent conditional scaffold but not an admitted physical
selector.

## Exact checker

- Checker: `checkers/wp219_source_detector_dynamics_audit.py`
- Result: `results/wp219_source_detector_dynamics_audit.json`

The checker verifies that only the full source-detector law passes admission
and that a renamed architecture fails.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: next work should either build the source action or prove
  that current flavor dynamics lacks the required detector-output channel.

## Report to `marici.Nima`

- Admitted state domain: candidate source laws for detector dynamics.
- Faithful quotient coordinate: original `physical16` with source-law descent
  explicitly included.
- Source-authorized probe family: none admitted until an independent source
  action entails the full detector tuple.
- Contextual partition: renamed architecture, source action without detector
  output, uncalibrated detector output, full source-detector dynamics.
- Classification: source-detector dynamics derivation audit.
- Smallest exact falsifier: independent source action that entails detector
  features and executability but lacks calibrated error contract.
- Remaining physical-instrument gate: provide a concrete source action whose
  equations entail the full detector tuple, including calibration.
