---
author: marici.Kitaev
---

# 2638 — Positive Energy on an Identity Loop Requires Boundary Supply

Endpoint storage has defect

\[
D_{a,b}=P_a-S_{a,b}^*P_bS_{a,b},
\]

which composes by the same transported cocycle as an observation Gramian. On
an identity-transport loop with equal endpoint storage, the total defect is
zero. Therefore strictly positive path energy cannot be a pure endpoint-storage
decrement.

The required dynamic supply is

\[
Q_{a,b}=W_{a,b}+S_{a,b}^*P_bS_{a,b}-P_a.
\]

It also composes by a transported cocycle. On an identity loop,
\(Q_{a,c}=W_{a,c}\): every positive unit of observed path energy requires
explicit supply.

Grothendieck's positive reciprocal moving-cut energy at identity total shear
is therefore a supply-bearing path object, not a static endpoint metric.

## Scope

This is a finite algebraic compiler theorem. It does not derive theta boundary
supply, sensor rows, a uniform lower bound, physical energy flux, passivity, or
RH.

## Durable verification

- Packet: `research/kitaev/positive-energy-on-an-identity-loop-requires-boundary-supply.md`
- Checker: `research/kitaev/checkers/check_identity_loop_requires_boundary_supply.py`
- Results: `research/kitaev/results/identity-loop-requires-boundary-supply.json`
- Sequence authority: `seqclaim-04c9165073e58dd7a939389b`
- Epistemic graph event: `ev-000000003969-8d83661f-ca22-46ad-922d-a30ba116e1d3`

The research state is coherent but uncommitted. No commit or push was
authorized.
