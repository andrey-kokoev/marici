---
author: marici.Figueiredo
---

# 3206 — Renormalization Scale Is Not a Physical Probe

## Correction

Ledger 3204 assigned physical-context status to two renormalization-scale
choices. That interpretation is withdrawn. At fixed physical momentum, the
running portal coordinate and its explicit logarithm combine as

\[
F(Q;\mu)=a+b\log(\mu/\mu_0)+b\log(Q/\mu)
=a+b\log(Q/\mu_0),
\]

so changing \(\mu\) does not create a second observation.

The affine theorem in WP689 remains valid for two genuinely distinct physical
contexts. In particular, distinct momenta give

\[
F(Q_2)-F(Q_1)=b\log(Q_2/Q_1),
\]

but this has no instrument authority until the finite-momentum amplitude and
two calibrated momentum-bin responses are derived.

## Durable verification

- Packet: research/flavor/flavor-renormalization-scale-noninstrument.md
- Checker: research/flavor/checkers/wp690_renormalization_scale_noninstrument.py
- Result: research/flavor/results/wp690_renormalization_scale_noninstrument.json
- Sequence claim: `seqclaim-1cfb1d629e62ce1b767e4bc7`
- Epistemic graph event: `ev-000000006688-8b62dcdc-270f-4bc1-a515-ed75aa2506bb`
- Superseded interpretation: ledger 3204
