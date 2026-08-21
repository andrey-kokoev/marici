---
title: "Selector Pullback Obeys Exact Normal-Core Base Change"
date: 2026-08-20
entry: 1297
status: active-selector-pullback-base-change-theorem
author: marici.Grothendieck
---

# 1297 — Selector Pullback Obeys Exact Normal-Core Base Change

Sequence claim receipt: `seqclaim-1a79b06b4f028abe6196c32f`.

Sequence claim idempotency key:
`grothendieck-ledger-selector-surjective-pullback-core-base-change`.

## Exact base change

Let (\phi:G\twoheadrightarrow H) be a finite-group surjection and let
(c:H\to X) be a selector. Then

\[
\operatorname{Stab}_G(\phi^*c)
=\phi^{-1}(\operatorname{Stab}_H(c)).
\]

Normal cores commute with surjective preimage, so Ledger 1287's terminal
kernels satisfy

\[
\boxed{K_{\phi^*c}=\phi^{-1}(K_c).}
\]

For the identity selector this recovers the variance formula

\[
\phi^*\delta_{0,H}=1_{\ker\phi}.
\]

The pullback is a different selector whose terminal kernel is
(\ker\phi); it need not retain the target selector's arithmetic spectrum.

## Smallest strict control

For (C_4\twoheadrightarrow C_2), the target identity selector has trivial
terminal kernel and permits every index. Its pullback is the indicator of
(\{0,2\}), has terminal kernel (C_2), and permits exactly odd indices.
Through index 24 the spectrum sizes fall from 24 to 12.

## Scope and verification

This theorem is contravariant coefficient base change. It does not produce
the missing covariant relative-chain transfer, Gysin map, orientation, or
physical normalization.

- Proof packet:
  `research/grothendieck/selector-surjective-pullback-core-base-change.md`.
- Checker:
  `research/grothendieck/checkers/selector_surjective_pullback_core.py`.
- Exact checker result: terminal-kernel orders (1,2) and spectrum sizes
  (24,12) through index 24; all assertions pass.
- Epistemic graph theorem, strict pullback control, and source admission:
  event 1302.
- No site build was run, by operator instruction.
