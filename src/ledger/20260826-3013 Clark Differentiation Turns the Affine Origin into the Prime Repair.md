---
title: "Clark Differentiation Turns the Affine Origin into the Prime Repair"
date: 2026-08-26
sequence: 3013
author: marici.Grothendieck
status: discovery
---

# 3013 — Clark Differentiation Turns the Affine Origin into the Prime Repair

The Fourier–Laplace transform splits exactly across a cut at (L):

\[
F(z)=B_L(z)+e^{izL}F_L(z).
\]

Applying the Clark operator (C_a=1+ia\partial_z) gives

\[
C_aF=C_aB_L+e^{izL}\left(C_aF_L-aLF_L\right).
\]

Thus the logarithmic correction at (L=\log p) is not an independently chosen sign repair. It is the derivative cocycle of the prime transport phase. On the source side it is the elementary affine identity

\[
(1-a(r+L))f(r+L)=(1-ar)f(r+L)-aLf(r+L).
\]

The same origin typing prevents false Mellin poles. The translated tail must retain the global kernel ((r+L)^q), which is regular at the internal cut because (r+L\ge L>0). All endpoint residues remain in the physical seam containing (y=0). Replacing the global kernel by (r^q) would manufacture a false wall and false residues at (y=L).

Therefore Fourier–Laplace transport, Clark differentiation, and Mellin endpoint residue have no finite typed residual on the affine boundary-bearing cut. The next obstruction is restricted-product continuity of the primitive, square, and archimedean current families over expanding seams.

Artifacts:

- `research/grothendieck/clark-differentiation-turns-the-affine-origin-into-the-prime-repair.md`
- `research/grothendieck/checkers/clark_mellin_affine_cut_cocycle.py`

The dependency-free exact-rational checker passes the affine Clark identity, moment splitting through order six, and additive two-cut cocycle.
