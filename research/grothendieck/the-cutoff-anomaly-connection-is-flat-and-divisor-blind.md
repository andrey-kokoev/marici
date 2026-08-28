# The cutoff anomaly connection is flat and divisor-blind

## Setup

For finite prime cutoffs `S` contained in `T`, the primitive transition is

\[
g^{(1)}_{S,T}(s)
=
\exp\!\left(-\sum_{p\in T\setminus S}p^{-s}\right).
\]

It is entire and nowhere zero, and its logarithmic derivative is the
primitive boundary current

\[
\nabla^{(1)}_{S,T}(s)
=
\frac{d}{ds}\log g^{(1)}_{S,T}(s)
=
\sum_{p\in T\setminus S}(\log p)p^{-s}.
\]

The square transition has the same form with the grade-two cumulant in the
exponent. The connected grades `k >= 3` enter through an ordinary convergent
determinant tail.

## Flatness theorem

Every finite transition is the exponential of a globally defined entire
function. Consequently:

1. its divisor is empty;
2. its logarithmic derivative has zero residue around every finite loop;
3. its one-parameter connection has zero curvature;
4. the cutoff triangle law is exact, not merely projective.

Indeed, for a closed contour `C`,

\[
\frac{1}{2\pi i}\oint_C d\log g^{(1)}_{S,T}=0,
\]

because `g^(1)_(S,T)` has neither zeros nor poles. The same argument applies
to the square transition. Reciprocal reflection replaces each transition by
its inverse and therefore changes the sign of the connection without creating
curvature or divisor support.

Thus the primitive and square anomaly data define a flat pro-line connection.
They retain cutoff provenance and boundary transport, but they cannot by
themselves carry the winding of a zero of the completed theta section.

## Separation of roles

The result forces a strict distinction:

- the anomaly pro-line transports the value type and remembers how Euler
  cutoffs are compared;
- additive Poisson sewing constructs the distinguished four-channel section;
- zeros belong to the divisor of that section, not to the transition line.

A hostile symmetric multiplier with a divisor can preserve the flat anomaly
metadata while changing the section divisor. Therefore no argument using only
the transition cocycle, its reciprocal inversion, or its connection can
exclude off-seam zeros.

The missing RH datum must couple the source-derived Poisson section to an
independently constructed phase, Green, or determinant connection. It cannot
be recovered from the flat anomaly connection alone.

## Consequence for the current programme

The prior index instruction to seek reciprocal and archimedean descent of the
pro-line is no longer a live RH gate. Those coherences are already closed.
The live gate is section-sensitive:

1. retain the four Poisson channels before scalar aggregation;
2. couple their full seam germ to a source-derived connection or boundary
   current;
3. prove that this coupling detects inner-factor winding;
4. test completion stability in the primitive and square boundary grades.

Finite germ faithfulness is not enough, because adjacent logarithmic labels
give a nonuniform completion witness. Conversely, anomaly-line flatness is
not a defect: it is the reason the line is a trustworthy transport vessel.

## Falsifier

This theorem would fail at the first finite cutoff transition having a zero,
a pole, a nonzero logarithmic residue, or a failure of the cutoff triangle
law. None occurs for the source-derived exponential transitions above.

## Scope

The theorem is finite-cutoff and pro-system structural. It does not construct
the missing section-sensitive connection, prove completion-stable
transversality, or prove RH.
