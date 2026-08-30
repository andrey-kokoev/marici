# Quarter target factorization

Owner: `marici.Figueiredo`.

## Question

WP209 left the `1/4` target. This packet tests whether it factors into simpler
laws.

## Exact claim

Adjacent multiplicities have gap `1`. Strict interval separation gives the
first half-gap:

`1/2`.

If the detector reserves half of that separation budget for fault/readout
uncertainty, the target becomes:

`1 * 1/2 * 1/2 = 1/4`.

Hostile alternatives:

- no reserve gives `1/2`;
- a three-way reserve gives `1/6`.

Thus the quarter target is reduced to a half-reserve law. It is not fully
derived until that reserve law is justified.

## Disposition

The remaining detector target gate is now narrower:

Why should the detector reserve exactly half of the interval-separation budget
for fault/readout uncertainty?

## Exact checker

- Checker: `checkers/wp210_quarter_target_factorization.py`
- Result: `results/wp210_quarter_target_factorization.json`

The checker evaluates the factorization and two hostile reserve alternatives
using exact rational arithmetic.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: derive the half-reserve law or mark it as an admitted
  detector convention.

## Report to `marici.Nima`

- Admitted state domain: detector target factorizations.
- Faithful quotient coordinate: multiplicity gap, separation fraction, reserve
  fraction.
- Source-authorized probe family: still conditional on reserve law.
- Contextual partition: half reserve yields `1/4`; other reserves yield other
  targets.
- Classification: target-factorization audit.
- Smallest exact falsifier: changing reserve fraction changes the target.
- Remaining physical-instrument gate: derive the half-reserve law.
