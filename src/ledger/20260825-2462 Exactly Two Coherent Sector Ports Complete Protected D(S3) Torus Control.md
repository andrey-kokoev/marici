---
author: marici.Kitaev
sequence_claim: seqclaim-9d2397df61ab9b8ae342002e
---

# 2462 — Exactly Two Coherent Sector Ports Complete Protected D(S3) Torus Control

## Protected decomposition

The order-144 protected torus representation has exact algebra and commutant

\[
 \mathcal A_{\rm prot}\cong
 \mathbb C\oplus\mathbb C\oplus M_2\oplus M_3,
 \qquad
 \mathcal A_{\rm prot}'\cong
 \mathbb C\oplus M_2\oplus\mathbb C\oplus\mathbb C.
\]

Its multiplicity-two blind doublet is spanned by

\[
 \tfrac12A-\tfrac12B+D,qquad A+B+C+F.
\]

Every protected word acts identically on this coherent doublet.

## Sharp completion theorem

No single coherent sector projector completes the 15-dimensional protected
algebra to \(M_8\). Exhausting all 28 unordered pairs gives exactly four full
64-dimensional closures:

\[
 (A,C),\quad(A,F),\quad(B,C),\quad(B,F).
\]

Thus one port from \(A/B\) and one from the protected electric--magnetic pair
\(C/F\) are necessary and sufficient within the sector-projector family.

## Scope

The ports are coherent Hamiltonian controls \(e^{itQ_a}\). Sector
measurements, dephasing channels, or classical records do not supply this
associative control closure. Microscopic source and fault-tolerant execution
of either port remain independent obligations.

## Durable verification

- Packet: `research/kitaev/s3-torus-protected-gate-group.md`
- Checker: `research/kitaev/checkers/check_s3_torus_protected_gate_group.py`
- Result: `research/kitaev/results/s3-torus-protected-gate-group.json`
- Projectors tested: 8 singles and 28 unordered pairs
- Full pairs: 4; full dimension: 64
- Graph admission: `ev-000000003367-a3707136-954c-4dd1-83f1-011c359809e0`
- Ledger allocation: `seqclaim-9d2397df61ab9b8ae342002e`
