# Clifford Formulation of the Four-Port RH Boundary Object

## The four generators

Let the labelled boundary space have four generators:

\[
e_P,
\quad e_Q,
\quad e_M,
\quad e_J.
\]

They represent the two reciprocal tail instruments, seam value, and seam flux.
The corresponding Clifford-valued state is

\[
\Psi=P e_P+Q e_Q+M e_M+J e_J.
\]

The metric used to form the Clifford algebra must be derived from the source
energy. The orientation calculation below does not require choosing its final
signature; it uses only the exterior grades embedded in the Clifford algebra.

## Two oriented planes

The four-port object contains two distinguished bivectors:

\[
I_{\mathrm{tail}}=e_P\wedge e_Q,
\qquad
I_{\mathrm{seam}}=e_M\wedge e_J.
\]

Their product is the four-dimensional pseudoscalar

\[
I_4=I_{\mathrm{tail}}I_{\mathrm{seam}}.
\]

Reciprocal sewing acts by

\[
e_P\leftrightarrow e_Q,
\qquad
e_M\mapsto e_M,
\qquad
e_J\mapsto-e_J.
\]

Therefore

\[
I_{\mathrm{tail}}\mapsto-I_{\mathrm{tail}},
\qquad
I_{\mathrm{seam}}\mapsto-I_{\mathrm{seam}},
\qquad
I_4\mapsto I_4.
\]

This is the key structural gain. Reciprocal sewing reverses each constituent
two-plane but preserves the orientation of the complete four-port object. The
seam-flux sign is the partner that compensates the tail-sector exchange.

If \(e_J\) is omitted, the remaining three-dimensional volume blade changes
sign. The three-port model therefore represents reciprocal sewing as an
unmatched orientation reversal.

## Boundary pairing inside the algebra

The seam boundary determinant is the coefficient of the seam bivector:

\[
(M e_M+J e_J)\wedge(M'e_M+J'e_J)
=(MJ'-JM')I_{\mathrm{seam}}.
\]

Thus the earlier symplectic test is already a Clifford-grade test. A nonzero
seam bivector coefficient proves that value and flux span a genuine plane. A
graph relation \(J=LM\) makes every pair collinear and annihilates this grade.

## Cutoff transport and the coherence line

If cutoff transport acts on the seam plane by \(S_{X,Y}\), then

\[
I_{\mathrm{seam}}
\mapsto
\det(S_{X,Y})I_{\mathrm{seam}}.
\]

The determinant-line coherencer is therefore not external bookkeeping. It is
the scalar coefficient by which transport acts on a source-defined Clifford
bivector. Together with tail transport, it determines the action on \(I_4\).

Strict four-port coherence requires the product of the tail-plane and
seam-plane determinant characters to preserve the total pseudoscalar. A
nonunit product is the exact top-grade anomaly.

## Candidate RH mechanism

A completed scalar zero sees only a grade-zero projection. The full
Clifford-valued comparison may still retain:

- tail orientation in \(I_{\mathrm{tail}}\);
- seam orientation in \(I_{\mathrm{seam}}\);
- their conserved total orientation in \(I_4\);
- mixed tail–seam bivectors encoding current matching.

The source theorem to seek is not generic positivity of this algebra. It is a
grade-resolved conservation law showing that an off-seam scalar cancellation
would require an unmatched odd bivector or a top-grade transport anomaly.

The immediate finite falsifier remains source-local: compute the seam-bivector
coefficient and the total-pseudoscalar transport factor after adjoining one
labelled arithmetic block. If either fails the declared reciprocal character,
the four-port Clifford model is wrong. If both close, the scalar projection has
been shown to discard a genuine conserved orientation channel.
