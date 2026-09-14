# The prolate contraction has an exact observer-weighted positive defect tower without a bare transition trace

## Positive prolate contraction

Let

\[
B_\Lambda
=P_\Lambda Q_\Lambda P_\Lambda.
\]

Since `P_Lambda` and `Q_Lambda` are orthogonal projections,

\[
0\le B_\Lambda\le I.
\]

For an observer amplitude

\[
A=U_S(g),
\]

the positive triple-compression feature is

\[
\Phi_{\Lambda,0}(g)
=B_\Lambda^{1/2}A.
\]

Its squared Hilbert--Schmidt norm, when finite, is

\[
\|\Phi_{\Lambda,0}(g)\|_{HS}^2
=
\operatorname{Tr}
(A^*B_\Lambda A).
\]

## Exact one-step bulk/transition split

Functional calculus gives

\[
\boxed{
B
=B^2+B(I-B).
}
\]

Both summands are positive because they are nonnegative functions of the same positive contraction.

Define

\[
\boxed{
\Phi_\Lambda^{bulk}(g)
=B_\Lambda A,
}
\]

and

\[
\boxed{
\Phi_\Lambda^{tr}(g)
=
\left(
B_\Lambda(I-B_\Lambda)
\right)^{1/2}A.
}
\]

Then

\[
\boxed{
\|B_\Lambda^{1/2}A\|_{HS}^2
=
\|B_\Lambda A\|_{HS}^2
+
\|
(B_\Lambda(I-B_\Lambda))^{1/2}A
\|_{HS}^2.
}
\]

This is an exact orthogonal feature decomposition after mapping into the direct sum of the two Hilbert--Schmidt target spaces.

## Why this fixes the angular trace problem

The bare transition trace

\[
\operatorname{Tr}
(B_\Lambda-B_\Lambda^2)
\]

may be infinite because of angular multiplicity. The observer-weighted transition norm is instead

\[
\boxed{
\operatorname{Tr}
\left(
A^*
(B_\Lambda-B_\Lambda^2)
A
\right)
=
\|
(B_\Lambda(I-B_\Lambda))^{1/2}A
\|_{HS}^2.
}
\]

Observer smoothing is retained on both sides. No trace is assigned to the angular identity.

Thus the correct prolate transition quantity is automatically typed whenever the positive observer feature is typed.

## Spectral interpretation

If

\[
B_\Lambda e_n
=\lambda_n e_n,
\qquad
0\le\lambda_n\le1,
\]

then one mode contributes

\[
\lambda_n
=
\lambda_n^2
+
\lambda_n(1-\lambda_n).
\]

The first term is concentrated bulk; the second is transition defect. Modes near zero or one contribute little to the defect, while modes near `1/2` contribute maximally.

This is precisely the prolate transition profile, now weighted by the observer coefficients.

## Dyadic iteration

Apply the same split to `B^(2^j)`:

\[
B^{2^j}
=
B^{2^{j+1}}
+
B^{2^j}
(I-B^{2^j}).
\]

Telescoping gives, for every `n>=1`,

\[
\boxed{
B
=
B^{2^n}
+
\sum_{j=0}^{n-1}
B^{2^j}
(I-B^{2^j}).
}
\]

Every summand is positive and commutes with every other summand.

Define scale features

\[
\boxed{
\Phi_{\Lambda,j}^{tr}(g)
=
\left[
B_\Lambda^{2^j}
(I-B_\Lambda^{2^j})
\right]^{1/2}A.
}
\]

Then

\[
\boxed{
\|B_\Lambda^{1/2}A\|_{HS}^2
=
\|B_\Lambda^{2^{n-1}}A\|_{HS}^2
+
\sum_{j=0}^{n-1}
\|\Phi_{\Lambda,j}^{tr}(g)\|_{HS}^2.
}
\]

The exponent in the first norm is correct because its square gives `B^(2^n)`.

## Infinite limit and intersection sector

For a positive contraction,

\[
B^m
\longrightarrow
P_{\{1\}}(B)
\]

strongly as `m->infinity`, where

\[
P_{\{1\}}(B)
\]

is the spectral projection onto the eigenvalue-one subspace.

Therefore

