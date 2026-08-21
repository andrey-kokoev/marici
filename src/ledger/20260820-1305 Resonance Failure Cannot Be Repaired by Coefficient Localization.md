---
title: "Resonance Failure Cannot Be Repaired by Coefficient Localization"
date: 2026-08-20
entry: 1305
status: active-resonance-localization-rigidity
author: marici.Grothendieck
---

# 1305 — Resonance Failure Cannot Be Repaired by Coefficient Localization

Sequence claim receipt: `seqclaim-1a24a0f6c8f2c7d0a2aafc01`.

Sequence claim idempotency key:
`grothendieck-ledger-resonance-localization-rigidity`.

## Localization rigidity

Let (w:X\to X) be a nonbijective self-map of a finite set. Its basis
linearization over any nonzero commutative coefficient ring has repeated
columns and a zero row. Hence it is noninvertible after every nonzero
coefficient localization.

Bad power--Mackey fiber words are exactly such nonbijective maps. Therefore
resonance failure is combinatorial and cannot be repaired by changing or
localizing coefficients. This sharply contrasts with the scalar norm

\[
\phi_!\phi^*=|\ker\phi|\operatorname{id},
\]

which becomes split after inverting the degree.

## Exact hostile control

For (A_4\to C_3) at index three, the order-three action (A) on (V_4)
satisfies

\[
I+A+A^2=0.
\]

The twisted norm is constant on all four kernel elements. Its basis matrix
has rank one in characteristics (2,3,5,7). In particular, degree four is a
unit at prime three while the resonance map remains rank deficient.

## Scope and verification

This excludes coefficient localization as a resonance repair. It neither
constructs nor obstructs by itself the missing physical relative-chain
pushforward.

- Proof packet: `research/grothendieck/resonance-localization-rigidity.md`.
- Checker:
  `research/grothendieck/checkers/resonance_localization_rigidity.py`.
- Exact checker result: all four twisted-norm images are zero and the basis
  matrix has rank one in characteristics (2,3,5,7); all assertions pass.
- Epistemic graph theorem, hostile control, and source admission: event 1312.
- No site build was run, by operator instruction.
