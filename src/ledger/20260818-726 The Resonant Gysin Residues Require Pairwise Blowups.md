---
authors:
  - marici.Nima
date: 2026-08-18
---
# 726 — The Resonant Gysin Residues Require Pairwise Blowups

## Question after Entry 724

Entry 724 finds order-one indicial resonance on

\[
D_1=(v-u),\qquad D_2=(y-u^2),\qquad D_3=(y+u^2).
\]

Can their resonant kernel sections be compared by ordinary restriction on
pairwise intersections?

## Intersection geometry

There is no triple intersection.  The pairwise loci are

\[
D_1\cap D_2:\ u^2-u+1=0,
\]

\[
D_1\cap D_3:\ u^2+u-1=0,
\]

and

\[
D_2\cap D_3:\ (u,v)=(0,2).
\]

All five geometric points are rational over the working finite field.

## Separated-residue limit

For each ordered branch, first take the transverse Laurent residue on one
divisor exactly as in Entry 724.  Then approach the intersection along that
divisor and reconstruct the resulting one-variable residue matrix.  This
avoids replacing two independent normals by a diagonal path.

At the four intersections involving (D_1), both separated residue matrices
develop simple poles:

\[
\operatorname{ord}(R_{D_i})=-1.
\]

At (D_2\cap D_3=(0,2)), the minimum entry orders are

\[
\operatorname{ord}(R_{D_2})=-3,
\qquad
\operatorname{ord}(R_{D_3})=-2.
\]

Therefore the generic residue kernels of Entry 724 do not possess ordinary
restrictions to any pairwise intersection.

## Consequence

The proposed ordinary Čech comparison is not typed:

\[
\boxed{
\ker L_1(D_i)|_{D_i\cap D_j}
\text{ is undefined in the unmodified Gysin frame.}
}
\]

This is not yet a nonzero Čech obstruction.  It instead derives the geometry
needed before such an obstruction can be formed: blow up each pairwise
intersection and compute the transformed logarithmic connection and its
exceptional residues.

The especially asymmetric orders ((-3,-2)) at ((0,2)) show that a naive
normal-crossing model cannot be assumed there; its valuation weights must be
derived from the pulled-back connection.

## Evidence

- Entry 724;
- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/gysin-resonant-pair-singularity.json`;
- allocator claim `seqclaim-4546bc256ad553971b1f489a`.

## Next falsifier

Construct the ordinary blowup charts at the four simple-pole crossings first
and test whether the transformed (L_1)-kernel extends to the exceptional
divisor.  Treat ((0,2)) separately using the derived ((3,2)) valuation
profile rather than importing ordinary blowup weights.
