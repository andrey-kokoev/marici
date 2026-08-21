---
title: "Selector Pullback Adds Exactly the Map-Kernel Resonance Surcharge"
date: 2026-08-20
entry: 1299
status: active-surjective-preimage-resonance-theorem
author: marici.Grothendieck
---

# 1299 — Selector Pullback Adds Exactly the Map-Kernel Resonance Surcharge

Sequence claim receipt: `seqclaim-b814d4967161c877772fde26`.

Sequence claim idempotency key:
`grothendieck-ledger-surjective-preimage-resonance-lcm`.

## Preimage resonance law

Let (\phi:G\twoheadrightarrow H), put (N=\ker\phi), and take
(K\triangleleft H). For (P=\phi^{-1}(K)),

\[
\boxed{R_G(P)=\operatorname{lcm}(R_G(N),R_H(K)).}
\]

The exact sequence (1\to N\to P\to K\to1) gives the union law for kernel
primes. For action primes, (A_P) maps to (A_N\times A_K) with surjective
projections. The kernel consists of extension automorphisms fixing (N) and
(P/N) pointwise; these are derivation terms valued in (Z(N)) and add no
primes outside (N).

Consequently

\[
\boxed{U_G(P)=U_G(N)\cap U_H(K).}
\]

Together with Ledger 1297, pulling back a selector adds exactly the
map-kernel resonance surcharge to its target terminal spectrum.

## Controls

For ((S_3\times C_5)\to S_3) over (A_3), the labels are (5,6,30). For
(Q_8\to C_2\times C_2) over an order-two subgroup, the labels are
(2,2,2); the cyclic order-four preimage and its inversion action introduce
no new prime. Both spectrum-intersection identities hold through index 60.

## Scope and verification

This is algebraic coefficient base change. It does not supply the missing
Betti relative-chain transfer, orientation, boundary covariance, or physical
normalization.

- Proof packet:
  `research/grothendieck/surjective-preimage-resonance-lcm.md`.
- Checker:
  `research/grothendieck/checkers/surjective_preimage_resonance_lcm.py`.
- Control results through index 60: mixed-prime spectrum sizes (48,20,16)
  and nonsplit quaternion sizes (30,30,30); all assertions pass.
- Epistemic graph theorem, extension controls, and source admission: event 1305.
- No site build was run, by operator instruction.
