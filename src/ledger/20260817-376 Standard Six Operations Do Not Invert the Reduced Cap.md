# Standard Six Operations Do Not Invert the Reduced Cap

## Result

None of the standard coefficient operations attached only to the divisor
\(i:V(x_3)\hookrightarrow\operatorname{Spec}R\) and its complement
\(j:D(x_3)\hookrightarrow\operatorname{Spec}R\) turns Entry 375's canonical
map

\[
\phi_{\mathrm{loc}}:
D_x:=R\operatorname{Hom}_R(R[x^{-1}],R)
\longrightarrow R
\]

into an isomorphism of retained rank-one lines.  Ordinary restriction,
extraordinary restriction, open localization, and local cohomology all leave
different images on the two sides.

Thus the required physical coefficient operation is not one of these
functors by itself.  A Verdier quotient by
\(R\operatorname{Hom}_R(R[x^{-1}]/R,R)\) would invert the map formally, but
using that quotient is circular unless its kernel is independently selected
by the physical support or endpoint geometry.

## Coefficient normal form

As in Entry 375, first make the common \(D_{03}\) and \(x_1\) factors units:

\[
R=A[(D_{03}x_1)^{-1}],\qquad x=x_3.
\]

Assume the established normal-crossing coefficient regime: \(R\) is
Noetherian and \(x\)-adically separated, and \(x\) is a regular parameter.
The telescope calculation gives

\[
H^0(D_x)=0,\qquad
H^1(D_x)\cong\widehat R^{(x)}/R.
\]

Multiplication by \(x\) is an automorphism of
\(\widehat R^{(x)}/R\).  Surjectivity follows by removing the constant term
of a power series and dividing the remainder by \(x\); injectivity follows
from \(x\widehat R\cap R=xR\).  Hence the completion quotient is invisible
to closed-fibre Koszul restriction but is not zero.

## Closed restriction

Let \(k_x=R/(x)\).  Ordinary derived restriction gives

\[
i^*D_x=D_x\otimes_R^L k_x\simeq0,
\qquad
i^*R\simeq k_x.
\]

The first equality uses invertibility of \(x\) on the completion quotient.
Therefore \(i^*(\phi_{\mathrm{loc}})\) is \(0\to k_x\), not an identity.

Extraordinary restriction behaves similarly:

\[
i^!D_x=R\operatorname{Hom}_R(k_x,D_x)\simeq0,
\qquad
i^!R\simeq k_x[-1]
\]

up to the fixed Cartier convention.  It produces \(0\to k_x[-1]\), again
not an identity.

## Open localization

Because \(x\) already acts invertibly on the completion quotient,

\[
j^*D_x\simeq D_x,
\qquad
j^*R\simeq R[x^{-1}].
\]

The two objects remain in different cohomological and module types.  Open
localization does not turn \(\phi_{\mathrm{loc}}\) into a unit scalar.

## Local cohomology

The completion quotient is \(x\)-local, so

\[
R\Gamma_{(x)}D_x\simeq0,
\]

whereas the center has the usual nonzero local-cohomology object

\[
R\Gamma_{(x)}R\simeq
[R\longrightarrow R[x^{-1}]].
\]

Thus local cohomology also sends the cap to a zero-to-nonzero arrow.

## Residue is additional structure

The algebraic residue

\[
\operatorname{res}_x:
H^1_{(x)}(\omega_R)\longrightarrow\omega_{R/(x)}
\]

extracts the \(x^{-1}dx\) coefficient after a normal orientation is chosen.
It acts on the supported localization quotient, not directly as an
isomorphism \(D_x\to R\).  Entry 176 supplies precisely a framed normal
orientation, but it does not yet supply a functorial comparison that inserts
this residue into the reduced exceptional dualizing packet.

Accordingly “take the residue” is a promising construction target, not a
completed solution.

## Sharp categorical boundary

Let

\[
\mathcal N_x=
\operatorname{thick}\langle
R\operatorname{Hom}_R(R[x^{-1}]/R,R)
\rangle.
\]

In the Verdier quotient \(D(R)/\mathcal N_x\), the cone of
\(\phi_{\mathrm{loc}}\) vanishes, so \(\phi_{\mathrm{loc}}\) becomes an
isomorphism.  This is a formal universal property, not yet physical
authority for the quotient.  The next geometric construction must prove
that the endpoint/relative-normal realization factors through this quotient,
or produce a smaller framed residue functor with the same effect.

## Correct next experiment

Construct the Entry-176 normal cap as a morphism of the full localization
triangles, including the supported term
\(R[x^{-1}]/R\), and apply the oriented Cartier residue on that term.  Test
whether the resulting square:

1. is a chain map with the recorded shifts;
2. sends \(x^{-1}dx\) to the positive endpoint generator;
3. kills higher negative powers by boundary relations rather than decree;
4. retains the center and \(x_3\) incidence sectors;
5. factors through the physical endpoint/\(Q\) support independently of the
   desired unit conclusion.

Failure of item 3 leaves an infinite completion tail.  Failure of item 5
shows that the Verdier quotient was fitted to the answer.

## Evidence boundary

\`research/voevodsky/check_d03_physical_coefficient_functor_gate.rs\`
records the four functor images and verifies that neither side agrees under
any tested standard operation.  The algebraic conclusions use the telescope
description from Entries 367 and 375.  No framed residue square or physical
Verdier localization is constructed here.
