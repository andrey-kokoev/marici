# The retained theta coordinate gives the holomorphic right Grushin splitting

## Retained normalization

On the constructed analytical G4 graph, the canonical Stokes section is

\[
\Psi(z)=(u_z,1,0).
\]

Let

\[
\ell(x)=x_{\theta}
\]

be projection to the retained theta/source coordinate. Because the common
domain is a source-retaining graph completion, coordinate projection is
continuous by construction. It is independent of `z` and therefore
holomorphic as a dual-valued map.

The canonical section obeys the exact normalization

\[
\ell(\Psi(z))=1
\]

throughout the common holomorphic parameter domain.

## Right projection

Define

\[
P_X(z)=\Psi(z)\ell,
\qquad
Q_X(z)=I-P_X(z).
\]

Then

\[
P_X(z)^2
=\Psi(z)\ell(\Psi(z))\ell
=P_X(z),
\]

and

\[
Q_X(z)\Psi(z)=0,
\qquad
\ell Q_X(z)=0.
\]

Since `Psi(z)` is a holomorphic graph-valued section and `ell` is continuous,
`P_X` and `Q_X` are holomorphic families of continuous operators on the
retained graph. Their ranges give the topological splitting

\[
X_1
=
\mathbb C\Psi(z)
\oplus
\ker\ell.
\]

No inverse estimate for the source-forgetting analytic record is needed: the
normalizing coordinate is retained in the graph itself.

## Compatibility with the pencil

The global Stokes identity gives

\[
D(z)\Psi(z)=0.
\]

Therefore

\[
D(z)P_X(z)=0,
\qquad
D(z)Q_X(z)=D(z).
\]

The right-reduced operator

\[
D(z)|_{\ker\ell}
\]

is consequently well-defined and holomorphic on a fixed source-coordinate
complement. The complement is selected before Xi specialization and cannot
be accused of fitting the zero set.

## Ordered-current compatibility

The ordered port is a retained odd-history coordinate, while `ell` is the
separate theta/source coordinate. Applying `Q_X` removes the universal
canonical Stokes line but does not quotient the endpoint, Hardy, or ordered
relative-response coordinates from the carrier. Their values on a general
transverse state remain available to the reduced Green identity.

## Remaining left gate

This closes only the right-hand normalization required by the two-sided
Grushin construction. A square reduced pencil still needs a holomorphic,
source-derived left section

\[
\Lambda(z)\in\ker D(z)^\dagger
\]

and a column `v(z)` satisfying

\[
\Lambda(z)v(z)=1.
\]

The contragredient existence of the G4 return does not by itself prove that
its candidate left kernel line has constant rank one or admits this global
normalization. Until that theorem is supplied, `Q_Y`, the full Grushin
operator, and its determinant remain conditional.
