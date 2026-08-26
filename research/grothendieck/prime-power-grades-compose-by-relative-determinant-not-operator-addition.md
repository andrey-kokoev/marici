# Prime-power grades compose by relative determinant, not operator addition

## Question

The primitive and square currents occupy different completion grades.  Must a
new archimedean sewing operator couple them before a global theorem is
possible, or has the source already specified how they compose?

## One transition, many cyclic cumulants

At a finite prime cutoff, let (A_X(s)) denote the source-derived bordered
valuation transition.  Its logarithmic determinant has the formal cyclic
expansion

\[
-\log\det(I-A_X)
=
\sum_{k\ge1}\frac1k\operatorname{Tr}(A_X^k).
\]

The primitive and square currents are

\[
\operatorname{Tr}(A_X),
\qquad
\frac12\operatorname{Tr}(A_X^2).
\]

They are not two transport operators.  They are two cyclic readouts of the
same transition.  Their source-authorized composition is therefore the
relative determinant identity

\[
\det(I-A_X)
=
\det_3(I-A_X)
\exp\left(
-\operatorname{Tr}(A_X)
-\frac12\operatorname{Tr}(A_X^2)
\right),
\]

with the sign adjusted according to the chosen determinant convention.  The
structural content is independent of that convention: the first two
cumulants remain explicit boundary coordinates and the (k\ge3) terms form
the regularized determinant tail.

## Why the mixed self-commutator is absent

Replacing the cyclic packet by

\[
T_1+T_2
\]

on one unilateral carrier creates products

\[
T_1^*T_2,
\qquad
T_2^*T_1.
\]

No such cross terms occur in the logarithmic determinant decomposition.  The
degrees are combined additively only after applying the cyclic trace, and are
then exponentiated to reconstruct the determinant.  Nima's negative
prime-five minor is therefore a decisive falsifier of the additive-operator
model, not a defect that the determinant packet must cancel.

## Fock interpretation

The same distinction appears in bosonic formation.  Prime powers are repeated
returns of one primitive mode.  The Euler factor

\[
\frac1{1-q}
=
\exp\left(
\sum_{k\ge1}\frac{q^k}{k}
\right)
\]

combines cycle lengths by exponentiating their connected cumulants.  It does
not add the (k=1) and (k=2) shifts and then compute the dynamics of their
sum.

Thus the three regularity ports are best typed as a graded logarithmic
determinant object:

\[
\mathfrak D_X
=
\left(
C_{1,X},
C_{2,X},
\det_3(I-A_X)
\right).
\]

Its reconstruction map is multiplicative and lossless at every finite cutoff.

## Revised archimedean target

The archimedean completion should not be sought first as a linear map from the
primitive distributional port into the square Hilbert port.  It should act on
the entire graded determinant packet:

\[
\mathfrak D_X
\longmapsto
\mathfrak D_X^{\infty}.
\]

The required coherence law is that archimedean completion commute with finite
determinant reconstruction, up to an independently derived nowhere-vanishing
unit and an explicit boundary anomaly.

This gives an exact finite diagram to test:

\[
\begin{array}{ccc}
\mathfrak D_X & \longrightarrow & \det(I-A_X)\\
\downarrow & & \downarrow\\
\mathfrak D_X^{\infty} & \longrightarrow & \det_{\mathrm{completed}}(I-A_X).
\end{array}
\]

The diagram must commute before taking the infinite Euler limit.

## Falsifiers

The revised route fails if:

- archimedean completion mixes (C_1) and (C_2) through an undeclared
  Hilbert-space addition;
- the completed reconstruction differs by a factor with a divisor rather than
  a nowhere-vanishing unit;
- the finite diagram commutes only after scalar analytic continuation;
- or the completion map discards either low cumulant.

## Result

The source already specifies how prime-power grades compose: by connected
cumulants followed by relative-determinant reconstruction.  No primitive to
square operator sewing is presently authorized or needed.  The remaining
global problem is the compatibility of archimedean completion with this
graded determinant functor.
