---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Q Is Regular in the Frozen Algebraic Plane at a Generic Q-Zero Point

## Result

The frozen absolute \(4\times4\) block and its algebraic plane

\[
\mathcal A_{--}
=
\langle e_6,v_{\rm alg}\rangle
\]

remain regular at a generic tested point of \(\mathcal Q=0\).  The source
quartic is therefore not an unavoidable singular-support divisor of this
connection in the tested finite model.

This is stronger than Entry 299's projected half-log mismatch: the
calculation crosses the quartic divisor itself and checks the complete
algebraic plane.

## Frozen computation

Use the exact absolute Griffiths--Dwork model of the source \(q\)-residue
sector:

\[
w^2=K(a,b),
\qquad
(e_6,e_7,e_8,e_9)
\]

with the same numerator degrees and exact-form fields as the frozen
\(4\times4\) reduction.  Work over

\[
\mathbb F_{1000003}
\]

on the \(z=1\) chart, with

\[
x=\rho\lambda,\qquad y=\lambda,
\qquad E=x+y+1.
\]

The point

\[
\boxed{
x=68688,\qquad y=1,\qquad E=68690
}
\]

obeys

\[
\boxed{\mathcal Q=0}
\]

modulo \(1000003\).

It is otherwise generic for the frozen comparison:

\[
B=164566,\qquad A=889817,\qquad AB=185123,
\]

\[
H=253483,\qquad
\Delta_1=512737,\qquad
\Delta_2=614554,
\]

all nonzero in \(\mathbb F_{1000003}\).  Thus the point is away from the
elliptic discriminant, the two conductor collisions, the \(e_6\)-Kummer
divisor, and soft support.

## Complete connection value

In the ordered basis

\[
(e_6,e_7,e_8,e_9),
\]

the exact reduction along the \(\lambda\)-direction gives

\[
\boxed{
A_\lambda=
\begin{pmatrix}
159764&808210&809146&588321\\
0&542779&593811&512702\\
0&711279&613309&33510\\
0&51479&721960&613309
\end{pmatrix}
}
\]

over \(\mathbb F_{1000003}\).

The three simple-pole columns are uniquely determined: each reduction has
rank \(10\) in \(10\) unknowns.  The double-pole \(e_6\) column has the
source value

\[
159764
=
-\frac12\partial_\lambda\log H
\]

and no component outside the \(e_6\) line.

No entry diverges or loses reduction rank at \(\mathcal Q=0\).

## Algebraic-plane invariance

Use the source-defined kernel vector

\[
\begin{aligned}
v_{\rm alg}
={}&
(x^2-y^2)(x^2y^2-E^4)e_7\\
&+2x^2(E^2+y^2)e_8
-2y^2(E^2+x^2)e_9.
\end{aligned}
\]

Including the derivative of its kinematic coefficients, direct substitution
into \(A_\lambda\) gives

\[
\boxed{
\nabla_\lambda v_{\rm alg}
=
977606\,e_6
+769398\,v_{\rm alg}.
}
\]

The three residual coordinates transverse to
\(\langle e_6,v_{\rm alg}\rangle\) are exactly

\[
(0,0,0).
\]

Hence the algebraic plane is invariant and its induced connection is finite
at the tested \(\mathcal Q\)-zero point.

For comparison, the source-normalized quotient coefficient

\[
769398
\]

is not

\[
\frac12\partial_\lambda\log(-\mathcal Q),
\]

which is undefined on the divisor.  The module connection nevertheless
extends regularly.

## Finite falsifier

The hard-to-vary claim

\[
\boxed{
\mathcal Q=0\text{ is an unavoidable singular divisor of the frozen
absolute algebraic-plane connection}
}
\]

fails in this exact finite model.  At a point where every predeclared
competing discriminant is nonzero, the connection and invariant plane are
both regular.

This does not yet prove a characteristic-zero global removal theorem.  A
second good prime or a universal cleared certificate is required for that
upgrade.  It does, however, rule out treating \(\mathcal Q\) as established
module support on the basis of the source algebraic letter alone.

## Current geometric home of Q

After Entries 209--212, 287--299, and the present divisor-crossing test, the
only surviving home is

\[
\boxed{
\text{apparent/cyclic-presentation discriminant or algebraic splitting
coordinate, not frozen carrier incidence.}
}
\]

The distinction is important:

- the rank-two algebraic plane is regular at the tested divisor;
- a chosen scalar operator, cyclic vector, or algebraic eigenline may still
  become singular there;
- such a singularity belongs to coefficient presentation/splitting data,
  not to the carrier or the underlying connection module.

The final provenance test is to derive \(\mathcal Q\) as the determinant of
the source scalarization/splitting transformation.  Until that determinant
is constructed, the presentation home is strongly supported but not proved.

## Classification

| Datum | Classification |
|---|---|
| \(\mathcal Q=0\) at tested point | regular for frozen \(4\times4\) module |
| \(\mathcal A_{--}\) | invariant algebraic coefficient plane |
| \(H=0\) | genuine \(e_6\) Kummer coefficient support |
| \(\Delta_i=0\) | conductor-collision coefficient support |
| scalar/cyclic \(\mathcal Q\) branch | surviving presentation-level candidate |
| new carrier datum | none |

## Deutsch--Popperian update M2.53

The smaller surviving conjecture is

\[
\boxed{
\mathcal Q\text{ is an apparent discriminant of scalarization or algebraic
splitting over a connection module regular at generic }\mathcal Q=0.
}
\]

## Next hostile test

Construct the source cyclic/splitting matrix from the frozen
\((e_6,e_7,e_8,e_9)\) connection and compute its determinant.  Test whether

\[
\det C_{\rm cyclic}
\stackrel?=
u\,\mathcal Q^m
\]

for a source-fixed unit \(u\) and positive integer \(m\).  Failure would
remove the last intrinsic geometric home for \(\mathcal Q\) and classify it
as a noncanonical alphabet rationalization.
