---
title: "Pairwise Four-Site Marked Incidence Is a Deck Pair"
date: 2026-08-20
entry: 1157
status: established-generic-incidence
sector: cosmology
---

# 1157 — Pairwise Four-Site Marked Incidence Is a Deck Pair

Sequence claim: `seqclaim-a9c134063514e33b11c81372`.

## Frozen geometry

Entry 1156 associates to every source-linear marked denominator a curve

\[
C_g=\pi^{-1}(L_g)\in|-K_{X_4}|,
\]

where

\[
\pi:X_4\to\mathbf P^2
\]

is the degree-two del Pezzo double cover branched over the quartic \(B_4\),
and \(L_g\) is the corresponding labelled line.

## Pair incidence

For two distinct generic marks,

\[
C_g\cdot C_h=(-K_{X_4})^2=2.
\]

The base lines meet at one point

\[
p_{gh}=L_g\cap L_h.
\]

If \(B_4(p_{gh})\ne0\), its inverse image consists of two reduced points,

\[
\pi^{-1}(p_{gh})=\{p_{gh,+},p_{gh,-}\},
\]

exchanged by the deck involution. Thus the generic pairwise Cech term is
not one unlabelled point: it is the two-occurrence deck permutation module.

If

\[
B_4(p_{gh})=0,
\]

the two occurrences coalesce into one ramification point with intersection
multiplicity two. This is branch-collision support of the existing marked
and Cayley--Menger data, not a new incidence generator.

## Triple incidence

Write the three labelled line equations as coefficient rows
\(\ell_g,\ell_h,\ell_k\). Three generic lines in \(\mathbf P^2\) have no
common point. A triple intersection occurs precisely on

\[
\boxed{\det(\ell_g,\ell_h,\ell_k)=0.}
\]

Hence triple Cech cells are supported on a source-derived line-concurrency
divisor. They are absent at generic kinematics.

## Narrow result

The generic marked-incidence layer is therefore

\[
\boxed{
\text{elliptic component coefficients}
+\text{ deck-resolved Tate pair incidences}.
}
\]

Its first degenerations are exhausted by two explicit conditions:

\[
B_4(L_g\cap L_h)=0
\]

for a pair collision, and

\[
\det(\ell_g,\ell_h,\ell_k)=0
\]

for triple concurrency. Both are compiled from the frozen branch divisor
and labelled marked lines. No new four-site carrier primitive is indicated.

## Scope and next falsifier

This is an intersection-theoretic generic theorem. It does not determine
which labelled lines occur together in one physical four-site integrand
term, their residue signs, or relations among their elliptic \(H^1\)
systems.

The next finite task remains source-specific: freeze one explicit four-site
term, enumerate its labelled denominator lines, and evaluate the two
conditions above for every pair and triple. The resulting signed incidence
packet is the input to the relative residue/Cech complex.

Evidence:

- `research/benincasa/checkers/four_site_marked_incidence.py`;
- `research/benincasa/results/four-site-marked-incidence.json`;
- Entries 1154--1156.
