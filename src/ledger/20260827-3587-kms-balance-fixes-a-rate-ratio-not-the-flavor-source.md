---
id: marici-ledger-20260827-3587
date: 2026-08-27
author: marici.Figueiredo
status: tested
programme: flavor
work_package: WP812
---

# KMS Balance Fixes a Rate Ratio, Not the Flavor Source

A two-sector Davies/KMS generator has a unique Gibbs attractor with bias

\[
p_+-p_-
=\tanh\!\left(\frac{\beta\Delta}{2}\right)
\]

and positive dissipative gap. Detailed balance therefore derives the
transition-rate ratio and global basin conditional on a bath temperature and
signed Hamiltonian splitting.

It does not select the sign of \(\Delta\), the absolute rate, or the two scales
\(\beta\) and \(\Delta\) separately. The mirror Hamiltonian reverses the bias
while satisfying the same KMS law. The exact pair

\[
(\beta,\Delta)=(1,2),\qquad(2,1)
\]

has the same equilibrium response. Threshold changes can preserve the basin
and sign while changing the numerical bias and clock. Portal normalization and
detector gain add further kernel directions.

## Evidence

- Packet: research/flavor/flavor-kms-detailed-balance-scale-fiber-audit.md
- Checker: research/flavor/checkers/wp812_kms_detailed_balance_scale_fiber_audit.py
- Generated result: research/flavor/results/wp812_kms_detailed_balance_scale_fiber_audit.json
- Exact result: 17 of 17 checks passed after repairing a canonical-form identity assertion.
- Ledger-sequence claim: seqclaim-cced33976d18a976d07e6bfa, value 3587.
- Graph admission: `ev-000000007684-98c6d6f9-b80d-4653-a6ee-094215edbfbc`.

## Claim boundary

The result assumes a weak-coupling two-level Davies/KMS source. A geometric
thermal constructor could fix \(\beta\), but must also derive the sign and
value of \(\Delta\), the portal scale, threshold transport, and calibrated
`physical16` detector frame without inserting a horizon-orientation port.
