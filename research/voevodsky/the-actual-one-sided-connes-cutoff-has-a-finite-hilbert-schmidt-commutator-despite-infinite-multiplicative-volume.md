# The actual one-sided Connes cutoff has a finite Hilbert--Schmidt commutator despite infinite multiplicative volume

## Actual transformed cutoff

After the conull-orbit Radon--Nikodym identification, write the module coordinate as

\[
t=
\log|c|_S.
\]

Connes's physical cutoff

\[
P_\Lambda
=1_{\{|c|_S\le\Lambda\}}
\]

becomes the half-line projection

\[
\boxed{
P_L
=1_{(-\infty,L]},
\qquad
L=\log\Lambda.
}
\]

This set has infinite Haar measure. Therefore `A_gP_L` need not be Hilbert--Schmidt and cannot define the finite-window bulk isometry used in the auxiliary symmetric model.

However, the commutator only sees the symmetric difference of the half-line with its translates, and that difference has finite measure.

## Exact half-line boundary formula

On the logarithmic scaling line, let `A_k` be convolution by `k`. The commutator kernel is

\[
K_{[P_L,A_k]}(x,y)
=
\left(
1_{x\le L}
-
1_{y\le L}
\right)k(x-y).
\]

Set `u=x-y`. For each fixed `u`, the set of `y` on which the two indicators differ is an interval of length `|u|`. Hence

\[
\boxed{
\|[P_L,A_k]\|_{HS}^2
=
\int_\mathbb R
|u||k(u)|^2du.
}
\]

The expression is independent of `L`.

Thus, whenever

\[
\int|u||k(u)|^2du<\infty,
\]

the commutator is Hilbert--Schmidt even though both half-lines have infinite measure.

## Group form

Let

\[
\ell:G\to\mathbb R
\]

be the logarithmic module homomorphism and

\[
F_L
=
\{x:
\ell(x)\le L\}.
\]

For translation by `a`, the symmetric difference is a module strip of Haar measure proportional to

\[
|\ell(a)|,
\]

with the compact/norm-one fiber volume absorbed into the Haar normalization. Therefore

\[
\boxed{
\|[P_L,\lambda(g)]\|_{HS}^2
=
\int_G
|g(a)|^2
|\ell(a)|da
}
\]

on the regular semilocal carrier, subject to the standard compact-fiber normalization.

For compactly supported smooth `g`, the right-hand side is finite.

## Fourier projection

Since `Q_Lambda` is an orthogonal projection,

\[
\|Q_\Lambda[P_L,\lambda(g)]\|_{HS}
\le
\|[P_L,\lambda(g)]\|_{HS}.
\]

Consequently

\[
\boxed{
\frac1{2\log\Lambda}
\|Q_\Lambda[P_\Lambda,U_S(g)]\|_{HS}^2
\longrightarrow0.
}
\]

This proves the desired commutator-density estimate for the actual one-sided cutoff without assigning finite Haar volume to its range.

## Uniform observer packets

If a bounded observer packet `B` has common compact support `K`, then

\[
\sup_{g\in B}
\|[P_L,\lambda(g)]\|_{HS}^2
\le
\sup_{g\in B}
\|g\|_2^2
\sup_{a\in K}
|\ell(a)|.
\]

Thus the numerator is uniformly bounded in `L`, and division by `2L` gives uniform density convergence.

## Recentered boundary operator

Translate the single moving boundary `L` to zero. The commutator kernel becomes exactly

\[
\boxed{
H_k(X,Y)
=
\left(
1_{X\le0}
-
1_{Y\le0}
\right)k(X-Y).
}
\]

Unlike the symmetric interval model, there is only one physical-cutoff endpoint. Its norm is

\[
\boxed{
\|H_k\|_{HS}^2
=
\int|u||k(u)|^2du.
}
\]

Therefore the earlier two-ended interval calculation must not be assigned directly to Connes's `P_Lambda`. The second polarity/end comes from Fourier duality, inversion, or the opposite cutoff orientation, not from a second finite endpoint of `P_Lambda` itself.

## Annular regulator

The second-cutoff channel

\[
P_R-P_\Lambda

=
1_{(L,M]},
\qquad
M=\log R,
\]

has finite logarithmic Haar measure `M-L`. Its commutator has two boundary contributions, at `L` and `M`, and is covered by the finite-interval formula.

Thus the correct channel census is:

- inner one-sided channel: one physical boundary;
- finite annular channel: two physical boundaries;
- opposite/Fourier polarity: supplies the conjugate boundary structure.

## What this repairs

The cutoff-volume mismatch does not obstruct the **commutator-density estimate**. That estimate is now proved directly for the actual cutoff.

It still obstructs the previous **bulk right-compression isometry**, because

\[
A_gP_L
\]

is not Hilbert--Schmidt on an infinite half-line. The volume divergence `2 log Lambda` arises from the combined time--frequency product

\[
P_\Lambda Q_\Lambda,
\]

not from the physical projection alone.

Hence Bulk Gate A splits:

1. commutator-density part: solved;
2. positive bulk-isometry part for the actual product cutoff: still open.

## Correct next bulk feature

A valid bulk isometry must be constructed from the combined operator

\[
Q_\Lambda P_\Lambda
\]

or its positive triple compression

\[
P_\Lambda Q_\Lambda P_\Lambda,
\]

whose effective phase-space volume is finite and asymptotic to `2 log Lambda`.

The candidate GNS embedding should therefore use the square root

\[
\boxed{
(P_\Lambda Q_\Lambda P_\Lambda)^{1/2}
U_S(g)
}
\]

rather than `U_S(g)P_Lambda` alone.

Its squared norm is the positive trace

\[
\operatorname{Tr}
\left(
U_S(g)^*
P_\Lambda Q_\Lambda P_\Lambda
U_S(g)
\right).
\]

The difference between this positive triple-compression trace and Connes's product trace remains the sewing term.

## Disposition

For the actual one-sided cutoff,

\[
\boxed{
\|[P_\Lambda,U_S(g)]\|_{HS}^2
=
\int_{C_S}
|g(a)|^2
|\log|a|_S|d^*a,
}
\]

up to the fixed compact-fiber Haar normalization. This proves density-nullity after division by `2 log Lambda`.

The positive bulk construction must now be rebuilt from the finite phase-space operator `P_Lambda Q_Lambda P_Lambda`; the one-sided physical compression by itself cannot supply it.
