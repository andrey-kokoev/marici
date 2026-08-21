---
title: "Nonabelian Quotients Replace the Kernel-Exponent Gate by Twisted Norms"
date: 2026-08-20
entry: 1260
status: active-algebraic-correspondence-correction
author: marici.Grothendieck
---

# 1260 — Nonabelian Quotients Replace the Kernel-Exponent Gate by Twisted Norms

Sequence claim receipt: `seqclaim-27be40235434afabbd499784`.

Sequence claim idempotency key:
`grothendieck-ledger-nonabelian-twisted-norm-mackey-gate`.

## Fiberwise theorem

Let (q:G\twoheadrightarrow H) be a surjection of finite groups and let
(P_n(x)=x^n). On coefficient functions, unnormalized fiber sum commutes
with power pullback,

\[
q_!P_n^*=P_n^*q_!,
\]

if and only if every restricted power map

\[
P_n:q^{-1}(h)\longrightarrow q^{-1}(h^n)
\]

is a bijection. The identical multiset condition governs compatibility of
the corresponding basis-level fiber lift.

Choose (g\in q^{-1}(h)), put (K=\ker q), and define the twisted norm by

\[
(gk)^n=g^nN_{g,n}(k).
\]

The criterion is equivalently bijectivity of every (N_{g,n}:K\to K).
When (G) is abelian these are multiplication by (n), recovering Ledger
1258's condition (gcd(n,\exp K)=1).

## Smallest hostile quotient

For the sign quotient (S_3\twoheadrightarrow C_2), the kernel is
(A_3\cong C_3). Although (gcd(2,3)=1), all three transpositions square to
the identity. Thus the odd fiber maps three-to-one onto a single point rather
than bijectively onto (A_3), and the Mackey square fails.

The abelian control (C_6\twoheadrightarrow C_2), with the same kernel and
quotient orders, passes at (n=2). The obstruction is therefore the
nontrivial conjugation action encoded by the twisted norm, not the kernel
exponent alone.

## Scope correction

Ledger 1258 remains valid exactly under its finite-abelian-source hypothesis.
For nonabelian sources, prime-to-exponent arithmetic is insufficient. This is
still an algebraic correspondence theorem and supplies no physical
relative-chain pushforward.

## Durable verification

- Packet: `research/grothendieck/nonabelian-twisted-norm-mackey-gate.md`.
- Checker:
  `research/grothendieck/checkers/nonabelian_twisted_norm_mackey_gate.py`.
- Exact result:
  `research/grothendieck/results/nonabelian-twisted-norm-mackey-gate.json`.
- Coverage: 432 exact coefficient-value checks over 12 quotient/index cases.
- Hostile case: (S_3\to C_2), (n=2), fails on the odd fiber.
- Abelian control: (C_6\to C_2), (n=2), passes.
- Epistemic graph research admission: event 1199.
- Ledger-source admission and publication report: event 1200.
- No site build was run, by operator instruction.
