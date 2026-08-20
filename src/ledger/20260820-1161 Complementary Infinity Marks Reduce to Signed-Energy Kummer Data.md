---
title: "Complementary Infinity Marks Reduce to Signed-Energy Kummer Data"
date: 2026-08-20
entry: 1161
status: established-filtered-normal-form
sector: cosmology
---

# 1161 — Complementary Infinity Marks Reduce to Signed-Energy Kummer Data

Sequence claim: `seqclaim-656caf645a213c1d31f3d064`.

## Frozen pair

Let \(S\) and \(S^c\) be complementary connected intervals of the
four-cycle which occur together in one of Entry 1159's OFPT terms. Their
affine denominators are

\[
q_S=L_{\partial S}(y)+X_S,
\qquad
q_{S^c}=L_{\partial S}(y)+X_{S^c},
\]

where

\[
X_S=\sum_{i\in S}X_i.
\]

They have the same edge-variable infinity normal because their boundary
edge set is the same.

## Compactified normal form

Homogenize with infinity coordinate \(s\):

\[
Q_S=L_{\partial S}+sX_S,
\qquad
Q_{S^c}=L_{\partial S}+sX_{S^c}.
\]

On the labelled residue \(Q_S=0\),

\[
L_{\partial S}=-sX_S,
\]

and therefore

\[
\boxed{
Q_{S^c}|_{Q_S=0}
=s(X_{S^c}-X_S).
}
\]

The reverse residue gives the same identity with the opposite sign.

Thus the apparently duplicated elliptic mark separates into two typed
factors:

\[
\boxed{
\text{infinity Cartier divisor }(s=0)
\quad+\quad
\text{rank-one Kummer letter }(X_{S^c}-X_S).
}
\]

It is not a second independent elliptic curve on the residue surface.

## Enhanced support

The only non-generic enhancement is

\[
X_{S^c}-X_S=0,
\]

equivalently

\[
\boxed{2X_S-E=0.}
\]

This is a signed-energy wall compiled from the existing site-energy
arrangement. No new carrier divisor is required.

## Complete census

The 28 terms contain 36 unordered complementary-pair occurrences and 72
ordered residue pivots. The six labelled complement partitions occur with
multiplicities

\[
8,8,8,8,2,2:
\]

four singleton--triple partitions occur eight times each, while the two
adjacent-pair partitions occur twice each. Up to sign, these produce six
source-labelled signed-energy letters. The full coefficient vectors and
term provenance are exported.

## Architectural result

Entry 1160's filtered infinity complication closes generically inside H2:

\[
\boxed{
\text{shared marked/infinity carrier}
+\text{ elliptic residue coefficient}
+\text{ Tate/Kummer extension data}.
}
\]

This is a higher-site realization of the recurring Marici distinction
between a resolved linear normal and a coarser coincident infinity section.

## Scope and next falsifier

The result treats complementary parallel pairs. It does not yet resolve
Entry 1160's forced triple concurrencies or compute residue orientations.

The next calculation should take one representative of each triple-
concurrency profile, derive the local intersection algebra on the del Pezzo
double cover, and determine whether its Cech/Kato contribution is Tate or
contains an extension among the component elliptic systems. No new support
cell may be added after the calculation.

Evidence:

- `research/benincasa/checkers/derive_four_cycle_parallel_pair_normal_form.py`;
- `research/benincasa/results/four-cycle-parallel-pair-normal-form.json`;
- Entries 1159--1160.
