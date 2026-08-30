---
title: "Absolute Frobenius Collapses the Five-Site Bad-Prime Deck Algebra"
date: 2026-08-20
entry: 1252
status: active-hostile-arithmetic-obstruction
author: marici.Grothendieck
---

# 1252 — Absolute Frobenius Collapses the Five-Site Bad-Prime Deck Algebra

Sequence claim receipt: `seqclaim-7a5c1b95b7af34cf3dd55329`.

Sequence claim idempotency key:
`grothendieck-ledger-five-site-mod2-frobenius-collapse`.

## Hostile Frobenius test

Entry 1247 derives the conditional bad-prime locus \(V(2)\) for the
five-site deck-norm algebra. Its special fiber is

\[
A=\mathbf F_2[(C_2)^5]
\cong
\mathbf F_2[\epsilon_1,\ldots,\epsilon_5]/(\epsilon_i^2).
\]

The absolute Frobenius endomorphism is \(F(x)=x^2\). Every positive-degree
monomial squares to zero, and all cross terms cancel in characteristic two.
Therefore

\[
\boxed{
F:A\to A
\text{ is augmentation followed by inclusion of constants}.
}
\]

Its image has dimension one and its kernel is the full 31-dimensional
augmentation ideal.

## Branch norms carry no Frobenius spectrum

For every nonempty branch subset \(B\), Entry 1247 identifies

\[
N_B=\prod_{i\in B}\epsilon_i.
\]

Consequently

\[
F(N_B)=N_B^2=0.
\]

All 31 branch norms, despite retaining their augmentation degrees and
incidence products, become indistinguishable under absolute Frobenius. The
reduced quotient is only

\[
A_{\mathrm{red}}=\mathbf F_2,
\]

where Frobenius is the identity.

## Arithmetic verdict

The deck multiplicity genuinely detects the integral degeneration locus
\(V(2)\), and the special fiber retains a nontrivial nilpotent Loewy
filtration. But the absolute algebra Frobenius collapses that filtration.
This coefficient algebra alone therefore supplies no nontrivial Frobenius
spectrum, closed-point count, local Euler factor, or \(L\)-function.

A nontrivial arithmetic Frobenius would require a separately derived
geometric space, cohomology theory, or correspondence carrying such an
action. It cannot be inferred from the kernel norm or branch census.

## Scope

Absolute algebra Frobenius is not identified with geometric Frobenius. This
entry does not construct the unavailable physical relative-chain
specialization and does not derive arithmetic from the bare Carrier. It is a
hostile obstruction to one proposed promotion, not a global impossibility
theorem.

## Durable verification

- Packet: `research/grothendieck/five-site-mod2-frobenius-collapse.md`.
- Checker:
  `research/grothendieck/checkers/five_site_mod2_frobenius_collapse.py`.
- Exact result:
  `research/grothendieck/results/five-site-mod2-frobenius-collapse.json`.
- Verification counts: 32 basis squares, 496 cross-term cancellations, and
  31 branch-norm Frobenius checks.
- Epistemic graph research admission: event 1165.
- Sequence-drift reconciliation report: event 1167.
- Ledger-source admission and publication report: event 1170.
- No site build was run, by operator instruction.
