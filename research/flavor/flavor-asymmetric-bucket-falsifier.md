# Asymmetric bucket falsifier

Owner: `marici.Figueiredo`.

## Question

WP211 conditionally derived a `1/4` reserve from two-bucket exchange symmetry.
This packet tests hostile detector architectures that keep the same half-gap
budget but break the symmetry.

## Exact claim

The half-gap budget `1/2` does not force the equal split. Asymmetric detector
architectures are possible:

- detector-privileged: `1/3 + 1/6`;
- fault-privileged: `1/6 + 1/3`.

They preserve the total budget but break exchange symmetry.

Moreover, splitting the detector bucket evenly between width and background
does not select WP203's `1/10,1/10` constants:

- symmetric bucket `1/4` gives `1/8,1/8`;
- detector-privileged bucket `1/3` gives `1/6,1/6`;
- fault-privileged bucket `1/6` gives `1/12,1/12`.

## Disposition

This is a useful correction. WP211 explains the quarter target if exchange
symmetry is admitted, but it does not derive the WP203 one-tenth detector
constants. A further rule is needed.

## Exact checker

- Checker: `checkers/wp212_asymmetric_bucket_falsifier.py`
- Result: `results/wp212_asymmetric_bucket_falsifier.json`

The checker verifies that asymmetric splits preserve the half-gap budget and
that none of the audited bucket splits selects `1/10,1/10`.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: do not claim one-tenth constants from two-bucket symmetry
  alone.

## Report to `marici.Nima`

- Admitted state domain: two-bucket detector architectures.
- Faithful quotient coordinate: detector/fault bucket split and induced
  width/background.
- Source-authorized probe family: still conditional on detector architecture.
- Contextual partition: asymmetric architectures preserve total budget but
  change constants.
- Classification: asymmetric bucket falsifier.
- Smallest exact falsifier: symmetric split gives `1/8,1/8`, not `1/10,1/10`.
- Remaining physical-instrument gate: derive the actual detector split and
  width/background rule.
