# The Schur function is meromorphic and needs the background determinant

## Correction to the spectral bridge

Let

\[
T=
\begin{pmatrix}
A_0&V\\
V^*&d
\end{pmatrix}
\]

be a self-adjoint bordered operator.  Away from the spectrum of \(A_0\), its
scalar Schur function is

\[
D(\lambda)
=
d-\lambda-V^*(A_0-\lambda)^{-1}V.
\]

This function is generally meromorphic.  Every eigenvalue of \(A_0\) seen by
the coupling \(V\) produces a pole.

Consequently an identity of the form

\[
\Xi(1/2+i\lambda)=u(\lambda)D(\lambda)
\]

with \(u\) holomorphic and nowhere zero cannot hold globally unless every
Schur pole is removable.  The completed \(\Xi\) section is entire, whereas a
nowhere-zero unit cannot cancel poles.

## Correct finite-dimensional identity

For finite blocks,

\[
\det(T-\lambda)
=
\det(A_0-\lambda)D(\lambda).
\]

The principal determinant cancels the Schur poles.  The full determinant is
the entire characteristic object, not \(D\) alone.

In infinite dimension the analogous statement requires a relative or
regularized determinant and explicit divisor bookkeeping.  One must track:

- poles of the Weyl or Schur function;
- zeros of the principal determinant;
- coupled eigenvalues of the full extension;
- uncoupled principal modes orthogonal to \(V\);
- regularization units and their zeros or poles.

## Minimal witness

Let \(A_0=(a)\), \(V=(v)\), and let the auxiliary scalar be \(d\).  Then

\[
D(\lambda)
=
d-\lambda-\frac{v^2}{a-\lambda}.
\]

For \(v\ne0\), \(D\) has a pole at \(\lambda=a\).  But

\[
(a-\lambda)D(\lambda)
=
(a-\lambda)(d-\lambda)-v^2
\]

is the polynomial \(\det(T-\lambda)\).  Its zeros are real because \(T\) is
self-adjoint.

This two-dimensional example disproves any unqualified entire identification
with the Schur function alone.

## Zero-to-state typing

Zeros of \(D\) away from \(\sigma(A_0)\) correspond to eigenstates with
nonzero auxiliary coordinate.  They do not automatically account for:

1. eigenstates inherited from \(A_0\) with \(V^*\psi=0\);
2. common zero-pole cancellations at principal eigenvalues;
3. modes introduced or removed by determinant regularization.

Therefore the two-way observation gate must be stated for a reduced full
determinant or an exact boundary incidence, not merely for the scalar Schur
zero set on its resolvent domain.

## Revised theta target

The source-derived spectralization may take one of two valid forms:

1. derive a regularized full characteristic determinant of the fixed
   self-adjoint extension and identify it with the framed \(\Xi\) section up to
   a nowhere-zero source unit;
2. derive a relative determinant in which the principal background divisor is
   explicitly divided out, while proving every resulting pole cancellation
   and excluded mode.

The second form cannot call the relative Schur factor entire unless the
background cancellation has already been included.

## Falsifiers

Reject the bridge when any of the following occurs:

1. a meromorphic Schur function is called entire without pole analysis;
2. a nowhere-zero unit is claimed to cancel a pole;
3. principal eigenmodes are omitted without a cyclicity or reduction theorem;
4. full and relative determinants are interchanged;
5. determinant regularization changes the divisor without explicit accounting.

