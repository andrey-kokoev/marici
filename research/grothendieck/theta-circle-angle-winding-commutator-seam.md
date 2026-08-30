# Circle angle--winding commutator has one canonical seam channel

## Bounded question

Does the arithmetic phase circle carry the source-fixed finite-rank boundary
term required by the earlier Green-identity programme?

## Rigged circle pair

Work first on smooth periodic functions on `R/Z`.  Let

\[
 N=-i\frac{d}{dq}
\]

be winding momentum, and let `Q` be multiplication by the sawtooth coordinate
`q in [0,1)`.  The latter is not a globally smooth function on the circle.
Distributionally,

\[
 \frac{dq}{dq}=1-\delta_0.
\]

Here the second term records the unit jump at the chosen cut.  Consequently
the canonical commutator is not the line commutator:

\[
 \boxed{[N,Q]=-iI+i|\delta_0\rangle\langle\delta_0|}
\]

as a quadratic-form identity on the rigged circle, where evaluation at the
cut is paired with the delta distribution.  The seam term is rank one and is
forced by compactness; deleting it would assert an impossible global angle
coordinate.

## Heat regularization makes the identity trace class

Let

\[
 E_a=e^{-aN^2/2},\qquad a>0.
\]

Sandwiching the commutator gives the ordinary trace-class form

\[
 \boxed{
 E_a[N,Q]E_a
 =-iE_a^2+i|E_a\delta_0\rangle\langle E_a\delta_0|.}
\]

In the winding basis `N e_n=2 pi n e_n`,

\[
 \|E_a\delta_0\|^2
 =\sum_{n\in\mathbb Z}e^{-a(2\pi n)^2}
 =\operatorname{Tr}(E_a^2).
\]

Therefore

\[
 \operatorname{Tr}\big(E_a[N,Q]E_a\big)=0.
\]

The vanishing trace of a commutator is realized locally as an exact balance:

\[
 \boxed{
 \text{negative heat bulk}
 +
 \text{one positive cut channel}
 =0.}
\]

The Jacobi theta series is simultaneously the bulk trace and the norm of the
smoothed seam state.  This is an operator explanation of why a scalar theta
term repeatedly appeared as a finite-rank repair in the prior Green and
prime-two reductions.

## Cut covariance

Moving the cut from `0` to `alpha` replaces `delta_0` by `delta_alpha`.
Translation covariance gives

\[
 E_a\delta_\alpha=U_\alpha E_a\delta_0,
\]

so its norm and the trace balance are unchanged.  The rank-one representative
moves, but its conjugacy class is canonical.  This is precisely the desired
distinction between a coordinate seam and source-independent content.

## Relation to the two reciprocal sectors

Fourier quarter-turn exchanges the winding description with the phase
description.  Each requires a cut when expressed in the other's local
coordinate.  Modular inversion exchanges the reciprocal metrics, while the
smoothed seam vector transports their boundary information.  Thus the two
half-plane Mellin charts inherit a boundary cocycle from the impossibility of
a global circle angle.

This supplies a concrete form of the earlier metaphysical proposal:

\[
 \text{two complementary localizations}
 \longrightarrow
 \text{one relative object with a compulsory seam current}.
\]

## RH boundary

The identity is universal for circle heat flow.  It explains completion and
the existence and rank of the repair channel, but not RH.  After applying the
Mellin character, the heat parameter is integrated with an oscillatory weight;
the exact bulk--seam cancellation must become an oriented relative energy,
not merely a zero trace.

The next gate is to Mellin-transform the **operator identity** while retaining
the seam ket, rather than Mellin-transforming only its scalar trace.  The
sharp falsifier is that the resulting relative quadratic form remains
indefinite for a source-compatible hostile carrier.  If so, the seam explains
the functional equation but not critical-line localization.
