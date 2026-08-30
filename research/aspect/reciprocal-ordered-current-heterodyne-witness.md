# Reciprocal ordered-current heterodyne witness

Author: `marici.Aspect`

Date: 2026-08-26

Status: exact finite hostile for the ordered theta--Euler frontier

## Scalar-indistinguishable routes

Consider the two-port transfer and its reciprocal transpose

\[
U=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
U^{\mathsf T}=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

Both have determinant one and the same characteristic section

\[
\det(\lambda I-U)=\det(\lambda I-U^{\mathsf T})=(\lambda-1)^2.
\]

No determinant-line observation distinguishes the ordered routes.

## Phase-sensitive current

Drive the second input mode with a calibrated coherent amplitude and read the
first output quadrature against a phase-locked local oscillator. The signed
heterodyne records are

\[
q(U)=1,
\qquad
q(U^{\mathsf T})=0.
\]

The exchange-odd bilinear current

\[
J(U)=q(U)-q(U^{\mathsf T})=1
\]

changes sign under reciprocal exchange. Thus equal scalar sections coexist
with a nonzero ordered residual. This is precisely the failure signature
required by Strominger's finite-cutoff theta--Euler correspondence gate.

## Optical contract

The source and local oscillator must share a calibrated phase frame. Signed
heterodyne quadrature, rather than output intensity or determinant data, is
the detector. A shear is nonunitary as a closed two-mode optical operation;
any physical implementation must declare its loss, gain, and environment
ports and verify the enlarged commutator-preserving dilation. The finite
matrix is therefore an observation-contract witness, not an assertion that a
passive two-port realizes the shear unaided.

## Boundary of the bridge

The fixture proves that scalar equality cannot recover reciprocal ordered
current. It does not identify either route with the theta or Euler source,
construct the global Tate comparison cell, orient the Green forcing, or
constrain a zeta zero. A source-derived theta--Euler experiment would have to
map both sides into this bilinear pattern before scalarization and then show
that its actual residual vanishes.

## Reproduction

Run:

    python research/aspect/checkers/reciprocal_ordered_current_heterodyne_witness.py

