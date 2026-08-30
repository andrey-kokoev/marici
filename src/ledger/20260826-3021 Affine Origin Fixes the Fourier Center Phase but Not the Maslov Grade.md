---
title: "Affine Origin Fixes the Fourier Center Phase but Not the Maslov Grade"
date: 2026-08-26
sequence: 3021
author: marici.Grothendieck
status: discovery
---

# 3021 — Affine Origin Fixes the Fourier Center Phase but Not the Maslov Grade

The affine origin forced by Weyl and Clark covariance also resolves the previously untyped center phase of the Fourier two-by-two minor.

For phase-space area (\mathcal A=(\xi_2-\xi_1)(q_2-q_1)) and center phase (\mathcal C=(\xi_1+\xi_2)(q_1+q_2)/2), the centered minor is

\[
\widetilde\Delta=ie^{i\mathcal C}\Delta
=2\sin(\mathcal A/2).
\]

Common position and frequency translations change the raw phase and center phase by compensating amounts. Hence the centered minor is invariant once the affine chart origin is retained.

Its sign still flips whenever (\mathcal A) crosses (2\pi n). The remaining orientation datum is the integer Maslov crossing grade (m=\lfloor\mathcal A/(2\pi)\rfloor). Reciprocal Gram squaring erases this grade.

High spectral frequency forces arbitrarily many crossings. A viable global theorem therefore cannot require every Fourier minor to remain positive. It must transport the accumulated crossing grade into the primitive, square, seam, and archimedean boundary currents and prove cutoff-path coherence.

This removes a genuine gauge ambiguity but does not orient the de Branges/Krein integral.

Artifacts:

- `research/grothendieck/the-affine-origin-fixes-the-fourier-center-phase-but-not-the-maslov-grade.md`
- `research/grothendieck/checkers/affine_origin_centers_fourier_minor.py`

The checker verifies centering, translation invariance, and lifted orientation after including the crossing grade.
