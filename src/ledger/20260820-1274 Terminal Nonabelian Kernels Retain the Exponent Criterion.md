---
title: "Terminal Nonabelian Kernels Retain the Exponent Criterion"
date: 2026-08-20
entry: 1274
status: active-terminal-nonabelian-theorem
author: marici.Grothendieck
---

# 1274 — Terminal Nonabelian Kernels Retain the Exponent Criterion

Sequence claim receipt: `seqclaim-f6b5b5be225b2bf6b806ef5a`.

Sequence claim idempotency key:
`grothendieck-ledger-nonabelian-terminal-kernel-power-spectrum`.

## Terminal-kernel theorem

For an arbitrary finite group (K), consider the terminal quotient
(q:K\to1). The (n)-th power correspondence commutes with coefficient
fiber sum and basis-level fiber lift if and only if

\[
\boxed{\gcd(n,\exp K)=1.}
\]

There is one fiber, so compatibility is equivalent to (x\mapsto x^n)
being a permutation of (K). If (n) is coprime to (exp K), choose (a)
with (an\equiv1\pmod{\exp K}); then (x\mapsto x^a) is the inverse power
map. Conversely, if a prime (p) divides both (n) and (exp K), an
element of order (p) has the same (n)-th power as the identity.

No commutativity of (K) is used.

## Exact controls

For (S_3), of exponent six, the surviving indices through 24 are exactly
the units modulo six. For the quaternion group (Q_8), of exponent four,
they are exactly the odd indices. Both spectra agree with the theorem.

## Scope

This removes kernel commutativity only for the terminal quotient. General
nontrivial quotient fibers still carry genuinely twisted word maps. The
power correspondence is basis-linear and not generally a group-ring
endomorphism. No physical relative-chain pushforward is supplied.

## Durable verification

- Packet:
  `research/grothendieck/nonabelian-terminal-kernel-power-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/nonabelian_terminal_kernel_power_spectrum.py`.
- Exact result:
  `research/grothendieck/results/nonabelian-terminal-kernel-power-spectrum.json`.
- Coverage: 2,400 exact coefficient-value checks over 48 index cases.
- Epistemic graph research admission: event 1237.
- Ledger-source admission and publication report: event 1239.
- No site build was run, by operator instruction.
