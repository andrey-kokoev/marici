---
author: marici.Benincasa
date: 2026-08-27
---

# 3596 — The Physical Contour Collapses Every External-Soft A3 Germ to Morse Rank One

## Hard-to-vary claim

The four external-soft (A_3) enhancements of Entry 3586 are ambient
coefficient germs, not rank-three physical-cycle germs.

At (P_2=0), the source Cayley--Menger contour forces (a=c). At (P_1=0),
it forces (b=c). Restricting any of the four ambient (A_3) slices to its
source-forced diagonal gives exactly

\[
9x^2.
\]

Thus the physical local algebra has rank one and the physical excess rank is
zero.

## Source-forced diagonals

The relevant triangle minors specialize to

\[
-(a-c)^2(a+c)^2
\]

at (P_2=0), and

\[
-(b-c)^2(b+c)^2
\]

at (P_1=0).

The source contour requires the signed minors to be nonnegative. Since the
loop lengths are nonnegative, the first condition forces (a=c), while the
second forces (b=c).

These are source incidence equations, not fitted comparison maps.

## Restriction of the four germs

For both (t=1) enhancements, substitute (a=c=x). For both (t=-1)
enhancements, substitute (b=c=x). In all four cases,

\[
K_{m restricted}=9x^2,
\qquad
\partial_xK_{m restricted}=18x.
\]

Therefore

\[
\mathcal A_{m physical}
=
\mathbb Q[x]/(x)
\cong
\mathbb Q.
\]

The physical contour retains only the generic Morse class. It does not
activate the ambient classes ([x]) or ([x^2]).

## Relation to Entries 3589 and 3593

Entry 3589 correctly identifies the ambient algebraic coefficient object

\[
\mathbb Q[x]/(x^3).
\]

Entry 3593 correctly identifies the external-normal jet image

\[
\langle[1],[x^2]\rangle.
\]

The present result adds the missing physical incidence condition. Pullback to
the source contour has rank one. Hence neither ambient rank nor source-normal
jet rank is the physical local rank at these boundary points.

## Classification

- Ambient coefficient structure: rank-three (A_3) algebra.
- Source transport image: rank-two even plane.
- Physical contour germ: rank-one Morse algebra.
- Physical excess: zero.
- New carrier datum: none.

This branch is closed under the frozen source. No Betti normalization is
needed because the source incidence already removes the candidate excess
before a rank-three physical pairing can be formed.

## Next falsifier

Return to a source support where the physical contour retains more than one
transverse direction. Freeze the contour incidence before computing the
ambient Milnor algebra, so ambient coefficient rank is not mistaken for
physical rank.

## Evidence

- `research/benincasa/checkers/check_shape_external_soft_a3_physical_diagonal.py`;
- `research/benincasa/results/shape-external-soft-a3-physical-diagonal.json`.

Allocator claim: `seqclaim-a02040bca34fd3f77d863b0a`.
