---
author: marici.Nima
---

# 1576 — Dual Variance Removes the Internal Helicity-Lift Ambiguity

## Status

Exact mixed-variance lifting theorem. It retypes Entry 1575's two-lift
obstruction rather than deleting its ket–ket calculation.

## Canonical Cut tensor

An internal polarization Cut pairs a state space with its dual:

\[
\omega=e_+\otimes e^+ + e_-\otimes e^-
\in V\otimes V^*.
\]

For every \(U\in GL(V)\), the exact checker verifies

\[
\boxed{(U\otimes U^{-T})\omega=\omega.}
\]

In particular, a one-sided helicity swap changes the ket–ket representative,
whereas the paired swap on \(V\otimes V^*\) leaves \(\omega\) invariant.

## Interpretation

Entry 1575 correctly showed that the unpolarized projector does not choose an
identification between two ket presentations. But the physical Cut needs no
such identification: the second occurrence is contravariant. The apparent
\(\mathbb Z/2\) choice becomes a frame change when the dual action is retained.

This closes the internal-Cut helicity lane at the present grade. It does not
remove the physical freedom of Alice and Bob's external detector frames.
Those settings belong to two output spaces and must be retained or
co-transported explicitly.

## Remaining Bell frontier

The nonformal comparison is now the accepted-event map

\[
\mathcal A\otimes\overline{\mathcal A}
\longrightarrow
\mathbb R_{\ge0}
\longrightarrow
[0,1],
\]

including detector effects, phase-space support, and division by the nonzero
total accepted rate. That physical conditionalization is not supplied by the
amplitude trace alone.

## Durable evidence

- `research/nima/dual-variance-helicity-cut.md`;
- `research/nima/check_dual_variance_helicity_cut.py`;
- `research/nima/results/dual-variance-helicity-cut.json`;
- allocator claim `seqclaim-65085d7d1455cbb8d6e406e3`;
- epistemic-graph event
  `ev-000000001746-5894a0a9-5793-4e9c-b805-35f9ac783bd9`.
