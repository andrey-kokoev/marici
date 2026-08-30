# The Clark polarization is functorial only for conformal form-preserving constructors

## Question

When can an ordered constructor acting on the Clark first jet be replaced by
a scalar action on the polarization line under composition?

## Hermitian Green lens

Let (V=\mathbb C^2) carry the nondegenerate Hermitian Clark form

\[
\Delta=
\begin{pmatrix}
0&2ia\\
-2ia&0
\end{pmatrix},
\qquad a\ne0.
\]

An invertible constructor (A:V\to V) acts on the polarized relation by

\[
\omega(Ax,Ay)=x^*A^*\Delta Ay.
\]

This action descends to multiplication by one scalar on the relation line if
and only if there exists a nonzero real multiplier (chi(A)) such that

\[
A^*\Delta A=\chi(A)\Delta.
\]

These are the conformal automorphisms of the indefinite Hermitian form.

## Composition cocycle

If (A) and (B) satisfy the conformal law, then

\[
(AB)^*\Delta(AB)
=\chi(A)\chi(B)\Delta.
\]

Hence

\[
\chi(AB)=\chi(A)\chi(B).
\]

The scalar relation line is functorial on this admitted constructor group.
The multiplier is a character, not an arbitrary normalization at each step.

Taking determinants gives the necessary constraint

\[
|\det A|^2=\chi(A)^2.
\]

Therefore

\[
|\chi(A)|=|\det A|.
\]

The determinant magnitude alone does not determine the sign of the Hermitian
multiplier.

## Bilinear determinant lens

Let

\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

For every complex (2\times2) matrix (A),

\[
A^TJA=(\det A)J.
\]

Thus the bilinear determinant line is automatically functorial for every
invertible complex-linear constructor, with multiplier (det A).

This law is not the Hermitian Green law. Replacing transpose by adjoint
changes the admitted constructor class. Conflating the two silently discards
conjugation and physical supply-rate typing.

## Ordered lens

If

\[
A^*\Delta A
\]

is not proportional to (Delta), the Hermitian scalar polarization does not
carry the constructor. The transformed form has new matrix information. The
full jet and ordered action of (A) must remain available.

Therefore the three outcomes are:

1. determinant-line descent for every invertible (2\times2) complex map;
2. Hermitian-current descent only for conformal form-preserving maps;
3. ordered-carrier retention for all other admitted constructors.

## Noninvertible maps

A singular map acts on the bilinear determinant line by zero. It destroys
oriented area and cannot be a faithful transport. Likewise, a conformal
Hermitian multiplier must be nonzero when (Delta) is nondegenerate.

Thus constructor equivalence on the polarization line is naturally an
invertible-sector statement. Singular operations require explicit kernel
typing.

## Theta compiler test

For each source-authorized theta constructor (A_C) acting on ((F,F')),
compute

\[
R_C=A_C^*\Delta A_C.
\]

Then classify:

- (R_C=\chi_C\Delta): the Hermitian seam current composes by the multiplier
  (chi_C);
- (A_C^TJA_C=(\det A_C)J) only: determinant phase descends, but the Green
  current does not;
- neither scalar representation is the required downstream target: retain
  the ordered jet action.

The multiplier must also respect cutoff and Fourier--Tate composition. A
cutoff-dependent rescaling that repairs each matrix separately is not a
cocycle.

## Network consequence

The polarization line can serve as a functor on a network only after every
edge constructor has passed the same conformal test and the multipliers obey
the composition character. Otherwise scalar-coherent edges may fail
closure-coherence around a path or associator cell.

This is the precise sense in which the additional network tower exposes
composition capability rather than merely closing a local residue.

## Falsifier certificate

    {
      "code": "clark_polarization_not_functorial_for_constructor",
      "constructor": "A_C",
      "residual": "A_C^* Delta A_C - chi_C Delta",
      "scalar_multiplier_exists": false,
      "determinant_lens_may_still_descend": true,
      "ordered_jet_required": true
    }

## Disposition

The Clark relation line is a genuine compositional functor only on the
conformal form-preserving constructor group. The bilinear determinant line
has a broader determinant law, while general source constructors require the
ordered jet carrier.

## Claim boundary

This theorem classifies finite-dimensional linear constructor actions on the
first jet. It does not establish that the actual Fourier--Tate, Clark,
arithmetic, or completion maps are bounded invertible matrices on this
module; those matrices and domains must be supplied source-first.
