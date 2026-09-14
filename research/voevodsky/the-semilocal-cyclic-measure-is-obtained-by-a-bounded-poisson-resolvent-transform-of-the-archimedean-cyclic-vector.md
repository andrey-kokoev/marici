# The semilocal cyclic measure is obtained by a bounded Poisson-resolvent transform of the archimedean cyclic vector

## Archimedean cyclic pair

Let

\[
X=M_t
\]

on

\[
H_\infty=L^2(\mathbb R,dm_\infty),
\]

with cyclic vector

\[
\mathbf1(t)=1.
\]

Its spectral measure is `dm_infinity`:

\[
\langle\mathbf1,
f(X)\mathbf1\rangle
=
\int f(t)dm_\infty(t).
\]

## One-prime Poisson resolvent

For a prime `p`, put

\[
r_p=p^{-1/2},
\qquad
\ell_p=\log p,
\qquad
U_p=e^{i\ell_pX}.
\]

The operator `U_p` is unitary. Since `r_p<1`, the resolvent

\[
I-r_pU_p
\]

is boundedly invertible. Define

\[
\boxed{
B_p
=
\frac{
\sqrt{1-r_p^2}
}{I-r_pU_p}.
}
\]

Then

\[
B_p^*B_p
=
(1-r_p^2)
(I-r_pU_p^*)^{-1}
(I-r_pU_p)^{-1}.
\]

In the spectral representation of `X`, this is multiplication by the Poisson kernel:

\[
\boxed{
B_p^*B_p
=
P_{r_p}(\ell_pX).
}
\]

## Euler-weighted cyclic measure

The finite Euler density is

\[
|L_p(1/2-it)|^2
=
\frac1{1-r_p^2}
P_{r_p}(t\ell_p).
\]

Therefore, with

\[
\widetilde B_p
=
(1-r_p^2)^{-1/2}B_p
=
(I-r_pU_p)^{-1},
\]

one has

\[
\boxed{
\langle
\widetilde B_p\mathbf1,
f(X)
\widetilde B_p\mathbf1
\rangle
=
\int f(t)
|L_p(1/2-it)|^2
dm_\infty(t).
}
\]

Thus adjoining a finite prime does not require reconstructing a new measure abstractly. It replaces the cyclic vector by the explicit bounded resolvent vector

\[
\mathbf1_p
=
(I-p^{-1/2}e^{i(\log p)X})^{-1}
\mathbf1.
\]

## Finite prime set

Because all `U_p` are functions of the same self-adjoint operator `X`, they commute. Define

\[
\boxed{
\widetilde B_S
=
\prod_{p\in S}
(I-p^{-1/2}e^{i(\log p)X})^{-1}.
}
\]

Then

\[
\mathbf1_S
=
\widetilde B_S\mathbf1
\]

has spectral measure

\[
\boxed{
dm_S
=
\prod_{p\in S}
|L_p(1/2-it)|^2
dm_\infty.
}
\]

This is an exact common-carrier realization of every finite semilocal cyclic measure.

## Prime-power expansion

The resolvent has the norm-convergent Neumann series

\[
\boxed{

(I-r_pU_p)^{-1}
=
\sum_{k\ge0}r_p^kU_p^k.
}
\]

Hence

\[
\mathbf1_p
=
\sum_{k\ge0}
p^{-k/2}
e^{ik(\log p)X}
\mathbf1.
\]

The operator powers

\[
U_p^k
=e^{ik(\log p)X}
\]

are exactly the spectral modulations corresponding in physical logarithmic coordinates to translations by

\[
k\log p.
\]

Thus the complete prime-power tower appears inside one bounded cyclic-vector transform.

## Contratower

The reciprocal orientation is

\[
\widetilde B_S^\#
=
\prod_{p\in S}
(I-p^{-1/2}e^{-i(\log p)X})^{-1}
=
\widetilde B_S^*.
\]

Their relative phase is

\[
\widetilde B_S
(\widetilde B_S^*)^{-1}
=
\prod_{p\in S}
\frac{1-p^{-1/2}e^{-i(\log p)X}}
     {1-p^{-1/2}e^{i(\log p)X}},
\]

which is the Euler scattering multiplier `J_S` in functional-calculus form, up to orientation.

