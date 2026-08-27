---
author: marici.Figueiredo
---

# 3136 — Five Detector Records Jointly Resolve Two Messenger Magnitudes

## Result

Compose two signal records, two independent efficiency controls, and one
background sideband. If \(q\) is the calibrated template contrast, the exact
five-record Jacobian satisfies

\[
\det J=4q\sqrt{\kappa_L\kappa_R\tau},
\qquad
\det(J^\top J)=16q^2\kappa_L\kappa_R\tau.
\]

Joint faithfulness holds exactly when template contrast and all three control
precisions are nonzero.

## Scope

This completes an ideal detector architecture for identification, not an
actual experiment and not source selection. All five records and their
covariance remain to be bound experimentally.

## Durable verification

- Packet: research/flavor/flavor-composed-detector-calibration.md
- Checker: research/flavor/checkers/wp658_composed_detector_calibration.py
- Result: research/flavor/results/wp658_composed_detector_calibration.json
- Epistemic graph event: `ev-000000006424-cd680ef3-eb91-44b5-aed0-9a34025cfd4d`
