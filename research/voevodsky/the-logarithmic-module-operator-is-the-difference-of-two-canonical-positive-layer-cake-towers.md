# The logarithmic-module operator is the difference of two canonical positive layer-cake towers

## Signed local operator

The common semilocal operator is

\[
\mathcal L_S
=M_{-\log|x|_S}
\]

on the semilocal additive carrier. Its sign changes at the unit module shell

\[
|x|_S=1.
\]

Instead of splitting place by place, use the spectral calculus of the **total semilocal module**.

## Layer-cake identity

For every real number `r>0`,

\[
\boxed{
-\log r
=
\int_0^\infty
\left[
1_{\{r\le e^{-t}\}}
-
1_{\{r\ge e^t\}}
\right]dt.
}
\]

Indeed:

- if `0<r<1`, the first indicator is one for `0<=t<=-log r` and the second vanishes;
- if `r>1`, the second indicator is one for `0<=t<=log r` and the first vanishes;
- if `r=1`, both contribute only at a measure-zero endpoint.

## Two projection towers

Define the nested projections

\[
P_{S,t}^{in}
=
1_{\{|x|_S\le e^{-t}\}},
\]

\[
P_{S,t}^{out}
=
1_{\{|x|_S\ge e^t\}}.
\]

For `t>=0`, both are orthogonal projections. As `t` increases, their ranges decrease:

\[
P_{S,t_2}^{in}
\preceq
P_{S,t_1}^{in},
\qquad
P_{S,t_2}^{out}
\preceq
P_{S,t_1}^{out}
\qquad(t_2\ge t_1).
\]

They are disjoint away from the unit shell:

\[
P_{S,t}^{in}
P_{S,u}^{out}=0
\qquad(t,u>0).
\]

The logarithmic operator has the strong quadratic-form representation

\[
\boxed{
\mathcal L_S
=
\int_0^\infty
P_{S,t}^{in}dt
-
\int_0^\infty
P_{S,t}^{out}dt.
}
\]

## Positive and negative parts

The two integrals are precisely the spectral positive and negative parts:

\[
\boxed{
\mathcal L_S^+
=
\int_0^\infty
P_{S,t}^{in}dt
=M_{(-\log|x|_S)_+},
}
\]

\[
\boxed{
\mathcal L_S^-
=
\int_0^\infty
P_{S,t}^{out}dt
=M_{(\log|x|_S)_+}.
}
\]

Thus

\[
\mathcal L_S
=
\mathcal L_S^+
-
\mathcal L_S^-,
\qquad
\mathcal L_S^\pm
\succeq0.
\]

## Common Hilbert bulk

Let

\[
\mathfrak H_S
=
L^2
\left(
\mathbb R_+\times X_S,
dtd\mu_S(x)
\right).
\]

Define layer features

\[
(\Phi_S^{in}\psi)(t,x)
=
P_{S,t}^{in}\psi(x),
\]

\[
(\Phi_S^{out}\psi)(t,x)
=
P_{S,t}^{out}\psi(x).
\]

Then, on the form domain,

\[
\boxed{
\|\Phi_S^{in}\psi\|_{\mathfrak H_S}^2
=
\langle\psi,
\mathcal L_S^+\psi\rangle,
}
\]

\[
\boxed{
\|\Phi_S^{out}\psi\|_{\mathfrak H_S}^2
=
\langle\psi,
\mathcal L_S^-\psi\rangle.
}
\]

Therefore

\[
\boxed{
\langle\psi,
\mathcal L_S\psi\rangle
=
\|\Phi_S^{in}\psi\|^2
-
\|\Phi_S^{out}\psi\|^2.
}
\]

This is a canonical positive-minus-positive factorization in one common layer Hilbert space.

## Polarization

For two vectors `psi,phi`,

\[
\boxed{
\langle\psi,
\mathcal L_S\phi\rangle
=
\langle
\Phi_S^{in}\psi,
\Phi_S^{in}\phi
\rangle
-
\langle
\Phi_S^{out}\psi,
\Phi_S^{out}\phi
\rangle.
}
\]

