# Sector-denominator sewing would confine completion zeros by Hurwitz

## Surviving architecture

The completed xi section cannot itself be a nonconstant positive-real
impedance. A positive-real impedance can also have a Cayley reflection with an
off-seam zero. There is, however, a third construction that avoids both
obstructions.

Keep positivity on the sector-local impedance and form its denominator before
forming any scattering readout.

## Finite-dimensional sector theorem

Let (M_+(z)) be an analytic matrix on the open right half-plane and suppose

\[
\operatorname{Re}\langle v,M_+(z)v\rangle\ge0
\]

for every vector (v). Then

\[
I+M_+(z)
\]

is invertible throughout that half-plane.

Indeed, if

\[
(I+M_+(z))v=0,
\]

then taking the real part of the quadratic pairing gives

\[
0
=
\lVert v\rVert^2
+
\operatorname{Re}\langle v,M_+(z)v\rangle.
\]

Both terms are nonnegative and the first is strictly positive for (v\ne0).
Thus (v=0), and finite dimensionality gives invertibility.

Consequently the source denominator

\[
D_+(z)=\det(I+M_+(z))
\]

is zero-free in the open right half-plane. The reflected sector has its own
zero-free denominator (D_-(z)) in the open left half-plane.

This conclusion concerns the denominator, not the Cayley numerator

\[
\det(M_+(z)-I),
\]

which may vanish at a matching point.

## Sewing and completion theorem

At finite cutoff (X), suppose source construction supplies

\[
F_X(z)=u_X(z)D_{+,X}(z)D_{-,X}(z),
\]

where (u_X) is nonvanishing, (D_{+,X}) is zero-free in the right sector,
and (D_{-,X}) is zero-free in the left sector.

Assume separately on each open half-plane that:

- the appropriate sector factors converge locally uniformly;
- the nonvanishing normalization factors converge locally uniformly;
- one source-fixed basepoint normalization prevents the limiting product from
  being identically zero;
- the finite sewn products converge locally uniformly to the centered
  completed section (F).

Hurwitz's theorem then implies that (F) is zero-free in both open
half-planes. Zeros may enter only through failure of uniform control at their
common boundary.

For the centered xi section, that boundary is

\[
\operatorname{Re}z=0,
\]

equivalently

\[
\operatorname{Re}s=\frac12.
\]

## Infinite-dimensional typing

For an infinite sector module, the determinant needs an admitted operator
ideal. If (M_+) is trace class, the Fredholm determinant of (I+M_+) is the
direct analogue. If only a higher Schatten class is available, a regularized
determinant may be used, but its exponential counterterms must remain typed as
boundary data.

The determinant is nonzero whenever (I+M_+) is invertible. Regularization
cannot be allowed to delete the primitive, square, seam, or archimedean
currents required by finite-cutoff sewing.

This connects directly to the existing three-level prime filtration: the
trace-class tail may support a regularized determinant, while the first two
currents must remain as relative boundary factors rather than being silently
discarded.

## What this theorem does not prove

No current packet supplies the required source identity between the sewn
sector denominators and the completed xi section. Constructing factors after
factoring the known scalar section would merely restate zero confinement.

The construction is noncircular only if all of the following are derived
before scalar completion:

1. the sector operators (M_{+,X}) and (M_{-,X});
2. their accretive law;
3. the admitted determinant or regularized determinant;
4. the finite-cutoff sewing identity for (F_X);
5. locally uniform convergence on compact subsets of each open sector;
6. a source-fixed nonzero basepoint normalization.

## Finite falsifiers

At any cutoff, the route fails if one finds:

- a vector in the kernel of (I+M_{+,X}(z)) in the right sector;
- a vector in the kernel of (I+M_{-,X}(z)) in the left sector;
- a nonzero residual in the proposed determinant sewing identity;
- a compact-set norm bound that diverges with cutoff;
- a basepoint determinant tending to zero;
- a boundary counterterm that cannot be reconstructed at finite cutoff.

## Decisive reduction

The remaining RH-bearing question can now be stated without assigning
positivity to the completed scalar:

Does the labelled theta/Tate source generate accretive sector operators whose
zero-free denominators sew, with all boundary currents retained, to the
completed xi section?

If yes, local uniform completion confines zeros to the seam by Hurwitz. If no,
the impedance programme has no remaining zero-exclusion mechanism.
