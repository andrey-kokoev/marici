---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Lambda Collision Normal Forms and the Joint Nearby-Cycle Frontier

## Result

The collision divisor of the two same-sheet marked-wall intersections is

\[
\Lambda
=
E(-x+y+z)(x-y+z)
=
-\ell_1\ell_2\ell_4.
\]

It is therefore not an additional generic support divisor. Every component
of \(\Lambda=0\) is already a signed-energy component of the frozen
elliptic/Cayley--Menger discriminant.

The three components do not have one common local model.

- At a generic point of \(\ell_1=0\) or \(\ell_2=0\), the affine
  Cayley--Menger double-cover surface acquires an \(A_2\) singularity at
  the marked-wall collision. The corresponding one-parameter total space
  has an ordinary double point.
- At \(\ell_4=E=0\), the full affine branch polynomial becomes an exact
  square. The central surface splits into two components and has a
  non-isolated double-curve singularity.

Meanwhile the incidence graph of the marked conductor drops from
\(b_1=3\) to \(b_1=2\) at a generic \(\ell_1\)- or
\(\ell_2\)-collision. Thus one marked top cycle disappears precisely
where the already frozen surface develops its finite vanishing geometry.

The hard conclusion is

\[
\boxed{
\Lambda=0
\text{ is coefficient support on the existing signed-energy carrier,}
}
\]

not a new carrier incidence generator. What remains unresolved is the
joint nearby-cycle extension between the finite surface vanishing classes
and the disappearing conductor cycle.

## Frozen source object

On the \(q_{\mathcal G_{12}}\)-residue surface set \(c=-E\) and use

\[
S_E:\qquad w^2=K_E(a,b).
\]

The two marked walls meet at

\[
P_\pm:
\qquad
a=x+z,
\quad
b=y+z,
\quad
w=\pm\Lambda.
\]

No denominator, boundary component, or carrier cell is added in this
calculation.

## The \(\ell_1=0\) normal form

Set

\[
\lambda=\ell_1=x-y-z,
\qquad
u=a-(x+z),
\qquad
v=b-(y+z).
\]

On the central fiber \(z=x-y\), write

\[
d=2x-y.
\]

The quadratic part of the branch polynomial at the collision is

\[
K_2
=
4x^2(du-yv)^2.
\]

It has rank one. Along its null direction

\[
u=y\tau,
\qquad
v=d\tau,
\]

the cubic part is

\[
K_3\big|_{\ker K_2}
=
4xy^4d\,\tau^3.
\]

This coefficient is nonzero at generic nonsoft kinematics. Hence the
surface germ

\[
w^2-K_E(u,v)=0
\]

has analytic type \(A_2\).

The moving family contains more information than the central fiber. The
quadratic coefficient matrix of \(K_E\) in \((u,v,\lambda)\) is

\[
M_1
=
4x^2
\begin{pmatrix}
d^2 & -yd & 2d(x-y)\\
-yd & y^2 & 2y(x-y)\\
2d(x-y) & 2y(x-y) & 4(x-y)^2
\end{pmatrix}.
\]

Its determinant is

\[
\det M_1
=
-1024x^6y^2d^2(x-y)^2.
\]

Therefore the quadratic form of the threefold total-space equation
\(w^2-K_E=0\) has full rank four: the total space has an ordinary double
point at the generic collision.

## The \(\ell_2=0\) normal form

The second component follows from the exact symmetry

\[
x\leftrightarrow y,
\qquad
u\leftrightarrow v.
\]

At generic nonsoft kinematics its central surface germ is again \(A_2\),
and the determinant of the moving quadratic matrix is

\[
-1024y^6x^2(2y-x)^2(y-x)^2.
\]

Its total space is again an ordinary double point.

These are source-derived polynomial statements. They do not by themselves
fix the complete monodromy of the marked relative pair.

## The total-energy component is different

At

\[
E=\ell_4=0,
\qquad
z=-x-y,
\]

use coordinates

\[
u=a+y,
\qquad
v=b+x.
\]

