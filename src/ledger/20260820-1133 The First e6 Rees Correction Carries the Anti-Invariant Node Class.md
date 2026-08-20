---
title: "The First e6 Rees Correction Carries the Anti-Invariant Node Class"
date: 2026-08-20
entry: 1133
status: established-higher-rees
sector: cosmology
---

# 1133 — The First \(e_6\) Rees Correction Carries the Anti-Invariant Node Class

Sequence claim: `seqclaim-8e039f71ec27a429fb059c49`.

## Calculation

Write the complete source expansions

\[
K=p^2(F+pG+O(p^2)),\qquad
K_1=p(J+pH+O(p^2)),
\]

where \(F=4T^2\) and \(J=-16T\). Expanding

\[
e_6=-\frac{K_1}{2}\frac{dA\wedge dB}{K^{3/2}}
\]

through first Rees order gives, on the sheet \(W=+2T\), a possible
cohomology class equal to the \(T^{-1}\) coefficient

\[
\frac1{32}[T^2]H+\frac3{16}[T^3]G,
\]

after substituting \(A=(3-s-T)/2\).

Exact Symbolica reduction gives

\[
[T^2]H=2,\qquad [T^3]G=-1,
\]

and therefore

\[
\boxed{\operatorname{Res}_{T=0}^{(+)}\operatorname{gr}_1(e_6)=-\frac18.}
\]

The opposite sheet reverses the odd square-root powers and gives \(+1/8\).
Hence

\[
\boxed{
\operatorname{Sp}^{(1)}(e_6)
=-\frac18(e_+-e_-).
}
\]

## Meaning

Entry 1132 remains essential: the ordinary leading grade is exact. The
node class appears only at first higher Rees order. This is precisely the
distinction required by the cosmology continuation note:

\[
\text{leading ordinary grade}
\not\Rightarrow
\text{higher normal coefficient class}.
\]

The class is anti-invariant and lives on the existing normalized nodal
coefficient geometry. It requires no new carrier stratum. The moving
conductor support remains \(s(B-1)=0\).

This result does not reinstate Entry 1127's inferred map. It directly
computes the higher-Rees class of \(e_6\); comparison with the physical node
must now be formed at this grade with the supported boundary included.

## Evidence and next falsifier

- `research/benincasa/marici-gm/src/bin/rank12_u2v0_e6_first_rees_residue.rs`;
- `research/benincasa/results/rank12-u2v0-e6-first-rees-residue.json`;
- Entry 1099's complete \(K,K_1\) expansion;
- Entries 1131--1132.

Next compute the supported pairing of

\[
\partial\gamma_{CM}=e_- - e_+
\]

with \(\operatorname{Sp}^{(1)}(e_6)\), retaining the integral sheet pairing
and the conductor faces \(s=0\), \(B-1=0\). Only then may an integral or
physical normalization be stated.

