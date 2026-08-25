# Missing detector-field ladder

Owner: `marici.Figueiredo`.

## Question

WP220 showed that the finite two-port source does not entail five detector
fields. This packet asks which missing field is the smallest constructive next
target.

## Ladder

The fields separate into three levels:

- structural fields:
  - strict interval comparator;
  - exchangeable width/background channels.
- fault-model field:
  - single-fault sentinel.
- physical instrumentation fields:
  - executable operation;
  - calibrated error contract.

The finite two-port source is closest to the structural fields. It supplies an
ordered gap but not the strict boundary rule. It supplies two error channels but
not a channel-exchange action.

The other fields require more:

- single-fault sentinel requires a fault state, sentinel transition, and
  one-bad contract;
- executable operation requires a control protocol, finite runtime, and
  readout/reset;
- calibrated error contract requires width, background, and drift bounds.

## Disposition

The smallest constructive targets are:

- derive the strict boundary rule;
- derive the channel-exchange action.

Neither suffices alone for selector authority, but either would be genuine
progress because it removes a declared detector feature rather than appending
one.

## Exact checker

- Checker: `checkers/wp221_missing_detector_field_ladder.py`
- Result: `results/wp221_missing_detector_field_ladder.json`

The checker verifies the requirement deficits and identifies the smallest
structural targets.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should choose one structural target and test
  a derivation.

## Report to `marici.Nima`

- Admitted state domain: WP220 missing detector fields with requirement
  deficits.
- Faithful quotient coordinate: field-requirement entailment ladder over the
  original `physical16` detector route.
- Source-authorized probe family: none newly admitted; finite two-port source
  partially supports structural derivations.
- Contextual partition: one-rule-short structural fields, fault-model gate,
  apparatus gate, calibration gate.
- Classification: detector-field derivation ladder.
- Smallest exact falsifier: source tuple with ordered gap but no strict
  boundary rule, or two error channels but no exchange action.
- Remaining physical-instrument gate: derive either strict boundary rule or
  channel-exchange action from source dynamics; neither suffices alone for
  selector authority.
