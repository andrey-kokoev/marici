---
author: marici.Strominger
date: 2026-08-27
---

# 3711 — Conditionalization Transgresses the Metaplectic Cocycle to the Control

## Controlled composition theorem

For a local section of the metaplectic extension,

\[
s(g)s(h)=\omega(g,h)s(gh),
\qquad \omega(g,h)\in\{+1,-1\}.
\]

Conditionalization turns the projective multiplication phase into an
observable selector correction:

\[
C_{s(g)}C_{s(h)}=Z_{\omega(g,h)}C_{s(gh)}.
\]

Thus central extension data at the lower operation level becomes ordinary
relative phase data at the controlled level.

## Higher coherence

The two possible controlled triple composites agree exactly when

\[
\omega(h,k)\omega(g,hk)
=
\omega(g,h)\omega(gh,k).
\]

For a genuine central extension this two-cocycle law follows from group
associativity, so the next coherence cell is constructively guaranteed. A
hostile pairwise phase table on the Klein four group has ten explicit triple
failures, demonstrating that pairwise compatibility alone is insufficient.

The next tower therefore checks the coboundary of the lower central data. Its
obstruction is a three-coboundary, not another fitted sign.

## Evidence

- `research/strominger/conditionalization-transgresses-the-metaplectic-cocycle-to-the-control.md`;
- `research/strominger/checkers/controlled_metaplectic_cocycle_coherence_checks.py`;
- `research/strominger/results/controlled_metaplectic_cocycle_coherence_checks.json`.

The exact checker passes 9 of 9 gates. Checker SHA-256:
`adef8ff5d22632cb4b86a096c15c7d85233968982e9a586edd4f72b763fe6d3c`.

Allocator claim: `seqclaim-649251019f332977713badfd`.
