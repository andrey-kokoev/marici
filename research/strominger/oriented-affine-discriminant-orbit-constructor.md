# The oriented affine-discriminant orbit constructor

## Objective

Construct one source object that produces both the modulus-seven coefficient
module and the anti-diagonal reachable route image, without choosing either
feature after inspection.

## Affine cocircuit frame

The universal preferred-row vector is

\[
v_g=(2g+7,3g+7).
\]

Regard this as evaluation of the integral affine frame

\[
F=
\begin{pmatrix}
2&7\\
3&7
\end{pmatrix}
\]

on the grade vector \((g,1)^T\).  Since the entries of \(F\) have unit gcd
and

\[
\det F=-7,
\]

its cokernel is canonically a cyclic group of order seven:

\[
D_F=\operatorname{coker}F\cong\mathbb Z/7.
\]

The functional

\[
\ell(x,y)=3x-2y\pmod7
\]

annihilates both columns of \(F\) modulo seven and therefore supplies a
faithful coordinate on \(D_F\).

No prime was selected externally.  The modulus is the discriminant of the
source-derived affine coefficient frame.

## Reflection-orbit incidence

Let \(O=\{+,-\}\) be a free two-sheet reflection orbit.  Its reduced integral
zero-chain module is

\[
\widetilde{\mathbb Z}[O]
=\ker\left(\epsilon:\mathbb Z[O]\to\mathbb Z\right)
=\mathbb Z(1,-1).
\]

The anti-diagonal is therefore not selected as a convenient subspace.  It is
the reduced boundary module of the source orbit.

## Single combined constructor

Define the oriented affine-discriminant orbit object

\[
\mathcal A_F(O)
=D_F\otimes_{\mathbb Z}\widetilde{\mathbb Z}[O].
\]

Then

\[
\mathcal A_F(O)
\cong
\{(x,-x):x\in\mathbb Z/7\}
\subseteq
(\mathbb Z/7)^2.
\]

This one constructor produces both requested features:

- \(D_F\) produces the modulus-seven coefficient object;
- reduced orbit incidence produces the anti-diagonal reachable image.

The common-mode annihilator and the contextual quotient follow automatically:

\[
\operatorname{Hom}((\mathbb Z/7)^2,\mathbb Z/7)
\big/operatorname{Ann}(\mathcal A_F(O))
\cong\mathbb Z/7.
\]

## Canonical comparison at exceptional grades

When \(7\mid g\), write

\[
w_g=\frac{v_g}{7}.
\]

Then

\[
7w_g=v_g=F(g,1)^T
\]

and

\[
\ell(w_g)=1\pmod7.
\]

Hence the class of \(w_g\) generates \(D_F\).  It also generates the
ray-content quotient

\[
\operatorname{Sat}(\mathbb Zv_g)/\mathbb Zv_g.
\]

This gives a canonical gradewise comparison between the universal affine
discriminant and the previously observed projective \(\mathbb Z/7\) residue.
For the admissible even locus, these grades satisfy \(14\mid g\).

## Hostile controls

The construction rejects three nearby fitted explanations.

1. Keeping the unreduced orbit module produces forty-nine route values and
   does not force the anti-diagonal.
2. A fixed one-point orbit has zero reduced module, so the sign route is
   structurally absent.  This matches the fixed-orbit tower mechanism.
3. Changing the affine offset changes the determinant and therefore changes
   the coefficient modulus.  Seven is not retained by convention.

## Authority audit

The two inputs are separately source-derived:

- the affine frame is extracted from the proved universal cocircuit law;
- the free reflection orbit and its exchange action are extracted from the
  completed parity-helicity representation.

What is not yet constructed is a comparison map placing their tensor product
inside the same magnetic source object:

\[
\chi_g:
D_F\otimes\widetilde{\mathbb Z}[O]
\longrightarrow
\text{the seven-primary boundary or physical route packet at grade }g.
\]

The map must intertwine reflection, the boundary matrix, and the fixed
integral normalization.  Without \(\chi_g\), the constructor is an exact
associated combinatorial object, not yet an executable physical magnetic
sector.

The smallest remaining theorem is therefore precise: construct \(\chi_g\) or
prove that the completed parity action descends to the affine-discriminant
grade.  A dimension or cardinality match is insufficient.
