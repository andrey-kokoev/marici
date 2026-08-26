---
author: marici.Kitaev
---

# 2642 — Minimal Endpoint–Forcing Incidence Is Direction-Sensitive

Let the state split as scalar endpoint displacement \(Y\) plus an already
faithfully observed forcing port \(F\). One additional static row observes the
full state exactly when it has a nonzero endpoint coefficient.

For dynamics

\[
A=\begin{pmatrix}a&p\\q&A_F\end{pmatrix},
\]

forcing-only sensors observe the endpoint in two steps exactly when the
endpoint-to-forcing block \(q\) is nonzero. With full forcing actuation, the
endpoint is reachable in two steps exactly when the opposite block \(p\) is
nonzero. Incidence direction therefore separates observability from
controllability.

A wrong-way coupling is reachable but unobservable, duplicated forcing rows
leave the endpoint hidden, and \(q_N=(1/N,0)^{\mathsf T}\) gives full finite
rank while endpoint observation energy collapses as \(1/N^2\).

## Scope

This is a finite-dimensional compiler theorem. It does not derive theta/Tate
incidence, prove uniform observability, build a physical controller, establish
passivity, orient zeros, or prove RH.

## Durable verification

- Packet: `research/kitaev/minimal-endpoint-forcing-incidence-is-direction-sensitive.md`
- Checker: `research/kitaev/checkers/check_minimal_endpoint_forcing_incidence.py`
- Results: `research/kitaev/results/minimal-endpoint-forcing-incidence.json`
- Sequence authority: `seqclaim-34d26a41babe0ee5e7be4ec4`
- Epistemic graph event: `ev-000000003987-6cf92c80-7932-4503-8e88-b68db55dc014`

The research state is coherent but uncommitted. No commit or push was
authorized.
