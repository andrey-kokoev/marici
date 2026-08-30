# Detector-gain audit for the X-state determinant

## Question

Which detector-gain modes cancel in normalized Stokes correlations, and which
can manufacture a false determinant sign?

## What normalization removes

A scalar brightness or efficiency multiplying every outcome channel within one
setting cancels exactly in the normalized same-minus-different correlation.
For the transverse `X` and `Y` settings of an X state, local marginals vanish.
Consequently outcome imbalance on only one detector side also cancels.

With imbalance parameters `e_A` and `e_B` on both sides, however, the observed
correlation is

```text
C_observed = (C + e_A e_B)/(1 + e_A e_B C).
```

The bias begins with the product of the two local imbalances. If that product
changes with analyzer setting, the four correlations no longer reconstruct
one coherence vector.

## Exact hostile

Apply imbalance product `+1/100` to `XX` and `-1/100` to `YY`, `XY`, and `YX`
for the existing true-boundary X-state record. The reconstructed determinant
becomes strictly positive. Thus normalization alone does not protect the NPT
claim.

## Repairs

Swapping the detector channels on one side flips the imbalance product.
Averaging the original and swapped normalized correlations suppresses the
leading bias, but the exact rational checker shows a nonzero residual remains.
It is a useful hostile diagnostic, not an exact calibration.

The exact repair is to calibrate every outcome-channel efficiency, divide each
raw coincidence count by the corresponding efficiency product, and only then
normalize and form the correlation. Uncertainty in those efficiencies must be
propagated into the existing per-correlation error radius; the current checker
freezes them exactly.

## Claim boundary

The model assumes factorized channel efficiencies and zero transverse local
marginals. It excludes accidental coincidences, dead time, saturation,
afterpulsing, and uncertainty in the efficiency calibration. Those are
distinct detector ports rather than generic gain.

## Verification

Run:

```text
python research/aspect/checkers/check_detector_gain_x_state_determinant.py
```

The dependency-free exact checker verifies common-gain cancellation, the
two-sided bias law, the false-positive hostile, incomplete swap suppression,
and exact efficiency correction.
