---
title: "The Selector Normal Core Is the Complete Quotient-Arithmetic Invariant"
date: 2026-08-20
entry: 1292
status: active-selector-core-classification-theorem
author: marici.Grothendieck
---

# 1292 — The Selector Normal Core Is the Complete Quotient-Arithmetic Invariant

Sequence claim receipt: `seqclaim-15f9c1e1d06298a59f049e31`.

Sequence claim idempotency key:
`grothendieck-ledger-selector-core-complete-quotient-arithmetic-invariant`.

## Complete invariant

For a selector (c) on a finite group (G), let

\[
K_c=\operatorname{Core}_G(\operatorname{Stab}_R(c)).
\]

A normal subgroup (K\triangleleft G) is selector-admissible if and only if

\[
K\subseteq K_c.
\]

Indeed, a normal (K) contained in the stabilizer is contained in every
conjugate of that stabilizer, hence in its core. The converse is immediate.
Therefore two selectors have the same admissible normal-kernel down-set if
and only if their normal cores agree.

Because Ledger 1285's resonance decoration depends only on (G) and (K), the
same condition is equivalent to equality of the entire decorated
quotient--arithmetic lattice. The normal core is a complete invariant of this
behavior, though not of the selector itself.

## Exact hostile separator

On (S_3), the fully labelled selector has trivial stabilizer, while the
right-coset selector for a nonnormal transposition subgroup has stabilizer
order two. Both cores are nevertheless trivial. Exact enumeration confirms
that each admits only the identity normal kernel, so their quotient and
arithmetic behavior is identical despite their different raw selectors.

## Scope and verification

This classification deliberately forgets selector data invisible to normal
deck quotients. It does not equate the physical observables or construct a
relative-chain pushforward or pairing.

- Proof packet:
  `research/grothendieck/selector-core-complete-quotient-arithmetic-invariant.md`.
- Checker:
  `research/grothendieck/checkers/selector_core_complete_invariant.py`.
- Exact checker result: stabilizer orders (1,2), core orders (1,1), and the
  same singleton admitted-kernel down-set; all assertions pass.
- Epistemic graph theorem, hostile separator, and source admission: event 1297.
- No site build was run, by operator instruction.
