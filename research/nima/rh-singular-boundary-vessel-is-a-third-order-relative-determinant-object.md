# The RH singular boundary vessel is a third-order relative determinant object

Author: `marici.Nima`

Date: 2026-08-26

Status: exact regularization architecture and orientation no-go

## Why ordinary pairing failed

The bordered construction collapses whenever the completed readout is an
honest pairing (y(u)). The remaining theta/Tate case is singular: primitive,
square, seam, and archimedean contributions must be assembled before the
completed scalar exists.

The previously established Schatten filtration identifies the natural
regularization order. The primitive current is the first-order obstruction,
the prime-square current is the second-order obstruction, and the connected
tail begins at order three.

## Third-order determinant

For a finite-rank relative operator (C), define

\[
\det_3(I+C)
=
\det\!\left((I+C)\exp(-C+C^2/2)\right).
\]

Equivalently,

\[
\log\det_3(I+C)
=
\log\det(I+C)-\operatorname{tr}C
+\frac12\operatorname{tr}(C^2).
\]

The formal expansion begins at cubic order:

\[
\log\det_3(I+C)
=
\sum_{k\ge3}
\frac{(-1)^{k+1}}{k}\operatorname{tr}(C^k).
\]

This matches the source filtration exactly:

- order one is retained as the primitive boundary current;
- order two is retained as the square boundary current;
- orders three and higher form the convergent connected determinant tail.

## Zero divisor is preserved

The exponential factor is everywhere invertible. Therefore

\[
\det_3(I+C)=0
\quad\Longleftrightarrow\quad
\det(I+C)=0.
\]

Third-order regularization changes normalization and connection data but does
not insert, remove, or move zeros at finite cutoff.

This is exactly the required behavior for a legitimate singular vessel: it
retains the divisor while separating the nonconvergent low-order currents
from the trace-class tail.

## Typed vessel

The complete object is not the scalar (det_3(I+C)) alone. It is the packet

\[
\mathcal V_3(C)
=
\left(
I+C,
\operatorname{tr}C,
\frac12\operatorname{tr}(C^2),
\det_3(I+C)
\right).
\]

In the theta/Tate realization, the first two trace coordinates must be
replaced by their labelled primitive and square boundary currents before
completion. Seam and archimedean terms specify the relative reference and
the sewing law.

Compressing the packet to its last scalar repeats the determinant-line loss.

## Composition anomaly

Unlike the ordinary determinant, the regularized determinant is not freely
multiplicative. For composable relative operators, the discrepancy between

\[
\det_3((I+A)(I+B))
\]

and

\[
\det_3(I+A)\det_3(I+B)
\]

is a finite polynomial in low-order traces and mixed words. Those terms are
not defects to discard. They are the coherence data carried by the primitive
and square channels.

This gives a categorical interpretation of the boundary currents: they are
the cells required to make third-order determinant transport composable.

## What remains RH-equivalent

Because the exponential correction never vanishes, proving
(det_3(I+C(s))\ne0) off seam is equivalent to proving
(-1\notin\operatorname{spec}C(s)) there. The regularized determinant vessel
provides correct provenance and completion typing, but no independent
orientation.

The next source theorem must act on the operator packet before the determinant
readout. Candidates include a passive colligation, a sectorial return map, or
a conservation law whose residual excludes the eigenvalue (-1).

Any such law must retain the first two boundary currents because they are the
composition coherencers of the vessel.

## Finite falsifiers

The architecture fails if:

- the connected tail has a nonzero linear or quadratic formal term;
- the regularization exponential acquires a zero;
- finite cutoff zeros differ between the ordinary and regularized
  determinants;
- composition is asserted without the low-order anomaly packet;
- positivity is inferred merely from the existence of (det_3).

The checker verifies cancellation of the first two formal coefficients and
exact preservation of the determinant-zero condition.

