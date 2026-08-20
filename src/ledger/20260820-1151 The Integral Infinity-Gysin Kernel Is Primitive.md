---
title: "The Integral Infinity-Gysin Kernel Is Primitive"
date: 2026-08-20
entry: 1151
status: established-integral-gysin-lattice
sector: cosmology
---

# 1151 — The Integral Infinity-Gysin Kernel Is Primitive

Sequence claim: `seqclaim-728095242bcf410c47f1b0a0`.

## Question

Entries 1149--1150 separate the physical algebraic Cut--nearby class from
the elliptic width-two coinvariant. Could the two nevertheless be identified
by hidden torsion in the generic integral infinity-Gysin lattice?

The finite falsifier is the integral localization sequence of the frozen
degree-two del Pezzo surface with its anticanonical elliptic boundary.

## Frozen integral geometry

Write the Picard lattice of the degree-two del Pezzo surface as

\[
H^2(S;\mathbb Z)
=\mathbb Z\langle H,E_1,\ldots,E_7\rangle.
\]

The anticanonical boundary has class

\[
[D_\infty]=-K_S=3H-E_1-\cdots-E_7.
\]

Its coefficient content is one. Equivalently, the degree map

\[
H^2(S;\mathbb Z)\longrightarrow H^2(D_\infty;\mathbb Z)\simeq\mathbb Z,
\qquad
\alpha\longmapsto\alpha\cdot D_\infty
\]

is surjective: each exceptional class satisfies (E_i\cdot D_\infty=1).
Therefore ([D_\infty]) is primitive in the Picard lattice.

## Integral localization sequence

For (U=S\setminus D_\infty), the relevant part of the integral Gysin
sequence is

\[
H^0(D_\infty)(-1)
\xrightarrow{[D_\infty]}
H^2(S)
\longrightarrow H^2(U)
\xrightarrow{R_\infty}
H^1(D_\infty)(-1)
\longrightarrow H^3(S).
\]

Since (H^3(S)=0) and the first map is primitive, this becomes

\[
\boxed{
0\longrightarrow\mathbb Z^7
\longrightarrow H^2(U;\mathbb Z)
\xrightarrow{R_\infty}\mathbb Z^2(-1)
\longrightarrow0.}
\]

This is the integral topological form of Entry 150's generic rank-nine
sequence

\[
0\to\mathcal T_7\to\mathcal M_q^{(9)}
\to\mathbb V_{\rm ell}(-1)\to0.
\]

Both kernel and quotient are free. As an extension of abelian groups the
sequence splits, because the quotient is free, but no canonical horizontal
or polarized splitting is asserted.

## Verdict

\[
\boxed{
\text{the generic rank-seven infinity-Gysin kernel is primitive and carries
no hidden integral torsion}.}
\]

Consequently:

- Entry 301's two conductor half-sum parities live inside the algebraic
  realization and are not static torsion of the rank-nine lattice;
- Entry 1147's elliptic (mathbb Z/2) appears only after taking the
  width-two monodromy coinvariant;
- Entry 1150's occurrence-pair factors of two arise from label forgetting;
- these three appearances of the prime two have different functorial
  provenance and cannot be identified from their Smith factors alone.

Any interaction among them must be carried by monodromy, supported nearby
cycles, or the nonsplit connection of the variation—not by a torsion
extension of the generic integral lattice. No new carrier datum appears.

## Next falsifier

Compute the integral nearby-cycle totalization of this exact sequence at the
total-energy cusp. The decisive issue is whether taking coinvariants is
exact across the nonsplit variation or produces a connecting class from the
elliptic width-two coinvariant into the algebraic conductor lattice. This
requires the integral off-diagonal monodromy, not merely the rational
infinity-Gysin projection.

Evidence:

- `research/benincasa/checkers/integral_del_pezzo2_gysin_lattice.py`;
- `research/benincasa/results/integral-del-pezzo2-gysin-lattice.json`;
- Entries 150, 301, 305, 312, 1147, 1149, and 1150.
