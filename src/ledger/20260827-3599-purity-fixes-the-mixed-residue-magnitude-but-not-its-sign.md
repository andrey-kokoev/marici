---
id: marici-ledger-20260827-3599
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP816
---

# Purity Fixes the Mixed Residue Magnitude but Not Its Sign

For a reflection-positive mixed one-pole residue

\[
R=\begin{pmatrix}A&C\\C&B\end{pmatrix},
\]

positivity requires \(C^2\le AB\). Conditional rank-one purity saturates the
bound and fixes

\[
\frac{C}{\sqrt{AB}}=\pm1.
\]

The two saturated matrices are positive, isospectral, and have identical
diagonal readouts. A calibrated mixed correlator separates their signs only
after the relative operator sign port is fixed. Conjugating one operator by a
minus sign exchanges the pair.

Positive diagonal threshold transport preserves the normalized sign pair,
while nonaligned mixing changes the fixed-axis cross readout. A complete
calibrated three-channel residue family is faithful; an uncalibrated mixed
channel retains a source--gain kernel.

## Evidence

- Packet: research/flavor/flavor-mixed-os-residue-sign-pair-audit.md
- Checker: research/flavor/checkers/wp816_mixed_os_residue_sign_pair_audit.py
- Generated result: research/flavor/results/wp816_mixed_os_residue_sign_pair_audit.json
- Exact result: 18 of 18 checks passed.
- Ledger-sequence claim: seqclaim-bb1899a7dc05717474bb4ae1, value 3599.
- Graph admission: `ev-000000007713-5cfc0b83-26ef-4183-9cf5-b60179194598`.

## Claim boundary

Purity and the relative operator incidence are tested conditionally, not
derived from flavor dynamics. The required source must select the pre-quotient
operator orientation, authorize saturation, protect the marked lines, fix
absolute residues, and realize the calibrated `physical16` cross detector.
