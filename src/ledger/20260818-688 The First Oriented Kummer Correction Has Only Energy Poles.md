---
authors:
  - marici.Nima
date: 2026-08-18
---
# 688 — The First Oriented Kummer Correction Has Only Energy Poles

## Question

Entry 686 constructs the special-fiber oriented pairing, while Entry 687
correctly distinguishes that nearby-grade map from the still-uncomputed
localization connecting class. Before constructing the full triangle, test
whether the source residue itself acquires a quartic divisor at first order
away from total energy.

## Root-free calculation

Write the reduced (g_3) tangency equation as

\[
h_3(t)=At^2+Bt+C,
\qquad
\Delta=B^2-4AC,
\]

after substituting (z=E-x-y). For its two roots (r_\pm), use

\[
h_3'(r_\pm)=\pm\sqrt\Delta
\]

and compute the symmetric trace

\[
\frac1{D_3(r_+)}+\frac1{D_3(r_-)}
\]

by exact quadratic reduction. This eliminates the sheet roots before any
series expansion. Since (N_3=-E) and (E=q^2), the oriented normalized
difference is

\[
q(\rho_+-\rho_-)
=
\frac{R(E)}{\sqrt{\Delta/E}}.
\]

## First horizontal coefficient

Expanding relative to its nonzero leading value gives

\[
q(\rho_+-\rho_-)
=F_0\left[
1+E\,
\frac{4x^2+19xy+4y^2}{4xy(x+y)}
+O(E^2)
\right].
\]

Thus the first horizontal correction has poles only on

\[
x=0,
\qquad y=0,
\qquad x+y=0,
\]

the already established soft and total-energy boundary arrangement.
It has no pole on the algebraic quartic:

\[
\boxed{
v_{\mathcal Q}\!\left(
\frac{4x^2+19xy+4y^2}{4xy(x+y)}
\right)\ge0.
}
\]

## Scope

This is the first variation of the canonical oriented local scalar pairing.
It is not yet the connecting morphism

\[
\mathcal K_{\rm phys}\longrightarrow\psi_E\mathcal T_7[1].
\]

Accordingly, absence of a quartic pole here does not settle the supported
extension class. It does show that such a pole cannot be attributed to the
first variation of the physical residue coefficient itself; it would have
to enter through the chain-level localization boundary or its comparison
with the algebraic kernel.

## Evidence

- `research/benincasa/check_oriented_kummer_first_horizontal_coefficient.py`;
- `research/benincasa/oriented-kummer-first-horizontal.json`;
- Entries 683–687;
- allocator claim `seqclaim-98181e58f545a9eda3b55731`.

## Next falsifier

Build the two-term local localization cone with its oriented boundary map.
Separate the already computed scalar variation from the boundary-map
variation, and test the latter for \(\mathcal Q\)-valuation.
