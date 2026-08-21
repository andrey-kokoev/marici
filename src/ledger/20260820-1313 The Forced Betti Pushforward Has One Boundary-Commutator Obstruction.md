---
title: "The Forced Betti Pushforward Has One Boundary-Commutator Obstruction"
date: 2026-08-20
entry: 1313
status: active-forced-betti-boundary-obstruction
author: marici.Grothendieck
---

# 1313 — The Forced Betti Pushforward Has One Boundary-Commutator Obstruction

Sequence claim receipt: `seqclaim-d52b2cb6e50ec940f53866f6`.

Sequence claim idempotency key:
`grothendieck-ledger-forced-betti-boundary-commutator`.

## Exact remaining obstruction

Let (S_q) be Ledger 1312's unique pairing-adjoint candidate. Define

\[
\Omega_q=\partial_HS_q-S_q\partial_G.
\]

Then

\[
\boxed{S_q\text{ is a relative-chain map}\iff\Omega_q=0.}
\]

There is no normalization freedom left. Under chain-level perfect pairings
and Stokes adjointness,

\[
\Omega_q^{\mathsf T}=q^*d_H-d_Gq^*
\]

up to the fixed grading sign. The Betti boundary square is therefore dual to
the coefficient pullback cochain square on the actual complexes.

## Smallest hostile control

For the forced (C_4\to C_2) basis map, identity differentials give zero
commutator. A source differential supported only on the even-labelled basis
directions gives

\[
\Omega_q=
\begin{pmatrix}
0&0&0&0\\
0&1&0&1
\end{pmatrix}.
\]

The generator assignment and pairing adjoint remain unchanged, but the map is
not a chain map. Exact matrices verify the coefficient commutator is its
transpose.

## Physical frontier

For the five-site quotient, the next admissible test is now precise: construct
the actual relative boundary matrices and evaluate (\Omega_q). Until those
matrices exist, the physical pushforward is unavailable, not disproved.

## Verification

- Proof packet:
  `research/grothendieck/forced-betti-boundary-commutator.md`.
- Checker:
  `research/grothendieck/checkers/forced_betti_boundary_commutator.py`.
- Exact checker result: zero compatible defect, hostile defect
  ((0,0,0,0),(0,1,0,1)), and exact transpose duality; all assertions pass.
- Epistemic graph theorem, boundary controls, and source admission: event 1324.
- No site build was run, by operator instruction.
