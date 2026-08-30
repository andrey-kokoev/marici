# Optical resolution with uncertain covariance

## A point covariance can overstate resolution sevenfold

For two normalized channels with unit marginal variance and correlation `rho`,
the squared separation of the sum witness `(1,1)` is

```text
2 / (1 + rho).
```

A nominal calibration at `rho=-3/4` reports score `8`. If the admitted
science-epoch interval is `[-3/4,3/4]`, the robust score is the worst value
`8/7`. The point estimate overstates guaranteed squared separation by a factor
of seven despite perfectly known marginal error bars.

An independently validated interval `[-4/5,-7/10]` retains worst-case score
`20/3`. The value comes from ruling out covariance rotation at the science
epoch, not from inverting the nominal covariance more precisely.

## Correlation is question-relative

For the orthogonal difference witness `(1,-1)`, the score is

```text
2 / (1 - rho).
```

At correlation `-3/4`, the sum and difference scores are `8` and `8/7`. At
correlation `+3/4`, they swap. Noise shaping that improves the current sum
question damages the orthogonal future question by the same factor.

This creates an information-preservation tradeoff. Balanced detection may be
excellent for a declared common-mode witness while erasing sensitivity to a
differential fault. The instrument contract should name both the optimized
domain and the sacrificed domain.

## Calibration protocol

Covariance must be measured with the same optical carrier topology, reference
lineage, bandwidth, and epoch as the science record. A dark run can estimate
electronics covariance but cannot authorize source-dependent common-mode
noise. A bright reference may alter saturation or back-action. Interleaved
reference records and independent physical noise injections are the cleanest
way to bound drift rather than assume stationarity.

The robust completion record is the minimum separation over the admitted
covariance set. A nominal inverse covariance remains useful for estimation but
cannot authorize an exclusion outside that set.

## Claim boundary

The exact checker varies only the correlation of two unit-marginal channels.
Marginal drift, finite-sample covariance estimation, non-Gaussian tails, and
higher-dimensional witness libraries remain open.

## Verification

```text
python research/aspect/checkers/check_covariance_uncertainty_resolution.py
```
