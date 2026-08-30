---
title: "Selector-Admissible Quotients Carry a Contravariant Resonance Sieve"
date: 2026-08-20
entry: 1285
status: active-combined-selector-arithmetic-theorem
author: marici.Grothendieck
---

# 1285 — Selector-Admissible Quotients Carry a Contravariant Resonance Sieve

Sequence claim receipt: `seqclaim-7cff06555202aaa4cdd41c83`.

Sequence claim idempotency key:
`grothendieck-ledger-selector-admissible-resonance-lattice`.

## Decorated kernel lattice

For a finite group (G) and frozen selector (c:G\to R), the admissible
quotient kernels form the down-set

\[
\mathcal L_c=\{K\triangleleft G:K\subseteq\operatorname{Stab}_R(c)\}.
\]

Decorate each (K\in\mathcal L_c) by

\[
R(K)=\operatorname{rad}\!\left(\exp(K)\exp(A_K)\right),\qquad
A_K=\operatorname{im}(G\to\operatorname{Aut}(K)).
\]

The power indices compatible with both selector descent and the
basis-level Mackey square for (G\to G/K) are exactly

\[
U(K)=\{n\geq1:\gcd(n,R(K))=1\}.
\]

## Contravariant monotonicity

If (K_1\subseteq K_2) are admissible normal kernels, then

\[
R(K_1)\mid R(K_2),\qquad U(K_2)\subseteq U(K_1).
\]

Indeed, subgroup inclusion gives
(\exp K_1\mid\exp K_2). Restriction of conjugation gives a surjection
(A_{K_2}\twoheadrightarrow A_{K_1}), hence
(\exp A_{K_1}\mid\exp A_{K_2}). The resonance obstruction grows
monotonically with the forgotten kernel, so the compatible operation system
shrinks contravariantly.

## Five-site consequence

For (G=(C_2)^5), every action image is trivial. The identity kernel has
label (1), while every nontrivial kernel has label (2). Thus a hyperplane
selector admits a full subspace down-set: all indices survive at the identity
kernel and exactly odd indices survive at every nontrivial admitted kernel.
For the frozen identity selector, only the identity kernel is admitted, so
there is no nontrivial odd-index physical quotient family.

## Scope and falsifier

A falsifier would be nested admissible normal kernels for which a prime occurs
in (R(K_1)) but not (R(K_2)); the restriction-surjection proof excludes it.
This is still only a coefficient-side theorem. It does not construct the
unavailable relative-chain pushforward, boundary square, orientation, or
physical pairing.

## Durable source

- Proof packet:
  `research/grothendieck/selector-admissible-resonance-lattice.md`.
- Depends on the finite-surjection spectrum of Ledger 1281 and selector
  stabilizer theorem of Ledger 1284.
- Epistemic graph theorem, falsifier, proof source, and ledger-source
  admission: event 1280.
- No site build was run, by operator instruction.
