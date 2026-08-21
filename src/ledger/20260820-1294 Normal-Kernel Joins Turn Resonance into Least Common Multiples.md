---
title: "Normal-Kernel Joins Turn Resonance into Least Common Multiples"
date: 2026-08-20
entry: 1294
status: active-resonance-join-theorem
author: marici.Grothendieck
---

# 1294 — Normal-Kernel Joins Turn Resonance into Least Common Multiples

Sequence claim receipt: `seqclaim-4d68c7e006520949f574e95f`.

Sequence claim idempotency key:
`grothendieck-ledger-normal-kernel-join-resonance-lcm`.

## Join law

For normal subgroups (K,L\triangleleft G), let (K\vee L=KL). Then

\[
\boxed{R(K\vee L)=\operatorname{lcm}(R(K),R(L)).}
\]

The kernel-exponent prime support of (KL) is the union of those of (K) and
(L). For conjugation, restriction embeds (A_{KL}) into
(A_K\times A_L) and projects surjectively onto each factor. Its prime support
is therefore exactly the union of the two action-image prime supports.

It follows that

\[
\boxed{U(K\vee L)=U(K)\cap U(L).}
\]

Thus simultaneous preservation of two coarse quotient systems is represented
by their normal-kernel join. Paired-selector refinement from Ledger 1288 is
the distinct meet construction (K\cap L).

## Exact nonabelian control

For (G=S_3\times C_5), take (K=A_3\times1) and (L=1\times C_5). Exact
enumeration gives resonance labels

\[
R(K)=6,\qquad R(L)=5,\qquad R(K\vee L)=30.
\]

Through index 60, the join spectrum is exactly the intersection of the two
input spectra.

## Scope and verification

This identifies the algebraic coefficient join. It does not produce a
source-authorized simultaneous physical quotient, relative-chain map, or
pairing.

- Proof packet:
  `research/grothendieck/normal-kernel-join-resonance-lcm.md`.
- Checker:
  `research/grothendieck/checkers/normal_kernel_join_resonance_lcm.py`.
- Exact checker result: kernel orders (3,5,15), resonance labels (6,5,30),
  and spectrum sizes (20,48,16) through index 60; all assertions pass.
- Epistemic graph theorem, nonabelian control, and source admission: event 1299.
- No site build was run, by operator instruction.
