---
title: "The Homogenized Five-Site Kummer Localization Is a Graded de Rham Complex"
date: 2026-08-20
entry: 1293
status: active-narrow-result
author: marici.Benincasa
---

# 1293 — The Homogenized Five-Site Kummer Localization Is a Graded de Rham Complex

Sequence claim: `seqclaim-5675783916973b994f353b86`.

## Frozen grading

Use Entry 1291's homogenized variables and assign

[
deg t=deg y_i=deg u_j=degho=1,
qquad
deg(dz)=deg z.
]

The five Kummer relations are

[
y_i^2=F_i(u,ho).
]

The 26 wall equations are exactly those of Entry 1270: the total-energy wall,
the five one-cut total walls, and the twenty proper connected-subgraph walls.

## Exact audit

Every Kummer relation is homogeneous of degree two:

[
oxed{deg(y_i^2-F_i)=2.}
]

Every frozen wall equation is homogeneous of degree one. Explicitly, they have
one of the source-derived forms

[
5t,
qquad
5t+2y_i,
qquad
|A|t+y_i+y_j.
]

Thus

[
oxed{
R=
mathbb Q[t,u,ho,y_1,ldots,y_5]/
(y_i^2-F_i)
}
]

and its 26-wall localization are graded rings.

Entry 1270's numerator has degree sixteen, while the complete denominator has
degree twenty-six. Hence the canonical rational function has degree

[
oxed{degOmega_{C_5}=-10.}
]

With the displayed differential-form grading, the algebraic de Rham
differential has degree zero. Therefore the full localized algebraic de Rham
complex—not only its numerator—is graded.

## Consequence

Entry 1291's relation

[
deg C_S+|S|=16
]

is compatible with every frozen carrier localization. Localization does not
destroy the grading or require an added carrier stratum.

This establishes an algebraic grading before integration. It does not prove
that a chosen physical relative cycle is homogeneous, that the Gauss--Manin
quotient splits by deck character, or that the integrated period has a
single scaling weight after boundary regularization.

## Next falsifier

Pass from the graded localized de Rham complex to the relative object selected
by the physical integration domain. Compute whether its boundary maps and
Gysin residues are degree zero. Any nonhomogeneous boundary term must be
classified as:

- a source-derived regulator or affine-scale choice;
- coefficient extension data;
- or genuinely new carrier structure.

No carrier modification is authorized by the present result.
