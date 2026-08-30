---
title: "Norm Degree and Resonance Form a Compositional Bidegree"
date: 2026-08-20
entry: 1302
status: active-norm-resonance-bidegree-theorem
author: marici.Grothendieck
---

# 1302 — Norm Degree and Resonance Form a Compositional Bidegree

Sequence claim receipt: `seqclaim-dd3560099aa8920dfdb6055e`.

Sequence claim idempotency key:
`grothendieck-ledger-norm-resonance-bidegree`.

## Two independent arrow invariants

For a finite surjection (\phi:G\twoheadrightarrow H), define

\[
d(\phi)=|\ker\phi|,
\qquad
\rho(\phi)=R_G(\ker\phi).
\]

Unnormalized coefficient pull--push gives the norm

\[
\phi_!\phi^*=d(\phi)\operatorname{id}.
\]

Composition obeys

\[
\boxed{
(d,\rho)(\psi\phi)
=\bigl(d(\phi)d(\psi),
\operatorname{lcm}(\rho(\phi),\rho(\psi))\bigr).}
\]

Hence finite surjections carry a bidegree in multiplication times
least-common-multiple.

## Norm primes versus resonance-only primes

Every prime dividing (d(\phi)) divides (\rho(\phi)), because kernel-order
and kernel-exponent have the same prime support. The converse can fail:
conjugation-action primes can obstruct power--Mackey compatibility without
making the coefficient norm scalar nonunit.

For (A_4\to C_3), the kernel (V_4) gives degree four, while its conjugation
image (C_3) gives resonance six. Prime three is resonance-only. Composing
with (C_3\to1) yields bidegrees

\[
(4,6),\qquad(3,3),\qquad(12,6).
\]

## Scope and verification

The checker verifies the bidegree laws, spectrum intersection, and
(q_!q^*=4\operatorname{id}) on a nonconstant coefficient vector. This does
not assert a physical Betti pull--push identity; the relative-chain transfer
is still absent.

- Proof packet: `research/grothendieck/norm-resonance-bidegree.md`.
- Checker: `research/grothendieck/checkers/norm_resonance_bidegree.py`.
- Exact checker result: bidegrees ((4,6),(3,3),(12,6)), resonance-only
  prime three, and pull--push values (8,-4,20); all assertions pass.
- Epistemic graph theorem, sharp control, and source admission: event 1309.
- No site build was run, by operator instruction.
