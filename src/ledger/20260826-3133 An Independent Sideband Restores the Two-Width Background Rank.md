---
author: marici.Figueiredo
---

# 3133 — An Independent Sideband Restores the Two-Width Background Rank

## Result

Profiling an unconstrained common background from two labelled signal records
leaves only rank-one source information and erases the common-rate mode.

An independently observed background-only sideband with Fisher precision
\(\tau>0\) restores rank two. The exact profiled determinant is

\[
\det F_{\mathrm{src}}=\frac{16\tau}{\tau+2}.
\]

The limit \(\tau\to0\) recovers the rank-one obstruction.

## Scope

The sideband is authoritative only if its support and transfer factors are
declared independently of the target signal. This packet supplies the typed
calibration channel, not experimental numerical calibration or source
selection.

## Durable verification

- Packet: research/flavor/flavor-sideband-background-calibration.md
- Checker: research/flavor/checkers/wp656_sideband_background_calibration.py
- Result: research/flavor/results/wp656_sideband_background_calibration.json
- Epistemic graph event: `ev-000000006415-d0333429-b8d8-45dd-bcc8-26f1ac639ae5`
