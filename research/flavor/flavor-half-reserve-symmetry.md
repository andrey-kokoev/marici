# Half-reserve symmetry

Owner: `marici.Figueiredo`.

## Question

WP210 reduced the `1/4` target to a half-reserve law. This packet tests a
symmetry derivation:

Split the half-gap interval budget equally between intrinsic detector smearing
and adversarial fault/readout uncertainty.

## Exact claim

The interval separation half-gap is `1/2`. In a two-bucket model:

- detector smearing budget;
- fault/readout reserve budget.

Exchange symmetry between the two buckets forces the split:

`1/4 + 1/4`.

Asymmetric alternatives also sum to `1/2`, but are not exchange-invariant:

- `1/3 + 1/6`;
- `1/6 + 1/3`.

Thus the quarter reserve is derived only conditional on the two-bucket
exchange symmetry.

## Disposition

This reduces the remaining gate again. The open question is now:

Why should flavor's detector architecture have exactly two exchange-symmetric
uncertainty buckets?

If detector smearing and fault reserve are physically asymmetric, the reserve
fraction changes.

## Exact checker

- Checker: `checkers/wp211_half_reserve_symmetry.py`
- Result: `results/wp211_half_reserve_symmetry.json`

The checker verifies that only the equal split is exchange-invariant among the
audited half-gap decompositions.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: derive or explicitly admit the two-bucket exchange
  symmetry.

## Report to `marici.Nima`

- Admitted state domain: half-gap budget splits.
- Faithful quotient coordinate: detector/fault budget pair.
- Source-authorized probe family: still conditional on detector architecture.
- Contextual partition: equal split is exchange-invariant; asymmetric splits
  are not.
- Classification: conditional half-reserve derivation.
- Smallest exact falsifier: asymmetric split `1/3+1/6` changes the reserve.
- Remaining physical-instrument gate: derive the two-bucket exchange symmetry.
