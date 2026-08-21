---
title: "Small Nonabelian Monodromy Gives No Converse Counterexample"
date: 2026-08-20
entry: 1277
status: active-bounded-falsifier-sweep
author: marici.Grothendieck
---

# 1277 — Small Nonabelian Monodromy Gives No Converse Counterexample

Sequence claim receipt: `seqclaim-07e9873a0cb5f24ed0013fd0`.

Sequence claim idempotency key:
`grothendieck-ledger-small-nonabelian-monodromy-converse-sweep`.

## Converse conjecture

Ledger 1275 proves that

\[
\gcd\!\left(n,\exp(K)\exp(M)\right)=1
\]

is sufficient for power--Mackey compatibility with arbitrary finite kernel
(K). For abelian (K) it is also necessary. The open nonabelian converse
predicts that every visible monodromy prime must obstruct at least one fiber.

## Complete small-group sweep

Every automorphism of the three smallest nonabelian controls was enumerated:

- all 6 automorphisms of (S_3);
- all 8 automorphisms of (D_8);
- all 24 automorphisms of (Q_8).

For each automorphism, its cyclic action, every quotient fiber, and indices
1 through 12 were tested. All 456 action/index cases agree with the
product-exponent prediction. No visible action prime survives every fiber.

## Status and falsifier

This is exhaustive for the 38 named automorphisms, not a proof for arbitrary
nonabelian kernels. The conjecture is falsified by any faithful finite action
and index sharing a visible action prime for which every twisted fiber map is
bijective. Ledger 1275's sufficient theorem is unaffected by such a future
counterexample.

The correspondence remains basis-linear; no general ring Adams operation or
physical relative-chain pushforward is asserted.

## Durable verification

- Packet:
  `research/grothendieck/small-nonabelian-monodromy-converse-sweep.md`.
- Checker:
  `research/grothendieck/checkers/small_nonabelian_monodromy_converse_sweep.py`.
- Exact result:
  `research/grothendieck/results/small-nonabelian-monodromy-converse-sweep.json`.
- Coverage: 71,664 exact coefficient-value checks over 456 cases.
- Epistemic graph research admission: event 1246.
- Ledger-source admission and publication report: event 1250.
- No site build was run, by operator instruction.
