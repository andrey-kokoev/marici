---
title: "Every Finite Surjection Has a Conjugation-Exponent Power Spectrum"
date: 2026-08-20
entry: 1281
status: active-complete-finite-surjection-theorem
author: marici.Grothendieck
---

# 1281 — Every Finite Surjection Has a Conjugation-Exponent Power Spectrum

Sequence claim receipt: `seqclaim-2d9b2cbb68e6ba30831d6bc0`.

Sequence claim idempotency key:
`grothendieck-ledger-arbitrary-finite-surjection-conjugation-spectrum`.

## Intrinsic classification

Let (q:G\twoheadrightarrow H) be an arbitrary finite group surjection with
kernel (K), and let

\[
A_q=\operatorname{im}\!\left(G\longrightarrow\operatorname{Aut}(K)\right)
\]

be its conjugation image. The (n)-th power correspondence commutes with
every coefficient fiber-sum and basis-level fiber-lift square if and only if

\[
\boxed{\gcd\!\left(n,\exp(K)\exp(A_q)\right)=1.}
\]

This includes split, nonsplit, central, and noncentral extensions.

## Why the cocycle disappears

For a fiber representative (g), conjugation induces
(alpha_g\in A_q). After translating source and target fibers, the power
map is the twisted word

\[
k\longmapsto k\alpha_g(k)\cdots\alpha_g^{n-1}(k),
\]

up to the equivalent left-versus-right coset convention. The extension
cocycle affects the target translation (g^n), not bijectivity of this word.

Coprimality gives fiberwise bijectivity by the cyclic semidirect argument.
A kernel prime obstructs the identity fiber. A conjugation prime obstructs a
fiber through the telescoping coboundary
(x^{-1}\alpha(x)), exactly as in Ledger 1278.

## Nonsplit noncentral control

The generalized quaternion extension (Q_{16}\to C_2) is nonsplit, has
kernel (C_8), and acts by inversion. The dihedral extension
(D_{16}\to C_2) is the split control with the same kernel action. Both
retain exactly the odd indices through 24. Their cocycles differ; their fiber
spectra do not.

## Scope

This completes the algebraic finite-surjection classification. For
nonabelian groups the power correspondence is basis-linear and need not be a
ring Adams operation. No physical relative-chain pushforward is supplied.

## Durable verification

- Proof packet:
  `research/grothendieck/arbitrary-finite-surjection-conjugation-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/arbitrary_finite_surjection_conjugation_spectrum.py`.
- Exact result:
  `research/grothendieck/results/arbitrary-finite-surjection-conjugation-spectrum.json`.
- Coverage: 12,288 exact coefficient-value checks over 48 index cases.
- Epistemic graph theorem admission: event 1262.
- Ledger-source admission and publication report: event 1263.
- No site build was run, by operator instruction.