The positive metric and the scattering phase are therefore the modulus and phase of the same resolvent product.

## Polynomial filtration

The semilocal orthogonal polynomials are obtained by Gram--Schmidt from

\[
\mathbf1_S,

X\mathbf1_S,

X^2\mathbf1_S,
\ldots
\]

inside the fixed archimedean Hilbert space. Since `B_S` commutes with `X`,

\[
X^n\mathbf1_S
=
\widetilde B_SX^n\mathbf1.
\]

Therefore the degree-`n` cyclic subspace is exactly

\[
\boxed{
\mathcal P_{n,S}
=
\widetilde B_S\mathcal P_{n,\infty},
}
\]

where

\[
\mathcal P_{n,\infty}
=
\operatorname{span}
\{\mathbf1,X\mathbf1,\ldots,X^n\mathbf1\}.
\]

This recovers the source statement that the polynomial filtrations correspond under a nonunitary semilocal map.

## Why the degree operator is not intertwined

Although `B_S` maps every filtration onto the corresponding filtration, it is not unitary in the archimedean metric. Gram--Schmidt after applying `B_S` changes the orthogonal complements of successive filtration levels. Hence

\[
N_S\widetilde B_S
\ne
\widetilde B_SN_\infty.
\]

The mismatch is entirely due to the nonorthogonality introduced by the positive Poisson metric

\[
G_S=
\widetilde B_S^*\widetilde B_S.
\]

## Explicit Gram matrices

Let `P_n^infinity` be the archimedean orthonormal polynomial basis. The semilocal moment/Gram matrix in this fixed basis is

\[
\boxed{
(G_S)_{mn}
=
\langle
P_m^\infty,
\widetilde B_S^*\widetilde B_S
P_n^\infty
\rangle.
}
\]

Using the Neumann expansion, every entry is an absolutely convergent sum of scaling-group matrix coefficients:

\[
(G_S)_{mn}
=
\sum_{\mathbf k,\mathbf l\ge0}

a_{\mathbf k}
a_{\mathbf l}
\langle
P_m^\infty,
 e^{i(\omega_{\mathbf k}-\omega_{\mathbf l})X}
P_n^\infty
\rangle.
\]

This replaces unstable recovery from moments by explicit matrix coefficients of the known archimedean scaling representation.

## Cholesky realization of the semilocal degree operator

On each finite polynomial block, let

\[
G_{S,n}=R_{S,n}^*R_{S,n}
\]

be the canonical positive Cholesky factorization. The orthonormal semilocal polynomial basis is obtained by the triangular change of basis `R_S,n^(-1)`.

Passing consistently through the nested blocks gives a triangular operator `R_S`, and the transported degree operator is

\[
\boxed{
\widetilde N_S
=
R_S^{-1}
N_\infty
R_S
}
\]

on the polynomial core, with adjoint/domain corrections determined by the chosen fixed-Hilbert-space convention.

Thus the missing prolate curvature is computable from the Cholesky factor of the explicit Poisson-resolvent Gram operator.

## Trace-ideal target

The problem is now reduced to estimating the off-diagonal decay of

\[
G_S-I
\]

and its Cholesky factor in the Meixner--Pollaczek/Hermite polynomial basis. A sufficient route is:

1. compute or bound
   \[
   \langle P_m^\infty,
e^{i\omega X}
P_n^\infty\rangle;
   \]
2. sum those bounds with the geometric Euler coefficients;
3. prove that `R_S-I` belongs to a weighted Schatten class;
4. deduce relative trace-ideal control of
   \[
   R_S^{-1}N R_S-N.
   \]

Unlike raw moment comparison, every step now preserves positivity and prime correlation.

## Disposition

The semilocal cyclic measure and its polynomial filtration admit an exact common-carrier realization:

\[
\boxed{
\mathbf1_S
=
\prod_{p\in S}
(I-p^{-1/2}e^{i(\log p)X})^{-1}
\mathbf1.
}
\]

This operator is bounded and boundedly invertible for every finite `S`, contains all prime powers through a norm-convergent Neumann series, and generates the semilocal Gram matrix explicitly. The remaining analysis is a Cholesky/Schatten estimate in the known archimedean orthogonal-polynomial basis.
