---
title: "The Residual Four-Site Odd Grade Is a Labelled Gram-Kummer Module"
date: 2026-08-20
entry: 1195
status: active-associated-grade
sector: cosmology
---

# 1195 — The Residual Four-Site Odd Grade Is a Labelled Gram-Kummer Module

Sequence claim: `seqclaim-900de37c1cb694251912bced`.

## Source evaluation

Write the four-site infinity branch as

\[
K_\infty
=
-\frac14\Delta^T A\Delta,
\qquad
A=\operatorname{adj}(G),
\]

\[
\Delta=(y_2^2-y_1^2,y_3^2-y_2^2,y_4^2-y_3^2).
\]

Each of Entry 1193's residual classes has a representative supported on one
off-branch marked triple. Its three pair faces are connected elliptic
curves, so no pair (H^0_-) generator reaches it. Evaluating (K_\infty)
at the exact projective triple point therefore gives its rank-one Kummer
coefficient line without choosing a primitive lift.

## Four occurrence radicands

Up to source-fixed nonzero squares and signs, the four cyclic radicands are

\[
\boxed{
A_{11},
\quad A_{11}+A_{22}-2A_{12},
\quad A_{22}+A_{33}-2A_{23},
\quad A_{33}.}
\]

Equivalently, they are

\[
r_i^T\operatorname{adj}(G)r_i
\]

for

\[
r_1=(1,0,0),quad
r_2=(-1,1,0),quad
r_3=(0,-1,1),quad
r_4=(0,0,-1).
\]

Each radicand occurs in two source terms, one from each regular (C_4)
orbit. The associated graded connection is therefore

\[
\boxed{
\nabla_i=d-\frac12d\log(r_i^T\operatorname{adj}(G)r_i).}
\]

## Classification

The vectors (r_i) are the labelled incidence covectors of the four-cycle.
Their quadratic cofactors are existing Gram/Cayley--Menger minor supports,
possibly after the corresponding unimodular external-basis change. Hence

\[
\boxed{
\text{residual rank eight}
=
\text{two occurrence copies of four Gram-Kummer lines}.}
\]

No new carrier divisor is present. This is a sector-specific coefficient
object compiled from the frozen Gram carrier, directly supporting H2.

## Scope

This proves horizontality and support of the associated grade. It does not
prove that the rank-eight grade splits from the elliptic-pair variation in
the full marked-relative Gauss--Manin system. A nontrivial extension may
still mix these pieces while preserving the weight filtration.

## Next falsifier

Compute the extension class between one residual Kummer line and the
elliptic (H^1) systems of its three incident pair curves. Since all three
faces are connected elliptic pairs, the diagonal (H^0) incidence vanishes
but the Gauss--Manin off-diagonal block need not. Test the class modulo all
regular triangular gauges before claiming a split coefficient module.

## Artifacts

- `research/benincasa/checkers/four_site_qg_residual_kummer_radicals.py`
- `research/benincasa/results/four-site-qg-residual-kummer-radicals.json`
