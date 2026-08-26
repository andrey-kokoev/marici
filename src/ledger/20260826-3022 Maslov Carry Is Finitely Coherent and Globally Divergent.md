---
title: "Maslov Carry Is Finitely Coherent and Globally Divergent"
date: 2026-08-26
sequence: 3022
author: marici.Grothendieck
status: discovery
---

# 3022 — Maslov Carry Is Finitely Coherent and Globally Divergent

Write phase-space area in (2\pi) units as (m+\theta), where (m\) is an integer and (0\le\theta<1). Composition is ordinary addition with carry:

\[
(m,\theta)\star(n,\phi)
=
\left(m+n+\lfloor\theta+\phi\rfloor,
\theta+\phi-\lfloor\theta+\phi\rfloor\right).
\]

This law is associative and commutative. Hence finite prime reorderings cannot produce a Maslov braid anomaly when every comparison cell is retained.

If position and frequency directions are both refined, the cross rectangles are mandatory. Omitting them can falsely create path dependence.

At expanding cutoff, the integer grade generally grows linearly with total phase-space area and diverges. Thus the completed object cannot be an absolute integer grade. It must be a source-derived relative grade, finite part, spectral-flow endpoint difference, or projective phase with the divergent integer exported as boundary data.

The universal carry law contains no arithmetic information and cannot orient the RH Krein form by itself. The next calculation must compare actual labelled theta grades in the reciprocal sectors and identify a named current that cancels their shared divergence.

Artifacts:

- `research/grothendieck/the-maslov-carry-is-finitely-coherent-and-globally-divergent.md`
- `research/grothendieck/checkers/maslov_carry_cocycle.py`

The dependency-free checker verifies the carry law and cross-area requirement exactly.
