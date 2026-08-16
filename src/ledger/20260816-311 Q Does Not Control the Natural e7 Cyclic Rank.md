---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Q Does Not Control the Natural e7 Cyclic Rank

## Result

At the generic finite-field point of Entry 310 lying on
\(\mathcal Q=0\), the natural source master

\[
e_7=\varphi_{001}
\]

remains cyclic of order three in the final homogeneous sector. Neither its
full Krylov rank nor its projection to the source last-three-master block
drops there.

Thus the hard-to-vary claim

\[
\boxed{
\mathcal Q=0
\text{ is the rank-drop divisor of the natural }e_7
\text{ scalarization}
}
\]

fails in this exact finite model.

## Frozen source prescription

The primary source defines

\[
e_7=\varphi_{001},\qquad
e_8=y_{23}^2\varphi_{001},\qquad
e_9=y_{31}^2\varphi_{001}
\]

in applications.tex, lines 405--407. Line 425 states that the last three
masters form the homogeneous sector whose third-order operator
\(\mathcal L_3=\mathcal L_1\mathcal L_2\) is constructed after

\[
X_1=a_1\lambda,\qquad X_2=\lambda,\qquad X_3=1.
\]

The general prescription in Fullintegration.tex, lines 26--35, rewrites a
\(k\times k\) homogeneous block as an order-\(k\) scalar equation for one
master \(\mathcal J_i\). The paper does not identify which of the three
masters was selected as \(\mathcal J_i\). Consequently \(e_7\), the
denominator-free first member of the printed last-three basis, is a natural
source candidate, not a source-proved unique cyclic vector.

## Exact finite test

Use the frozen absolute Griffiths--Dwork connection of Entry 310 over
\(\mathbb F_{1000003}\) on the ray

\[
x=\rho\lambda,\qquad y=\lambda,\qquad z=1
\]

at

\[
(x,y,E)=(68688,1,68690).
\]

Here \(\mathcal Q=0\), while

\[
A,\ B,\ H,\ \Delta_1,\ \Delta_2\ne0.
\]

In the ordered basis \((e_6,e_7,e_8,e_9)\), exact dual-jet reduction gives

\[
\nabla_\lambda e_7
=
\begin{pmatrix}
808210\\542779\\711279\\51479
\end{pmatrix},
\]

and differentiating the reduced column gives

\[
\partial_\lambda(A_\lambda e_7)
=
\begin{pmatrix}
455181\\788715\\562894\\915676
\end{pmatrix}.
\]

Including connection transport,

\[
\nabla_\lambda^2e_7
=
\begin{pmatrix}
946865\\281985\\268664\\437584
\end{pmatrix}.
\]

The Krylov matrix

\[
C_{e_7}
=
\left(e_7,\nabla_\lambda e_7,\nabla_\lambda^2e_7\right)
\]

has rank

\[
\boxed{\operatorname{rank}C_{e_7}=3}.
\]

Its four maximal minors, ordered by the omitted row
\((e_6,e_7,e_8,e_9)\), are

\[
\boxed{
(863644,\ 0,\ 813443,\ 889857).
}
\]

In particular, omitting the \(e_6\) row gives the determinant of the
projection to the printed last-three block:

\[
\boxed{
\det C_{e_7}^{(e_7,e_8,e_9)}
=863644\ne0.
}
\]

The lone vanishing coordinate minor omits \(e_7\) and uses
\((e_6,e_8,e_9)\). Since the other three Pluecker coordinates are nonzero,
that vanishing is not a rank loss and has no invariant module meaning by
itself.

## Finite falsifier and scope

This one good-prime, one-point test falsifies any universal divisibility

\[
\mathcal Q\mid
\gcd\{\text{all maximal minors of }C_{e_7}\}
\]

and also falsifies divisibility of the natural last-three projection
determinant by \(\mathcal Q\), provided the frozen reduction has good
reduction at the point. The latter condition is witnessed by the unique
rank-\(10\) reductions and the nonvanishing competing discriminants recorded
in Entry 310.

It does not prove a characteristic-zero formula for the complete cyclic
determinant, and it does not test an unpublished, differently normalized
choice of \(\mathcal J_i\).

## Combined provenance update

The evidence now separates three levels:

1. the absolute \(4\times4\) module is regular at generic tested
   \(\mathcal Q=0\) (Entry 310);
2. the invariant algebraic plane is regular there (Entry 310);
3. the natural \(e_7\) order-three scalarization and its printed
   last-three projection remain cyclic there (this entry).

Together with the exact global physical-chain certificate, which gives
\(T_{\mathcal Q}=1\), \(N_{\mathcal Q}=0\), and zero physical variation at
generic nonsoft \(\mathcal Q=0\), the surviving interpretation shrinks to

\[
\boxed{
\mathcal Q
\text{ is an algebraic-letter rationalization or a noncanonical
presentation divisor, not detected intrinsic support.}
}
\]

No frozen carrier incidence, relative-cycle pinch, connection singularity,
algebraic-plane singularity, or natural \(e_7\) cyclic-rank loss has produced
\(\mathcal Q\).

## Classification

| Datum | Classification |
|---|---|
| \(C_{e_7}\) at tested \(\mathcal Q=0\) | rank-three cyclic coefficient presentation |
| last-three projected determinant | nonzero |
| lone vanishing coordinate minor | basis-dependent Pluecker coordinate |
| \(\mathcal Q\) | apparent alphabet/presentation datum in current evidence |
| new carrier datum | none |

## Deutsch--Popperian update M2.54

The smaller surviving conjecture is

\[
\boxed{
\mathcal Q
\text{ has no intrinsic geometric home in the frozen homogeneous
coefficient module; it enters only through the chosen algebraic alphabet
or an as-yet-unpublished noncanonical scalarization.}
}
\]

## Next hostile test

Reconstruct the algebraic letter itself from the published differential
alphabet and determine whether \(\sqrt{\mathcal Q}\) is merely the quadratic
discriminant of a rationalizing coordinate. Independently seek a universal
cleared certificate, or a second good-prime divisor crossing, for regularity
of the algebraic plane and nonvanishing of the natural last-three cyclic
minor. Only an invariant extension or monodromy detected after these
crossings may restore \(\mathcal Q\) as coefficient support.
