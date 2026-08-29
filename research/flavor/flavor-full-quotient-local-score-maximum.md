# Full-quotient local score maximum: WP1008

## Question

Does the WP1007 exposed orbit remain a maximum when the analyst-selected
one-parameter family is opened to every local Hermitian direction, modulo the
declared simultaneous weak-basis action and positive rescalings?

## Quotient reduction

For a generic Hermitian pair, simultaneous unitary conjugation diagonalizes
the first matrix. Trace components and the component of the second matrix
diagonal in that basis commute with everything relevant to the score while
increasing its norm denominators, so they cannot improve a positive score.
After quotienting two positive scales and diagonal rephasings, a local
coordinate system consists of:

- one eigenvalue-shape coordinate z for the traceless diagonal first matrix;
- two relative edge magnitudes a,t for the second matrix;
- one rephasing-invariant triangle phase delta.

Use representatives

\[
X_z=\operatorname{diag}(-1,z,1-z),
\qquad
Y_{a,t}=
\begin{pmatrix}
0&a&-it\\
a&0&1\\
it&1&0
\end{pmatrix}.
\]

The WP1007 point is

\[
(z,a,t)=\left(0,1,\frac65\right),
\qquad
\frac RQ=\frac{44376}{275}.
\]

No physical time or causal ordering is assigned to any of these coordinates.

## Exact transverse certificate

For

\[
S=K+\frac{44376}{275}P,
\]

the gradient in (z,a,t) vanishes at the witness. Its exact Hessian is

\[
H=
\begin{pmatrix}
-9294/473&75/86&0\\
75/86&-3273750/874577&1296000/874577\\
0&1296000/874577&-2160000/874577
\end{pmatrix}.
\]

The leading principal minors have signs minus, plus, minus, with

\[
\det H=-\frac{14458500000}{105823817}.
\]

Sylvester's criterion therefore makes H negative definite.

The score is phase-independent in K, while its determinant term is
proportional to \(\cos^2\delta\) near the chosen maximally CP-odd triangle
phase. Its phase curvature is \(-2(R/Q)P_\star<0\). Traceless diagonal
perturbations of Y leave the commutator numerator fixed and increase the
positive norm denominators, so their quadratic block is also strictly
negative. Gauge and scale directions have already been quotiented.

Thus the witness is a strict local maximum on the complete reduced generic
Hermitian-pair quotient, not merely along the WP1007 curve.

## Classification

This is a local quotient-level selector capacity theorem. It does not prove a
global maximum, derive the coefficient ratio from a source action, or supply a
physical preparation/readout instrument.

## Smallest exact falsifier

A nonnegative eigenvalue of the reduced Hessian would falsify local exposure.
The checker also verifies that replacing the frozen ratio by R/Q=1 makes the
witness nonstationary, so the numerical point is not independently selected.

## Claim boundary

The theorem concerns a neighborhood of a generic Hermitian orbit under the
specified invariant score. It does not establish uniqueness on the full
Hermitian quotient, does not identify a physical16 flavor point, and does
not authorize the algebraic score as an executable instrument.

## Disposition

Retain the orbit as a full-quotient strict local maximum. The next mathematical
gate is a global upper-hull theorem or an exact remote dominator. The physical
gate remains a source-derived coefficient ratio and calibrated instrument.

