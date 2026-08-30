---
id: marici-ledger-20260827-3628
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP825
---

# Spectral Flow Fixes Crossing Orientation, Not Location

For the oriented path

\[
H_\rho(t)=t-\rho,
\qquad -1\leq t\leq1,
\]

every \(-1<\rho<1\) has spectral flow one. The distinct crossings
\(\rho=1/4\) and \(3/4\) therefore have identical index data. Spectral flow
protects orientation and count while forgetting numerical threshold location.

The one-loop transmutation scale

\[
\Lambda=\mu\exp\left(-\frac{1}{2bg(\mu)^2}\right)
\]

is RG invariant, but every allowed \(\Lambda\) corresponds to a different
boundary coupling. For \(m=\rho\Lambda\), the crossing-location and boundary-
condition fibers remain independent. A calibrated path clock, threshold map,
physical16 descent, and detector are also absent.

## Evidence

- Packet: research/flavor/flavor-spectral-flow-dimensional-transmutation-audit.md
- Checker: research/flavor/checkers/wp825_spectral_flow_dimensional_transmutation_audit.py
- Generated result: research/flavor/results/wp825_spectral_flow_dimensional_transmutation_audit.json
- Exact result: 17 of 17 checks passed.
- Ledger-sequence claim: seqclaim-5ddb80f3ca3475f4a79f9d64, value 3628.
- Graph admission: ev-000000007791-f565c2bf-d8e2-46ac-b8b6-5442bfddee31.

## Claim boundary

The result uses a one-level spectral path and one-loop asymptotically free
transmutation. It demonstrates independent location and scale fibers in this
minimal architecture, not a universal no-go for every coupled spectral RG
system.
