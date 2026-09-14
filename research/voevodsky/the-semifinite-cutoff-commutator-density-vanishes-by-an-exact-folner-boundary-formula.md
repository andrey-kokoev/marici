# The semifinite cutoff-commutator density vanishes by an exact Folner boundary formula

## Setting

Let `G` be a unimodular locally compact group with Haar measure `mu`; the semilocal scaling group `C_S` is abelian and therefore amenable.

Let

\[
(\lambda(u)\xi)(x)
=
\xi(u^{-1}x)
\]

be the left regular representation on `L2(G)`. For

\[
g\in C_c(G),
\]

define

\[
A_g
=
\lambda(g)
=
\int_G
g(u)\lambda(u)du.
\]

For a finite-measure set `F subset G`, let

\[
P_F=M_{1_F}.
\]

## Exact commutator kernel

The convolution kernel of `A_g` is

\[
K_g(x,y)
=g(xy^{-1})
\]

under the displayed convention. Therefore the kernel of the commutator is

\[
\boxed{
K_{[P_F,A_g]}(x,y)
=
\left(
1_F(x)-1_F(y)
\right)
g(xy^{-1}).
}
\]

Its Hilbert--Schmidt norm is

\[
\begin{aligned}
\|[P_F,A_g]\|_{HS}^2
&=
\int_{G\times G}
|1_F(x)-1_F(y)|^2
|g(xy^{-1})|^2dxdy.
\end{aligned}
\]

Set `u=xy^(-1)`. Unimodularity gives

\[
\boxed{
\|[P_F,A_g]\|_{HS}^2
=
\int_G
|g(u)|^2
\mu
\left(
F\triangleuF
\right)
du.
}
\]

This identity is exact.

## Folner limit

Let `(F_n)` be a Folner sequence:

\[
\frac{
\mu(F_n\triangleuF_n)
}{
\mu(F_n)
}
\longrightarrow0
\]

uniformly for `u` in compact subsets of `G`.

If the support of `g` is contained in a compact set `K`, divide the exact identity by `mu(F_n)`:

\[
\frac{
\|[P_{F_n},A_g]\|_{HS}^2
}{
\mu(F_n)
}
=
\int_K
|g(u)|^2
\frac{
\mu(F_n\triangleuF_n)
}{
\mu(F_n)
}
du.
\]

Since the boundary ratio is at most `2`, dominated convergence gives

\[
\boxed{
\frac1{\mu(F_n)}
\|[P_{F_n},A_g]\|_{HS}^2
\longrightarrow0.
}
\]

## Fourier-cutoff insertion

Let `Q_n` be any orthogonal projection. Since left multiplication by a contraction does not increase Hilbert--Schmidt norm,

\[
\|Q_n[P_{F_n},A_g]\|_{HS}
\le
\|[P_{F_n},A_g]\|_{HS}.
\]

Hence

\[
\boxed{
\frac1{\mu(F_n)}
\|Q_n[P_{F_n},A_g]\|_{HS}^2
\longrightarrow0.
}
\]

No commutation between `Q_n` and `A_g` is required for this estimate.

## Uniformity on observer packets

Let `B` be a bounded packet of observers supported in one compact set `K` and bounded in `L2`. Then

\[
\sup_{g\in B}
\frac{
\|[P_{F_n},A_g]\|_{HS}^2
}{
\mu(F_n)
}
\le
\left(
\sup_{u\in K}
\frac{
\mu(F_n\triangle uF_n)
}{
\mu(F_n)
}
\right)
\sup_{g\in B}
\|g\|_2^2.
\]

Therefore convergence is uniform on such packets:

\[
\boxed{
\sup_{g\in B}
\frac1{\mu(F_n)}
\|Q_n[P_{F_n},A_g]\|_{HS}^2
\longrightarrow0.
}
\]

This is the bounded-packet form needed for functorial propagation.

## Logarithmic intervals

For the scaling line `G=R` in logarithmic coordinates, take

\[
F_L=[-L,L].
\]

For translation by `a`,

\[
\mu(F_L\triangle(F_L+a))
\le
2|a|
\]

when `L` is sufficiently large relative to `a`. Thus

\[
\frac{
\mu(F_L\triangle(F_L+a))
}{2L}
\le
\frac{|a|}{L}
\to0.
\]

With

\[
L=\log\Lambda,
\]

the volume is `2 log Lambda`, exactly Connes's counterterm scale.

## Annular channel

Let

\[
F_{L,M}^{ann}
=[-M,M]\setminus[-L,L],
\qquad
M>L.
\]

For `a` in a fixed compact set, its symmetric-difference boundary has uniformly bounded measure:

\[
\mu
\left(
F_{L,M}^{ann}
\triangle
(F_{L,M}^{ann}+a)
\right)
\le
4|a|.
\]

The annular volume is

\[
\mu(F_{L,M}^{ann})
=2(M-L).
\]

Consequently the annular windows form a Folner family precisely when

\[
\boxed{
M-L
\longrightarrow\infty.
}
\]

For the correlated power law

\[
R=\Lambda^\rho,
\qquad
\rho>1,
\]

one has

\[
M-L
=(\rho-1)\log\Lambda
\to\infty.
\]

Thus both inner and annular channel commutator densities vanish.

## Semilocal regular carrier

For `G=C_S`, choose compact-by-logarithmic Folner windows compatible with the module map

\[
\log|\cdot|_S:
C_S\to\mathbb R.
\]

The compact/norm-one directions are included in each window, while the module coordinate is truncated to `[-L,L]`. Translation by any element in a fixed compact observer support changes only a boundary strip of bounded logarithmic width.

Therefore

\[
\boxed{
\frac1{V_i}
\|Q_\Lambda[P_i,U_S(g)]\|_{HS}^2
\longrightarrow0
}
\]

for the inner and annular windows on the regular representation of `C_S`, uniformly on bounded compact-support observer packets.

## Effect on the bulk projection

Since

\[
QP_iA_g
=
QA_gP_i
+
Q[P_i,A_g],
\]

the normalized regulated channel and normalized right-compression bulk channel have the same trace-density class:

\[
\boxed{
V_i^{-1/2}QP_iA_g
-
V_i^{-1/2}QA_gP_i
\longrightarrow0
}
\]

in Hilbert--Schmidt norm.

Thus the channelwise bulk symbol is `QA_g` in the density quotient.

## Remaining representation gate

The proof above is exact for the regular scaling representation. Connes's geometric carrier is

\[
L^2(X_S),
\]

not simply one declared copy of `L2(C_S)`. To transfer the estimate, one still needs either:

1. a direct-integral decomposition of the `C_S` action on `L2(X_S)` with controlled multiplicity and decomposable cutoffs; or
2. a quotient-kernel proof reproducing the symmetric-difference estimate directly on a fundamental domain of `X_S`.

The orbit sum over `S`-units is the additional analytic datum. It cannot be discarded by calling the representation regular.

## Disposition

Bulk Gate A is proved on the regular semilocal scaling carrier:

\[
\boxed{
\frac1{V_i}
\|Q_\Lambda[P_i,U_S(g)]\|_{HS}^2
\to0.
}
\]

The proof is the exact Folner boundary formula

\[
\|[P_F,\lambda(g)]\|_{HS}^2
=
\int_G
|g(u)|^2
\mu(F\triangle uF)du.
\]

The sole remaining part of this gate is descent from the regular group carrier to the semilocal quotient carrier `L2(X_S)`.
