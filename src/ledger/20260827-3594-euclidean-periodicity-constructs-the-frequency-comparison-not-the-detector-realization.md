---
id: marici-ledger-20260827-3594
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP814
---

# Euclidean Periodicity Constructs the Frequency Comparison, Not the Detector Realization

A horizon thermal circle with \(\beta=2\pi/\kappa\) canonically gives

\[
\omega_n^{\rm B}=n\kappa,
\qquad
\omega_n^{\rm F}=\left(n+\frac12\right)\kappa.
\]

This derives the primitive Euclidean frequency attachment that WP813 had
inserted as \(\Delta=n\kappa\). It passes Aspect's comparison-cell gate at the
Euclidean level, but neither bosonic nor fermionic periodicity selects one mode.

The physical realization remains separate. Raw Matsubara values have explicit
analytic kernels: \(\sinh(\beta z/2)\) vanishes on every bosonic Matsubara
frequency while remaining \(\sinh\pi\) at \(z=\kappa\), and the corresponding
fermionic witness is \(\cosh(\beta z/2)\). A unique Lorentzian reconstruction
requires an admitted Osterwalder--Schrader positivity and growth packet, plus a
detector interaction. None is yet source-authorized in flavor.

## Evidence

- Packet: research/flavor/flavor-matsubara-comparison-realization-audit.md
- Checker: research/flavor/checkers/wp814_matsubara_comparison_realization_audit.py
- Generated result: research/flavor/results/wp814_matsubara_comparison_realization_audit.json
- Exact result: 17 of 17 checks passed.
- Ledger-sequence claim: seqclaim-8d5fb4228cb2a281b43d5b65, value 3594.
- Graph admission: `ev-000000007701-cdac7293-396c-422a-85a0-7ca58e8cc310`.

## Claim boundary

The continuation witnesses inhabit the raw analytic sampling domain and are
not claimed to satisfy OS reflection positivity. The next source must provide
a reflection-positive chiral flavor--horizon correlator, unique mode incidence,
threshold protection, and a calibrated Lorentzian `physical16` detector map.
