# Reversal parity separates endpoint offset from link bias

## One symmetry-changing intervention resolves the hostile kernel

Assume physical path reversal leaves the endpoint offset unchanged and flips
the sign of the antisymmetric link term. With true endpoint offset `1/3` and
link bias `1/4`, the two orientation measurements are

```text
forward orientation:  7/12
reversed orientation: 1/12.
```

Their half-sum is exactly `1/3`, and their half-difference is exactly `1/4`.
The intervention turns one ambiguous observable into even and odd symmetry
channels, identifying both target and nuisance.

This succeeds because reversal changes the nuisance while preserving the target.
The parity law is part of the constructor and must be derived or independently
tested; merely renaming two acquisitions “forward” and “reverse” supplies no
authority.

## ABBA ordering rejects linear temporal drift

For orientations `+,-,-,+` at four equally spaced times, let the endpoint drift
linearly by `1/60` per step while the odd link term remains `1/4`. Averaging the
two `+` records and the two `-` records makes their mean acquisition time equal.
The even channel recovers the endpoint at the common midpoint exactly, and the
odd channel recovers the link bias exactly.

ABBA does not reject nonlinear drift or orientation-switching transients. Those
need additional order randomization, dwell controls, and explicit residual tests.

## Optical instrument

Use a physically reversible fiber/free-space route or swap propagation direction
through a reciprocal switching network. Acquire ABBA and BAAB blocks, retain
time tags, and monitor temperature and mechanical state. Validate odd parity by
varying a known nonreciprocal element while holding endpoint references local.

## Claim boundary

The checker assumes exact target-even and nuisance-odd reversal parity, constant
odd bias, equally spaced acquisitions, and linear endpoint drift. Switching
transients, nonlinear drift, incomplete reversal, and noise remain open.

## Verification

```text
python research/aspect/checkers/check_reversal_parity_separates_endpoint_and_link.py
```
