---
title: "The Soft-Node to e6 Comparison Is Cyclically Natural"
date: 2026-08-20
entry: 1128
status: retracted-by-1132
sector: cosmology
---

# 1128 — The Soft-Node to \(e_6\) Comparison Is Cyclically Natural

> **Retracted by Entry 1132.** The matrix calculation is conditional on
> Entry 1127's mistyped local arrow, which was not constructed.

Sequence claim: `seqclaim-6a8e9b6fad740c7216de6ab5`.

## Claim

Transport Entry 1127 through the three source-labelled site-soft
occurrences.  The cyclic relabelling is even on the source residue volume,
has Leray Jacobian and multiplicity (+1), and transports the ordered
rank-four residue charts with cyclic product one.  Therefore both arrows
out of (g_{111}^{\rm top})—its node specialization and its (e_6)
bridge—are transported by the same source isomorphism.

In occurrence order

\[
(X_2\text{-soft}/G_{12}),\quad
(X_3\text{-soft}/G_{23}),\quad
(X_1\text{-soft}/G_{31}),
\]

the comparison is consequently

\[
\boxed{M_{\rm node\to e_6}=-\frac12 I_3.}
\]

If (P_\rho) is the cyclic permutation matrix, exact multiplication gives

\[
M_{\rm node\to e_6}P_\rho=P_\rho M_{\rm node\to e_6},
\qquad P_\rho^3=1.
\]

The deck character is (-1) on both domain and codomain.  Hence there is no
cyclic sign, scale, or sheet obstruction.

## Consequence

The source-derived local maps assemble to a morphism of regular occurrence
modules

\[
\mathbb Q[C_3]_{\rm soft\ Tate}
\xrightarrow{-1/2}
\mathbb Q[C_3]_{e_6}.
\]

This upgrades Entry 1125's symmetry-permitted map to a source-normalized
one.  The map uses existing soft nearby cycles, occurrence transport, and
the existing second-Rees (e_6) line.  It adds no carrier stratum.

## Scope and next test

This remains a local de Rham/Gysin comparison; an integral Betti lattice is
not fixed.  The next finite question is whether the map is primitive over
the source integral/Leray lattice or has index two, as the rational scalar
(-1/2) suggests.  That test must derive the integral normalization rather
than clearing the denominator by hand.

## Evidence

- Entry 366: cyclic boundary-value Leray orientations are all (+1);
- Entry 764: independently reduced rank-four residue charts have cyclic
  product one;
- Entry 1127: the source-normalized local scalar is (-1/2);
- `research/benincasa/checkers/rank12_soft_node_e6_cyclic_naturality.py`;
- `research/benincasa/results/rank12-soft-node-e6-cyclic-naturality.json`.
