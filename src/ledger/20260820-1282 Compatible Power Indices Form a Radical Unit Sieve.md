---
title: "Compatible Power Indices Form a Radical Unit Sieve"
date: 2026-08-20
entry: 1282
status: active-congruence-spectrum-corollary
author: marici.Grothendieck
---

# 1282 — Compatible Power Indices Form a Radical Unit Sieve

Sequence claim receipt: `seqclaim-cd17cd4339ba6cc9c9bc48a7`.

Sequence claim idempotency key:
`grothendieck-ledger-radical-resonance-unit-sieve`.

## Radical resonance modulus

For a finite surjection (q:G\twoheadrightarrow H), let (K=\ker q), let
(A_q\subseteq\operatorname{Aut}(K)) be its conjugation image, and define

\[
R_q=\operatorname{rad}\!\left(\exp(K)\exp(A_q)\right).
\]

Ledger 1281 implies that the compatible power indices are exactly

\[
\boxed{\{n\ge1:\gcd(n,R_q)=1\}.}
\]

Compatibility is therefore periodic modulo (R_q). Its residue classes are
the unit group ((\mathbf Z/R_q\mathbf Z)^\times), and compatibility is
closed under multiplication, coherently with (P_mP_n=P_{mn}).

Each complete period contains (arphi(R_q)) survivors, giving density

\[
\frac{\varphi(R_q)}{R_q}
=\prod_{p\mid R_q}\left(1-\frac1p\right).
\]

## Examples

- five-site (2)-deck quotients: (R_q=2), exactly odd indices;
- (A_4\to C_3) and (Q_8\rtimes C_3\to C_3): (R_q=6);
- (C_5\rtimes C_4\to C_4): (R_q=10);
- (operatorname{Heis}_3\to C_3^2): (R_q=3).

## Scope

This is a finite congruence sieve on algebraic correspondence operations. It
is not an Euler product, a distribution of Carrier-derived primes, a
geometric Frobenius spectrum, or a physical selection theorem. Actual basis
power maps can depend on exponents larger than (R_q); only the
compatibility indicator factors through the radical modulus.

## Durable verification

- Packet: `research/grothendieck/radical-resonance-unit-sieve.md`.
- Checker: `research/grothendieck/checkers/radical_resonance_unit_sieve.py`.
- Exact result:
  `research/grothendieck/results/radical-resonance-unit-sieve.json`.
- Coverage: 5,049 exact periodicity, multiplicativity, and density checks.
- Epistemic graph research admission: event 1268.
- Ledger-source admission and publication report: event 1269.
- No site build was run, by operator instruction.
