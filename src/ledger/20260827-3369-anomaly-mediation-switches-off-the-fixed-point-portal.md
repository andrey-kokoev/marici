---
author: marici.Figueiredo
---

# 3369 — Anomaly Mediation Switches Off the Fixed-Point Portal

## Claim

Pure anomaly mediation gives

\[
M_\lambda=\frac{\beta_g}{g}m_{3/2},
\qquad
m_i^2=\frac{|m_{3/2}|^2}{2}\beta^I\partial_I\gamma_i.
\]

At an interacting fixed point, every \(\beta^I\) vanishes. The soft mass needed
by the WP747 nondecoupling threshold therefore vanishes and forces
\(\epsilon_*=0\). The additional \(D\)-term portal decouples exactly.

Off the fixed point, a linearized mode gives

\[
m_{\mathrm{soft}}^2
\propto |m_{3/2}|^2c\lambda C e^{\lambda t},
\]

so the portal depends on the critical-mode amplitude, RG time, and
supersymmetry-breaking scale, with no automatic positive sign.

## Classification

Exact fixed-point gauge normalization and pure anomaly-mediated
nondecoupling are incompatible: the former kills the latter, while restoring
the latter restores the amplitude and clock fibers.

## Scope

This covers pure anomaly mediation. Deflected anomaly mediation, gauge or
gravity mediation, and mixed mechanisms add source data requiring separate
authority and matching audits.

## Durable verification

- Packet:
  `research/flavor/flavor-fixed-point-anomaly-nondecoupling-incompatibility.md`
- Checker:
  `research/flavor/checkers/wp748_fixed_point_anomaly_nondecoupling_incompatibility.py`
- Generated result:
  `research/flavor/results/wp748_fixed_point_anomaly_nondecoupling_incompatibility.json`
- Exact checker outcome: 11/11 PASS.
- Sequence authority: `seqclaim-81cc6b5b6d116884f01e11ad`.
- Epistemic-graph admission:
  `ev-000000007221-323dde7b-54db-4e7c-adf0-bad5ac36a3a0`.
