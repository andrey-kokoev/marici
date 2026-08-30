# Theta two-endpoint nullity does not imply a bounded reciprocal lift

## Source-derived tail state

Let (f) be a nonzero source and define the forced tail

\[
 G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv.
\]

It obeys

\[
 (\partial_q+s)G_s+f=0
\]

and decays at the infinite endpoint whenever the source has the required
tail decay. At the finite endpoint,

\[
 G_s(0)=\int_0^\infty f(v)e^{sv}\,dv.
\]

Thus a scalar transform zero gives the genuine two-endpoint condition

\[
 G_s(0)=G_s(\infty)=0.
\]

## The attempted bounded lift

The complete moving-cut source state retains both its tail and reflected seam
history. Packet 202 proves that its two reciprocal Mellin orientations have
full energy

\[
 E_\delta^{\mathrm{full}}(q)
 =2\cosh(2\delta q)\|f\|_2^2,
 \qquad
 \delta=\Re(s-\tfrac12).
\]

For nonzero (f), this trajectory is unbounded whenever (\delta\ne0).
Crucially, the formula is independent of (G_s(0)). Scalar nullity does not
alter the crossed seam history or its norm.

Therefore

\[
 G_s(0)=G_s(\infty)=0
\]

does not imply boundedness of the full reciprocal lift.

## Exact obstruction

The tail differential system provides a source-derived zero-to-state bridge,
but only into its two-endpoint solution space. The cosh law supplies a
source-derived bounded-trajectory obstruction, but scalar nullity does not
place the solution in that bounded domain.

Consequently, scalar zero implying a bounded full reciprocal state cannot be
asserted from the tail equation and Fourier--Tate doubling alone.
It would be an additional domain axiom and would encode the desired
zero-confinement conclusion unless independently derived.

## Hostile realization

The logical gap is not special to theta. For a prescribed spectral parameter,
one may choose a nonzero compactly supported signed source whose Laplace
transform vanishes there. Its forced tail satisfies both endpoint conditions,
while the complete reciprocal moving-cut energy still follows the same cosh
law and is unbounded off the seam.

This hostile source shows that no theorem using only the forced tail equation,
endpoint nullity, reciprocal symmetry, and complete moving-cut isometry can
close the RH argument.

## Surviving route

A proof now requires an independently constructed operator or determinant
functor whose canonical kernel domain already carries the full reciprocal
graph norm. The required derivational direction is:

1. construct the completed boundary-bearing operator from labelled
   theta/Tate data;
2. derive its graph norm and domain without examining its determinant zeros;
3. prove that its determinant section is the completed theta transform up to
   a nowhere-vanishing unit; and
4. only then apply the cosh law to a kernel state.

If this construction exists, boundedness is earned and packet 202 supplies
the confinement mechanism. Without it, the cosh law explains the seam but
does not locate scalar zeros.

## Falsifier

Any proposed zero-to-bounded-state theorem fails if its domain is defined by
bounded reciprocal energy only after the scalar transform is known, or if a
compactly supported hostile source with a two-endpoint null state is admitted
without the same bounded lift. A successful construction must reject that
source through independently specified operator provenance or boundary data.

## Scope

This closes the direct tail-equation route to RH and isolates the missing
operator-domain theorem. It does not weaken the exact reciprocal cosh law or
the source-derived two-endpoint interpretation of a transform zero.
