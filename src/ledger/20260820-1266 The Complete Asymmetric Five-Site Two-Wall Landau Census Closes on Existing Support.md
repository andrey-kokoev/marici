---
title: "The Complete Asymmetric Five-Site Two-Wall Landau Census Closes on Existing Support"
date: 2026-08-20
entry: 1266
status: active-finite-closure
author: marici.Benincasa
---

# 1266 — The Complete Asymmetric Five-Site Two-Wall Landau Census Closes on Existing Support

Sequence claim: `seqclaim-538654fe932e7b8f96ccf5a5`.

## Final mixed-pair calculation

Seventy source-compatible pairs contain one one-cut total wall.

For the forty pairs sharing its labelled cut occurrence with a proper wall,
stationarity gives parallel and antiparallel branches

\[
P_A^2-(5-|A|)^2t^2=0,
\qquad
P_A^2-|A|^2t^2=0.
\]

These are exactly the individual-wall thresholds of \(A^c\) and \(A\)
from Entry 1259. No new factor occurs.

For each of the remaining thirty disjoint-incidence pairs, use

\[
y_e=-\frac52t,
\qquad
y_i=b,
\qquad
y_j=-|A|t-b.
\]

All three focus distances are recomputed from Entry 1257. Eliminating \(b\)
between the exact three-focus Cayley--Menger coplanarity equation and the
collinearity condition for \(n_i+n_j\) with \(n_e\) gives

\[
\boxed{\operatorname{Res}_b(C,L)=1}
\]

for every labelled pair.

## Complete accounting

All 245 source-compatible labelled pairs are now classified:

\[
\begin{array}{c|r|l}
\text{class}&\text{count}&\text{result}\\ \hline
G\text{-containing}&25&t=0\\
\text{same-cut proper}&10&t=0\\
\text{shared-cut proper}&105&\text{unit resultant}\\
\text{disjoint-cut proper}&35&\text{unit staged resultant}\\
\text{shared one-cut/proper}&40&\text{existing }A,A^c\text{ thresholds}\\
\text{disjoint one-cut/proper}&30&\text{unit resultant}
\end{array}
\]

Therefore

\[
\boxed{
\text{the asymmetric five-site family has no anomalous two-wall Landau
component beyond existing one-wall, total-energy, and soft support.}
}
\]

This is a closure theorem for source-compatible pairs only. It does not yet
classify triples or higher active sets on the corrected asymmetric slice.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_shared_mixed_pairs.rs`
- `research/benincasa/results/five-site-asymmetric-shared-mixed-pairs.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_disjoint_mixed_pairs.rs`
- `research/benincasa/results/five-site-asymmetric-disjoint-mixed-pairs.json`

## Next falsifier

Regenerate the source-compatible triple census without cyclic quotienting.
Classify every triple by its pair subobjects. Only triples containing neither
a unit pair nor a forced existing-support pair require a new simultaneous
three-wall elimination.
