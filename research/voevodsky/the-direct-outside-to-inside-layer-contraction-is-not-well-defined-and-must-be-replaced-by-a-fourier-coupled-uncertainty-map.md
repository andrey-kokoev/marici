# The direct outside-to-inside layer contraction is not well-defined and must be replaced by a Fourier-coupled uncertainty map

## Proposed contraction

The layer-cake factorization suggested a map

\[

\mathcal C_S:
\overline{\Phi_S^{in}\mathcal D}
\to
\overline{\Phi_S^{out}\mathcal D}
\]

such that

\[
\Phi_S^{out}\psi
=
\mathcal C_S
\Phi_S^{in}\psi.
\]

Before testing its norm, one must test whether it is well-defined.

## Explicit layer norms

The layer features satisfy

\[
\boxed{
\|\Phi_S^{in}\psi\|^2
=
\int_{|x|_S<1}
(-\log|x|_S)
|\psi(x)|^2d\mu_S(x),
}
\]

\[
\boxed{
\|\Phi_S^{out}\psi\|^2
=
\int_{|x|_S>1}
(\log|x|_S)
|\psi(x)|^2d\mu_S(x).
}
\]

Thus

\[
\ker\Phi_S^{in}
=
\{\psi:
\psi=0
\text{ almost everywhere on }|x|_S<1\},
\]

while

\[
\ker\Phi_S^{out}
=
\{\psi:
\psi=0
\text{ almost everywhere on }|x|_S>1\}.
\]

## Douglas well-definedness criterion

A linear rule

\[
\Phi^{in}\psi
\longmapsto
\Phi^{out}\psi
\]

is well-defined on a subspace `D` only if

\[
\boxed{
\ker(\Phi^{in}|_\mathcal D)
\subseteq
\ker(\Phi^{out}|_\mathcal D).
}
\]

On the unrestricted semilocal Hilbert space this fails immediately. Choose a nonzero vector supported in

\[
|x|_S>1.
\]

Then

\[
\Phi^{in}\psi=0,
\qquad
\Phi^{out}\psi\ne0.
\]

Therefore

\[
\boxed{
\text{no direct outside-from-inside operator exists on the full carrier}.}
\]

This failure precedes contractivity.

## Endpoint coordinates cannot repair the kernel failure

Adding finitely many endpoint evaluations to the input feature gives

\[
(\Phi^{in}\psi,E_+\psi,E_-\psi).
\]

The subspace of outside-supported vectors annihilating two fixed linear functionals remains infinite-dimensional. Hence one can choose nonzero `psi` with

\[
\Phi^{in}\psi=0,
\qquad
E_+\psi=E_-\psi=0,
\qquad
\Phi^{out}\psi\ne0.
\]

Thus a rank-two endpoint extension cannot make the direct layer map well-defined.

## Fourier-dual feature

The cutoff geometry provides another positive tower:

\[
\widehat P_{S,t}^{in}
=
F_SP_{S,t}^{in}F_S^{-1}.
\]

Define

\[
(\widehat\Phi_S^{in}\psi)(t,x)
=
P_{S,t}^{in}F_S\psi(x).
\]

The natural positive input feature is therefore

\[
\boxed{
\mathcal A_S\psi
=
\Phi_S^{in}\psi
\oplus
\widehat\Phi_S^{in}\psi.
}
\]

A function cannot generally be supported entirely outside the unit module ball in both physical and Fourier variables. This is the Sonin/uncertainty mechanism missing from the direct layer split.

## Correct kernel test

A candidate map

\[
\mathcal A_S\psi
\longmapsto
\Phi_S^{out}\psi
\]

is well-defined only if

\[
\boxed{
\ker
\Phi_S^{in}
\cap
\ker
\widehat\Phi_S^{in}
\subseteq
\ker
\Phi_S^{out}
}
\]

on the physical observer subspace.

But the semilocal Sonin space is specifically made of vectors with simultaneous physical and Fourier gaps near zero. Such vectors lie in the kernel of both inside features while remaining nonzero outside. Therefore even the doubled map fails on the full Sonin space if its output is the entire outside feature.

This shows that the Sonin space should be quotiented, projected, or assigned to the harmonic boundary rather than subjected to the same contraction.

## Required decomposition

Let

\[
\mathcal S_S
=
\ker\Phi_S^{in}
\cap
\ker\widehat\Phi_S^{in}
\]

be the relevant Sonin sector. Decompose

\[
\mathcal H_S
=
\mathcal S_S
\oplus
\mathcal S_S^\perp.
\]

The contraction can only be sought on `S_S^perp`:

\[
\boxed{
\Phi_S^{out}P_{\mathcal S_S^\perp}
=
\mathcal C_S
\left(
\Phi_S^{in}

y\oplus
\widehat\Phi_S^{in}
\right)
P_{\mathcal S_S^\perp}.
}
\]

The Sonin component must be retained separately as a harmonic/prolate boundary sector.

## Logarithmic uncertainty form

The corresponding norm inequality is a semilocal logarithmic uncertainty inequality. Schematically it compares

\[
\int
\log|x|_S
|\psi(x)|^2

d\mu_S(x)
\]

with the analogous integral for `F_S psi`, plus a source-fixed constant and endpoint correction.

At the archimedean place this is related to the classical logarithmic uncertainty principle and to the Connes--Consani positive trace identity. Finite places must enter through the common semilocal Fourier transform.

## Revised positive architecture

The local logarithmic operator provides two polarities, but positivity requires four coupled features:

\[
\boxed{
\text{physical inside/outside}
\quad\times\quad
\text{Fourier inside/outside}.
}
\]

Their pair-of-projections geometry is exactly the Halmos/prolate colligation. The Sonin space is the common-gap harmonic sector, and endpoint data must be sewn to that sector rather than expected to control all outside layers.

## Disposition

The direct contraction

\[
\Phi^{out}
=

\mathcal C\Phi^{in}
\]

is not well-defined. Neither a finite endpoint extension nor simple Fourier doubling repairs it on the Sonin sector.

The correct target is a Fourier-coupled logarithmic uncertainty inequality on the orthogonal complement of the Sonin space, with the Sonin component retained as the separate harmonic boundary of the completed pyramid.
