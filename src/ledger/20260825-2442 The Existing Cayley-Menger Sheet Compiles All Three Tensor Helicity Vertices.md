---
author: marici.Benincasa
date: 2026-08-25
---

# 2442 — The Existing Cayley--Menger Sheet Compiles All Three Tensor Helicity Vertices

## Question

Entries 2440--2441 derive a faithful local helicity pair and its scalar time
seed. Does inserting that pair into the three-site loop require new angular
Carrier coordinates, or can it be reconstructed from the frozen labelled
distance geometry?

## Labelled tetrahedral geometry

Use

\[
(c,a,b)=(y_{12},y_{23},y_{31}).
\]

The three base edges are labelled by the external momentum magnitudes:

\[
P_1:y_{12}\leftrightarrow y_{31},
\qquad
P_2:y_{23}\leftrightarrow y_{12},
\qquad
P_3:y_{31}\leftrightarrow y_{23}.
\]

This is exactly the source Cayley--Menger tetrahedron: the loop momentum is
the apex and the external momentum triangle is its base.

For site 1, place the $P_1$ edge on the $x$ axis and the external triangle in
the $(x,y)$ plane. Write the apex as $(x,Y,Z)$. Trilateration gives

\[
x=\frac{c^2+P_1^2-b^2}{2P_1},
\]

and determines $Y^2$ rationally from $(a,b,c;P_1,P_2,P_3)$. The remaining
normal coordinate satisfies

\[
\boxed{
Z^2=\frac{K_{\rm CM}}
{\Lambda(P_1,P_2,P_3)}.
}
\]

Here the source normalization is $D_{\rm CM}=-2K_{\rm CM}$ and

\[
\Lambda
=(P_1-P_2-P_3)(P_1-P_2+P_3)
(P_1+P_2-P_3)(P_1+P_2+P_3).
\]

The identity follows exactly from

\[
\det G_{(P_1,P_2,\ell)}=-\frac14K_{\rm CM}.
\]

The other two sites follow by the labelled cyclic action.

## Helicity compilation

At site $i$, the transverse part of the source momentum difference is twice
the apex displacement $(Y_i,Z_i)$. After Entry 2441's time-weight
cancellation, the two tensor coefficients are therefore

\[
\boxed{
H_i^+=(Y_i+iZ_i)^2,
\qquad
H_i^-=(Y_i-iZ_i)^2.
}
\]

The deck involution $Z_i\mapsto-Z_i$ exchanges the two labelled helicities.
Thus the tensor numerator uses:

- the already frozen external Gram orientation;
- the existing $K_{\rm CM}^{1/2}$ coefficient sheet;
- the labelled occurrence ordering.

It introduces no additional angular incidence coordinate.

## Faithfulness and rank loss

For each site, the real quadrupole coordinates

\[
(Y_i^2-Z_i^2,\;2Y_iZ_i)
\]

map to $(H_i^+,H_i^-)$ with determinant $-2i$. Across all three sites the
block transfer has rank six and determinant

\[
(-2i)^3=8i.
\]

The local quadrupole Jacobian is

\[
4(Y_i^2+Z_i^2)
=-rac{Lambda(P_i,y_{i-1,i},y_{i,i+1})}{P_i^2}.
\]

Hence rank is lost only when the corresponding apex/base face is collinear.
These are existing triangular face Gram divisors. Soft factors $P_i=0$ are
also already frozen support.

## Result

\[
\boxed{
\text{all three occurrence-labelled finite-$q$ tensor vertices are compiled
from the existing Gram and Cayley--Menger coefficient sheets.}
}
\]

This is evidence for H2's shared Carrier plus sector-specific coefficient
objects: spin two uses the scalar carrier's orientation cover without adding
a tensor-specific cell.

## Scope

This is an exact geometric compilation of the local numerator. It does not
yet prove that multiplication by these six coefficients is closed on the
rank-sixty twisted cohomology, nor that the Ward-correlated channel/contact
sum is flat. It also does not identify which tensor ports are accessible to
the physical relative cycle after integration.

## Durable evidence

- `research/benincasa/check_cyclic_tensor_vertex_cm_sheet.py`;
- `research/benincasa/cyclic-tensor-vertex-cm-sheet.json`;
- the frozen generic Cayley--Menger matrix and occurrence ordering;
- Entries 2440--2441;
- sequence claim `seqclaim-f222c34446f41e16a0fe35df`.

## Next falsifier

Reduce multiplication by the six labelled helicity coefficients in the
generic rank-sixty marked-relative quotient. Verify cyclic covariance and
localization compatibility before summing helicities or occurrences. A
failure to close must be classified as a coefficient-module enlargement or
as genuinely new Carrier support.
