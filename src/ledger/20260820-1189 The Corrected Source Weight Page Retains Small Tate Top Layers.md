---
title: "The Corrected Source Weight Page Retains Small Tate Top Layers"
date: 2026-08-20
entry: 1189
status: superseded-by-higher-concurrence-complex
sector: cosmology
---

# 1189 — The Corrected Source Weight Page Retains Small Tate Top Layers

Sequence claim: `seqclaim-b0439ebf1b3e394cab3642c9`.

> **Supersession notice.** This entry computes only the pair-to-triple
> cokernel. The source arrangement also has genuine fourfold concurrence
> cells, so this cokernel is not the cohomology of the full marked Čech
> complex. Entry 1192 restores the next differential and replaces the
> displayed (W_6) ranks by the corresponding (H^2) ranks.

## Component-resolved differential

Entry 1188 gives two pair-curve types:

- a connected elliptic curve, with one \(H^0\) generator;
- a split rational deck pair, with two component generators.

For every distinct triple of marked hyperplanes, compute the exact shared
sign-node set.

If the triple point is off the branch, its lift has two deck points. A split
pair maps sheetwise,

\[
(1,0)\mapsto(1,0),
\qquad
(0,1)\mapsto(0,1),
\]

while a connected elliptic pair maps diagonally.

If the triple point is a shared sign node, its lift is one ramification
point and both rational components map to it. Combine these maps with the
standard signed triangle boundary.

## Exact ranks

The source packet has three corrected profiles:

\[
\begin{array}{c|c|c|c|c|c|c|c}
m&\text{branch triples}&\text{off branch}&\dim C_1&\dim C_2&\operatorname{rank}d&W_6&\text{terms}\\
\hline
5&8&2&20&12&8&4&4\\
5&4&6&16&16&12&4&4\\
6&8&12&25&32&20&12&20.
\end{array}
\]

The first row is the all-nodal five-mark profile; the second has one smooth
mark; the third has one smooth and five nodal marks.

## Corrected source-associated page

Combining Entries 1184, 1188, and the present differential gives

\[
\boxed{
\begin{array}{c|c}
\text{term count}&(W_3,W_4,W_5,W_6)\\
\hline
4&(20,15,0,4)\\
4&(20,19,8,4)\\
20&(20,22,10,12).
\end{array}
}
\]

These supersede Entry 1187's branch-avoiding ranks for the actual source
packet.

## Meaning

The hostile branch collisions remove most apparent elliptic complexity and
shrink the top Tate layer, but do not kill it completely. The surviving
architecture remains

\[
\boxed{
\text{rank-20 threefold variation}
+
\text{Tate surface lattices}
+
\text{at most five elliptic pair systems}
+
\text{small Tate top cokernel}.
}
\]

No new carrier or coefficient type is required.

## Scope and next falsifier

The calculation is over the coherent quadratic splitting field where deck
components are labelled. Descent to the base may produce Kummer characters,
but cannot change the geometric ranks.

Next compute the deck/Kummer representation of the surviving \(W_6\)
cokernel and its cyclic transport across the three profiles. Then test
whether any extension between \(W_5\) and \(W_6\) is nontrivial under
Gauss--Manin transport.

## Evidence

- `research/benincasa/checkers/four_site_qg_source_pair_triple_differential.py`
- `research/benincasa/results/four-site-qg-source-pair-triple-differential.json`
- Entries 1186--1188.
