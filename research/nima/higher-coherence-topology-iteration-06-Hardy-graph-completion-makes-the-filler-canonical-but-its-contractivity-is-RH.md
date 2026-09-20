# Higher-coherence topology iteration 06: Hardy graph completion makes the filler canonical, but its contractivity is RH

## Candidate topology

Pass from the half-line theta-tail space to the bilateral carrier

\[
\widehat{\mathcal H}_\Phi
\]

on which reciprocal reflection `R` is unitary. Split it into reflection parity
sectors

\[
\widehat{\mathcal H}_\Phi
=P_+\widehat{\mathcal H}_\Phi
\oplus P_-\widehat{\mathcal H}_\Phi,
\qquad
P_\pm=\frac12(I\pm R).
\]

Hardy boundary values replace unbounded half-line analytic continuation by an
oriented boundary relation. This removes the bounded-reflection obstruction
found in the Krein iteration.

## Canonical control graph

The source determines the Clark/de Branges transfer function

\[
\Theta(z)=\frac{E^*(z)}{E(z)}
\]

with the declared spectral-coordinate convention. On upper-half-plane Hardy
space, the only canonical graph controller is multiplication

\[
M_\Theta:f\longmapsto\Theta f.
\]

Its storage defect is

\[
D_\Theta=I-M_\Theta^*M_\Theta.
\]

If `D_Theta>=0`, the higher cone has the canonical positive filler

\[
D_\Theta^{1/2}.
\]

Thus Hardy topology does not merely postulate another system: it identifies a
unique source-derived candidate higher coherencer.

## Exact positivity condition

Multiplication is contractive exactly when

\[
\Theta\in H^\infty,
\qquad
\|\Theta\|_\infty\le1.
\]

Equivalently,

\[
|E^*(z)|\le|E(z)|
\]

throughout the upper half-plane. This is the Hermite--Biehler/Schur condition
and is equivalent to the desired zero confinement.

Hence the Hardy graph succeeds at construction but not proof: the positive
five-dimensional cone exists precisely if RH holds.

## Full reciprocal-family obstruction

Even on the bilateral carrier, no single-valued linear graph over the even
sector contains both reciprocal exponential branches. They have the same even
projection and opposite odd projections. A valid Hardy realization must
therefore retain one of:

- branch-labelled input fibers;
- one Hardy orientation with the other recovered by adjoint boundary values;
- a multivalued linear relation;
- an enlarged spectral/input coordinate.

The labelled adelic-to-Hardy incidence already supplies the first option on a
saturated ordered graph. Its remaining normalization comparison does not imply
contractivity of `M_Theta`.

## Relation to repeated cones

Iterating defect dilations gives the standard Schur realization hierarchy only
when the first defect operator is positive. If `D_Theta` has a negative
direction, adjoining another Hilbert defect space cannot turn it positive
without switching to an indefinite realization. That returns to the Krein
case and loses positive confinement.

Thus repeated Hardy cones do not postpone the first contractivity test: every
positive dilation begins with

\[
I-M_\Theta^*M_\Theta\ge0.
\]

## Verdict for topology 6

Hardy/closed-graph topology provides the cleanest canonical higher filler:

\[
(I-M_\Theta^*M_\Theta)^{1/2}.
\]

But existence of this positive filler is exactly the RH-strength Schur
condition. The topology removes the reflection-domain artifact while exposing,
rather than solving, the terminal positivity problem.

The next nonredundant topology to test is a nuclear/trace-ideal or determinant
completion, where higher residuals might become trace-null even when the
operator defect is not positive.