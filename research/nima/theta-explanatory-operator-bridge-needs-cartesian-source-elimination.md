# An explanatory operator bridge needs source-local elimination

## Universal realization is not a bridge

Grothendieck's rank-one construction proves a general no-go result. Given any
scalar section \(f(s)\), choose vectors \(u_s,\Omega\) with
\(\langle\Omega,u_s\rangle=f(s)-1\), and set

\[
T_s=I+|u_s\rangle\langle\Omega|.
\]

Then

\[
\det T_s=f(s).
\]

Every scalar zero is now an operator kernel. The construction works equally
for the completed theta section and for hostile sections with inserted
off-seam divisors. Therefore neither determinant realization nor
zero-to-kernel conversion carries source authority.

## The missing categorical condition

Let \(X\) be a finite labelled source packet and let \(X\subset Y\) be an
authorized packet extension. A genuine operator construction must assign

\[
X\longmapsto (\mathcal H_X,D_X)
\]

before scalar readout. The extension must be represented by an independently
typed block decomposition

\[
D_Y=
\begin{pmatrix}
D_X&B_{X,Y}\\
C_{X,Y}&E_{X,Y}
\end{pmatrix}.
\]

Eliminating the added states gives the Schur complement

\[
\operatorname{Schur}_{Y/X}(D_Y)
=
D_X-B_{X,Y}E_{X,Y}^{-1}C_{X,Y}.
\]

The explanatory gate is not merely that determinants agree. The eliminated
operator must agree with the operator assigned to \(X\), up to a declared
boundary-current transformation:

\[
\operatorname{Schur}_{Y/X}(D_Y)
\simeq
\mathcal R_{X,Y}(D_X).
\]

Here \(\mathcal R_{X,Y}\) must be derived from source transport. It may carry
the primitive, square, seam, and archimedean anomaly, but it cannot be fitted
from the final scalar section.

This is a cartesian elimination condition: restricting the source packet and
eliminating its complement must describe the same retained operator system.

## Composition gate

For \(X\subset Y\subset Z\), elimination must compose:

\[
\operatorname{Schur}_{Z/X}
=
\operatorname{Schur}_{Y/X}\circ
\operatorname{Schur}_{Z/Y},
\]

with the associated boundary transformations satisfying

\[
\mathcal R_{X,Z}
=
\mathcal R_{X,Y}\circ\mathcal R_{Y,Z}.
\]

This is the operator form of the determinant-line connection. Its first
logarithmic jet is the already isolated boundary anomaly. The scalar
determinant is only the final shadow of this compositional law.

## Why the rank-one lift fails

The universal rank-one lift begins with the aggregated scalar \(f_X\).
Consequently its new vector \(u_X\) changes globally whenever any source label
is added or removed. It supplies no independently constructed blocks
\(B_{X,Y},C_{X,Y},E_{X,Y}\), and no deletion square exists before the scalar
answer is known.

One can manufacture such blocks afterward, but then the source-extension
functor is defined by the scalar determinant it was meant to explain. Hostile
sections inherit the same manufactured functor.

## Finite hostile test

For two independently added labels \(p\) and \(q\), construct the four
operators

\[
D_X,\qquad D_{X+p},\qquad D_{X+q},\qquad D_{X+p+q}
\]

from labelled source rules alone. Then test:

1. deletion of \(p\) and \(q\) recovers the declared retained systems;
2. both two-step Schur eliminations are defined on the same retained domain;
3. their operator residual is exactly the declared boundary coherence;
4. the determinant increments agree with the primitive currents at each
   addition;
5. a hostile scalar multiplier cannot be inserted without changing at least
   one local block or coherence residual.

Failure of any one test rejects the operator bridge. Passing only the final
determinant equality is insufficient.

## Current disposition

The RH lane now has a sharper construction target. It needs a source-local
operator functor whose restriction maps are realized by compositional Schur
elimination and whose independent Green or index law excludes kernels.

Until that object is built, determinant, kernel, reflection positivity, and
observability remain faithful representations of the completed scalar
problem, not explanations of its zero confinement.
