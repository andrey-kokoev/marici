# 1406 — A Rational Five-Cycle Kummer Base Requires Four Dimensions

## Status

Exact representation-theoretic gate.

## Problem

Entry 1404 proves directly that the declared three-variable asymmetric Kummer profile does not admit the source \(C_5\) action.

This is not an accident of its coefficients.

## Affine actions of a finite group

Let \(C_5\) act affinely on a rational affine space.

Because the characteristic is zero, averaging any point over the finite group produces a fixed point.

After translating that fixed point to the origin, the affine action becomes linear.

Therefore a nontrivial rational affine \(C_5\)-action requires a nontrivial rational linear representation of \(C_5\).

## Minimum rational dimension

Let \(T\) be a nontrivial rational operator satisfying

\[
T^5=1.
\]

Its minimal polynomial divides

\[
x^5-1=(x-1)\Phi_5(x),
\]

where

\[
\Phi_5(x)=x^4+x^3+x^2+x+1
\]

is irreducible over \(\mathbb Q\).

Any nontrivial order-five summand therefore contains the cyclotomic representation

\[
\mathbb Q(\zeta_5),
\]

whose rational dimension is

\[
[\mathbb Q(\zeta_5):\mathbb Q]=4.
\]

Hence

\[
\boxed{
\dim_{\mathbb Q}V<4
\quad\Longrightarrow\quad
\text{every rational }C_5\text{ action on }V\text{ is trivial}.
}
\]

In particular, no three-dimensional rational affine base can carry the nontrivial cyclic permutation required by the labelled five-cycle source.

## Canonical next base

The five labelled radicands

\[
(s_1,s_2,s_3,s_4,s_5)
\]

carry the permutation representation of \(C_5\).

It decomposes as

\[
\mathbb Q^5
=
\mathbb Q_{\rm triv}
\oplus
\mathbb Q(\zeta_5).
\]

Removing the common scale or diagonal direction leaves the canonical four-dimensional cyclic base

\[
\boxed{
V_{\rm cyc}
=
\{(s_1,\ldots,s_5):\sum_i s_i=0\}
\simeq
\mathbb Q(\zeta_5).
}
\]

Equivalently, one may retain all five labelled radicands and quotient projectively by their common scale.

## Consequence

The three-variable mismatch plane of Entry 1393 cannot become a rational cyclic coefficient object without changing its base.

The admissible successor is not another fitted three-variable profile. It is the full labelled five-radicand Kummer family, or its four-dimensional augmentation quotient.

## Next finite falsifier

Rebuild the cubic primitive/torsor audit on

\[
y_i^2=s_i,
\qquad i=1,\ldots,5,
\]

with the cyclic permutation retained exactly.

Then determine:

1. whether every pairwise occurrence boundary remains trivializable;
2. whether a ternary mismatch survives;
3. whether its span is preserved by the exact \(C_5\) action;
4. whether the result descends through the diagonal/projective quotient.

Failure of the ternary class on this base would identify Entry 1393 as an artifact of the asymmetric specialization.

Allocator claim: `seqclaim-9113b7821a2186518f47c3c7`.
