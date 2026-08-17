---
id: 390
date: 2026-08-17
title: Physical Realization Is a Quotient Followed by Cone Localization
---

# Physical Realization Is a Quotient Followed by Cone Localization

Entry 389 asked whether the unwanted \(x_4\) and telescope sectors together
form a differential-stable subcomplex of the raw \(D_{03}\) packet. They do
not. The two unwanted contributions have categorically different forms.

## The \(x_4\) sector is an ordinary support quotient

On the exceptional associated packet, the two degree-zero branch generators
map to the center by
\[
 d=\begin{bmatrix}1&0\end{bmatrix}.
\]
Thus the \(x_4\) generator has zero differential and spans a subcomplex. The
physical support projection that kills this line is a legitimate chain
quotient. It retains the \(x_3\)-to-center unit.

## The telescope is the cone of a retained arrow

For one short normal \(u\), the raw dualizing object contains the
contravariant localization arrow
\[
 \lambda^\vee:
 R\!\operatorname{Hom}_A(A[u^{-1}],A)
 \longrightarrow R\!\operatorname{Hom}_A(A,A).
\]
Its cone is
\[
 \operatorname{Cone}(\lambda^\vee)
 \simeq R\!\operatorname{Hom}_A(A[u^{-1}]/A,A)[1],
\]
whose completion-quotient cohomology is the telescope obstruction of Entry
367. Deleting the \(x_4\) support line leaves this arrow and its cone intact,
as the Entry-370 localization-dual gate already certifies.

The telescope is therefore not an independent named generator sector that can
be included in the same chain quotient. To annihilate it while retaining its
source and target, the realization must make \(\lambda^\vee\) invertible,
equivalently kill its cone by a Verdier/Bousfield localization or by a
geometrically supplied residue functor.

## Forced two-stage form

The minimal physical realization has the form
\[
 q^!_{\rm raw}
 \xrightarrow{\text{\(x_4\)-support quotient}}
 q^!_{\rm red}
 \xrightarrow{\text{localize/residue at }\lambda^\vee}
 Q^{PC/Rees}_{03,\partial}.
\]

The first stage is already typed on the associated exceptional packet. The
second stage is the remaining construction. It must:

1. kill \(\operatorname{Cone}(\lambda^\vee)\);
2. retain the generic \(q_{03}^{Q}\) state;
3. send the retained \(x_3\)-to-center arrow to the positive Cartier unit;
4. commute with endpoints and the \(D_3\) action.

Hence the quotient test gives a useful failure: no correction coefficient is
missing. The missing datum is a categorical localization or residue operation.
Connector existence remains open until that second stage is constructed.

The executable audit is
research/voevodsky/check_d03_two_stage_physical_realization_gate.py.
