# Mixed OS Residue Sign-Pair Audit

## Question

Can a sign-sensitive reflection-positive mixed correlator supply the odd flavor
probe missing from WP815, while purity fixes its magnitude and thresholds
preserve the result?

## Marked spectral germ

Take two independently identified source operators \(O_1,O_2\) with a common
positive pole \(\Delta\). Their one-pole Euclidean residue matrix is

\[
R=
\begin{pmatrix}
A&C\\
C&B
\end{pmatrix}.
\]

The mixed entry \(C\) is sign-sensitive. The marked germ must retain both
operator identities, their relative sign port, state provenance, pole,
diagonal residues, mixed residue, and detector attachments. Without those
marks, \(C\) can be changed by the presentation transformation
\(O_2\mapsto-O_2\).

## Reflection positivity and purity

Reflection positivity requires

\[
A\ge0,
\qquad
B\ge0,
\qquad
AB-C^2\ge0.
\]

Thus positivity bounds the normalized mixed residue

\[
\rho=\frac{C}{\sqrt{AB}}
\]

by \(|\rho|\le1\), but is invariant under \(C\mapsto-C\).

If an independent purity condition makes the residue rank one, then

\[
AB-C^2=0
\quad\Longrightarrow\quad
C=\pm\sqrt{AB},
\qquad
\rho=\pm1.
\]

Purity therefore fixes the normalized magnitude exactly while retaining two
sign branches. The normalized hostile matrices

\[
R_+=
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
R_-=
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\]

are both positive rank-one matrices with identical spectra and diagonal
readouts. Their mixed correlators have opposite sign.

## Physical versus presentation sign

The matrix \(S=\operatorname{diag}(1,-1)\) obeys

\[
S R_+ S=R_-.
\]

Consequently the mixed sign is physical only relative to independently fixed
operator identities and their incidence with the source and detector. If the
relative operator sign port is unconsumed, the pair is one presentation orbit.
Fixing it defines a relational experiment over its stabilizer groupoid; it does
not make positivity choose the sign.

This exactly parallels the earlier flavor distinction between a weak-basis
invariant and a chart phase. A mixed matrix entry is not automatically a
faithful flavor orientation.

## Threshold transport

Positive diagonal wavefunction transport

\[
R\longmapsto ZRZ,
\qquad
Z=\operatorname{diag}(z_1,z_2),quad z_i>0,
\]

preserves \(\rho=\pm1\). This supplies a conditional threshold-protection
theorem for the normalized relation. A nonaligned mixing threshold can rotate
\(R_+\) to a diagonal residue and erase the fixed-axis cross readout. Protection
therefore requires the source to preserve the two marked operator lines, not
merely positivity of the total spectral matrix.

The absolute diagonal residues \(A,B\) still run. Rank-one purity fixes only a
ratio-normalized magnitude, not the absolute portal scale.

## Probe family and instrument

The calibrated three-channel family

\[
(R_{11},R_{22},R_{12})=(A,B,C)
\]

is faithful on the real symmetric residue packet. This is a genuine
sign-sensitive readout. Without cross-channel gain calibration, the record
\(r=s_C C\) has rank one on \((C,s_C)\); for example
\((C,s_C)=(1,2)\) and \((1/2,4)\) give the same value.

The actual flavor instrument must realize \(O_1\) and \(O_2\) in a common
source/detector frame and must prove that \(C\) descends to the faithful
`physical16` orientation. Formal access to a matrix entry is insufficient.

## Aspect germ classification

The sign target is relational and must be formed before quotienting either
operator by its independent sign port. Its minimal germ contains:

```text
MixedFlavorOSGerm
  first_operator_germ
  second_operator_germ
  common_state_and_pole_germ
  relative_operator_sign_cell
  mixed_residue
  purity_authority
  threshold_line_preservation
  detector_cross_calibration
  physical16_descent
```

The target fails descent through a local quotient that forgets either operator
sign, because the mixed contraction changes sign. The relational mate must be
formed first.

## Classification and smallest falsifiers

Reflection positivity is a bound and realization condition. Rank-one purity is
a conditional normalized-magnitude selector. The mixed correlator is a
sign-sensitive probe. None selects the sign: \(R_+\) and \(R_-\) are the
smallest exact pair. Nor is purity presently source-authorized. The smallest
instrument falsifier is the cross-residue/gain pair above.

## Deutschian appraisal

This architecture explains how magnitude and sign should be separated. A
positive pairing plus purity can make the normalized magnitude unavoidable,
while an odd mixed channel makes the sign observable. But positivity is even
in that sign. The missing explanation is now concentrated in a source-derived
orientation of the operator incidence, not in the spectral reconstruction.

The sharp successor is an anomaly- or index-authorized trilinear incidence
among the two operators and the horizon orientation. It must fix the relative
operator sign before the OS quotient, protect the marked lines through
thresholds, and supply the calibrated cross-channel detector. If the incidence
again has a conjugate partner, the mirror no-go returns.

## Assumptions and falsifiers

The positive results assume a common one-pole domain and real symmetric residue
matrix. Purity is tested conditionally and is not claimed as flavor dynamics.
A source action deriving rank-one saturation, one relative incidence sign,
absolute residues, line-preserving thresholds, and detector gain would falsify
the residual negative conclusion.

## Disposition

Progressive architecture, incomplete source. Mixed OS data supplies the first
faithful sign-sensitive probe and purity can fix normalized magnitude, but the
relative operator orientation, purity law, absolute scale, and instrument
calibration remain unselected.
