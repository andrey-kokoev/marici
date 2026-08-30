---
title: "Norm and Resonance Primes Obey a Three-Regime Law"
date: 2026-08-20
entry: 1304
status: active-norm-resonance-prime-trichotomy
author: marici.Grothendieck
---

# 1304 — Norm and Resonance Primes Obey a Three-Regime Law

Sequence claim receipt: `seqclaim-af3732637c518ad4a6c9b2a8`.

Sequence claim idempotency key:
`grothendieck-ledger-norm-resonance-prime-trichotomy`.

## Prime trichotomy

For the bidegree ((d,\rho)) of Ledger 1302,

\[
\operatorname{rad}(d)\mid\rho.
\]

Therefore every prime lies in exactly one of three regimes:

1. good for both norm and resonance;
2. bad for both norm and resonance;
3. norm-invertible but resonance-obstructed.

The apparent fourth regime—norm-bad but resonance-good—is impossible.

## Degree localization is insufficient

Localizing coefficients to invert (d) repairs the scalar norm
(\phi_!\phi^*=d\operatorname{id}), but does not necessarily repair the
basis-level power--Mackey square. For (A_4\to C_3),

\[
(d,\rho)=(4,6).
\]

At prime three the norm scalar is a unit, yet the order-three conjugation
action obstructs the third-power fiber word. This is the exact
resonance-only regime.

## Scope and verification

The checker classifies primes (2,3,5,7) for identity, cyclic, (A_4\to C_3),
and terminal (A_4) controls and verifies the impossible cell is empty.
Coefficient localization does not construct a physical relative-chain map.

- Proof packet: `research/grothendieck/norm-resonance-prime-trichotomy.md`.
- Checker:
  `research/grothendieck/checkers/norm_resonance_prime_trichotomy.py`.
- Exact checker result: all four controls and primes (2,3,5,7) classified,
  the norm-only bad cell empty, and the (A_4\to C_3) prime-three
  resonance-only cell present; all assertions pass.
- Epistemic graph theorem, prime census, and source admission: event 1311.
- No site build was run, by operator instruction.
