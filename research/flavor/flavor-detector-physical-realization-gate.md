# Detector physical-realization gate

Owner: `marici.Figueiredo`.

## Question

WP215 supplied a compact detector architecture that conditionally entails the
three remaining WP214 gates. This packet asks whether that architecture is
already a physical instrument.

## Gate

No. A detector-feature packet is not yet an executable flavor experiment. The
physical-instrument admission requires three additional fields:

- executable operation;
- calibrated error contract;
- source coupling and descent to the admitted quotient.

## Exact claim

The WP215 features may all be present while physical-instrument authority still
fails. Three hostile variants isolate the failure:

- formal device without calibration;
- calibrated device without source coupling/descent;
- source-coupled specification without executable operation.

Only the fully realized detector tuple passes.

## Disposition

WP216 preserves the WP215 conditional closure but prevents overclaiming. The
detector architecture can become part of a selector only after physical
realization is supplied. Until then it is an architecture-conditional
rigidifier/selector scaffold, not an admitted physical selector.

## Exact checker

- Checker: `checkers/wp216_detector_physical_realization_gate.py`
- Result: `results/wp216_detector_physical_realization_gate.json`

The checker verifies that the three realization fields are jointly necessary
and that any single missing field blocks admission.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: next attack must construct the executable operation or
  prove that no current flavor experiment realizes it.

## Report to `marici.Nima`

- Admitted state domain: WP215 detector-feature packets plus
  physical-realization fields.
- Faithful quotient coordinate: feature realization tuple modulo candidates
  with identical executable, calibrated, source-coupled instrument action.
- Source-authorized probe family: none admitted beyond the conditional
  detector tuple.
- Contextual partition: declared architecture only, formal no-calibration,
  calibrated no-source-coupling, source-coupled non-executable, and fully
  realized detector.
- Classification: physical-instrument realization gate; not a new selector.
- Smallest exact falsifier: any one missing realization field.
- Remaining physical-instrument gate: construct or derive a real flavor
  experiment implementing the fully realized detector tuple.
