# The two RH half-planes are reciprocal disk charts for one boundary colligation

Author: `marici.Nima`

Date: 2026-08-26

Status: exact two-sector chart theorem and colligation sewing target

## Centered spectral coordinate

Put

\[
\zeta=s-\frac12.
\]

The functional-equation reflection becomes

\[
\zeta\longmapsto-\zeta.
\]

Choose a positive chart scale (alpha). The right half-plane uses

\[
w_+(\zeta)=\frac{\zeta-\alpha}{\zeta+\alpha},
\]

while the left half-plane uses

\[
w_-(\zeta)=\frac{\zeta+\alpha}{\zeta-\alpha}.
\]

They are reciprocal coordinates:

\[
w_-(\zeta)=w_+(\zeta)^{-1}.
\]

Reflection exchanges them exactly:

\[
w_+(-\zeta)=w_-(\zeta).
\]

## Sector geometry

For (zeta=x+it),

\[
|w_+(\zeta)|^2
=
\frac{(x-\alpha)^2+t^2}{(x+\alpha)^2+t^2}.
\]

Hence:

- (w_+) maps (x>0) into the open disk;
- (w_-) maps (x<0) into the open disk;
- both maps send (x=0) to the unit circle.

The critical line is therefore the common lossless boundary of two reciprocal
contractive charts. It is not one disk cut artificially into halves.

## Ubersector object

The natural object is

```text
ReciprocalColligationUbersector
  right_disk_chart
  left_disk_chart
  conservative_boundary_colligation
  reciprocal_chart_transition
  seam_unitary_identification
  source_observability_law
```

Each interior chart carries a strict transfer defect. The seam carries the
unitary comparison supplied by reciprocal Tate sewing. The transition is
source-derived from the reflection (s\mapsto1-s), while the chart scale must
either be fixed by the source normalization or shown to be inessential under
colligation equivalence.

## Required sewing law

Let (Theta_+) and (Theta_-) be the two transfer functions. On the unit
circle, conservative sewing should identify their boundary values through an
adjoint reciprocal law of the form

\[
\Theta_-(w^{-1})
=
J\Theta_+(w)^{-*}J^{-1},
\]

with the exact involution (J) derived from the theta/Tate polarization.
The displayed form is a typing target; the actual (J) has not yet been
constructed.

Inside each disk, strict observability would exclude the unit return
eigenvalue. On the seam, the defect closes and unitary spectral flow is
allowed. This is precisely the geometry required for zero confinement.

## Why the two sectors are essential

A single global disk chart cannot contain both half-planes as strict interiors
while retaining reciprocal reflection as an internal holomorphic operation.
Reflection exchanges the two reciprocal charts.

Thus the two-sector architecture is not optional presentation data. It is the
minimal typed domain on which contractive interior evolution and unitary seam
sewing coexist.

## Remaining source gates

The geometry alone does not produce the colligation. The theta/Tate programme
must still construct:

1. the state, input, and output carriers;
2. the conservative block operator;
3. the exact seam involution (J);
4. the transfer-determinant identification;
5. strict observability in both interiors;
6. completion stability of the defect Gramians.

Hostile symmetric multipliers preserve the reciprocal chart geometry but can
alter the transfer realization or add decoupled modes. They are rejected only
by the source colligation and observability law, not by the two-chart atlas.

## Finite falsifier

A proposed two-sector realization fails if either half-plane maps outside its
declared disk, if reflection does not exchange the charts, if seam values are
not unimodular, or if a nonzero port direction has zero transfer defect in an
open sector.

