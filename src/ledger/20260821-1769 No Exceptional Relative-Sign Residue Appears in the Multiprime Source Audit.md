---
title: "No Exceptional Relative-Sign Residue Appears in the Multiprime Source Audit"
entry: 1769
date: 2026-08-21
status: supported-multiprime
---

# 1769 — No Exceptional Relative-Sign Residue Appears in the Multiprime Source Audit

## Question

Entry 1767 identifies one admissible relative-sign Hom slot over each of the
existing intersections

\[
P_6\cap D,
\qquad
P_6\cap H.
\]

Entry 1768 shows why ordinary specialization on the wall cannot test its
occupancy.  Does the canonical off-wall source connection develop a
logarithmic coefficient when approached along a transverse arc?

## Algebraic branches

Exact elimination gives

\[
\operatorname{Res}_v(P_6,D)
=u^4(u-1)^2(1-8u+12u^2-4u^3),
\]

\[
\operatorname{Res}_v(P_6,H)
=u^3(-2+2u+2u^2-u^3).
\]

The repeated rational (D)-point ((1,1)) is excluded.  Over each split
prime the checker chooses a point on the remaining cubic factor, verifies a
nonzero Jacobian for ((P_6,D)) or ((P_6,H)), and checks that the arc

\[
u=u_0+s,
\qquad
v=v_0+2s
\]

is normal to both incident divisors.

## Source reconstruction

For (D), use the labelled wall-1 source column.  For (H), use wall 2.
At every off-wall sample:

1. solve the complete 132-equation reduction;
2. require rank (117) and fixed mask (3847);
3. project the fixed final four-vector to
   (mathcal L_{P_6^{-1/2}});
4. contract (B_u,du+B_v,dv) with the arc tangent;
5. reconstruct the one-variable rational function from 48 samples;
6. verify it on 24 unused samples.

The test was repeated over

\[
2305843009213693951,
\qquad
2305843009213693723.
\]

## Result

The (D)-branch reconstructions have degree profile

\[
(\deg N,\deg D)=(6,7),
\]

and the (H)-branch profiles are

\[
(6,8).
\]

All four have

\[
\operatorname{ord}_sN=0,
\qquad
\operatorname{ord}_sD=0.
\]

Therefore

\[
\boxed{
\operatorname{ord}_s B_{\rm rel}=0,
}

not (-1), in every tested transverse branch.  No exceptional logarithmic
residue occupies Entry 1767's relative-sign slot.

## Scope

This is strong source-derived multiprime evidence, but not yet an exact
characteristic-zero vanishing theorem.  The intersection cubics may have
additional conjugate branches, and no exact resultant-module identity has
yet proved divisibility of the residue numerator over (mathbb Q).

The remaining finite certification is now small: compute the residue
numerator modulo each cubic resultant and prove that both remainders vanish
identically.  Until then the supported relative-sign route is disfavored,
not formally closed.

## Durable artifacts

- exact resultant checker:
  `research/benincasa/checkers/p6_wall_resultants.py`;
- resultant packet:
  `research/benincasa/results/p6-wall-resultants.json`;
- checker: `research/benincasa/marici-gm/src/bin/p6_d_exceptional_source_residue.rs`;
- (D)-branch packets:
  `research/benincasa/results/p6-d-exceptional-source-residue-p1.json`,
  `research/benincasa/results/p6-d-exceptional-source-residue-p3.json`;
- (H)-branch packets:
  `research/benincasa/results/p6-h-exceptional-source-residue-p1.json`,
  `research/benincasa/results/p6-h-exceptional-source-residue-p3.json`;
- convention note:
  `research/benincasa/p6-wall-exceptional-source-residue.md`;
- allocator claim: `seqclaim-c10b2e60217043c4624058d0`.
