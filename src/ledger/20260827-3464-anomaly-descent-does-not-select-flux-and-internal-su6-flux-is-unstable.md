---
author: marici.Figueiredo
---

# 3464 — Anomaly Descent Does Not Select Flux and Internal SU(6) Flux Is Unstable

## Claim

For a local six-dimensional anomaly coefficient \(A_6\), one internal flux
insertion produces a descended coefficient

\[
A_4(m)=mA_6.
\]

Therefore \(A_6=0\) implies \(A_4(m)=0\) for every integer \(m\). Parent
anomaly cancellation constrains the source packet but does not select flux
three or its orientation.

The minimal integrated tadpole equation

\[
c\,m+Q_{\mathrm{loc}}=0
\]

selects \(m=3\) only if the independently derived source charge satisfies
\(Q_{\mathrm{loc}}=-3c\). Without such a source it selects \(m=0\); inserting
the ratio by hand merely moves the fitted three into the tadpole data.

A Cartan flux embedded in the non-Abelian \(SU(6)\) field also has a
spin-aligned charged-vector lowest Landau mode

\[
M^2_{0,-}=-|qB|,
\]

so the naive background lacks a stable basin.

## Classification

Local anomaly descent is neither selector nor rigidifier of the flux integer.
A sourced tadpole could select a signed sector, but only if its quantized
localized charge is independently compulsory. The smallest surviving window
is a distinct anomaly-free \(U(1)_F\) whose flux leaves \(SU(6)\) vectors
neutral and whose complete charge lattice forces oriented flux three.

## Durable verification

- Packet: research/flavor/flavor-flux-anomaly-tadpole-stability-gate.md
- Checker:
  research/flavor/checkers/wp778_flux_anomaly_tadpole_stability_gate.py
- Generated result:
  research/flavor/results/wp778_flux_anomaly_tadpole_stability_gate.json
- Exact checker outcome: 9/9 PASS.
- Primary anomaly-descent source: https://arxiv.org/abs/1907.00536
- Primary magnetized-vector-spectrum source: https://arxiv.org/abs/2306.00644
- Sequence authority: seqclaim-e665989dc93b6a69a0cda3ed.
- Epistemic-graph admission:
  ev-000000007428-aaad79c6-719a-45c4-857b-a8b1a4a107ab.
