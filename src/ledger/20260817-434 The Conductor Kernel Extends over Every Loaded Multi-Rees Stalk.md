---
id: 434
date: 2026-08-17
title: The Conductor Kernel Extends over Every Loaded Multi-Rees Stalk
---

# The Conductor Kernel Extends over Every Loaded Multi-Rees Stalk

Entry 433 constructed the universal normalization–conductor kernel. It now
instantiates on the complete occurrence/multi-Rees coefficient diagram.

For a loaded PC cell \((S,H)\), let \(L=S\setminus H\) and
\[
B_L=R[X,u][u_a^{-1}:a\in L].
\]
The standard labelled SNC normalization chart over this base is
\[
A_{+,L}=B_L[z_+],\qquad
A_{-,L}=B_L[z_-],\qquad
C_L=B_L,
\]
with conductor restrictions given by \(z_+=0\) and \(z_-=0\). Define
\[
\mathcal K_L=
\left[
B_L[z_+]\oplus B_L[z_-]
\xrightarrow{\epsilon_+-\epsilon_-}
B_L
\right].
\]
The difference row is primitive and split surjective at every stalk, so its
degree-zero kernel is the node algebra
\(B_L[z_+,z_-]/(z_+z_-)\), with no higher homology or integral torsion.

Every one of the 522 PC covering incidences is a localization
\(B_L\to B_{L\cup\{a\}}\). Polynomial extension in \(z_\pm\), evaluation at
zero, and the sheet difference commute with this localization. The executable
audit tests constants, positive monomials, branch-positive monomials killed by
evaluation, and the newly admitted inverse \(u_a^{-1}\) on every square.

All 840 composable two-step routes were also checked. Their endpoint
localization set is independent of the route, so the conductor kernels form a
strict complex of bimodules over the entire 215-cell fs monoidal diagram.

The three rotated charts carry the normalized logarithmic trace of Entry 429,
which fixes their branch transition unit to one. In exponent notation the
resulting unit cocycle is zero. The full augmented-simplex overlap nerve of
Entry 431 has vanishing integral \(H^1\), so no branch-line twist survives
Čech descent.

Thus the universal kernel is now instantiated on all actual loaded
occurrence/multi-Rees stalks and descends globally. What remains is not another
ring choice: it is to package these stalkwise complexes as the global
mixed-variance integral transform from the normalization–conductor source to
the PC target, and verify that applying it to the distinguished sheet object
reproduces the already unique framed connector.

The executable audit is
`research/voevodsky/check_multirees_conductor_stalk_kernel.py`.
