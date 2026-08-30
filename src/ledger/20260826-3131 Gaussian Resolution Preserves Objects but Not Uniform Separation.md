---
author: marici.Figueiredo
---

# 3131 — Gaussian Resolution Preserves Objects but Not Uniform Separation

## Result

Gaussian detector convolution has Fourier transfer
\(e^{-\sigma^2k^2/2}\), which is strictly positive at every finite real
frequency. It therefore preserves exact separation of Lorentzian mass-width
objects. Two convolved templates coincide only when both mass and width agree.

Uniform separation nevertheless fails as their mass-width parameters
coalesce. A positive Gram lower bound defines an operational target domain,
not evidence of detector calibration.

## Scope

This establishes injectivity and the completion-stability distinction. It does
not supply detector-derived resolution, background covariance, efficiencies,
or uncertainty bounds.

## Durable verification

- Packet: research/flavor/flavor-gaussian-convolution-pullback.md
- Checker: research/flavor/checkers/wp655_gaussian_convolution_pullback.py
- Result: research/flavor/results/wp655_gaussian_convolution_pullback.json
- Epistemic graph event: `ev-000000006405-412e6a98-ef25-4106-a503-57460e2503ed`
