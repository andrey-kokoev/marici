# Normal action comes from conjugate reciprocity, not holomorphic reflection alone

## Correction of scope

The recent finite equalizer calculations used a rational real parameter \(z\).
They are exact on the horizontal slice, where \(z\) represents
\(\operatorname{Re}(s)\).  Extending the formulas to the full complex spectral
plane by replacing \(z\) with \(s\) would be wrong.

Holomorphic reflection gives

\[
s-(1-s)=2s-1.
\]

This vanishes only at \(s=1/2\), not along the critical line.  It cannot be the
normal action required by the operative coherencer.

## The correct two-sector operation

The Hilbert-space comparison pairs a sector with its conjugate reciprocal:

\[
s\longmapsto1-\overline{s}.
\]

Therefore

\[
s-(1-\overline{s})
=2\operatorname{Re}(s)-1
=2\left(\operatorname{Re}(s)-\frac12\right).
\]

The tangential Mellin frequency cancels, while the normal displacement
survives.  This vanishes on the entire critical line and nowhere else.

For the first-order sector generators

\[
D_+(s)=P+s,
\qquad
D_-(s)=P+1-\overline{s},
\]

their difference is the source-independent normal action

\[
D_+(s)-D_-(s)
=2\left(\operatorname{Re}(s)-\frac12\right)I.
\]

## Source genesis

The conjugation is not an added symmetry chosen to fit the critical line.  It
is forced when the reciprocal comparison is realized as a dagger or adjoint
relation on the additive Haar carrier.  For the dilation generator

\[
E=x\partial_x,
\]

formal adjunction under additive Haar measure gives

\[
E^*=-E-1.
\]

The centered generator \(E+1/2\) is therefore skew under the dagger.  Mellin
eigenparameters are paired as \(s\) and \(1-\overline{s}\), and the half-density
offset is the fixed point of that adjoint relation.

This supplies a plausible source genesis for the normal face of the dynamic
\(+1\): additive Haar adjunction plus reciprocal sector sewing.

## What remains conditional

The calculation identifies the correct normal generator, but it does not yet
prove that the actual mixed theta/Tate residue presentation carries this dagger
without extra boundary terms.  Integration by parts may produce endpoint,
primitive, square, seam, or archimedean currents.  Those terms must be retained
and shown to form the other faces of the same operative coherencer.

The exact source theorem required is a boundary-bearing adjoint identity of the
form

\[
D_+(s)-D_-^{\dagger}(s)
=2\left(\operatorname{Re}(s)-\frac12\right)I+B_{\partial}(s),
\]

followed by a proof that the typed boundary law absorbs \(B_{\partial}\) without
creating an off-seam kernel.

## DPC verdict

The dynamic normal action is not arbitrary and need not be written in by hand.
Its candidate source is the daggered reciprocal comparison.  Holomorphic
functional-equation symmetry alone is insufficient; the anti-linear Hilbert
structure is essential.

The finite falsifiers are:

- use \(1-s\) instead of \(1-\overline{s}\), which leaves tangential frequency
  in the alleged normal generator;
- omit the boundary term in the adjoint identity;
- choose a parameter-dependent dagger or frame after inspecting the scalar
  divisor.

## Verification

`check_rh_conjugate_reciprocal_normal_action.py` verifies exact cancellation of
the tangential coordinate for rational complex parameters, shows failure of
holomorphic reflection on the critical line, and checks the centered dilation
adjoint relation on monomial test functions including its boundary term.
