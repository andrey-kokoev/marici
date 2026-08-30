# Dead-time audit for the X-state determinant

## Question

Does normalized coincidence analysis remove detector dead time, and how can
rate-dependent compression be separated from physical coherence?

## Frozen detector law

For each coincidence channel, use the nonparalyzable response

```text
r = lambda p / (1 + tau lambda p),
```

where `p` is the ideal channel probability, `lambda` is source rate, and `tau`
is the channel dead time. This response is nonlinear in `p`; normalization
therefore does not generally cancel it.

Equal dead time on all four channels contracts the magnitude of transverse
correlations in the frozen zero-marginal records. It does not manufacture NPT
in the checker, but it can hide a genuine NPT signal and cannot support a PPT
claim without correction.

## Channel-dependent hostile

Saturate the different-outcome channels in `XX`, and the same-outcome channels
in `YY`, `XY`, and `YX`. Applied to the true-boundary record, this enlarges
both reconstructed coherence quadratures and produces a strictly positive
false determinant.

## Exact repair and falsifier

With independently calibrated channel dead times, invert every observed rate:

```text
true_rate = r / (1 - tau r).
```

Normalize only after this channelwise inversion. The checker recovers all four
ideal correlations exactly.

Repeat at two source rates. Uncorrected correlations change with rate, while
the corrected correlations coincide when the source state and dead times are
stable. This rate sweep is a falsifier for unmodelled compression, not by
itself a calibration: source-rate dependence of the physical state would be a
competing explanation and must be independently excluded.

## Claim boundary

The result assumes independent nonparalyzable channels. Pileup, shared
electronics, afterpulsing, dead-time uncertainty, and a rate-dependent source
state require larger nuisance dynamics. Their covariance must be hardware-
derived rather than fitted to restore the determinant.

## Verification

Run:

```text
python research/aspect/checkers/check_dead_time_x_state_determinant.py
```

The dependency-free exact checker verifies common compression, a
channel-dependent false-positive hostile, exact inverse correction, and the
two-rate falsifier.
