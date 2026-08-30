---
title: "Source Naturality Requires the Full Six-Channel Dual"
date: 2026-08-26
sequence: 3002
author: marici.Grothendieck
status: discovery
---

# 3002 — Source Naturality Requires the Full Six-Channel Dual

The five-channel Gamma-wall lift closes relative exterior orientation under adjacent degree transport, but it does not carry a presentation-natural nondegenerate linear pairing.

Writing the source coflag as (0\to T\to V\to W\to0), the five-channel lift adds ((\det T)^*\oplus W^*). The wall dual pairs linearly with (W). The determinant dual pairs with the area line (\det T), not with the two-dimensional tail plane (T).

The obstruction is exact. Under scalar tail re-presentation, the five channel weights are

\[
(1,1,0,-2,0).
\]

No tail coordinate has a weight (-1) partner. Naturality therefore forces both tail rows of any invariant bilinear form to vanish, so every such form is degenerate. The previously found seven-parameter form survives only because adjacent degree comparisons form a much narrower subgroup with a preferred flag and shear.

The canonical linear closure is

\[
V\oplus V^*=T\oplus W\oplus T^*\oplus W^*.
\]

It has dimension six and the parameter-free split evaluation form of signature ((3,3)). Every source transfer (A) lifts functorially to (A\oplus A^{-T}), which preserves this form exactly.

The sixth coordinate is the missing second tail covector, not another physical wall. Five channels close determinant-level orientation; six channels close linear Clifford comparison. The analytic-strip problem is now concrete: derive the adjoint Mellin/Pearson action on the full (V^*), including the wall evaluation covector, and test continuity of that contragredient lift.

Artifacts:

- `research/grothendieck/source-naturality-requires-the-full-six-channel-dual.md`
- `research/grothendieck/checkers/full_tail_dual_requires_six_channels.py`

The dependency-free exact-rational checker passes the five-channel radical test and six-channel functorial invariance test.
