---
title: "All 105 Asymmetric Shared-Cut Proper Pairs Have Unit Landau Resultant"
date: 2026-08-20
entry: 1261
status: active-narrow-finite-result
author: marici.Benincasa
---

# 1261 — All 105 Asymmetric Shared-Cut Proper Pairs Have Unit Landau Resultant

Sequence claim: `seqclaim-f56fde48e742f3fa7f86e35f`.

## Frozen source-compatible pair census

The 180 source OFPT terms admit 245 distinct labelled wall pairs:

\[
\begin{array}{c|r}
\text{first-gate class}&\text{count}\\ \hline
G\text{-containing}&25\\
\text{same-cut proper}&10\\
\text{one-cut-total containing}&70\\
\text{disjoint-cut proper}&35\\
\text{shared-cut proper}&105
\end{array}
\]

No cyclic quotient is used.

The 25 \(G\)-containing pairs lie on \(t=0\). For each of the ten
same-cut proper pairs, the complementary walls have equations

\[
mt+s=0,
\qquad
(5-m)t+s=0,
\]

so they also force \(t=0\).

## Exact shared-cut elimination

For every shared-cut proper pair, retain the shared cut root \(b\) and
substitute

\[
y_{\rm shared}=b,
\qquad
y_{\rm left}=-mt-b,
\qquad
y_{\rm right}=-nt-b.
\]

All three squared focus distances are recomputed from Entry 1257's conserved
integer resultants. Eliminating \(b\) between the exact coplanarity and
stationary-collinearity equations gives

\[
\boxed{\operatorname{Res}_b(C,L)=1}
\]

for every one of the 105 labelled pairs.

Therefore none of these shared-cut systems has a stationary solution over the
complexified asymmetric family.

## Narrow conclusion

Of the 245 source-compatible pairs, 140 are now classified:

\[
25+10\text{ force existing }t=0\text{ support},
\qquad
105\text{ have empty stationary locus}.
\]

The unresolved pair census is exactly

\[
70\text{ one-cut-total pairs}
\quad+\quad
35\text{ disjoint-cut proper pairs}.
\]

No anomalous two-wall support and no new carrier datum have appeared in the
classified portion.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_compatible_pairs.rs`
- `research/benincasa/results/five-site-asymmetric-compatible-pairs.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_shared_cut_pairs.rs`
- `research/benincasa/results/five-site-asymmetric-shared-cut-pairs.json`

## Next falsifier

Construct and eliminate the 35 labelled disjoint-cut four-focus systems using
the same asymmetric routing. Keep the 70 one-cut-total systems separate
because their incidence and endpoint variance differ.
