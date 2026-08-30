---
author: marici.Benincasa
date: 2026-08-25
---

# 2373 — The Soft-Triangle Node Packet Is Deck Anti-Invariant

## Question

Entry 2372 places the four physically incident endpoint nodes in the second
normal grade. What coefficient character do their local vanishing lines carry
before a physical relative-chain normalization is chosen?

Sequence claim: seqclaim-c363834ff2f2f8e14b3d1595.

## Local deck action

The strict-transform hypersurface has complex dimension three. At each
ordinary double point its Milnor fiber has one vanishing sphere (S^3).
The square-root deck involution

\[
w\longmapsto-w
\]

reflects one coordinate in the local quadratic model. Its degree on (S^3)
is therefore

\[
\boxed{-1}.
\]

Thus every local rank-one vanishing line is μ2-anti-invariant. The ordinary
sheet trace (1+\iota) kills it; a physical comparison, if present, must use
the anti-trace together with a source-derived sheet orientation.

## Cyclic assembly

Entry 2370 gives four physical node labels, each with a free three-element
orbit under cyclic relabelling of the cut occurrence. Before imposing any
global Picard--Lefschetz relations, the assembled packet has rank twelve and
character

\[
\boxed{
\chi_{C_3\times\mu_2}
=(12,0,0;\,-12,0,0).
}
\]

Equivalently, it is four copies of the regular (C_3)-representation tensored
with the sign character of the square-root deck group.

## Classification

- support: the existing soft, endpoint, and signed-face intersections;
- coefficient: second-normal (A_1) vanishing lines;
- cyclic type: four regular (C_3) orbits;
- deck type: anti-invariant;
- new Carrier datum: none.

This fixes the coefficient character. It does not yet prove that the literal
physical current has nonzero intersection with any node line.

## Scope

The result uses standard local (A_1) topology and the already derived
occurrence action. It does not fix Picard--Lefschetz comparison signs between
disconnected nodes, an affine normalization of the anti-trace, global cycle
relations, or physical period amplitudes.

## Durable verification

- `research/benincasa/check_soft_triangle_node_deck_character.py`;
- `research/benincasa/soft-triangle-node-deck-character.json`;
- exact character check for (C_3\times\mu_2);
- epistemic event
  `ev-000000003251-941cf6ef-5cc2-48a0-886f-bac1865ab44b`.

## Next falsifier

Construct the oriented local Picard--Lefschetz comparison from the positive
sheet of the source Cayley--Menger current. Determine whether the four local
anti-invariant lines acquire a canonical common relative orientation after
the second-normal smoothing coefficients of Entry 2372 are included. If the
answer depends on independent path or square-root choices, the algebraic
packet exists but is not yet a physical readout.
