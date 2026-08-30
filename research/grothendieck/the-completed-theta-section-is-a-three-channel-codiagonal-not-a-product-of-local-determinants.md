# The completed theta section is a three-channel codiagonal, not a product of local determinants

## Exact global decomposition

Let

\[
\Psi(t)=\sum_{n\ge1}e^{-\pi n^2t}
\]

and define the entire half-Mellin amplitude

\[
I(s)=\int_1^\infty\Psi(t)t^{s/2}\frac{dt}{t}.
\]

Splitting the global theta integral at \(t=1\) and applying Poisson
reciprocity on the lower chamber gives

\[
\Lambda(s)
=
\frac{1}{s(s-1)}+I(s)+I(1-s),
\]

where

\[
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Consequently the completed entire section is

\[
\xi(s)
=
\frac12
+
\frac{s(s-1)}2I(s)
+
\frac{s(s-1)}2I(1-s).
\]

Define the three source channels

\[
C(s)=\frac12,
\qquad
U(s)=\frac{s(s-1)}2I(s),
\qquad
V(s)=\frac{s(s-1)}2I(1-s).
\]

Then

\[
\xi(s)=C(s)+U(s)+V(s).
\]

The global readout is therefore the codiagonal

\[
\nabla:\mathbb C^3\longrightarrow\mathbb C,
\qquad
\nabla(c,u,v)=c+u+v,
\]

applied to the source curve \(s\mapsto(C(s),U(s),V(s))\).  It is not the
ordinary product of the local boundary minors.

## Meaning of a zero

Every local comparison may remain invertible while the codiagonal vanishes.
A nontrivial zero is exactly

\[
(C(s),U(s),V(s))\in\ker\nabla.
\]

The kernel is a two-dimensional comparison plane.  Thus the zero is not loss
of one local object.  It is destructive interference among three globally
typed channels:

1. the completion carrier;
2. the direct Mellin chamber;
3. the reciprocal Mellin chamber.

This is the precise mathematical form of one scalar thing secretly being a
three-channel relation.

## Why the critical line is special

Reciprocity exchanges \(U\) and \(V\).  On

\[
s=\frac12+it,
\]

one has \(1-s=\overline s\), and the real theta source gives

\[
V(s)=\overline{U(s)}.
\]

Moreover \(s(s-1)\) is real there.  Hence the scalar equation becomes

\[
\xi(s)=\frac12+2\operatorname{Re}U(s)=0.
\]

On the seam, the two reciprocal channels are complementary quadratures of
one relative amplitude.  Off the seam they are independent complex
directions constrained only by reciprocity.

This explains why the seam is the natural real collision locus.  It does not
yet prove that the physical source curve cannot meet \(\ker\nabla\) away from
that locus.

## The revised RH target

RH is now an intersection theorem:

\[
\text{the completed theta source curve meets }\ker\nabla
\text{ only on the fixed locus of reciprocal conjugation}.
\]

Symmetry alone is insufficient; hostile Fourier-fixed carriers already give
source curves with off-seam intersections.  The missing invariant must
constrain the tangent, curvature, or oriented incidence of the particular
minimal-theta curve relative to the codiagonal kernel plane.

The best next observable is therefore not another local determinant.  It is
the source-derived normal component of the three-channel curve against
\(\ker\nabla\), retained before scalar compression.  Equivalently, construct
the two comparison coordinates

\[
U-V,
\qquad
2C-U-V,
\]

together with the scalar codiagonal.  These three linear coordinates retain
the full channel packet.  A zero of the codiagonal then remains meaningful as
a point carrying two transverse comparison values rather than an erased
state.

## Multi-tower interpretation

The three principal towers now have literal roles:

- direct-sector tower: \(U\);
- reciprocal-sector tower: \(V\);
- control/completion tower: \(C\).

Their coherence tower is the reciprocal exchange \(U\leftrightarrow V\).
Their physical readout is the codiagonal.  Confusing the codiagonal with the
complete object is exactly the projection error that made a scalar zero look
like disappearance of the underlying relation.

