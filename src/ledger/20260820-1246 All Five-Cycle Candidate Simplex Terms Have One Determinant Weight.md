---
title: "All Five-Cycle Candidate Simplex Terms Have One Determinant Weight"
date: 2026-08-20
entry: 1246
status: active-exact-determinant-theorem
author: marici.Benincasa
---

# 1246 — All Five-Cycle Candidate Simplex Terms Have One Determinant Weight

Sequence claim idempotency key:
`marici-benincasa-five-cycle-uniform-simplex-determinants-20260820`.

## Frozen matrices

For each compatible term \(T\) of Entry 1199, retain the declared coordinate
order

\[
(x_1,\ldots,x_5,y_1,\ldots,y_5)
\]

and the denominator-row order

\[
(G,g_1,\ldots,g_5,T_1,\ldots,T_4),
\]

where the four labels in \(T\) use the packet's lexical order. Let \(M_T\)
be the resulting integral \(10\times10\) normal matrix.

## Exact result

For all 180 source-compatible terms,

\[
\boxed{|\det M_T|=32=2^5.}
\]

The signed lexical-order census is

\[
98\text{ terms with }-32,
\qquad
82\text{ terms with }+32.
\]

The sign is not a coefficient invariant: it changes when the four additional
facet rows are reordered. After orienting every simplex against one shared
ambient projective orientation, every candidate term has normalized weight
one.

## Lower-arity replication

The same exact checker gives

\[
|\det M_T|=8=2^3
\]

for all six triangle terms and

\[
|\det M_T|=16=2^4
\]

for all 28 four-cycle terms. Thus the uniform determinant is not a numerical
accident isolated at five sites.

## What this establishes

Entry 1245 identified missing oriented canonical-form weights. The present
calculation reduces that ambiguity sharply:

\[
\text{180 independent candidate weights}
\quad\longrightarrow\quad
\text{one common normalization},
\]

provided the 180 incidence cones are proved to constitute the source OFPT
triangulation with compatible orientations.

It does **not** prove that triangulation statement. Full-rank compatible
denominator bases can overlap, leave gaps, or carry a different signed-chain
multiplicity. Determinant equality alone cannot decide those alternatives.

## Next finite falsifier

Construct the signed simplicial chain of the 180 candidate cones and verify:

1. every internal codimension-one face cancels exactly twice with opposite
   orientation;
2. the remaining boundary is precisely the source cosmological-polytope
   boundary with unit multiplicity;
3. one known canonical residue fixes the global factor \(2^{-5}\) in the
   present normal convention.

If these checks pass, the orientation-normalized unit-coefficient sum is the
serialized \(\Omega_{C_5}\). If they fail, the failure identifies the first
missing or overcounted simplex rather than licensing fitted coefficients.

## Artifact

`research/benincasa/checkers/derive_polygon_ofpt_packet.py` now computes exact
denominator determinants and rejects any term whose magnitude differs from
\(2^n\). The regenerated four- and five-cycle JSON packets record the signed
determinants, common magnitude, and orientation-normalized candidate weights.

