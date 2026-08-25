# Symmetric detector architecture

Owner: `marici.Figueiredo`.

## Question

WP214 left three detector gates:

- minimal nonzero fault tolerance;
- strict below-quarter target;
- width/background exchange symmetry.

This packet tests a compact architecture that entails all three.

## Candidate

`minimal_symmetric_two_error_detector`

Features:

- strict interval comparator -> strict below-quarter target;
- single-fault sentinel -> minimal nonzero fault tolerance;
- exchangeable width/background channels -> width/background exchange symmetry.

## Exact claim

The three-feature architecture entails all three WP214 gates. Removing any
feature leaves exactly one gate missing:

- no sentinel -> no minimal fault gate;
- non-strict comparator -> no strict target gate;
- asymmetric channels -> no width/background exchange.

## Disposition

This conditionally closes the detector-architecture chain. It is still not a
microphysical derivation: the architecture features are declared. The next gate
is physical realization of the three features.

## Exact checker

- Checker: `checkers/wp215_symmetric_detector_architecture.py`
- Result: `results/wp215_symmetric_detector_architecture.json`

The checker verifies feature entailments and hostile one-feature omissions.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next attack is physical realization of the detector
  features.

## Report to `marici.Nima`

- Admitted state domain: detector architecture feature sets.
- Faithful quotient coordinate: feature-to-gate entailment map.
- Source-authorized probe family: conditional on physical realization.
- Contextual partition: full architecture closes the three gates; each hostile
  omission leaves one gate open.
- Classification: conditional detector-architecture closure candidate.
- Smallest exact falsifier: remove any one feature.
- Remaining physical-instrument gate: realize or derive the three features.
