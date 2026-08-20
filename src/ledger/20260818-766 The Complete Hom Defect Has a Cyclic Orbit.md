---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 766 — The Complete Hom Defect Has a Cyclic Orbit

## Frozen inputs

Use Entry 764's independently reduced raw residue connections and cyclic
gauge

\[
D_i=\operatorname{diag}(z_i^{-2},z_i^{-1},z_i,z_i),
\qquad
D_0D_1D_2=1.
\]

Use Entries 762--765's complete Hom data:

\[
e_{\rm Hom}=(1,1,1,0,0,1,1,1,1,1,1,2),
\]

in the ordered twelve-factor lattice

\[
\begin{aligned}
(&u,v,y,1-y,1+y,v-u,y-u^2,y+u^2,\\
&P_6,u-2,v-2,u^2+1),
\end{aligned}
\]

and the infinity target-column shear

\[
(w_0,w_1)=(0,6).
\]

## Transported Gysin frame

Let \(P_i\) be the adapted \(T\oplus E\) frame in chart \(i\).  The chart
filtration must not be independently reset after each occurrence move.
Instead define it recursively by

\[
\boxed{P_{i+1}=P_iD_i.}
\]

Since the raw frames obey \(e_i=D_i e_{i+1}\), the adapted transition is

\[
P_iD_iP_{i+1}^{-1}=1.
\]

Exact tests at 24 generic points give zero adapted-transition failures and
zero threefold frame failures.  Thus in the transported adapted frame,

\[
A_{T,i+1}=A_{T,i},\qquad
A_{E,i+1}=A_{E,i},\qquad
C_{i+1}=C_i.
\]

Equivalently, in arbitrary block gauges the cocycle transforms by

\[
C_{i+1}=S_{E,i}^{-1}C_iS_{T,i}.
\]

## Complete pole lattice

The twelve factors are transported by chartwise pullback under the cyclic
base map.  Their exponent vector is retained positionally; the factors are
not identified with the same fixed polynomials in every normalized chart.

Their degrees are

\[
(1,1,1,1,1,1,2,2,4,1,1,2),
\]

so the complete denominator degree remains \(18\).  The labelled factor
family and all twelve valuations return after three transports.  The exact
audit gives zero threefold pole-lattice failures at 24 generic points.

## Rank-one defect orbit

Transporting the complete filtered splitting complex carries both its
coefficient matrix and augmented cocycle column by an invertible chain
isomorphism.  Therefore Entry 763's one-dimensional augmented-rank cokernel
has a canonical occurrence orbit:

\[
\boxed{
[C_{12}]\longmapsto[C_{23}]\longmapsto[C_{31}]
\longmapsto[C_{12}].
}
\]

In the recursively transported frame the three representatives are
literally identical.  No solver section or fitted projector is used.

This is covariance of the filtered rank-one defect.  It does not upgrade
Entry 763 to absolute rational nonsplitting; Entry 765's degree-thirty test
and local pole stabilization remain separate obligations.

## Infinity shear

The degree-six shear is a filtration on the transported (T)-lattice, not a
fixed pair of ordinary-coordinate column degrees in every chart.  Its rule is

\[
\boxed{
\mathcal F_{i+1}=D_i^{-1}\mathcal F_i
}
\]

in raw residue coordinates, or simply \((0,6)\) in the recursively
transported adapted frame.  After three steps,

\[
\mathcal F_3=(D_0D_1D_2)^{-1}\mathcal F_0=\mathcal F_0.
\]

Thus the degree-six shear is occurrence-covariant but is not a
fixed-\(G_{12}\) filtration imposed separately on the other charts.

## Evidence

- `research/benincasa/check_cyclic_hom_defect_transport.py`;
- `research/benincasa/cyclic-hom-defect-transport.json`;
- Entries 762--765;
- allocator claim `seqclaim-f6d5cc02de21eef39d37f49c`.
- epistemic event
  `ev-000000000380-a169898d-b5e4-4fb3-8c25-5d5947e1ed5d`.

## Next falsifier

Repeat Entry 765's certified degree-thirty rank tests in one transported
chart and verify the four resonant graded pieces (15,17,28,30) are carried
isomorphically around the cyclic orbit.  Then determine local pole-order
stabilization along one representative of each cyclic divisor orbit.
