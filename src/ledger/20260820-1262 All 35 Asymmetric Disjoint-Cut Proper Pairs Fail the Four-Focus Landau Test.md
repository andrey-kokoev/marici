---
title: "All 35 Asymmetric Disjoint-Cut Proper Pairs Fail the Four-Focus Landau Test"
date: 2026-08-20
entry: 1262
status: active-narrow-finite-result
author: marici.Benincasa
---

# 1262 — All 35 Asymmetric Disjoint-Cut Proper Pairs Fail the Four-Focus Landau Test

Sequence claim: `seqclaim-c2fbfa1e853ab370e35f9af9`.

## Frozen systems

Entry 1261 leaves 35 source-compatible proper-wall pairs whose two labelled
cut supports are disjoint. Each pair therefore has four distinct focus
occurrences and two independent cut roots \(b,c\).

For every labelled pair, reconstruct from Entry 1257:

- the four ordered focus vectors;
- the full \(3\times3\) routing Gram matrix;
- its nonzero determinant;
- the realization equation for the common integration point;
- the three minors imposing collinearity of the two wall gradients.

No cyclic representative or inherited distance is used.

## Exact staged elimination

First eliminate \(b\) between the realization equation and each of the three
collinearity minors. Then eliminate \(c\) between pairs of the resulting
necessary conditions.

For every one of the 35 systems, at least one second-stage resultant is

\[
\boxed{1}.
\]

A common Landau solution would have to annihilate every staged necessary
condition. The unit certificate therefore excludes such a solution.

## Consequence for all proper--proper pairs

The 150 source-compatible proper--proper pairs now split as

\[
10\text{ complementary same-cut pairs forcing }t=0,
\]

\[
105\text{ shared-cut pairs with unit direct resultant},
\]

\[
35\text{ disjoint-cut pairs with unit staged resultant}.
\]

Thus no proper--proper pair produces anomalous two-wall support on the
asymmetric physical family.

Across the full 245-pair census, 175 pairs are now classified. The only
remaining class is the 70 pairs containing one one-cut total wall.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_disjoint_cut_pairs.rs`
- `research/benincasa/results/five-site-asymmetric-disjoint-cut-pairs.json`

## Next falsifier

Derive the correctly typed endpoint/stationarity equations for the 70
one-cut-total pairs and eliminate them without treating the one-cut total wall
as an ordinary two-focus proper-region wall.
