# Compressed curvature does not protect a flagged overlap

## Status

Exact rank-one separation theorem. Curvature of a compressed connection measures
motion of the selected subspace. A transmission zero measures incidence of an
ordered reference vector with that subspace. Curvature alone does not determine
that incidence.

The same source-independent projection family, with the same nonzero curvature,
admits one fixed flag whose overlap vanishes at a chosen point and another whose
overlap does not. Therefore compressed curvature is not yet an RH orientation
law.

## A curved line in a flat two-state carrier

Let

\[
u(a,t)=
\begin{pmatrix}
\cos a\\
e^{it}\sin a
\end{pmatrix},
\qquad
P(a,t)=u(a,t)u(a,t)^*.
\]

The vector \(u\) is normalized, so \(P\) is a rank-one orthogonal projection.
The ambient bundle \(\mathbb C^2\) is flat, while the compressed line moves in
both parameters.

The Berry connection in this frame is

\[
\mathcal A=u^*du=i\sin^2a\,dt.
\]

Its curvature is

\[
\mathcal F=d\mathcal A
=i\sin(2a)\,da\wedge dt.
\]

At

\[
a_0=\frac\pi4
\]

the curvature is nonzero.

## A zero with nonzero curvature

Fix any \(t_0\), and define the ordered reference vector

\[
b_0=
\begin{pmatrix}
-e^{-it_0}\sin a_0\\
\cos a_0
\end{pmatrix}.
\]

Then

\[
b_0^*u(a_0,t_0)=0.
\]

Thus the flagged scalar overlap vanishes at \((a_0,t_0)\), while

\[
\mathcal F(a_0,t_0)=i\,da\wedge dt
\]

is nonzero.

Positive magnitude, nondegeneracy, or fixed orientation of the compressed
curvature cannot exclude this zero.

## Same curvature, different divisor

Keep the identical projection \(P(a,t)\) and choose instead

\[
b_1=u(a_0,t_0).
\]

Then

\[
b_1^*u(a_0,t_0)=1.
\]

The connection and curvature have not changed, but the distinguished overlap
has changed from zero to nonzero. Therefore the divisor depends on the ordered
flag, not only on the moving subspace.

This is the differential-geometric version of the earlier distinction between
a full Weyl determinant and one cross-transfer entry.

## Why topology is still too coarse

Curvature can determine a Chern class after integration over a closed surface.
Such a class controls a net divisor count for suitable holomorphic sections. It
does not locate the zeros of one chosen section or exclude them from an open
half-plane.

The open half-plane is contractible. Bundle topology there does not prohibit a
section from vanishing at isolated points. A hostile multiplier can change the
section divisor without changing the underlying line bundle.

## Parallel-section trap

One might demand that the distinguished section \(\sigma\) be parallel:

\[
\nabla^P\sigma=0.
\]

Applying the connection twice gives

\[
(\nabla^P)^2\sigma=\mathcal F\sigma.
\]

For a line bundle, a nowhere-zero parallel section therefore forces

\[
\mathcal F=0.
\]

Hence nonzero curvature and global parallel nonvanishing cannot be used
simultaneously on the same line. A weaker transport equation would need its own
source derivation and finite falsifier.

## Correct typed object

The required datum is not merely \((P,\nabla^P)\). It is the framed triple

\[
(P,\nabla^P,b_0)
\]

together with the section

\[
\sigma(a,t)=b_0^*u(a,t).
\]

An RH-bearing law must couple the connection to this ordered section. Possible
forms include:

- a source-derived differential equation for \(\sigma\);
- a conserved indefinite charge that is definite on zero states;
- a boundary index equating flagged incidence to a signed current;
- a source-local transversality estimate for \(b_0^*P\).

Each proposal must survive hostile changes of the flag that leave \(P\) and
its curvature unchanged.

## Finite falsifier

Use the two-state projection above at \((a_0,t_0)=(\pi/4,0)\). Then

\[
u=2^{-1/2}
\begin{pmatrix}
1\\1
\end{pmatrix},
\qquad
b_0=2^{-1/2}
\begin{pmatrix}
-1\\1
\end{pmatrix}.
\]

The exact witness is

\[
b_0^*u=0,
\qquad
\mathcal F=i\,da\wedge dt.
\]

It disproves any inference from nonzero compressed curvature to nonvanishing of
the ordered scalar overlap.

## Decisive conclusion

Compression is necessary to create curvature from the flat Mellin bundle, but
curvature still belongs to the moving subspace rather than its ordered
endpoint/source incidence. The RH divisor lives in that incidence.

The next legitimate target is a source-derived equation coupling the flagged
section to the compressed connection. If its nonvanishing theorem merely
assumes a positive logarithmic derivative or reconstructs the completed scalar
kernel, the route is circular. Without such a coupling, the connection rotation
has again reached a structural side theorem rather than zero confinement.
