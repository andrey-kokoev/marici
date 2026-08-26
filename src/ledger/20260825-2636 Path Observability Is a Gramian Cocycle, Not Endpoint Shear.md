---
author: marici.Kitaev
---

# 2636 — Path Observability Is a Gramian Cocycle, Not Endpoint Shear

For consecutive state transports and authorized observation maps, the exact
relationship-energy law is

\[
W_{a,c}=W_{a,b}+S_{a,b}^*W_{b,c}S_{a,b}.
\]

Its kernel is

\[
\ker W_{a,c}
=\ker W_{a,b}\cap S_{a,b}^{-1}(\ker W_{b,c}).
\]

The endpoint shear cannot determine this path energy. Two opposite nonzero
shears have identity total transport, while two identical rank-one sensors
along the path produce a positive-definite Gramian. With shear coefficient
\(1/N\), every finite Gramian remains positive but a normalized direction has
energy \(1/N^2\to0\).

Thus endpoint coherence, finite observability, and completion-stable
observability are three separate gates.

## Scope

This is an abstract finite-dimensional compiler theorem. It does not derive
theta/Tate sensor rows, prove theta observability, construct a positive
reciprocal energy, establish passivity, or prove RH.

## Durable verification

- Packet: `research/kitaev/path-observability-is-a-gramian-cocycle-not-endpoint-shear.md`
- Checker: `research/kitaev/checkers/check_path_observability_gramian_cocycle.py`
- Results: `research/kitaev/results/path-observability-gramian-cocycle.json`
- Sequence authority: `seqclaim-121d5a63e56d45dca4fc6a6f`
- Epistemic graph event: `ev-000000003959-f89afc51-dcfc-4fbb-a701-83c4663fa107`

The research state is coherent but uncommitted. No commit or push was
authorized.
