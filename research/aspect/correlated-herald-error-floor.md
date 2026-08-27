# Correlated false heralds defeat coincidence suppression

## A common-mode floor survives detector multiplication

Let a blocked-signal trial contain a common false-trigger event with probability
`c=1/1000`. When it does not occur, each herald detector fires independently
with probability `q=1/100`.

Each detector then has marginal false-trigger probability `1099/100000`.
An independence calculation would predict a two-detector coincidence rate equal
to the square of that marginal, about `0.000121`. The actual coincidence rate is
`10999/10000000`, about `0.001100`: more than nine times larger.

A third detector scarcely helps. Its false coincidence rate is approximately
`0.001001`, because the common event triggers all detectors together. Redundancy
suppresses the independent component exponentially but leaves the common-mode
component almost untouched.

## The missing observable is covariance

Single-channel dark-rate calibration cannot certify coincidence suppression.
The blocked-signal control must retain joint event records and estimate

```text
P(D1 and D2) - P(D1) P(D2).
```

This quantity is strictly positive in the pilot. It directly detects the
independence failure that marginal rates conceal.

For recovery claims, event-provenance fidelity therefore needs a joint law, not
one reliability number per detector. Coincidence is an error-rejecting code only
against error modes transverse to its acceptance rule.

## Optical instrument

Time-tag unsummed detector streams during blocked-source, shifted-window, and
illuminated runs. Compare zero-lag coincidences with deliberately offset windows
and perturb shared clock, bias, and optical-background sources separately. A
third detector is useful for diagnosing correlation order, but cannot remove a
shared trigger by voting alone.

## Claim boundary

The checker uses a binary all-detector common event plus identical independent
Bernoulli noise. Afterpulsing kernels, continuous-time coincidence windows,
unequal detectors, and higher-order partial correlations remain open.

## Verification

```text
python research/aspect/checkers/check_correlated_herald_error_floor.py
```
