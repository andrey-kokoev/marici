# The Aspect complementary readout is complex-faithful but loses one integral parity

## Question

Does the existing two-channel Aspect readout meet the newly derived requirement for an integral parity-sensitive readout?

## Claim boundary

This audits the simulation contract's readout matrix on its route-coordinate lattice. The contract explicitly disclaims physical realization. Its readout lattice is not automatically the conductor cokernel lattice.

## Existing readouts

The Aspect contract gives the scalar dark-port row

\[
R_{\rm dark}=\begin{pmatrix}1&-1\end{pmatrix}
\]

and the complementary phase-sensitive readout

\[
R=\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}.
\]

For route coordinates \((a,b)\), these channels record

\[
(a-b,a+b).
\]

## Integral audit

The two-channel matrix has

\[
\det R=2,
\qquad
\operatorname{Smith}(R)=(1,2).
\]

Its image is

\[
\{(u,v)\in\mathbb Z^2:u=v\pmod2\}.
\]

The inverse is

\[
R^{-1}=\frac12
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]

Thus the complementary readout is invertible over \(\mathbb R\) or \(\mathbb C\), but not unimodular over \(\mathbb Z\). Reconstructing integral route coordinates from arbitrary integral output coordinates requires halves.

Modulo two, both output rows coincide and the readout has rank one. It retains only one parity combination.

## Closed Aspect class

The primitive closed route vector is

\[
z=(1,1)^T.
\]

Its readout is

\[
Rz=(0,2)^T.
\]

The dark port vanishes, while the complementary channel is twice its output-lattice unit. Hence the primitive closed class is not represented primitively in the naive detector-coordinate lattice.

## Relation to the conductor defect

The readout contributes one index-two lattice mismatch on the route side. The conductor completion has two independent degree-zero index-two defects. These occur in different typed spaces and cannot be added or cancelled without a comparison map.

Nevertheless, the repeated arithmetic mechanism is now present inside the Aspect contract itself: a complex-faithful two-channel readout can hide one integral parity normalization.

## Acceptance test

An integral physical readout must specify its actual record lattice. It must either:

1. declare the same-parity sublattice as the admissible output lattice, making \(R\) unimodular onto its image;
2. supply a source-derived half-unit calibration; or
3. replace \(R\) by a unimodular wall-labelled readout before symmetric/phase aggregation.

It must then provide a typed map from conductor parity classes to those records. The present simulation contract provides none of these integral authorities.

## Disposition

The complementary Aspect readout is faithful over characteristic zero but loses one integral parity. It does not yet satisfy the two-bit conductor-parity readout requirement.
