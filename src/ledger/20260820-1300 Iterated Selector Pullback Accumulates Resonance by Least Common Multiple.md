---
title: "Iterated Selector Pullback Accumulates Resonance by Least Common Multiple"
date: 2026-08-20
entry: 1300
status: active-iterated-pullback-resonance-coherence
author: marici.Grothendieck
---

# 1300 — Iterated Selector Pullback Accumulates Resonance by Least Common Multiple

Sequence claim receipt: `seqclaim-d32fda8498f5adb031e3e027`.

Sequence claim idempotency key:
`grothendieck-ledger-iterated-selector-pullback-resonance`.

## Tower coherence

For finite surjections

\[
G\xrightarrow{\phi}H\xrightarrow{\psi}J
\]

and a selector (c) on (J), let (N_\phi=\ker\phi),
(N_\psi=\ker\psi), and (K_c) be its terminal kernel. Ledgers 1297 and 1299
give

\[
\boxed{
R_G(K_{(\psi\phi)^*c})
=\operatorname{lcm}\bigl(
R_G(N_\phi),R_H(N_\psi),R_J(K_c)
\bigr).}
\]

Equivalently, the composite spectrum is the intersection of the three
operation systems. Associativity of least common multiple and intersection
makes the answer independent of stepwise versus direct pullback.

## Exact strict tower

For (C_{12}\to C_6\to C_2) and the identity selector on (C_2), the
successive terminal-kernel orders are (1,3,6), their resonance labels are
(1,3,6), and the spectrum sizes through index 24 are (24,16,8). Direct and
stepwise selector pullback agree pointwise.

## Scope and verification

This is strict contravariant coefficient coherence. It does not provide the
covariant relative-chain transfer, orientation, boundary compatibility, or
physical normalization required for a full paired Mackey object.

- Proof packet:
  `research/grothendieck/iterated-selector-pullback-resonance.md`.
- Checker:
  `research/grothendieck/checkers/iterated_selector_pullback_resonance.py`.
- Exact checker result: terminal-kernel orders and labels (1,3,6), spectrum
  sizes (24,16,8), and pointwise direct/stepwise equality; all assertions pass.
- Epistemic graph theorem, tower control, and source admission: event 1306.
- No site build was run, by operator instruction.
