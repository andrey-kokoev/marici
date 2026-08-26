# Critical coordinate is the antisymmetric completed boundary channel

## Question

Theta modular completion turns a rank-two continuation boundary packet into
the neutral scalar carrier \(1/2\).  What is the complementary boundary
direction discarded by that scalar compression?

## Completed boundary vector

Before completion, the two continuation currents are

\[
b(s)
=
\left(
\frac1{s-1},-\frac1s
\right).
\]

Apply the canonical scalar completion factor \(s(s-1)/2\) componentwise.
The completed boundary vector is

\[
B(s)
=
\left(
\frac{s}{2},\frac{1-s}{2}
\right).
\]

Passing to symmetric and antisymmetric coordinates gives

\[
B_{\mathrm{sym}}(s)
=
\frac{s}{2}+\frac{1-s}{2}
=
\frac12,
\]

\[
B_{\mathrm{asym}}(s)
=
\frac{s}{2}-\frac{1-s}{2}
=
s-\frac12.
\]

Therefore the usual centered spectral coordinate

\[
z=s-\frac12
\]

is not an externally convenient recentering.  It is exactly the
antisymmetric channel of the completed modular boundary packet.

## Why the half offset is forced

The two boundary components carry a fixed total charge:

\[
B_+(s)+B_-(s)=\frac12.
\]

The critical seam is where their real parts are equally shared:

\[
\Re B_+(s)=\Re B_-(s)
\quad\Longleftrightarrow\quad
\Re s=\frac12.
\]

Thus the half offset records equal division of the completed origin and
infinity boundary current.  It is selected before any zero is inspected.

## Sector involution

Reciprocal reflection exchanges the two boundary components:

\[
s\longmapsto1-s,
\qquad
B_+\longleftrightarrow B_-.
\]

Consequently,

\[
B_{\mathrm{sym}}\longmapsto B_{\mathrm{sym}},
\qquad
B_{\mathrm{asym}}\longmapsto-B_{\mathrm{asym}}.
\]

The two half-planes are therefore shadows of the two possible orientations
of one antisymmetric boundary coordinate.  On the critical line the two
components are complex conjugates, so the antisymmetric channel is purely
imaginary.

## Connection to the doubled conservation law

The coefficient that appeared in the proposed doubled Green identity was

\[
2\Re z=2\Re s-1.
\]

It is now identified as twice the real part of the discarded boundary
channel.  A conservation law of the form

\[
2\Re z\,\mathcal E
=
\mathcal J_{\mathrm{boundary}}
\]

would therefore pair relationship energy with boundary polarization.  The
coefficient is source-derived; it is not a spectral multiplier chosen to
force the critical line.

## What this explains and what remains open

This gives a hard-to-vary explanation of three facts:

1. Why the functional equation centers at \(1/2\).
2. Why two reciprocal half-planes behave as oppositely oriented sectors.
3. Why the natural conservation coefficient is \(2\Re s-1\).

It does not prove that zeros lie on the seam.  Scalar completion keeps only
the symmetric carrier, and a scalar zero can still arise by interference with
the theta tail.  RH requires a theorem coupling the discarded antisymmetric
boundary channel to a faithful positive or exact relationship object before
compression.

## Completion warning

Even a faithful finite boundary pairing may fail after completion in two
different ways:

- a new kernel vector may appear outside the closure of the finite-core
  kernel;
- the kernel may remain stable while the reduced minimum modulus collapses to
  zero.

Thus a future boundary-polarization theorem must establish both kernel-core
stability and a nonvanishing reduced minimum modulus on each fixed off-seam
compact set.  Finite injectivity alone is insufficient.

## Next exact target

Retain both completed boundary components and the theta tail before scalar
aggregation.  Construct the smallest source-native pairing in which

\[
\left(
\frac12,z
\right)
\]

acts on symmetric and antisymmetric tail channels.  The decisive question is
whether the antisymmetric channel enters only through a relationship energy
whose vanishing is forbidden for an admissible zero-state.

The hostile falsifier is any source-compatible packet with the same boundary
vector \(B(s)\), the same reciprocal swap, and an off-seam scalar zero.  Such
a witness would show that boundary polarization explains the geometry but
still does not constrain the divisor.

## Result

The critical coordinate \(s-1/2\) is exactly the antisymmetric completed
boundary channel discarded when theta continuation is compressed to its
neutral half carrier.  The critical line is the equal-real-share locus of the
two reciprocal boundary sectors.
