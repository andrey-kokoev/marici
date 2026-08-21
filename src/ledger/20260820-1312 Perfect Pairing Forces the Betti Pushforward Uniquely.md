---
title: "Perfect Pairing Forces the Betti Pushforward Uniquely"
date: 2026-08-20
entry: 1312
status: active-conditional-betti-pushforward-uniqueness
author: marici.Grothendieck
---

# 1312 — Perfect Pairing Forces the Betti Pushforward Uniquely

Sequence claim receipt: `seqclaim-8f0ef26e3deb5eb2f2b40efd`.

Sequence claim idempotency key:
`grothendieck-ledger-perfect-pairing-forces-betti-pushforward`.

## Conditional uniqueness

Suppose coefficient and Betti modules carry perfect pairings. A Betti map
(\operatorname{sp}_q:B_G\to B_H) compatible with coefficient pullback must
satisfy

\[
\langle q^*c,\Gamma\rangle_G
=\langle c,\operatorname{sp}_q\Gamma\rangle_H.
\]

Nondegeneracy makes this map unique: it is the adjoint transpose of (q^*).
On deck-labelled dual bases,

\[
\boxed{\operatorname{sp}_q(\Gamma_g)=\Gamma_{q(g)}}
\]

with coefficient one. Once pairing normalization is fixed, averaging,
multiplicity, and sign are not free choices.

## Forced composition and norm

Adjoint transposition forces strict composition

\[
\operatorname{sp}_{rq}
=\operatorname{sp}_r\operatorname{sp}_q.
\]

For (C_4\to C_2\to1), exact matrices recover basis images with coefficient
one, strict composition, and pull--push norms two and four.

## What remains unavailable

This is a conditional uniqueness theorem, not a construction on the physical
relative complex. It does not show that the forced generator assignment
commutes with relative boundaries, respects support, or arises from source
geometry. Those existence checks remain the missing fifth certificate of
Ledger 1311.

## Verification

- Proof packet:
  `research/grothendieck/perfect-pairing-forces-betti-pushforward.md`.
- Checker:
  `research/grothendieck/checkers/perfect_pairing_forces_betti_pushforward.py`.
- Exact checker result: forced coefficient-one basis images, strict tower
  composition, and norms (2,4); all assertions pass.
- Epistemic graph theorem, forced-adjoint control, and source admission:
  event 1323.
- No site build was run, by operator instruction.
