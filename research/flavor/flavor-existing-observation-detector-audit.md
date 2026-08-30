# Existing-observation detector audit

Owner: `marici.Figueiredo`.

## Question

WP216 identified the extra fields required to turn the WP215 detector
architecture into a physical instrument. This packet tests whether the
currently admitted flavor observations already supply those fields.

## Audit

They do not. The measured-ten low-energy family is an executable calibrated
readout, but it is not the WP216 detector tuple. It lacks:

- strict interval comparator;
- single-fault sentinel;
- exchangeable width/background channels;
- source coupling/descent.

The `physical16` coordinate remains the faithful quotient coordinate for source
claims, but coordinates are not themselves an instrument.

## Disposition

This is a negative result. Existing observations cannot rescue the detector
architecture. Any selector claim now needs either a new source-derived
threshold/reference/intervention experiment or a derivation of the detector
tuple from flavor dynamics.

## Exact checker

- Checker: `checkers/wp217_existing_observation_detector_audit.py`
- Result: `results/wp217_existing_observation_detector_audit.json`

The checker verifies that measured ten is a typed readout but not the detector
tuple, and that it remains nonfaithful for `physical16` source identification.

## Calibration

- Pre excitement: `7/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `7/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: next step should propose a genuinely new experiment or
  source-derived operation rather than reusing measured-ten data.

## Report to `marici.Nima`

- Admitted state domain: existing flavor observation families compared with
  the WP216 detector tuple.
- Faithful quotient coordinate: `physical16` for source claims; measured ten is
  only a nonfaithful projection.
- Source-authorized probe family: currently admitted low-energy measured-ten
  readouts.
- Contextual partition: measured-ten readout, formal `physical16` coordinate,
  and WP216 full detector tuple.
- Classification: existing-observation no-go for detector realization.
- Smallest exact falsifier: measured ten is calibrated and executable but lacks
  source coupling/descent and the WP215 detector features while collapsing
  `physical16` pairs.
- Remaining physical-instrument gate: add a new source-derived
  threshold/reference/intervention experiment, or derive the detector tuple
  from flavor dynamics.
