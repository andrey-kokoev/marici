# Erratum: site exchange does not yet identify v_alg inside one split-fiber pencil

## Question

Does the known exchange \(x\leftrightarrow y\) induce the specific permutation \(d_2\leftrightarrow d_3\), \(d_1,d_4\) fixed, on the four component differences of the reflection-adapted pencil?

## Claim boundary

This packet retracts that unsupported identification. It retains the verified exchange character of the displayed de Rham expression \(v_{\rm alg}\) and the independently verified \(A_1^3\) primitive closure.

## Two different diagrams

The four total-energy critical values are

\[
0,
\quad2x,
\quad2y,
\quad2(x+y).
\]

Site exchange fixes the endpoint values and swaps the two middle values.

The four split fibers defining \(d_1,\ldots,d_4\), however, belong to the reflection-adapted pencil with base coordinate \(q=b/h\):

\[
q=\pm(y+z),
\qquad
q=\pm(2x+y+z).
\]

Site exchange also swaps \(a\) and \(b\). It therefore changes the chosen projection and reflection-adapted pencil rather than acting as a proved automorphism of this fixed \(q\)-pencil. No current artifact supplies an integral Picard comparison from the exchanged pencil back to the original one.

Consequently the assignment

\[
d_1\mapsto d_1,
\qquad d_2\leftrightarrow d_3,
\qquad d_4\mapsto d_4
\]

is not derived.

## Surviving character statement

The de Rham expression

\[
v_{\rm alg}=x^2y^2\bigl((x^2-y^2)e_7+2e_8-2e_9\bigr)
\]

changes sign under the displayed coordinate exchange \(x\leftrightarrow y\), \(e_8\leftrightarrow e_9\). This proves its character in that presentation. It does not select an odd line in a fixed integral \(A_1^3\) lattice until the exchanged-pencil comparison is constructed.

Indeed, the lattice \(A_1^3\) admits three coordinate-swap involutions. Their odd primitive lines are respectively

\[
\alpha_1-\alpha_2,
\qquad
\alpha_1-\alpha_3,
\qquad
\alpha_2-\alpha_3.
\]

All preserve the same Gram matrix. Without a labelled action, the abstract character \(-1\) does not choose among them.

## Correct information flow

The required route is

\[
\text{source site exchange}
\longrightarrow
\text{comparison of the two reflection-adapted pencils}
\longrightarrow
\text{integral action on }\langle d_1,d_2,d_3,d_4\rangle^{\rm sat}
\longrightarrow
\text{odd primitive line}
\longrightarrow
v_{\rm alg}.
\]

The second arrow is the first missing typed map. Skipping it conflates exchange of total-energy punctures with an action on split fibers of another pencil.

## Disposition

The primitive half-sum-edge carrier remains valid, but the claimed identification of \((d_2-d_3)/2\) with \(v_{\rm alg}\) is withdrawn. The normalization problem cannot yet be reduced to one scalar because the integral odd line itself has not been selected in the fixed pencil.

Verification:

- `research/voevodsky/checkers/check_site_exchange_fixed_pencil_gate.py`
- `research/voevodsky/results/site_exchange_fixed_pencil_gate.json`
