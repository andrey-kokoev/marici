---
id: 449
date: 2026-08-17
title: Naive Fiber Multiplication Does Not Descend to the Soft Resonance
---

# Naive Fiber Multiplication Does Not Descend to the Soft Resonance

Benincasa Entry 443 canonically identifies a tested length-two vector-space
cokernel
\[
T=(a^4)/\operatorname{im}d_{\rm ex}.
\]
Before asking for its annihilator or Fitting ideal, one must verify that the
ordinary fibre-coordinate multiplications preserve the exact image.

Reconstructing the complete frozen differential from
\(K=a^4\), \(L_1=b+1\), and \(L_2=a\), and dividing its image by the common
factor \(a^4\), gives a two-dimensional cokernel at every tested cutoff
\(D=12,16,20,24,28\). However, multiplication by either \(a\) or \(b\) fails
to preserve the factored exact image. Each multiplication adds a rank-one
direction modulo the image at every tested cutoff.

Thus \(T\) is not presently an \(\mathbf F[a,b]\)-module under naive
multiplication. This is expected for a differential image: multiplication by
an integration variable need not commute with the exact-form differential.
Consequently an annihilator, Fitting ideal, or multiplication matrix for the
two greedy representatives would be ill-typed without first constructing
chain-level corrected operators and their homotopies.

This sharpens rather than weakens Entry 443. Its length-two filtered
resonance is intrinsic as a cokernel dimension, but its coefficient-module
structure is additional Gauss--Manin/de Rham data. The next gate is to derive
homotopy-corrected \(a\)- and \(b\)-operators from the full relative complex,
then ask whether they preserve a two-dimensional subquotient and how the
first-normal soft operator extends it.

The calculation is over the same large finite field and tested cutoff range;
it is not an all-degree characteristic-zero theorem.

The executable audit is
research/voevodsky/check_soft_axis_resonance_multiplication_defect.py.
