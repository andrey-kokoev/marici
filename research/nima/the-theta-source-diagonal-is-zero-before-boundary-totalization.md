# The theta source diagonal is zero before boundary totalization

## Homogeneous augmentation

The forced theta history

\[
(A-z)u=Vc
\]

is homogenized by adjoining a constant source coordinate \(c\).  The source
equation is

\[
\partial_qc=0
\]

or, after passing to the static source port,

\[
D_\theta c=0.
\]

Therefore the source-derived bulk theta diagonal is

\[
D_\theta(z)=0.
\]

It is not an unknown scalar constitutive law.

## Paired block

Adjoint completion gives the theta/history block

\[
\begin{pmatrix}
A-z&-V\\
V^\dagger&0
\end{pmatrix}.
\]

The zero diagonal retains the original constant-source semantics while the
lower adjoint incidence supplies backreaction.  Adding a nonzero scalar to the
lower-right corner changes the source equation and requires independent
authority.

## Boundary factors are not bulk source dynamics

The endpoint polynomial, Gaussian Mellin factor, seam relation, and
archimedean completion line act in boundary totalization and determinant-line
normalization.  They do not by themselves define a bulk evolution law for the
constant source coordinate.

Placing \(B_\infty(s)\), \(\xi(s)\), or a logarithmic derivative in
\(D_\theta\) would move a scalar readout upstream into the source equation and
would alter the kernel problem.

## Three-port source characteristic

With \(D_\theta=0\) and no independently authorized direct
arithmetic--theta arrow, source ordering sets \(R=0\). The
history-eliminated characteristic is

\[
M_{\theta U}(z)
=
\begin{pmatrix}
V^\dagger R_HV & V^\dagger R_HB\\
B^\dagger R_HV & D_U+B^\dagger R_HB
\end{pmatrix},
\]

up to the frozen adjoint signs. The mixed blocks arise only through the
propagated history path.

The upper-left entry is the theta Weyl function, not Xi.  Its strict
half-plane sign is already known.

## Evans mismatch remains a boundary map

The Xi section is the mismatch of left- and right-stable histories at the
seam.  It belongs to the boundary matching complex.  It should not be
identified with the bulk source diagonal \(D_\theta\).

This keeps two roles distinct:

- \(D_\theta=0\): constant source law;
- \(\tau(z)\): two-ended Evans boundary mismatch.

## Consequence for G4

The theta diagonal source law is closed and contains no fitted spectral data.
The remaining diagonal datum is the arithmetic law \(D_U\).  More importantly,
one must prove that imposing the Evans seam relation on the full three-port
paired system yields a determinant section equal to Xi, rather than replacing
the scalar mismatch by the theta Weyl entry.

## Disposition

Set

\[
D_\theta=0
\]

in the source three-port pencil.  Archimedean and endpoint factors remain in
the boundary determinant line.  G4 remains open at the arithmetic diagonal,
direct-versus-propagated cross-path coherence, and the full paired
Evans/determinant comparison.  No RH conclusion is authorized.
