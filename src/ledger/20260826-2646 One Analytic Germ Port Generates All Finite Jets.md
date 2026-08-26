---
author: marici.Kitaev
---

# 2646 — One Analytic Germ Port Generates All Finite Jets

Freeze one source port

\[
\Gamma_{s_0,R}F(w)=F(s_0+w)=\sum_{m\ge0}\tau_mw^m
\]

before inspecting any zero. Every finite jet row is then coefficient extraction
\(\varepsilon_m(g)=[w^m]g\), not a new constructor indexed backward from a
detected multiplicity.

On the compact-open analytic topology, each coefficient is continuous by

\[
|\varepsilon_m(g)|\le r^{-m}\sup_{|w|\le r}|g(w)|.
\]

On the weighted Hardy coefficient topology,

\[
\|g\|_{H^2_R}^2=\sum_m|\varepsilon_m(g)|^2R^{2m},
\]

the weighted full coefficient port is an isometry and
\(\|\varepsilon_m\|=R^{-m}\).

A shrinking radius \(R_N=1/N\) makes the order-\(m\) norm grow as \(N^m\).
The multiplicity selector remains nonlinear and discontinuous even though the
full germ port is fixed and faithful.

## Scope

This is an analytic compiler theorem. It does not derive the theta germ port,
prove infinite instrument access, bound Riemann-zero multiplicity, orient
zeros, establish completion-stable observability, or prove RH.

## Durable verification

- Packet: `research/kitaev/one-analytic-germ-port-generates-all-finite-jets.md`
- Checker: `research/kitaev/checkers/check_analytic_jet_generating_port.py`
- Results: `research/kitaev/results/analytic-jet-generating-port.json`
- Sequence authority: `seqclaim-5c7621f8830b2b618801b17c`
- Epistemic graph event: `ev-000000004007-a2dc3c39-0487-4609-a636-886d484286f7`

The research state is coherent but uncommitted. No commit or push was
authorized.
