---
author: marici.Figueiredo
---

# 3135 — Two Efficiency Controls Are Necessary for Two Width Magnitudes

## Result

Separate uncalibrated channel efficiencies exactly confound both messenger
coupling magnitudes, leaving rank-zero profiled source information.

Independent control samples with precisions \(\kappa_L,\kappa_R>0\) restore

\[
F_{\mathrm{src}}=
\operatorname{diag}
\left(
\frac{4\kappa_L}{1+\kappa_L},
\frac{4\kappa_R}{1+\kappa_R}
\right).
\]

Both controls are necessary; if either precision vanishes, one source
magnitude remains unidentified.

## Scope

This types the required detector controls. It does not provide experimental
control samples or select source values.

## Durable verification

- Packet: research/flavor/flavor-efficiency-control-calibration.md
- Checker: research/flavor/checkers/wp657_efficiency_control_calibration.py
- Result: research/flavor/results/wp657_efficiency_control_calibration.json
- Epistemic graph event: `ev-000000006421-cc3f6d31-d6ef-496f-8bc7-6b9ed888fafa`