The complete branch polynomial, not only its lowest jet, factors as

\[
\boxed{
K_E
=
\left[
2xy(u+v)-xu^2-yv^2
\right]^2.
}
\]

Thus

\[
S_{E=0}
=
\{w=R(u,v)\}
\cup
\{w=-R(u,v)\}.
\]

This is a global split double cover with a non-isolated double curve
\(w=R=0\). The isolated \(A_2\) analysis used on
\(\ell_1\) and \(\ell_2\) is inapplicable here. The physical
total-energy boundary requires the global nearby-cycle calculation already
signaled by the elliptic nodal degeneration.

## Marked-conductor specialization

Generically, the normalization-incidence graph of

\[
W=W_1\cup W_2
\]

has four component vertices and six incidence edges:

- two internal branches joining the sheets of \(W_1\);
- two internal branches joining the sheets of \(W_2\);
- the two same-sheet intersections \(P_+\) and \(P_-\).

Hence

\[
b_1(W)=6-4+1=3.
\]

At a generic \(\ell_1\)- or \(\ell_2\)-collision, \(P_+=P_-\)
and that point is simultaneously one branch point on each marked wall.
Using one incidence vertex for this four-branch point and one for each
remaining two-branch node gives

\[
V=4+3,
\qquad
E=4+2+2,
\qquad
b_1=8-7+1=2.
\]

Exactly one graph class specializes to zero. This is the top conductor
class detected in entries 264 and 280, but the static rank drop does not
yet determine its logarithmic extension into the absolute surface system.

## Monodromy discipline

Three statements must remain separate.

1. The \(A_2\) central-fiber type is directly computed.
2. The ordinary-double-point type of the moving total space is directly
   computed.
3. The joint monodromy on
   \(H^2(S_E\setminus W)\) is not determined by either fact alone.

In particular, one must not replace the required nearby-cycle map by the
Coxeter monodromy of a generic \(A_2\) smoothing. The physical
one-parameter slice is fixed by the signed-energy normal and has a singular
total space.

## Classification

The new structures classify as follows:

| Structure | Classification |
|---|---|
| \(\ell_1\), \(\ell_2\), \(\ell_4\) | existing signed-energy carrier |
| finite \(A_2\) surface singularities | Cayley--Menger coefficient support |
| ordinary-double-point total spaces | coefficient-family degeneration |
| disappearing conductor cycle | frozen marked-wall relative coefficient data |
| split \(E=0\) double cover | global Cayley--Menger nearby-cycle geometry |
| new incidence generator | none found |

This is positive evidence for

\[
\text{shared carrier}
+
\text{shared derived calculus}
+
\text{sector-specific coefficient objects}.
\]

It is not yet a global splitting theorem.

## Deutsch--Popperian conjecture M2.25

For a generic transverse signed-energy normal to
\(\ell_1=0\) or \(\ell_2=0\), the canonical nearby-cycle triangle of
the frozen pair \((S_E,W)\) accounts simultaneously for

- the rank-two \(A_2\) surface vanishing lattice;
- the rank-one loss in \(H^1(W)\);
- the top extension column of
  \(H^2(S_E\setminus W)\);

without introducing any stratum beyond the existing signed-energy divisor.

The finite falsifier is to construct a semistable model of the pair and
compute the specialization and variation maps. If the disappearing
conductor class requires a boundary component not generated by the frozen
Cayley--Menger surface and marked walls, the shared-carrier hypothesis
fails here.

## Next hostile test

Treat \(\ell_1=0\) first.

1. Resolve or semistabilize the ordinary-double-point total space together
   with the four-branch marked divisor.
2. Compute the nearby-cycle complex of the pair.
3. Determine \(T_s\), \(N\), \(\operatorname{rank}N\), and
   \(N^2\) on the finite surface and conductor pieces.
4. Locate the specialization of the invariant top lift from entry 280.
5. Repeat by symmetry for \(\ell_2=0\).
6. Analyze \(E=0\) separately using the global split model.
7. Admit no new carrier component after seeing the answer.
