# The three positive faces determine an internal positive H134 filler but not the external endpoint Schur identification

## Fixed tetrahedron

Fix one lattice tetrahedron. Its four faces are

\[
H_{123},
\qquad
H_{124},
\qquad
H_{134},
\qquad
H_{234}.
\]

The repository now supplies internal positive lifts of three faces:

1. \(H_{123}^+\) by unitary source-to-spectral transport;
2. \(H_{124}^+\) by the regulated eight-leg cutoff feature with its volume coordinate;
3. \(H_{234}^+\) by the common-face decomposition of the two internal polarities.

All three are source labelled and agree on their shared edges.

## Derived fourth face

Let \(S_i^+\) denote the positive source chart at vertex \(i\), restricted to the generated essential image. Let \(R_i^+\) be its inverse there.

The positive transition from vertex \(3\) to vertex \(4\) is forced by the other source-rooted faces:

\[
C_{34}^{+,derived}
=
S_4^+R_3^+.
\]

Both routes around the boundary reduce to this map:

\[
C_{24}^+C_{32}^+
=
S_4^+R_2^+S_2^+R_3^+
=
S_4^+R_3^+,
\]

and

\[
C_{14}^+C_{31}^+
=
S_4^+R_1^+S_1^+R_3^+
=
S_4^+R_3^+.
\]

Thus the internal positive horn has a unique derived \(H_{134}\) face up to the canonical target isometry.

No Schur estimate is needed to construct this derived internal face.

## Derived endpoint row

Let

\[
X_{134}^{derived}
\]

be the resulting positive feature. Its endpoint coordinate is obtained by projection to the odd endpoint target:

\[
b_k^{derived}
=
P_{odd}X_{134}^{derived}.
\]

Let \(C_k^{derived}\) be the Gram of the complementary bulk coordinate. Since both coordinates belong to one Hilbert feature, Cauchy--Schwarz and orthogonal decomposition give

\[
C_k^{derived}
\succeq
b_k^{derived}(b_k^{derived})^*.
\]

Equivalently, the associated Schur block is positive because it is already a Gram block.

Therefore the internal positive tetrahedron is complete.

## External Green endpoint row

Independently, contour deformation and Green's identity construct a source endpoint coupling

\[
b_k^{Green}.
\]

They prove equality of its signed scalar pullbacks with the spectral endpoint term. They do not automatically prove

\[
b_k^{Green}
=
b_k^{derived}
\]

as vectors in the same positive bulk feature carrier.

This equality is the missing positive comparison.

## Reinterpretation of the Schur gate

The inequality

\[
C_k\succeq b_k^{Green}(b_k^{Green})^*
\]

should not be described as existence of an internal positive \(H_{134}\) filler. That filler is derived from the other three positive faces.

The inequality asks whether the independently constructed Green/endpoint realization embeds contractively into the derived internal positive face.

Equivalently, it asks for an isometry or contraction \(J_k\) satisfying

\[
J_kb_k^{Green}
=b_k^{derived}.
\]

At Gram level, this is the rank-one Douglas leverage condition.

## Two possible conventions

### Internal endpoint convention

Define the positive endpoint row to be

\[
b_k:=b_k^{derived}.
\]

Then the positive tetrahedron and its Schur inequality are closed formally. The contour Green row remains a signed readout comparison.

### External physical endpoint convention

Require the endpoint row to be the independently normalized Green/Wronskian feature

\[
b_k:=b_k^{Green}.
\]

Then one must prove the contractive identification with the derived row. This is the arithmetic Schur--Douglas theorem.

## Analogy with the regular C34 distinction

The same distinction occurred for the regular positive cell:

- internal transported positive feature: coherence is formal;
- external prolate/Widom realization: positive comparison is additional.

Here the distinction is:

- internal derived endpoint feature: positive horn filling is formal;
- external Green/Wronskian endpoint feature: contractive comparison is additional.

## Consequence for the 210-cell lattice

Every tetrahedron has its internal positive fourth face determined by the other three positive source-rooted faces. Successor naturality follows from the strict source chart construction.

The remaining arithmetic theorem is one natural transformation comparing the external Green endpoint bundle with these derived internal endpoint rows. It is not 210 unrelated positivity inequalities.

## Disposition

The lattice-positive \(H_{134}\) filler is constructed internally by source-chart transport. The Schur gate survives only as external realization compatibility:

\[
b_k^{Green}
\longrightarrow
b_k^{derived}
\]

contractively and successor-naturally.

Thus positive lattice completion is closed internally. Identification with the physical Green endpoint realization remains the arithmetic-strength theorem.
