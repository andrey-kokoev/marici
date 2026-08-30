---
title: "The Five-Site Character Filtration Is the Shadow of an Exact Homogeneous Grading"
date: 2026-08-20
entry: 1291
status: active-narrow-result
author: marici.Benincasa
---

# 1291 — The Five-Site Character Filtration Is the Shadow of an Exact Homogeneous Grading

Sequence claim: `seqclaim-e15fbe68211a934e86a3f4fc`.

## Question

Entry 1286 found on the physical slice that a character (S) of weight
(w=|S|) obeys

[
deg_tequiv wpmod 2,
qquad
deg_t+deg_ule16-w.
]

This could have been an accidental filtration caused by setting the external
kinematic scale to one.

## Frozen homogenization

Restore one scale (ho) in the five physical radicands:

[
F_1=2u_1^2+2u_2^2+u_3^2-2u_1u_2-2u_2u_3,
]

[
F_2=F_1-2ho u_1+ho^2,
qquad
F_3=F_1-2ho u_2+2ho^2,
]

[
F_4=F_1-2ho u_3+3ho^2,
]

[
F_5=F_1+2ho u_1+2ho u_2-8ho u_3+29ho^2.
]

Each (F_i) is homogeneous of degree two in ((u_1,u_2,u_3,ho)).
No coefficient or normalization is fitted.

## Exact result

Reduce Entry 1270's degree-sixteen numerator by (y_i^2=F_i):

[
N_{16}
=
sum_{Ssubseteq{1,ldots,5}}
C_S(t,u,ho)y_S.
]

Every one of the 32 coefficients is nonzero, and every monomial of (C_S)
has exactly the same total degree:

[
oxed{
deg_{t,u,ho} C_S=16-|S|.
}
]

The degree table is therefore

[
egin{array}{c|c|c}
|S|&#	ext{ characters}&deg C_S\
hline
0&1&16\
1&5&15\
2&10&14\
3&10&13\
4&5&12\
5&1&11
end{array}
]

The exact term count remains 43296. All 32 rows pass both the homogeneous
degree audit and Entry 1286's parity/filtration audit.

## Interpretation

The physical (ho=1) filtration is the specialization of the bigrading

[
oxed{
deg(C_S)+|S|=16.
}
]

Thus deck-character weight consumes one unit of the ambient numerator degree.
This grading comes from the frozen Kummer algebra and source numerator; it is
not inferred from a residual permutation symmetry.

It is still a grading of the algebraic numerator. It does not yet prove that
the full localized canonical form, its de Rham quotient, or Gauss--Manin
transport splits by this grading.

## Next falsifier

Construct the source-localized differential in the homogenized character
basis. Test whether it is homogeneous after assigning

[
deg y_i=1,qquad deg F_i=2.
]

If localization necessarily mixes total grades beyond the shifts dictated by
the 26 frozen walls, then this is only a numerator grading. If the differential
is graded, it supplies a canonical filtration for the five-site coefficient
complex.
