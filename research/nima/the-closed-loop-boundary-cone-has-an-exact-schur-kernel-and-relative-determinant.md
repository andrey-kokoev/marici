# The closed-loop boundary cone has an exact Schur kernel and relative determinant

> **Variance correction.** The Schur kernel and finite ordinary determinant
> calculations below remain valid. The successor packet
> `the-euler-block-must-enter-the-closed-loop-determinant-line-contravariantly.md`
> shows that this ordinary determinant has the wrong Euler variance for Xi.
> The completed scalar compiler must use the corresponding graded determinant
> line, with the Euler block in dual degree.

## Source block

Let

\[
A_0(s)=I-L(s)
\]

be the prime-loop block and let

\[
D_0(s)=I-A(s)
\]

be the reduced boundary-history block.  The source incidence is

\[
B(s):E\to H.
\]

Form the closed-loop boundary cone operator

\[
\mathcal C(s)
=
\begin{pmatrix}
A_0(s)&-B(s)^\dagger\\
-B(s)&D_0(s)
\end{pmatrix}

after the declared radical quotients.

This block is source-derived: its diagonal entries are the open prime loop and
open boundary return, while its off-diagonal entries are the incidence and its
seam-metric adjoint.

## Schur reduction

Assume \(A_0(s)\) and \(D_0(s)\) are invertible on the chart under discussion.
Set

\[
G(s)=D_0(s)^{-1},
\]

\[
R(s)=B(s)^\dagger G(s)B(s),
\]

and

\[
K_{\rm rel}(s)=A_0(s)^{-1}R(s).
\]

The first Schur complement is

\[
S_E(s)
=A_0(s)-B(s)^\dagger G(s)B(s)
=A_0(s)(I-K_{\rm rel}(s)).
\]

Thus the relative return previously obtained from seam-weighted incidence is
exactly the closed-loop Schur return; it is not a separate fitted operator.

## Kernel equivalence

The equation

\[
\mathcal C(s)\binom{x}{y}=0
\]

gives

\[
y=G(s)B(s)x
\]

from the second row.  Substitution into the first gives

\[
A_0(s)(I-K_{\rm rel}(s))x=0.
\]

On the invertible open-loop chart,

\[
\ker\mathcal C(s)
\cong
\ker(I-K_{\rm rel}(s))
\]

through

\[
x\longmapsto\binom{x}{G(s)B(s)x}.
\]

Therefore a relative eigenvalue-one collision is a genuine closed boundary
state, not merely a vanishing scalar determinant.

## Algebraic multiplicity

Gaussian block elimination factors the cone as

\[
\mathcal C
=
\begin{pmatrix}I&-B^\dagger G\\0&I\end{pmatrix}
\begin{pmatrix}S_E&0\\-B&D_0\end{pmatrix}.
\]

The triangular factor is invertible and holomorphic whenever \(G\) is.  Hence
local root spaces and algebraic multiplicities of the closed-loop defect agree
with those of \(I-K_{\rm rel}\), provided the family is analytic Fredholm in
the declared operator ideal.

## Relative determinant

At finite cutoff,

\[
\det\mathcal C(s)
=
\det A_0(s)\det D_0(s)
\det(I-K_{\rm rel}(s)).
\]

Thus the normalized closed-loop determinant is

\[
\frac{\det\mathcal C(s)}{
\det A_0(s)\det D_0(s)}
=
\det(I-K_{\rm rel}(s)).
\]

On the centered seam this is an ordinary Fredholm relative determinant.  In
the reciprocal overlap it must be read as an order-two regularized relative
determinant together with its first-trace anomaly.  The triangular
factorization still gives the kernel equivalence; only the scalar determinant
normalization changes.

## Relation to the bare Euler compiler

The open-loop factor \(\det A_0\) is not an ordinary determinant in the
critical strip.  Its source completion is the bare Euler determinant line

\[
u^{(1)}(s)u^{(2)}(s)\det_3(I-L(s)).
\]

The boundary factor \(\det D_0\), the relative \(\det_2\), and their anomaly
lines must be composed with that Euler section.  The cone factorization shows
where each factor belongs and prevents counting the relative return as another
primitive Euler current.

## Green-pencil bridge

The cone kernel is now linked exactly to the relative return.  To identify it
with the positive Green-pencil collision, one still must prove that the G3
coherent/disagreement Schur operator is the same reduced
\(I-K_{\rm rel}(s)\) under the retained constructor comparison.  Equality of
lower bounds or dimensions is insufficient.

## G4 consequence

The missing closed-loop boundary state has a canonical construction, exact
Schur reduction, and multiplicity-preserving kernel map on every invertible
open-loop chart.

The remaining G4 obligations are:

1. identify the cone determinant-line section with \(E(s)\Xi(s)\);
2. reconcile \(\det_3\), \(\det_2\), and low-order anomaly factors;
3. identify the cone Schur return with the positive Green pencil;
4. pass these identities through the completed holomorphic families.

No RH conclusion is authorized.