No placewise orthogonalization occurs. The total module `|x|_S` is formed before the layer projections, retaining semilocal cross-place geometry.

## Counterdirection involution

Module inversion exchanges the two towers. Formally, let

\[
(J\psi)(x)
=
|x|_S^{-1/2}
\overline{\psi(x^{-1})}
\]

with the modular factor adjusted to the source Haar normalization. Then

\[
|x^{-1}|_S
=|x|_S^{-1},
\]

and consequently

\[
\boxed{
J P_{S,t}^{in}J^{-1}
=P_{S,t}^{out}.
}
\]

Hence

\[
J\mathcal L_SJ^{-1}
=-\mathcal L_S.
\]

This gives the two polarities intrinsically:

\[
\text{inside layers}
\longleftrightarrow
\text{outside layers}.
\]

## Relation to the cutoff pair

Connes's physical cutoff projection is a finite module interval. In logarithmic coordinates, it is assembled from the same layer projections. Its Fourier conjugate supplies the transverse tower

\[
\widehat P_{S,t}
=F_SP_{S,t}F_S^{-1}.
\]

Thus the layer-cake factorization and the Halmos two-projection colligation use the same geometric ingredients:

- module filtration;
- Fourier-dual filtration;
- inside/outside polarity;
- angle operator between the two filtrations.

This is the natural setting for the two coherence planes.

## Observer form

For a positive convolution observer

\[
A_g=U_S(g)U_S(g)^*,
\]

the local Weil pairing is distributionally

\[
\operatorname{Tr}_{rel}
(A_g\mathcal L_S).
\]

The layer decomposition gives formally

\[
\boxed{
\operatorname{Tr}_{rel}
(A_g\mathcal L_S)
=
\int_0^\infty
\operatorname{Tr}_{rel}
(A_gP_{S,t}^{in})dt
-
\int_0^\infty
\operatorname{Tr}_{rel}
(A_gP_{S,t}^{out})dt.
}
\]

Each integrand is positive when represented by a legitimate positive trace/compression. The sign is entirely the difference between the two polarity towers.

Trace-classness and interchange of trace and integral require cutoff regularization; the identity is first a quadratic-form/layer-cake statement.

## Exact remaining contraction

Rung-four positivity would follow from an isometry or contraction

\[
\boxed{
\mathcal C_S:
\overline{
\Phi_S^{out}
\mathcal D_{phys}
}
\longrightarrow
\overline{
\Phi_S^{in}
\mathcal D_{phys}
}
}
\]

such that

\[
\Phi_S^{out}\psi
=
\mathcal C_S
\Phi_S^{in}\psi
\]

for every physical completed observer `psi`, after endpoint--gamma boundary sewing.

Then

\[
\|\Phi_S^{out}\psi\|^2
\le
\|\Phi_S^{in}\psi\|^2
\]

and the completed logarithmic form is positive.

This contraction cannot hold on the unrestricted semilocal Hilbert space, since inversion exchanges the two sectors symmetrically. It must use the physical convolution-square subspace and global boundary condition.

## Eight-node interpretation

The layer parameter gives a canonical geometric refinement of the signed local operator:

1. total module;
2. logarithmic generator;
3. inside spectral projections;
4. outside spectral projections;
5. common layer Hilbert space;
6. primal/contra feature maps;
7. boundary sewing contraction;
8. positive defect norm.

The first six stages are unconditional. Stages seven and eight are exactly the rung-four filler.

## Disposition

The signed semilocal logarithmic operator has a canonical two-polarity realization:

\[
\boxed{
M_{-\log|x|_S}
=
(\Phi_S^{in})^*
\Phi_S^{in}
-
(\Phi_S^{out})^*
\Phi_S^{out}.
}
\]

This supplies one common positive Hilbert bulk and two nested countertowers exchanged by module inversion. The sole remaining positivity datum is a source-derived contraction sewing the outside feature into the inside feature on the completed physical observer space.
