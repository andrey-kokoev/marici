# The logarithmic cutoff commutator has a two-ended Hankel boundary limit after recentering

## Why density zero is not boundary zero

For a logarithmic interval

\[
F_L=[-L,L],
\qquad
P_L=1_{F_L},
\]

the normalized commutator density satisfies

\[
\frac1{2L}
\|[P_L,A_k]\|_{HS}^2
\to0.
\]

However, its unnormalized Hilbert--Schmidt norm generally has a nonzero limit. The mass is concentrated near the two moving endpoints `-L` and `+L`.

A boundary limit therefore requires recentering each endpoint before sending `L` to infinity.

## Exact norm formula on the line

Let `A_k` be convolution by `k` on `L2(R)`, with

\[
\int_\mathbb R
|u||k(u)|^2du
<\infty.
\]

The Folner boundary formula gives

\[
\|[P_L,A_k]\|_{HS}^2
=
\int_\mathbb R
|k(u)|^2
\left|
[-L,L]\triangle([-L,L]+u)
\right|du.
\]

For fixed `u` and `L>|u|/2`,

\[
\left|
[-L,L]\triangle([-L,L]+u)
\right|
=2|u|.
\]

Dominated convergence therefore yields

\[
\boxed{
\lim_{L\to\infty}
\|[P_L,A_k]\|_{HS}^2
=
2
\int_\mathbb R
|u||k(u)|^2du.
}
\]

For compactly supported `k`, the equality is exact once `L` exceeds half the support diameter.

## Right-end boundary operator

Translate the right endpoint to zero:

\[
x=L+X,
\qquad
y=L+Y.
\]

Near `+L`, membership in `[-L,L]` becomes

\[
1_{\{X\le0\}}.
\]

The limiting commutator kernel is

\[
\boxed{
H_k^+(X,Y)
=
\left(
1_{\{X\le0\}}
-
1_{\{Y\le0\}}
\right)
k(X-Y).
}
\]

It is supported on pairs lying on opposite sides of zero. Its Hilbert--Schmidt norm is

\[
\boxed{
\|H_k^+\|_{HS}^2
=
\int_\mathbb R
|u||k(u)|^2du.
}
\]

This is a Hankel-type cross-boundary operator.

## Left-end boundary operator

Translate the left endpoint to zero:

\[
x=-L+X,
\qquad
y=-L+Y.
\]

Membership becomes `1_(X>=0)`, producing

\[
\boxed{
H_k^-(X,Y)
=
\left(
1_{\{X\ge0\}}
-
1_{\{Y\ge0\}}
\right)k(X-Y)
=-H_k^+(X,Y).
}
\]

The two signs refer to the same fixed coordinate orientation. The two operators occupy different endpoint copies of the boundary Hilbert space.

## Boundary Hilbert space

Define

\[
\boxed{
\mathcal H_{bdry}
=
\mathcal L^2_{cross}(\mathbb R_-\times\mathbb R_+)
\oplus
\mathcal L^2_{cross}(\mathbb R_+\times\mathbb R_-),
}
\]

or equivalently the direct sum of the two endpoint Hilbert--Schmidt cross-channel spaces.

The recentered commutator feature converges to

\[
\boxed{
\mathfrak h(k)
=
H_k^-
\oplus
H_k^+.
}
\]

Its norm is

\[
\boxed{
\|\mathfrak h(k)\|_{bdry}^2
=
2
\int_\mathbb R
|u||k(u)|^2du.
}
\]

Thus the boundary quadratic form is positive.

## Polarized boundary kernel

For `k_1,k_2` with finite first weighted moment,

\[
\boxed{
\langle
\mathfrak h(k_1),
\mathfrak h(k_2)
\rangle_{bdry}
=
2
\int_\mathbb R
|u|
\overline{k_1(u)}k_2(u)du.
}
\]

The boundary completion is therefore canonically isometric to

\[
L^2
\left(
\mathbb R,
2|u|du
\right)
\]

on the convolution-kernel source, while retaining two oriented endpoint realizations.

## Annular channel

For

\[
F_{L,M}^{ann}
=[-M,-L]
\cup
[L,M],
\]

there are four moving endpoints:

\[
-M,
-L,
L,
M.
\]

If

\[
L\to\infty,
\qquad
M-L\to\infty,
\]

and `k` has compact support, the four boundary neighborhoods are disjoint. After recentering, the annular commutator is the orthogonal direct sum of four half-line Hankel copies, with signs determined by entrance or exit orientation.

Hence

\[
\boxed{
\lim
\|[P_{L,M}^{ann},A_k]\|_{HS}^2
=
4
\int_\mathbb R
|u||k(u)|^2du.
}
\]

The annular positive completion therefore carries additional boundary channels as well as additional volume.

## Relation to orthogonal bulk removal

The exact bulk model uses right compression `A_kP_L`, while the cutoff feature contains `P_LA_k`. Their difference is

\[
[P_L,A_k].
\]

After removing the translation-density bulk, the surviving finite feature is precisely the recentered Hankel boundary operator.

Thus, in the elementary regular model,

\[
\boxed{
\text{orthogonal bulk residual}
=
\text{endpoint Hankel feature}
}
\]

up to the additional left Fourier cutoff and the exact projection convention.

## Fourier cutoff

If `Q_L` is translation invariant and converges strongly to `I`, then for a fixed Hilbert--Schmidt boundary operator

\[
\|(I-Q_L)H_k^\pm\|_{HS}
\to0.
\]

Consequently insertion of `Q_L` does not change the recentered limit in the elementary time--frequency model.

For Connes's transported semilocal Fourier projection, translation invariance on the logarithmic group is not established. Its action on the recentered boundary operators is therefore a separate prolate limit.

## Semilocal interpretation

The two logarithmic ends correspond to

\[
|x|_S\to0
\qquad\text{and}\qquad
|x|_S\to\infty.
\]

Module inversion exchanges them. This is the correct two-ended carrier for endpoint sewing.

The norm-one directions and `S`-unit quotient can contribute multiplicity to the boundary fibers even though they do not create multiplicity in the conull regular scaling action itself.

Thus the semilocal boundary should be a field of Hankel cross-channel spaces over the compact/norm-one quotient, not merely two scalar endpoint coordinates.

## Relation to the completed Weil form

The positive model boundary norm

\[
2\int|u||k(u)|^2du
\]

is not yet identified with the completed Weil quadratic form. It supplies the geometric boundary feature generated by cutoff noncommutation.

The remaining arithmetic theorem must compare its semilocal Fourier/prolate transform and Sonin-conditioned quotient with

\[
W_{completed,S}(g*g^*).
\]

## Disposition

On the logarithmic regular line, the boundary residual exists explicitly after recentering:

\[
\boxed{
[P_L,A_k]
\rightsquigarrow
H_k^-
\oplus
H_k^+.
}
\]

The bulk divergence and finite boundary have now been separated at feature level. The remaining gate is the semilocal prolate action of the transported Fourier cutoff on these Hankel boundary fibers and its identification with the completed Weil form.
