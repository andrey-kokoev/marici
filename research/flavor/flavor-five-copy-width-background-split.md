# Five-copy width-background split

Owner: `marici.Figueiredo`.

## Question

WP212 showed that half-gap bucket symmetry does not derive the
`1/10,1/10` detector constants. This packet tests the direct route:

Split the WP207 `1/5` safety cap equally between width and background.

## Exact claim

The five-copy safety cap is:

`width + background <= 1/5`.

Exchange symmetry between width and background forces:

`width = background = 1/10`.

Hostile controls:

- `3/20 + 1/20` is within the cap but not exchange-invariant;
- `1/20 + 3/20` is within the cap but not exchange-invariant;
- `1/5 + 1/5` is exchange-invariant but exceeds the cap.

## Disposition

This conditionally derives WP203's detector constants. The remaining gates are
now explicit:

- derive the five-copy `1/5` safety cap;
- derive exchange symmetry between width and background.

## Exact checker

- Checker: `checkers/wp213_five_copy_width_background_split.py`
- Result: `results/wp213_five_copy_width_background_split.json`

The checker verifies the cap, exchange symmetry, and hostile asymmetric splits
using exact rational arithmetic.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: derive the cap and width/background symmetry; the
  one-tenth arithmetic itself is now closed.

## Report to `marici.Nima`

- Admitted state domain: detector width/background splits under the five-copy
  cap.
- Faithful quotient coordinate: cap satisfaction and exchange symmetry.
- Source-authorized probe family: conditional on detector architecture.
- Contextual partition: equal split uniquely satisfies cap and exchange in the
  audit.
- Classification: conditional detector-constant derivation.
- Smallest exact falsifier: asymmetric splits are within cap but violate
  exchange symmetry.
- Remaining physical-instrument gate: derive the cap and width/background
  exchange symmetry.
