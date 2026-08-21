---
title: "A Selection-Preserving Split Requires Symmetry-Breaking Lift Data"
date: 2026-08-20
entry: 1307
status: active-equivariant-transfer-selection-nogo
author: marici.Grothendieck
---

# 1307 — A Selection-Preserving Split Requires Symmetry-Breaking Lift Data

Sequence claim receipt: `seqclaim-d1f9a4c7f8087289d1c3a062`.

Sequence claim idempotency key:
`grothendieck-ledger-equivariant-transfer-selection-nogo`.

## Equivariant weighted no-go

For a degree-(d>1) surjection, let a weighted transfer be

\[
T(f)(h)=\sum_{g\in q^{-1}(h)}w_gf(g).
\]

The condition (Tq^*=\operatorname{id}) makes the weights in every fiber sum
to one. Kernel equivariance makes them equal because (\ker q) acts
transitively on each fiber. Thus every weight equals (1/d), and

\[
T\delta_{0,G}=\frac1d\delta_{0,H}\neq\delta_{0,H}.
\]

No kernel-equivariant weighted left inverse can preserve frozen identity
selection for a nontrivial quotient.

## The exact escape and its cost

Choose a set-theoretic section (s:H\to G) with (s(0)=0), and define
(T_s f)(h)=f(s(h)). Then

\[
T_sq^*=\operatorname{id},
\qquad T_s\delta_{0,G}=\delta_{0,H}.
\]

But (T_s) is not kernel-equivariant: it distinguishes one lift per fiber.
Thus a selection-preserving split requires symmetry-breaking section data.

## Exact control and scope

For (C_4\to C_2), the section choosing lifts (0,1) splits pullback and
preserves delta but fails translation by two. Averaging is equivariant and
split but sends delta to ((1/2,0)). All checks use exact rational arithmetic.

This identifies a missing algebraic resource; it does not claim that source
geometry supplies the section or the absent Betti chain transfer.

- Proof packet:
  `research/grothendieck/equivariant-transfer-selection-nogo.md`.
- Checker:
  `research/grothendieck/checkers/equivariant_transfer_selection_nogo.py`.
- Exact checker result: section split/selection pass with equivariance failure;
  averaging split/equivariance pass with selection failure; all assertions pass.
- Epistemic graph theorem, exact separator, and source admission: event 1316.
- No site build was run, by operator instruction.
