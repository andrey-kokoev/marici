---
title: "Resonance Preserves Normal Joins but Not Normal Meets"
date: 2026-08-20
entry: 1295
status: active-resonance-meet-defect-theorem
author: marici.Grothendieck
---

# 1295 — Resonance Preserves Normal Joins but Not Normal Meets

Sequence claim receipt: `seqclaim-9b5acf87058a1cb1204925ed`.

Sequence claim idempotency key:
`grothendieck-ledger-resonance-meet-defect`.

## Meet bound

For normal kernels (K,L\triangleleft G), Ledger 1285 gives only

\[
R(K\cap L)\mid\gcd(R(K),R(L)),
\]

or equivalently

\[
U(K)\cup U(L)\subseteq U(K\cap L).
\]

Unlike Ledger 1294's exact join law, equality can fail. Radical resonance is
therefore a join-semilattice morphism under least common multiple, not a
lattice morphism.

## Smallest strict hostile test

Take two distinct coordinate subgroups (K,L) of (C_2\times C_2). Then

\[
R(K)=R(L)=2,
\qquad K\cap L=1,
\qquad R(K\cap L)=1.
\]

Both input spectra contain exactly the odd indices, but the meet spectrum
contains every positive index. Exact enumeration through index 24 verifies
the strict inclusion. The join is the full group and still obeys the lcm law.

## Scope and verification

The disappearing meet obstruction is purely coefficient-side. It does not
activate a physical selector, relative-chain pushforward, or pairing.

- Proof packet: `research/grothendieck/resonance-meet-defect.md`.
- Checker: `research/grothendieck/checkers/resonance_meet_defect.py`.
- Exact checker result: kernel orders (2,2,1,4), labels (2,2,1,2), and
  meet/input spectrum sizes (24,12) through index 24; all assertions pass.
- Epistemic graph theorem, smallest hostile test, and source admission:
  event 1300.
- No site build was run, by operator instruction.
