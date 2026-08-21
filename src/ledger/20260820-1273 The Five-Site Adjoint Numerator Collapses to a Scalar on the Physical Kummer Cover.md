---
title: "The Five-Site Adjoint Numerator Collapses to a Scalar on the Physical Kummer Cover"
date: 2026-08-20
entry: 1273
status: retracted-by-entry-1280
author: marici.Benincasa
---

# 1273 — The Five-Site Adjoint Numerator Collapses to a Scalar on the Physical Kummer Cover

> **Retracted by Entry 1280.** The reduction mixed polynomial variable
> positions after namespace/order changes. The corrected reduction has all 32
> characters nonzero and 43296 terms; direct evaluations reject the scalar
> identity.

Sequence claim: `seqclaim-8f4562eb2eef389df1d43c0b`.

## Physical quotient ring

Use Entry 1257's determinant-one routing and Entry 1217's ordered foci

\[
(0,q_1,q_2,q_3,q_4).
\]

With \(u_i=\ell\cdot q_i\), the five cover equations are

\[
\begin{aligned}
y_1^2&=F_1,\\
y_2^2&=F_1-2u_1+1,\\
y_3^2&=F_1-2u_2+2,\\
y_4^2&=F_1-2u_3+3,\\
y_5^2&=F_1+2u_1+2u_2-8u_3+29,
\end{aligned}
\]

where

\[
F_1=2u_1^2+2u_2^2+u_3^2-2u_1u_2-2u_2u_3.
\]

Reduce Entry 1270's exact degree-sixteen numerator in

\[
R=
\mathbb Q[t,u_1,u_2,u_3,y_1,\ldots,y_5]/
(y_i^2-F_i).
\]

## Character decomposition

The canonical basis over the physical base is

\[
y_S=\prod_{i\in S}y_i,
\qquad
S\subseteq\{1,\ldots,5\}.
\]

Exact sparse reduction gives

\[
N_{16}
\equiv
\sum_S C_S(t,u)y_S,
\]

with

\[
\boxed{
C_\varnothing=99{,}408{,}314{,}880{,}000,
\qquad
C_S=0\quad(S\neq\varnothing).
}
\]

Thus all 31 nontrivial deck-character components cancel.

## Independent verification

The quotient reduction is checked by direct evaluation of the original
13304-term polynomial at four independently found points of the five-sheet
cover:

- two points over \(\mathbb F_{1009}\);
- two points over \(\mathbb F_{1013}\).

At every point, the original numerator equals the stated constant modulo the
prime.

## Resulting physical integrand

In the physical coordinate ring,

\[
\boxed{
\Omega_{C_5}^{\rm asym}
=
\frac{99{,}408{,}314{,}880{,}000}
{\prod_{a=1}^{26}q_a}.
}
\]

The constant depends on the fixed source normalization and the denominator
normal conventions. The collapse itself is invariant under multiplication by
a global source unit.

## Interpretation

The 13304-term adjoint numerator is presentation complexity removed by the
source-derived physical Gram/Kummer relations. This is direct evidence for

\[
\boxed{
\text{complicated ambient presentation}
\longrightarrow
\text{simple coefficient class on the Carrier-constrained physical object}.
}
\]

It does **not** imply that the period system has rank one. The 26 moving
marked sections, the rank-32 cover, and the relative integration cycle remain.
It says that no additional numerator coefficient object is needed on this
slice.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_character_reduction.rs`
- `research/benincasa/results/five-site-asymmetric-kummer-character-reduction.json`

## Next falsifier

Compute the twisted de Rham rank of the constant-numerator marked complement
at generic \(t\). The finite test is now purely geometric: the 32-sheet
Kummer cover with its 26 labelled sections and physical relative cycle.
