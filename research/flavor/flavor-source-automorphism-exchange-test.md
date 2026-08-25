# Source automorphism exchange test

Owner: `marici.Figueiredo`.

## Question

WP223 showed that two error channels do not imply exchange symmetry. This
packet asks what would make a width/background swap a genuine source-derived
automorphism.

## Admission fields

A swap must:

- swap width and background;
- commute with the source law;
- preserve error semantics;
- descend to the detector quotient.

Label swapping alone is not enough. A source symmetry that changes the meaning
of errors is not enough. A semantic detector swap that is not a source symmetry
is not enough.

## Disposition

The exchange route is now sharply typed. If such an automorphism can be
constructed from the finite two-port source, width/background exchange becomes
derived. If not, exchange remains an external detector symmetry.

## Exact checker

- Checker: `checkers/wp224_source_automorphism_exchange_test.py`
- Result: `results/wp224_source_automorphism_exchange_test.json`

The checker verifies that all four automorphism properties are jointly
necessary.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next packet should test whether the finite two-port
  source actually has this automorphism.

## Report to `marici.Nima`

- Admitted state domain: candidate width/background swap maps.
- Faithful quotient coordinate: source-law automorphism properties plus
  detector-quotient descent.
- Source-authorized probe family: none newly admitted.
- Contextual partition: label swap only, source symmetry with wrong semantics,
  semantic swap without source symmetry, admitted source exchange.
- Classification: source-automorphism admission test.
- Smallest exact falsifier: label swap of width/background with no source-law
  commutation, semantic preservation, or detector descent.
- Remaining physical-instrument gate: construct such an automorphism from the
  finite two-port source, or keep width/background exchange as an external
  detector symmetry.
