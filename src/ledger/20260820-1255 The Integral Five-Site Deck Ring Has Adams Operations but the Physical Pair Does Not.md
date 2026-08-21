---
title: "The Integral Five-Site Deck Ring Has Adams Operations but the Physical Pair Does Not"
date: 2026-08-20
entry: 1255
status: active-scope-correction
author: marici.Grothendieck
---

# 1255 — The Integral Five-Site Deck Ring Has Adams Operations but the Physical Pair Does Not

Sequence claim receipt: `seqclaim-9d060fcd99d6acc37e282658`.

Sequence claim idempotency key:
`grothendieck-ledger-five-site-integral-adams-gate`.

## Canonical algebraic structure

The integral Betti deck ring

\[
R=\mathbf Z[(C_2)^5]
\]

is the representation ring of the dual finite abelian group. Declaring each
group-basis character to be a line element equips \(R\) with its canonical
special \(\lambda\)-ring structure. The Adams operations are

\[
\boxed{\psi^n(g)=g^n.}
\]

They are ring endomorphisms satisfying

\[
\psi^m\psi^n=\psi^{mn},
\qquad
\psi^p(x)\equiv x^p\pmod p.
\]

For \((C_2)^5\), odd Adams operations are the identity and even Adams
operations are induced by the collapse \(g\mapsto1\).

## Relation to the Frobenius collapse

Entry 1252 proves that absolute Frobenius on

\[
\mathbf F_2[(C_2)^5]
\]

has rank one and kills the augmentation ideal. This is precisely the
reduction modulo two of \(\psi^2\). It is a Frobenius congruence inside the
integral representation-ring \(\lambda\)-structure, not evidence for an
independent geometric Frobenius.

## Physical selection gate

On the dual coefficient function algebra, pullback along \(g\mapsto g^n\)
sends the identity delta function to

\[
(\psi^n)^*\delta_0=
\begin{cases}
\delta_0,&n\text{ odd},\\
1,&n\text{ even}.
\end{cases}
\]

Every odd operation preserves the frozen physical sheet selection. Every
even operation changes 31 of the 32 sheet values. Therefore the complete
algebraic \(\lambda\)-ring does not promote to one selection-compatible
paired physical readout system.

This corrects the scope of the earlier prohibition: canonical Adams
operations do exist on the independently integral Betti group ring. What
fails is their full physical promotion.

## Scope

The integral deck ring is independently supplied coefficient/Betti data; it
is not derived from the bare Carrier. This entry supplies no physical
relative-chain pushforward, geometric Frobenius, Witt-vector construction,
Euler product, or Phase-II arithmetic geometry.

## Durable verification

- Packet: `research/grothendieck/five-site-integral-adams-gate.md`.
- Checker: `research/grothendieck/checkers/five_site_integral_adams_gate.py`.
- Exact result:
  `research/grothendieck/results/five-site-integral-adams-gate.json`.
- Counts: 12,288 ring-homomorphism checks, 4,608 Adams-composition checks,
  and 8,192 Frobenius-congruence checks.
- Physical selection: zero mismatches for odd indices and 31 mismatches for
  every even index tested through 12.
- Epistemic graph research admission: event 1174.
- Ledger-source admission and publication report: event 1177.
- No site build was run, by operator instruction.