\[
\boxed{
B
=
P_{\{1\}}(B)
+
\sum_{j\ge0}
B^{2^j}
(I-B^{2^j})
}
\]

in the strong monotone sense.

Observer-weighted quadratic forms give

\[
\boxed{
\|B^{1/2}A\|_{HS}^2
=
\|P_{\{1\}}(B)A\|_{HS}^2
+
\sum_{j\ge0}
\|\Phi_j^{tr}(g)\|_{HS}^2.
}
\]

The first term is the exact common-range/intersection feature. It is the alternating-projection/Sonin harmonic sector.

## No threshold choice

A split by spectral threshold

\[
1_{[1-\varepsilon,1]}(B)
]

would introduce an arbitrary `epsilon`. The dyadic defect tower is canonical: it uses only multiplication and the functional calculus of `B`.

Each eigenvalue `lambda` is resolved by the identity

\[
\lambda
=
1_{\{1\}}(\lambda)
+
\sum_{j\ge0}
\lambda^{2^j}
(1-\lambda^{2^j}).
\]

## Relation to alternating projections

The operator

\[
B=PQP|_{P\mathcal H}
\]

is the alternating-projection contraction. Its powers converge strongly to the projection onto

\[
\operatorname{ran}P
\cap
\operatorname{ran}Q.
\]

Thus

\[
P_{\{1\}}(B)
=P_{\operatorname{ran}P\cap\operatorname{ran}Q}.
\]

The dyadic tower separates the stable common-support sector from all transient prolate angles.

## Connection with the sewing term

Connes's nonpositive product trace differs from the positive triple feature by the off-diagonal sewing term. The defect tower does not identify that signed cross term, but it supplies the complete positive transition mass against which sewing must be compared.

At the observer-weighted level, a sharp contraction would have the form

\[
\boxed{
|\mathcal E_{\Lambda,S}(g)|
\le
\left(
\sum_{j\ge0}
\|\Phi_{\Lambda,j}^{tr}(g)\|_{HS}^2
\right)^{1/2}
\|\mathfrak h_{\Lambda,S}(g)\|,
}
\]

for a correctly typed opposite boundary feature `mathfrak h`. Constructing this pairing remains part of the boundary sewing theorem.

## Relation to bulk renormalization

The term `B^(2^n)` selects increasingly concentrated modes. At fixed `Lambda`, its limit is the true intersection projection, not the translation-volume bulk. As `Lambda->infinity`, the number of near-one prolate modes grows and the order of limits matters:

\[
n\to\infty
\qquad\text{versus}\qquad
\Lambda\to\infty.
\]

The volume counterterm lives in a joint scaling regime of near-one eigenvalues, while the fixed-cutoff `n->infinity` limit retains only exact eigenvalue one.

Therefore the dyadic tower solves positive typing but does not by itself compute the `2 log Lambda` subtraction.

## Two-parameter spectral scaling

A candidate bulk scale chooses `n=n(Lambda)` so that

\[
2^{n(\Lambda)}
\]

resolves eigenvalues at the prolate transition width. The residual tower below that scale is finite and positive; the surviving `B^(2^n)` feature carries concentrated bulk plus the exact Sonin intersection.

The choice must be derived from prolate eigenvalue asymptotics rather than imposed arbitrarily.

## Refinement consequence

The positive edge acquires a canonical multiscale refinement:

1. positive prolate feature `B^(1/2)A`;
2. first concentrated feature `BA`;
3. first transition defect;
4. iterated concentrated powers;
5. dyadic transition tower;
6. eigenvalue-one/Sonin limit;
7. joint cutoff--power bulk scaling;
8. boundary sewing.

This may be represented simplicially by a filtered/ind object rather than by finitely many ordinary nodes.

## Disposition

The observer-weighted positive prolate feature has the exact decomposition

\[
\boxed{
\|B^{1/2}A\|_{HS}^2
=
\|P_{\{1\}}(B)A\|_{HS}^2
+
\sum_{j\ge0}
\left\|
[B^{2^j}(I-B^{2^j})]^{1/2}A
\right\|_{HS}^2.
}
\]

This avoids the undefined bare semilocal transition trace and produces a canonical positive defect tower. The remaining gates are the joint `(Lambda,n)` bulk asymptotic and the identification of the signed sewing term with a contraction/pairing on this positive tower.
