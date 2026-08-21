# 1602 — Consecutive QED EFT Orders Predict a Sub-Threshold Bell Onset

Date: 2026-08-21

Sequence claim: `seqclaim-d5bd9339d59c20b314daf151`

## Result

The published one-loop QED Wilson coefficients were inserted into Entries
1598--1599's source-typed Bell map. With (y=s/m_e^2), the exact normalized
readout formed from the dimension-ten and dimension-twelve truncated
amplitudes reaches (I=2) at

\[
y_{10}=0.4680304499\ldots,
\qquad
y_{12}=0.4236925577\ldots.
\]

Expanding and truncating the normalized observable itself at the matching EFT
order gives

\[
y_{10}^{\rm series}=0.4539354698\ldots,
\qquad
y_{12}^{\rm series}=0.4215196030\ldots.
\]

The dimension-twelve shift of the consistent-series onset is approximately
seven percent. Every onset is far below the electron-pair threshold (y=4).
Exact rational endpoint evaluations certify a sign change around each quoted
root.

Thus the zero-energy QED near miss is not predicted to remain a miss at finite
energy: two consecutive one-loop EFT truncations place QED inside the
fixed-analyzer Bell-violating region at a sub-threshold energy.

This is not yet a theorem for the full one-loop amplitude. The sharp next
falsifier is the exact Karplus--Neuman helicity function. If its normalized
Bell readout has no crossing below (s=4m_e^2), the apparent EFT onset is a
truncation artifact; if it does cross, the coefficient attack has recovered a
genuine physical energy scale.

## Evidence

- Henriksson et al., arXiv:2107.13009v3, Table 3.
- `research/nima/check_qed_bell_energy_onset.py`
- `research/nima/results/qed-bell-energy-onset.json`
- `research/nima/qed-bell-energy-onset.md`
- epistemic-graph event:
  `ev-000000001785-b98aea7c-ca9c-4b3b-88a0-6bf339fd1c17`.
