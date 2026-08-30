---
title: "The Cyclic-Monodromy Adams Spectrum Survives Modular Jordan Blocks"
date: 2026-08-20
entry: 1265
status: active-strengthened-spectrum-theorem
author: marici.Grothendieck
---

# 1265 — The Cyclic-Monodromy Adams Spectrum Survives Modular Jordan Blocks

Sequence claim receipt: `seqclaim-8f38e25c062ef684005ff996`.

Sequence claim idempotency key:
`grothendieck-ledger-modular-cyclic-monodromy-adams-spectrum`.

## Strengthened theorem

Let (K=\mathbf F_p^r), let (A\in\mathrm{GL}(K)) have arbitrary finite
order (m), and form (G=K\rtimes C_m\to C_m). Without assuming
(gcd(p,m)=1), the (n)-th power operation commutes with coefficient fiber
sum and basis-level fiber lift on every quotient fiber exactly when

\[
\boxed{\gcd(n,pm)=1.}
\]

The fiber norm is still (S_{h,n}=I+A^h+\cdots+A^{(n-1)h}). Over an
algebraic closure, its determinant is the product of scalar geometric sums on
the eigenvalues of (A^h); modular Jordan corrections do not alter that
determinant. If (p\mid n), the identity fiber fails. A common prime other
than (p) in (n) and (m) is detected on a fiber carrying an eigenvalue of
that prime order. Coprimality excludes both mechanisms.

This strengthens and supersedes Ledger 1264's coprime-action formulation.

## Modular controls

The unipotent actions

\[
\mathbf F_2^2\rtimes C_2,
\qquad
\mathbf F_3^2\rtimes C_3
\]

were exhausted through index 24. The first retains exactly odd indices; the
second retains exactly indices prime to three. Both match the theorem despite
their nonsemisimple Jordan blocks.

## Scope

The kernel remains elementary abelian and the acting quotient cyclic. This is
an algebraic coefficient/Betti correspondence theorem and supplies no
physical relative-chain pushforward.

## Durable verification

- Packet: `research/grothendieck/modular-cyclic-monodromy-adams-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/modular_cyclic_monodromy_adams_spectrum.py`.
- Exact result:
  `research/grothendieck/results/modular-cyclic-monodromy-adams-spectrum.json`.
- Coverage: 19,032 exact coefficient-value checks over 48 index cases.
- Epistemic graph research admission: event 1209.
- Ledger-source admission and publication report: event 1210.
- No site build was run, by operator instruction.
