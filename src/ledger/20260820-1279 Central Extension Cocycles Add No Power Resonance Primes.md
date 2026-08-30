---
title: "Central Extension Cocycles Add No Power Resonance Primes"
date: 2026-08-20
entry: 1279
status: active-central-extension-theorem
author: marici.Grothendieck
---

# 1279 — Central Extension Cocycles Add No Power Resonance Primes

Sequence claim receipt: `seqclaim-d4bb1a024af28b9e5688c039`.

Sequence claim idempotency key:
`grothendieck-ledger-central-extension-power-mackey-spectrum`.

## Central-extension theorem

Let (q:G\twoheadrightarrow H) be any finite group surjection with central
kernel (K). The (n)-th power correspondence commutes with every
coefficient fiber-sum and basis-level fiber-lift square if and only if

\[
\boxed{\gcd(n,\exp K)=1.}
\]

For a fiber representative (g) and (k\in K), centrality gives

\[
(gk)^n=g^n k^n.
\]

Every restricted fiber map is therefore a translate of (k\mapsto k^n) on
(K). The quotient group and the extension cocycle contribute no additional
resonance primes. This conclusion does not require the extension to split.

## Nonsplit controls

Exact fiber enumeration through index 18 was performed for

\[
C_4\to C_2,
\qquad
Q_8\to V_4,
\qquad
\operatorname{Heis}_3\to C_3^2.
\]

The first two retain exactly odd indices. The order-27 Heisenberg extension
retains exactly indices prime to three. All agree with the kernel exponent.

## Scope

This removes the split-extension hypothesis for central kernels. A
noncentral nonsplit extension requires separate outer-action and cocycle
analysis. For nonabelian total groups the power correspondence is
basis-linear and need not be a ring Adams operation. No physical
relative-chain pushforward is supplied.

## Durable verification

- Packet:
  `research/grothendieck/central-extension-power-mackey-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/central_extension_power_mackey_spectrum.py`.
- Exact result:
  `research/grothendieck/results/central-extension-power-mackey-spectrum.json`.
- Coverage: 14,562 exact coefficient-value checks over 54 index cases.
- Epistemic graph research admission: event 1256.
- Ledger-source admission and publication report: event 1257.
- No site build was run, by operator instruction.
