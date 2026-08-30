# Covariance-bearing optical moment resolution

## Equal error bars can hide a sevenfold difference

Normalize the second- and third-moment separation channels by their
source-derived expected gaps before observing the records. The frozen
two-versus-one witness is then `(1,1)`.

Compare three covariance matrices with identical unit marginal variances:

```text
independent correlation: 0
positive correlation:    3/4
negative correlation:   -3/4.
```

The exact squared Mahalanobis separation scores are respectively

```text
2, 8/7, 8.
```

The positive- and negative-correlation instruments have identical per-channel
error bars, yet their multiplicity power differs by a factor of seven.

The reason is geometric. The desired witness moves both normalized moment
channels in the same direction. Positive common-mode noise lies along that
direction and obscures it. Negative correlation suppresses noise in the sum
direction and exposes it.

## Basis invariance requires covariance transport

Rescale the two readout coordinates by factors `2` and `3`. If the covariance
is transported by the same transformation, the score remains exactly `8/7`.
Rescaling the records while leaving covariance fixed would manufacture a new
condition number and a false sensitivity claim.

## Replication versus duplicated carriers

Two independent records reduce the variance of their average to `1/2`. Two
electronics readings of one common carrier have covariance matrix

```text
((1,1),(1,1)),
```

whose determinant is zero. The second label can help diagnose electronics
faults, but it does not supply independent physical averaging.

## Optical design implication

Balanced detection should be designed so dominant reference noise occupies a
mode orthogonal to the desired moment witness. That is stronger than demanding
small individual error bars. The phase reference, spatial-mode sorter, and
detector covariance must be calibrated as one instrument.

The normalization of the witness must be source-derived before the comparison.
Choosing channel scales or a covariance threshold after seeing the desired
atom count would fit the metric.

## Claim boundary

The checker uses two exactly normalized channels and known covariance geometry.
Covariance estimation error, non-Gaussian tails, nuisance parameters, and
adaptive channel selection require a robust statistical extension.

## Verification

```text
python research/aspect/checkers/check_covariance_bearing_moment_resolution.py
```
