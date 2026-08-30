# 2269 — The Missing Tensor Polarization Exactly Recovers the Detector Blind Line

## Detector complexes

Let the occurrence packet be \(P=\mathbb Q^3\).  A detector exposing the
scalar and plus ports has map

\[
D_+=
\begin{pmatrix}
1&1&1\\
2&-1&-1
\end{pmatrix}
\]

and kernel

\[
K_+=\mathbb Q\langle(0,1,-1)\rangle.
\]

The omitted cross port is

\[
q_\times=(0,-1,1).
\]

Its restriction to the detector kernel is

\[
q_\times(0,1,-1)^T=-2.
\]

Hence

\[
q_\times|_{K_+}:K_+\xrightarrow{\sim}\mathbb Q.
\]

The reciprocal statement also holds.  Scalar plus cross has kernel

\[
K_\times=\mathbb Q\langle(-2,1,1)\rangle,
\]

and the plus port restricts by multiplication by \(-6\).

## Supported-cone classification

The one-polarization observation cone has one rank-one kernel class.  Adding
the complementary source-derived polarization kills that class exactly; the
completed detector cone is acyclic:

\[
\boxed{
H^\bullet\operatorname{Cone}(D_+\oplus q_\times)=0
}
\]

and similarly with plus and cross exchanged.

Therefore the one-polarization rank loss is an instrument projection, not
route loss, transport support, or a missing Carrier cell.  The lost occurrence
combination survives completely in the omitted physical port.

## Scope

This closes the detector mapping cone at the leading soft grade.  It does not
close a finite-\(q\) cone, because Entry 2267 shows that the corresponding
source transfer remains underived.

## Verification

`research/benincasa/checkers/polarization_detector_recovery_cone.rs` verifies
both kernels and complementary recovery maps exactly.
