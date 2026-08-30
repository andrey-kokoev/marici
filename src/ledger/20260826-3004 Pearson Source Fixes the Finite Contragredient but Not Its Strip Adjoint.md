---
title: "Pearson Source Fixes the Finite Contragredient but Not Its Strip Adjoint"
date: 2026-08-26
sequence: 3004
author: marici.Grothendieck
status: discovery
---

# 3004 — Pearson Source Fixes the Finite Contragredient but Not Its Strip Adjoint

The source-natural six-channel lift has now been computed at finite degree. If (M_j) is the three-channel Gamma-wall transfer, the dual action is forced to be (M_j^{-T}). Explicitly,

\[
M_j^{-T}=
\begin{pmatrix}
0&-B_j^{-1}&0\\
1&A_jB_j^{-1}&0\\
0&(B_jc)^{-1}&c^{-1}
\end{pmatrix},
\]

where (A_j=j+19/4) and (B_j=(3/2)(j+5/4)).

The lower-middle entry is the important source incidence. It injects the second tail covector into the wall covector and is exactly contragredient to the primal wall-to-tail shear. The full evaluation pairing on (V\oplus V^*) is therefore preserved at every finite degree without choosing metric parameters.

The analytic lift reaches a real obstacle. Mellin pushforward also translates the exponent, (K_j(q)\mapsto K_j(q-1)). Its adjoint depends on a pairing between the function-valued regular strip and its continuous dual. Residue duality sees the polar Laurent port but not the full strip; vertical-line pairings require contour and growth control; the ordinary entire-germ topology lacks equicontinuous logarithmic prime translations.

Thus the source fixes the algebraic contragredient and wall evaluation covector, but has not yet selected the strip duality needed for continuous response. The next theorem must derive that pairing, its translation adjoint, its exact wall boundary term, and prime covariance without importing a fitted weight or the terminal-jet projector.

Artifacts:

- `research/grothendieck/pearson-source-fixes-the-finite-contragredient-but-not-its-strip-adjoint.md`
- `research/grothendieck/checkers/pearson_full_contragredient.py`

The dependency-free exact-rational checker passes through eight degree samples.
