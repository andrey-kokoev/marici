---
title: "A Selector Stabilizer Is Its Maximal Coefficient Quotient"
date: 2026-08-20
entry: 1284
status: active-selector-descent-theorem
author: marici.Grothendieck
---

# 1284 — A Selector Stabilizer Is Its Maximal Coefficient Quotient

Sequence claim receipt: `seqclaim-56c62cfaab7dc438f193ae2b`.

Sequence claim idempotency key:
`grothendieck-ledger-selector-stabilizer-maximal-quotient`.

## Stabilizer theorem

Let (G) be a finite deck group and (c:G\to R) a frozen coefficient
selector. Define its right-translation stabilizer

\[
\operatorname{Stab}_R(c)
=\{k\in G:c(gk)=c(g)\text{ for every }g\in G\}.
\]

For a normal subgroup (K\triangleleft G), the selector descends through
(G\to G/K) if and only if

\[
\boxed{K\subseteq\operatorname{Stab}_R(c).}
\]

Thus the admissible normal quotient kernels are exactly the normal subgroups
inside the stabilizer. When the stabilizer itself is normal, it is the
maximal coefficient-side quotient kernel.

Power--Mackey compatibility is a second gate applied only after this selector
admission. It cannot enlarge the stabilizer.

## Five-site consequences

For (G=(C_2)^5):

- (delta_0) has trivial stabilizer, so only the identity quotient is
  coefficient-admissible;
- the constant orbit trace has full stabilizer, so every quotient descends,
  but it is a different observable;
- character and coordinate selectors have intermediate hyperplane
  stabilizers and admit precisely kernels contained in those hyperplanes.

## Scope

This classifies coefficient-side descent. It does not construct a Betti
relative-chain pushforward, prove boundary compatibility, or identify a
physical observable after changing the selector. It explains structurally
why Ledger 1282's algebraic unit sieve cannot repair Ledger 1283's frozen
selector failure.

## Durable verification

- Packet:
  `research/grothendieck/selector-stabilizer-maximal-quotient.md`.
- Checker:
  `research/grothendieck/checkers/selector_stabilizer_maximal_quotient.py`.
- Exact result:
  `research/grothendieck/results/selector-stabilizer-maximal-quotient.json`.
- Coverage: 38,880 exact stabilizer and fiber-constancy checks.
- Epistemic graph research admission: event 1273.
- Ledger-source admission and publication report: event 1276.
- No site build was run, by operator instruction.
