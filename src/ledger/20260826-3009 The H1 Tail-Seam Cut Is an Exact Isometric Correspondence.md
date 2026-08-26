---
title: "The H1 Tail–Seam Cut Is an Exact Isometric Correspondence"
date: 2026-08-26
sequence: 3009
author: marici.Grothendieck
status: discovery
---

# 3009 — The H1 Tail–Seam Cut Is an Exact Isometric Correspondence

The boundary-bearing completion suggested by Mellin–Parseval has an exact realization. For (f\in H^1(0,\infty)), define

\[
C_Lf=\left(f(\,\cdot+L),f|_{[0,L]}\right).
\]

Splitting the integrals of (|f|^2) and (|f'|^2) at (L) proves

\[
\|f\|_{H^1(0,\infty)}^2
=
\|f(\,\cdot+L)\|_{H^1(0,\infty)}^2
+
\|f|_{[0,L]}\|_{H^1(0,L)}^2.
\]

The image is the closed incidence subspace where the terminal seam trace equals the initial translated-tail trace. Successive cuts concatenate their seam intervals canonically, so prime resegmentation coherence is simply associativity of interval cutting.

At infinite cutoff, translated-tail energy tends to zero while expanding-seam energy tends to the full source norm. No state or energy disappears. This repairs the earlier completion witness without reconstructing the seam from the tail or fitting a new weight.

The theorem closes completion stability for the translation skeleton, not yet for the full theta/Pearson system. The next calculation is the commutator between this cut correspondence and the Pearson/Clark differential operator. A pure interface distribution is expected; any bulk residual is a genuine obstruction.

Artifacts:

- `research/grothendieck/the-h1-tail-seam-cut-is-an-exact-isometric-correspondence.md`
- `research/grothendieck/checkers/h1_tail_seam_cut_isometry.py`

The dependency-free exact-rational checker passes one-cut energy, two-cut energy, seam concatenation, and interface matching.
