---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Occurrence Chart Does Not Land in the Entry143 Cech Promotion

## Question

Entry 530 identifies the geometric mixed-support cell with

\[
\left[\frac1{x_3u_3}\right]
\]

and its two chart faces with (1/x_3) and (1/u_3).  Test whether all
three terms land in the canonical target-side Entry-143 Koszul--Čech
promotion.

## Target variance

The proved target promotion has differential coefficients

\[
\epsilon\frac{X_a}{u_a}
\]

and localization factor

\[
\lambda(S,H)=\prod_{a\in S\setminus H}u_a^{-1}.
\]

Thus normal-circle inverses are legal only in their prescribed Čech
summands.  The occurrence layer remains polynomial in every (X_a); no
occurrence inverse (X_a^{-1}) is introduced.

For the (D03) mixed pair this gives:

| source term | target status |
|---|---|
| (1/u_3) | legal normal Čech term |
| (1/x_3) | absent occurrence-reciprocal term |
| (1/(x_3u_3)) | absent because its occurrence-reciprocal factor is absent |

## Divisibility theorem

The Koszul--Čech comparison sends a middle coefficient (b) to (b/x_3)
on the occurrence chart.  A map into the polynomial Entry-143 occurrence
layer can exist only when

\[
x_3\mid b.
\]

Consequently the primitive choice (b=1) cannot land.  The smallest legal
choice is (b=x_3), whose occurrence-chart value is (1) and whose
restriction to the conductor is zero.

Hence

\[
\boxed{
\text{the mixed-support fundamental class has no primitive map into the
current Entry-143 Čech target.}
}
\]

This recovers Entry 177's smallest solution (k=x_3) from the geometry of
the two blowup charts.  The previous incidence divisibility obstruction was
not an artifact of truncating the source; it is the failure of the
occurrence-reciprocal chart to land in the target variance.

## What would repair the type

The missing datum is not another Čech localization and not a new free cell.
It is the extraordinary occurrence Thom line

\[
(x_3)^\vee
\]

with evaluation

\[
(x_3)^\vee\otimes(x_3)\longrightarrow A.
\]

Such a line may arise from an occurrence-supported Gysin or relative
dualizing functor.  It is not contained in the established polynomial
Entry-143 target.  Adjoining (x_3^{-1}) as an ordinary scalar would erase
the conductor support and is prohibited.

## Consequence for the Beck--Chevalley class

The mixed-ideal blowup and supported Čech source determine the candidate
homotopy class, but the current target cannot receive its occurrence-chart
face.  Therefore the physical obstruction

\[
\operatorname{ob}_{03}(k,b)
\]

remains untyped rather than nonzero or zero.  It can be tested only after a
variance-correct occurrence-supported Thom/Gysin enlargement is derived.

## Evidence

- Entry 177: (x_3\mid k) and smallest solution (k=x_3);
- Entry 530: canonical Koszul--Čech comparison;
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: normal-only
  reciprocal target promotion with polynomial occurrence layer;
- `research/voevodsky/check_d03_compatible_face_bm_cech_primitive_obstruction.rs`:
  failure of the primitive in legal Entry-143 BM--Čech summands.
