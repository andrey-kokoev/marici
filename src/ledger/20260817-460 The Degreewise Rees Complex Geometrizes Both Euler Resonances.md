---
id: 460
date: 2026-08-17
title: The Degreewise Rees Complex Geometrizes Both Euler Resonances
---

# The Degreewise Rees Complex Geometrizes Both Euler Resonances

Entry 459 requires following each homogeneous block separately.  For a divided
target monomial (a^Ic^J), with (c=b+1), its restriction to the Cartier
section carries the boundary divisor

\[
B(I,J)=
\left(
\left\lfloor\frac I2\right\rfloor,
\left\lfloor\frac I2\right\rfloor+J
\right)
\]

at ((b=1,b=-1)).  The first component counts tautological Rees factors
(t=(b-1)(b+1)/2); the extra (J) in the second counts incidence factors
(c=b+1).

This assignment makes the frozen exact operators regular degree by degree.
For

\[
D_b=a(1-c\partial_c),
\]

the map into target degree ((I,J)) comes from ((I-1,J)).  Its lattice
increment is zero when (I) is odd and (operatorname{div}(t)=(1,1)) when
(I) is even, exactly matching the conversion (a^2=ut).  For

\[
D_a=c(a\partial_a-7),
\]

the map comes from ((I,J-1)) and its increment is always
(operatorname{div}(c)=(0,1)).

The scalar coefficients into ((I,J)) are

\[
1-J
\quad\text{and}\quad
I-7.
\]

Scanning the entire nonnegative bidegree grid, both incoming maps fail
simultaneously only at

\[
(I,J)=(0,0),qquad(7,1).
\]

The first has (B(0,0)=(0,0)).  The second has

\[
B(7,1)=(3,4),
\]

recovering the sevenfold boundary divisor of Entries 455--457.  The other
three exact sectors also vanish at ((7,1)) by the source-degree coefficient
test of Entries 449 and 459.

Thus the degreewise exceptional Rees cokernel has exactly two primitive
homogeneous classes, with the same bidegrees and representatives as the Euler
quotient.  This is the first construction that simultaneously derives their
dimension, grading, and boundary lattices from the weighted geometry.

It is not yet a nearby-cycle theorem.  The construction identifies the
exceptional associated graded cokernel.  The next gate is to derive the
specialization/monodromy operator and test whether these two classes survive
in the relative nearby-cycle object rather than only its associated grade.

The executable audit is
research/voevodsky/check_soft_axis_degreewise_rees_complex.py.
