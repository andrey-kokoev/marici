# Complementary observers are stable exactly when the row operator is bounded below

## Question

What is the first exact operational theorem for an analytic observer and a complementary observer?

## Claim boundary

For bounded operators between Hilbert spaces, stable joint reconstruction is equivalent to a lower frame bound for the row operator. If the analytic channel is compact, stability forces the complementary channel to be bounded below outside a finite-dimensional defect. Joint injectivity alone is insufficient. No symmetry-equivariant refinement is asserted here.

## Problem

Let

\[
A:X\to Y,
\qquad
D:X\to Z
\]

be bounded operators between Hilbert spaces. Define the joint observer

\[
T=\binom AD:X\longrightarrow Y\oplus Z.
\]

The programme needs a criterion stronger than

\[
\ker A\cap\ker D=0,
\]

because injectivity does not control reconstruction stability.

## Bold conjecture

Joint injectivity of \(A\) and \(D\) suffices for stable reconstruction.

## Named rivals

1. Stability requires a quantitative lower frame bound.
2. When \(A\) is compact, \(D\) must control every asymptotically \(A\)-invisible direction.
3. It is enough for \(D\) to be nonzero coordinatewise, even if its response tends to zero.

## Theorem 1: row-operator criterion

The following are equivalent.

1. There exists \(\delta>0\) such that

   \[
   \|Ax\|_Y^2+\|Dx\|_Z^2
   \ge
   \delta^2\|x\|_X^2
   \qquad(x\in X).
   \]

2. \(T\) is bounded below.
3. \(T\) is injective and has closed range.
4. \(T^*T=A^*A+D^*D\) satisfies

   \[
   A^*A+D^*D\ge\delta^2I
   \]

   for some \(\delta>0\).
5. The inverse \(T^{-1}:\operatorname{ran}T\to X\) is bounded.

### Proof

The identity

\[
\|Tx\|^2
=
\|Ax\|^2+\|Dx\|^2
=
\langle(A^*A+D^*D)x,x\rangle
\]

proves the equivalence of 1, 2, and 4. A bounded operator is bounded below exactly when it is injective with closed range, proving 2 equivalent to 3. The inequality gives

\[
\|T^{-1}y\|\le\delta^{-1}\|y\|
\]

on \(\operatorname{ran}T\), and the bounded-inverse statement conversely supplies a lower bound.

## Theorem 2: compact-channel necessity

Assume \(X\) is infinite-dimensional, \(A\) is compact, and \(T\) has lower bound \(\delta>0\). Then for every \(0<\varepsilon<\delta\), there is a finite-codimensional closed subspace \(E\subset X\) such that

\[
\|Dx\|
\ge
\sqrt{\delta^2-\varepsilon^2}\,\|x\|
\qquad(x\in E).
\]

### Proof

Choose a finite-rank operator \(A_0\) with

\[
\|A-A_0\|<\varepsilon.
\]

Set \(E=\ker A_0\). This subspace has finite codimension. For \(x\in E\),

\[
\|Ax\|<\varepsilon\|x\|.
\]

The row lower bound then gives

\[
\|Dx\|^2
\ge
(\delta^2-\varepsilon^2)\|x\|^2.
\]

Thus the compact analytic channel may handle a finite-dimensional defect, but the complementary observer must carry the completed-source margin on a cofinite subspace.

## Corollary: weakly null test

If \(A\) is compact and \(T\) is bounded below by \(\delta\), then every normalized weakly null sequence \((x_n)\) satisfies

\[
\liminf_{n\to\infty}\|Dx_n\|\ge\delta.
\]

Indeed compactness gives \(Ax_n\to0\). In particular, the claim holds for every orthonormal sequence.

This is a necessary test for any proposed complementary observer.

## Converse with the finite defect stated correctly

Suppose \(D\) is bounded below on a finite-codimensional subspace. Then

\[
D:X\to Z
\]

is upper semi-Fredholm: it has closed range and finite-dimensional kernel. The row operator \((0,D)^\top\) is likewise upper semi-Fredholm. Since \(T-(0,D)^\top=(A,0)^\top\) is compact, \(T\) is upper semi-Fredholm. Therefore, if additionally

\[
\ker A\cap\ker D=0,
\]

then \(T\) is injective with closed range and hence bounded below.

Thus for compact \(A\), stable complementarity is equivalent to:

1. \(D\) is bounded below outside a finite-dimensional defect; and
2. \(A\) detects the residual kernel of \(D\).

The two clauses cannot be replaced by joint injectivity alone.

## Hostile counterexample

Take

\[
X=Y=Z=\ell^2(\mathbb N).
\]

Define

\[
Ae_n=\frac1n e_n
\]

and let \(D\) be projection onto the odd coordinates. The operator \(A\) is compact and injective, so \(T\) is injective. Yet for the even basis vectors,

\[
De_{2n}=0,
\qquad
\|Ae_{2n}\|=\frac1{2n}\longrightarrow0.
\]

Hence

\[
\|Te_{2n}\|\to0,
\]

and \(T\) is not bounded below. This refutes the bold conjecture.

It also refutes rival 3: every coordinate is seen by at least one channel, but the observation strength on an infinite family collapses.

## Constructor-role interpretation

The analytic channel \(A\) and complementary channel \(D\) are not two interchangeable formulas. Their roles are:

- \(A\): structured analytic realization, allowed to be compact;
- \(D\): completed-source margin on the asymptotically invisible directions;
- \(T\): joint reconstruction operator.

A coefficient family appropriate for \(A\) need not satisfy the cofinite lower bound required of \(D\). Substituting the analytic loading into the discrete complementary slot is therefore a type error detectable by Theorem 2.

## Green/Real worked-example interface

In the radial example, \(A\) is the compact Euler-to-theta-to-radial loading, followed by Green/Laplace response. The fold and Real comparison ensure that this analytic channel respects

\[
C_uF^2=W_uC_u
\]

and

\[
U^\top=U^*.
\]

Those exact sewing identities do not imply a lower frame bound. Any proposed discrete arithmetic observer must be tested on normalized prime sequences for which the radial analytic response tends to zero.

## Disposition

The elementary operational theorem is proved. Stable complementary observation is a lower-frame property, not joint injectivity. For a compact analytic channel, the complement must be bounded below on a finite-codimensional subspace, while the analytic channel need only detect its finite-dimensional residual kernel. The next frontier is the symmetry-equivariant refinement: determine how this cofinite complement interacts with \(G\to H\) and whether it must separately detect the kernel representation of the symmetry descent.
