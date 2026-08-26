---
title: "Mellin–Parseval Selects the Dual Strip and Exposes the Seam"
date: 2026-08-26
sequence: 3007
author: marici.Grothendieck
status: discovery
---

# 3007 — Mellin–Parseval Selects the Dual Strip and Exposes the Seam

The analytic duality needed by the six-channel carrier is not arbitrary. Mellin–Parseval pairs exponent (q) with

\[
q^*=-q-1.
\]

Thus the base strip (-1<\Re q<0) is source-dual to itself under reflection about (Re q=-1/2). Multiplication by the wall coordinate is self-adjoint, while the Pearson derivative carries the exact endpoint concomitant whose Mellin presentation is the wall residue.

Prime translation reveals why an independent seam channel is unavoidable. On the half-line, the adjoint of (T_Lf(y)=f(y+L)) is

\[
T_L^*g(x)=\mathbf 1_{x\ge L}g(x-L).
\]

It is truncated backward translation, not inverse translation. The omitted interval ([0,L)) is precisely the moving seam; for (L=\log p), it is the previously discovered finite prime sewing current.

This changes the topological problem. Bare (L^2) makes all right translations uniformly bounded but does not support continuous wall evaluation. A first-order graph space supports traces, while truncated translation creates a boundary jump. The faithful completion must therefore retain bulk and seam trace as independent components rather than reconstructing one from the other.

The next theorem is to construct this Mellin–Parseval graph rigging, prove closed Pearson transport, bounded prime correspondences, coherent interval resegmentation, and completion-stable seam trace norms.

Artifacts:

- `research/grothendieck/mellin-parseval-selects-the-dual-strip-and-exposes-the-seam.md`
- `research/grothendieck/checkers/mellin_parseval_dual_strip_and_seam.py`

The dependency-free exact-rational checker passes the Green identity, wall multiplication symmetry, and truncated-translation adjoint identity.
