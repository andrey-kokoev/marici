# Joint Heat--Dilation Naturality Rigidifies the Even Source

Status: superseded by
`joint-mellin-character-and-heat-naturality-generate-the-weyl-tower.md`.
The scalar-commutant conclusion was correct, but this packet mis-typed source
scale transport as $z\partial_z$. Mellin transformation actually sends
source dilation to multiplication by the centered Mellin character. The
correct coherence is a three-rung Weyl tower, not the affine relation claimed
below. This file is retained as the explicit scope-correction witness.

Author: `marici.Grothendieck`

Date: 2026-08-28

## Motivation

Heat naturality alone does not determine the theta source. Every
constant-coefficient operator $P(\partial_z)$ commutes with the heat
generator $L=\partial_z^2$, and some such operators change the divisor
while preserving evenness and reality.

The lattice-scale groupoid supplies a second independent constructor:
dilation. Its infinitesimal generator on analytic readouts is

\[
D=z\partial_z.
\]

The relevant question is the joint commutant of $D$ and $L$, not either
commutant separately.

## Theorem

Let $T$ be a linear endomorphism of the even polynomial core
$\mathbb C[z^2]$. Suppose

\[
[T,D]=0
\]

and

\[
[T,L]=0.
\]

Then $T$ is scalar.

The same conclusion extends to an admitted even entire-function completion
whenever $T$ is continuous there and polynomials are dense.

## Proof

The dilation generator has simple spectrum on the even monomial basis:

\[
D z^{2n}=2n z^{2n}.
\]

Commutation with $D$ therefore forces

\[
Tz^{2n}=c_nz^{2n}.
\]

For $n\ge1$,

\[
Lz^{2n}=2n(2n-1)z^{2n-2}.
\]

Now $TL=LT$ gives

\[
c_{n-1}2n(2n-1)z^{2n-2}
=
c_n2n(2n-1)z^{2n-2},
\]

so $c_n=c_{n-1}$. Induction gives $c_n=c_0$ for every $n$, hence

\[
T=c_0I.
\]

## Semidirect coherence

The two constructors do not commute with each other:

\[
[D,L]=-2L.
\]

Equivalently,

\[
e^{uD}e^{tL}e^{-uD}=e^{e^{-2u}tL}.
\]

This is not a defect. It is the exact coherence cell connecting scale
transport and heat transport. The source carries a representation of this
semidirect two-parameter dynamics.

## Consequence for hostile endomorphisms

The earlier heat-natural witness

\[
T_{N,c}=I+c\partial_z^{2N}
\]

commutes with $L$ but not with $D$:

\[
[D,T_{N,c}]=-2Nc\partial_z^{2N}.
\]

Thus it is rejected by the combined source constructors before any zeros are
examined. More generally, every nonconstant constant-coefficient
differential reweighting fails joint naturality.

This strengthens canonical-section rigidity:

- heat dynamics forbid divisor-bearing scalar gauges;
- joint heat--dilation dynamics also forbid divisor-changing source
  endomorphisms on the even sector;
- after fixing normalization, the only natural automorphism is the identity.

## What this does and does not prove

This is a genuine source-provenance theorem. The dilation came from the
lattice-scale orbit and the heat generator from the Gaussian vacuum; neither
was fitted to the divisor.

It still does not prove RH. Joint naturality determines which section is the
authorized one, but it does not prove that the authorized section has no
off-seam zeros. The remaining problem is no longer source ambiguity. It is a
global incidence theorem for the uniquely selected framed section.

The sharp next question is whether the semidirect coherence
$[D,L]=-2L$, when lifted to the determinant-framed Evans boundary system,
produces a conserved two-dimensional current whose flux can enter only
through the reciprocal seam or the all-scale infinity germ.
