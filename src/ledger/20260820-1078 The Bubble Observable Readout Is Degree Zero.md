# 1078 — The Bubble Observable Readout Is Degree Zero

## Question

Entry 1075 found a genuine one-dimensional degree-one class in the full
three-wall Čech nerve of the two-site bubble spurious-kernel arrangement:

\[
\dim H^0=3,
\qquad
\dim H^1=1,
\qquad
\dim H^2=0.
\]

Does the physical bubble observable defined in the frozen primary source
canonically evaluate this degree-one class?

## Frozen source readout

In arXiv:2408.16386, equation (40) writes the loop-edge bubble as a linear
combination of global rational integrals. Equations (43)--(45) place these
integrals in one six-master period family and choose its canonical basis.
Equation (46) supplies the connection on that global master vector. Appendix B
fixes boundary data at the single common point

\[
(\widetilde x_1,\widetilde x_2,P)=(1,1,1),
\]

and equation (47) is the resulting closed physical expression.

Thus the source-defined observable is a degree-zero functional on a global
master fiber, together with the exchanged labelled occurrence. Its boundary
input is likewise degree zero: Entry 1074 proved that the source boundary space
is the common kernel and factors through \(H^0\).

## Variance gate

For the full Čech complex

\[
C^0=K_6\oplus K_7\oplus K_8,
\qquad
C^1=V_{67}\oplus V_{68}\oplus V_{78},
\qquad
C^2=V_{678},
\]

the surviving corner line is

\[
H^1=\ker(d_1)/\operatorname{im}(d_0).
\]

To evaluate it, the source would have to provide a degree-one, pair-overlap
functional

\[
\eta:C^1\longrightarrow \mathbb F
\]

that annihilates \(\operatorname{im}(d_0)\), respects the labelled overlap
orientations, and has the required support provenance. Equations (39)--(47)
and Appendix B provide no such map. A linear functional on the global master
vector cannot be silently retyped as a functional on pair-overlap cochains.

## Narrow result

\[
\boxed{
\text{The frozen physical bubble readout factors through degree zero and does
not canonically activate the degree-one corner line.}
}
\]

This does **not** say that the \(H^1\) class vanishes. It says that the class is
an intrinsic derived coefficient obstruction that remains physically
unselected by the published source prescription.

The closed expression in equation (47) cannot be used retrospectively to fit
an overlap functional: that would add a map after seeing the target.

## Consequence for the cosmology program

The two-site bubble now exhibits all three layers distinctly:

\[
\text{shared labelled wall carrier}
\quad+\quad
\text{nontrivial derived coefficient }H^1
\quad+\quad
\text{degree-zero physical readout}.
\]

This supports the refined H2 architecture while preserving the central
warning

\[
\text{coefficient cohomology}
\not\Rightarrow
\text{physical activation}.
\]

## Next falsifier

Seek a source-defined observable or factorization operation whose domain is
genuinely a labelled pair-overlap or supported degree-one object. If none is
present, the bubble corner line should remain classified as unselected
coefficient data rather than promoted to a cosmological primitive.

## Durable packet

- `research/benincasa/bubble-observable-readout-variance.json`
- `research/benincasa/check_bubble_parabolic_complex.rs`
- `research/benincasa/bubble-full-cech-nerve.json`
- `research/benincasa/bubble-physical-boundary-factorization.json`

