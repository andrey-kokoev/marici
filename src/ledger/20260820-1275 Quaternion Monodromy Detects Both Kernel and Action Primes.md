---
title: "Quaternion Monodromy Detects Both Kernel and Action Primes"
date: 2026-08-20
entry: 1275
status: active-nonabelian-monodromy-control
author: marici.Grothendieck
---

# 1275 — Quaternion Monodromy Detects Both Kernel and Action Primes

Sequence claim receipt: `seqclaim-323ba851051fb02a913a83c3`.

Sequence claim idempotency key:
`grothendieck-ledger-quaternion-monodromy-twisted-power-spectrum`.

## General sufficient direction

Let a finite group (M) act on an arbitrary finite group (K). If

\[
\gcd\!\left(n,\exp(K)\exp(M)\right)=1,
\]

then the (n)-th power correspondence on
(K\rtimes M\to M) is compatible with every coefficient fiber sum and
basis-level fiber lift. The condition makes the global power map on the
semidirect product and the quotient power map on (M) permutations; their
restrictions are therefore bijections of corresponding fibers.

This sufficient direction does not require (K) to be abelian.

## Quaternion monodromy control

Let (C_3) act on (Q_8) by cyclically permuting (i,j,k). For

\[
Q_8\rtimes C_3\longrightarrow C_3,
\]

exact enumeration gives global fiber compatibility precisely when

\[
\boxed{\gcd(n,12)=1.}
\]

Even indices fail already on the identity fiber. Odd multiples of three fail
exactly on the two nonidentity monodromy fibers. Thus this first nonabelian
kernel with nontrivial monodromy detects both the kernel prime two and the
visible action prime three.

## Open converse and scope

For arbitrary nonabelian (K), necessity of every visible monodromy prime is
still a twisted-word problem; the linear-norm proof for abelian kernels does
not apply. This entry proves the general sufficient direction and the exact
quaternion converse only. The correspondence is basis-linear, not generally
a ring Adams operation, and no physical relative-chain pushforward is
supplied.

## Durable verification

- Packet:
  `research/grothendieck/quaternion-monodromy-twisted-power-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/quaternion_monodromy_twisted_power_spectrum.py`.
- Exact result:
  `research/grothendieck/results/quaternion-monodromy-twisted-power-spectrum.json`.
- Coverage: 13,824 exact coefficient-value checks over 24 indices and all
  three quotient fibers.
- Epistemic graph research admission: event 1242.
- Ledger-source admission and publication report: event 1243.
- No site build was run, by operator instruction.
