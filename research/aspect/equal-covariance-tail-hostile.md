# Equal-covariance optical noise with incompatible tails

## Covariance does not determine false alarms

Freeze two symmetric noise laws along the scientific witness:

```text
bounded law:  -1 or +1, each with probability 1/2
burst law:    -2 or +2, each with probability 1/8; 0 with probability 3/4.
```

Both have mean zero and variance one. Add the same independent unit-variance
orthogonal channel to each, and both full two-channel covariance matrices are
exactly the identity.

Nevertheless, at threshold `3/2` their tail probabilities are `0` and `1/4`.
No covariance inversion or Mahalanobis score can distinguish those false-alarm
rates.

## Smallest useful extra ports

Their fourth moments are `1` and `4`, so a calibrated fourth-moment record
separates these two frozen noise families. In optics this requires time-tagged
or unsaturated amplitude records with enough dynamic range; an RMS meter alone
cannot supply it.

If the scientific question is specifically the probability of crossing
`3/2`, the more direct port is a threshold-event counter frozen at that level.
It measures the desired event rather than inferring it from a Gaussian tail.

The fourth moment and event counter answer different questions. A fourth
moment does not globally reconstruct an arbitrary tail distribution, while a
single threshold counter does not describe other thresholds.

## Instrument implications

Shot-noise-like calibration records do not authorize Gaussian science tails
when burst noise, cosmic events, saturation recovery, or intermittent phase
slips remain possible. The calibration ensemble must share carrier topology,
bandwidth, trigger logic, and operating point with the science ensemble.

Detector clipping is especially dangerous: it can erase the burst amplitude
while leaving a deceptively tame recorded histogram. Dynamic-range and
overflow counters are part of the tail instrument, not implementation detail.

## Claim boundary

The checker compares two exact discrete symmetric laws. It establishes that
mean and covariance do not determine the declared tail probability. It does
not estimate tails from finite data or claim that a fourth moment determines
arbitrary noise.

## Verification

```text
python research/aspect/checkers/check_equal_covariance_tail_hostile.py
```
