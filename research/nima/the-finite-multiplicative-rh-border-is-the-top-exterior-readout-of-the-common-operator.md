# The finite multiplicative RH border is the top-exterior readout of the common operator

## Source operator

Let \(V_X\) be a finite labelled source carrier and let

\[
T_X(s):V_X\longrightarrow V_X
\]

be the complete finite relative operator assembled before scalar evaluation.
It must retain the declared arithmetic, seam, endpoint, and archimedean ports.
Write

\[
K_X(s)=I-T_X(s)
\]

when comparison with a relative determinant is convenient.

The construction below is formal for any such \(T_X\). Its RH authority
depends entirely on deriving \(T_X\) from the common theta/Tate packet rather
than installing the desired scalar as a matrix entry.

## Top exterior state

Let \(n_X=\dim V_X\). The determinant line is

\[
\mathcal L_X=\bigwedge^{n_X}V_X.
\]

Choose a source-oriented volume section

\[
\omega_X\in\mathcal L_X
\]

and its dual observer

\[
\omega_X^\vee\in\mathcal L_X^\vee,
\qquad
\omega_X^\vee(\omega_X)=1.
\]

Apply the top exterior functor:

\[
u_{\Delta,X}(s)
=
\bigwedge^{n_X}T_X(s)\,\omega_X.
\]

Then the ordered readout is

\[
\Delta_X(s)
=
\omega_X^\vee u_{\Delta,X}(s)
=
\det T_X(s).
\]

This is a source-forward state and observer construction of the full
multiplicative determinant. The scalar is evaluated only after \(T_X\), its
orientation, and its top exterior state exist.

## Canonical multiplicative border

Define

\[
D_{\Delta,X}(s)
=
\begin{pmatrix}
I_{\mathcal L_X}&u_{\Delta,X}(s)\\
\omega_X^\vee&0
\end{pmatrix}
\]

on \(\mathcal L_X\oplus\mathbb C\). Since \(\mathcal L_X\) is one-dimensional,

\[
\det D_{\Delta,X}(s)
=
-\omega_X^\vee u_{\Delta,X}(s)
=
-\Delta_X(s).
\]

If \(\Delta_X(s)=0\), the bordered complex has the canonical kernel vector

\[
\binom{-u_{\Delta,X}(s)}{1}.
\]

For a top exterior map, \(\Delta_X(s)=0\) also means that
\(\bigwedge^{n_X}T_X(s)=0\), equivalently that \(T_X(s)\) is singular.

Thus the finite multiplicative zero is simultaneously:

- failure of the full relative operator to be invertible;
- vanishing of its top exterior state;
- cohomology of the multiplicative border.

## Why this is not the current border

The endpoint-current border uses the relative logarithmic column

\[
u_J=(H_X-\varepsilon(H_X)I)G
\]

and reads the additive current \(J_X\).

The multiplicative border instead uses

\[
u_{\Delta,X}
=
\bigwedge^{n_X}T_X\,\omega_X
\]

and reads \(\det T_X\).

The first records a boundary countercurrent. The second records singularity of
the complete finite operator. Their determinants have different zero loci and
different categorical roles.

The current border may contribute to the construction and normalization of
\(T_X\), but it cannot replace the top-exterior state.

## Composition law

For composable source operators \(T_1,T_2\),

\[
\bigwedge^n(T_2T_1)
=
\left(\bigwedge^nT_2\right)
\left(\bigwedge^nT_1\right).
\]

Therefore

\[
\Delta(T_2T_1)
=
\Delta(T_2)\Delta(T_1).
\]

The determinant line automatically supplies the generator-wise
semi-invariance character required by the zero sieve, provided the source
action acts on the same carrier and preserves the chosen determinant-line
typing.

Presentation coherence follows from functoriality of the top exterior power,
not from scalar fitting.

## Third-order regularized form

At large cutoff, the ordinary top exterior power is replaced by the relative
determinant line. For an \(S_3\)-class perturbation, the connected section is

\[
\det_3(I-K_X).
\]

Primitive and square anomaly lines normalize it by

\[
\Delta_{3,X}
=
e^{P_1(K_X)+P_2(K_X)}
\det_3(I-K_X)^{-1}
\]

for the inverse-determinant convention, or by the corresponding signed direct
determinant convention.

At finite rank this equals the ordinary determinant section. The equality is
the transition map from the top-exterior line to the third-order relative
determinant line.

Hence the finite top-exterior border and the third-order boundary
totalization are two presentations of one multiplicative object, provided all
three terms come from the same \(K_X\).

## Orientation dependence

Replacing \(\omega_X\) by \(c_X\omega_X\) and
\(\omega_X^\vee\) by \(c_X^{-1}\omega_X^\vee\) leaves
\(\Delta_X\) unchanged. But changing only one side multiplies the readout by a
unit.

Therefore the determinant scalar is canonical only after the source supplies
a paired orientation or duality frame. A cutoff-dependent unpaired rescaling
can preserve every zero while destroy completion and reciprocal coherence.

The Gaussian Mellin line and reciprocal sewing must participate in fixing this
frame; positivity of the finite determinant magnitude is not enough.

## Xi bridge

To identify the completed border with RH, one needs a source-derived line
isomorphism

\[
\theta_s:
\mathcal L_{\Delta,s}
\longrightarrow
\mathcal L_{\Xi,s}
\]

such that

\[
\theta_s(u_\Delta(s))
=
v(s)\Xi(s)
\]

for an independently controlled invertible section \(v(s)\).

This is stronger than matching finite scalar values. The map must commute with:

- cutoff inclusions;
- reciprocal transport;
- seam orientation;
- Gaussian Mellin dilation;
- primitive and square anomaly-line transitions.

Without these cells, the top-exterior determinant is a valid multiplicative
readout but not yet the completed \(\Xi\) readout.

## Completion and observability

The top exterior line is automatically one-dimensional at each finite cutoff,
but its inverse or direct limit need not remain a faithful observer of the
completed state.

The completion gate requires:

1. a relative determinant line \(\mathcal L_\Delta\);
2. compatible finite sections \(u_{\Delta,X}\);
3. no escape of singular directions outside every finite cutoff;
4. a uniform lower determinant or singular-value margin on compact subsets of
   each claimed open sector;
5. exactness of the limit kernel comparison.

Finite nonvanishing alone does not provide these conditions.

## Hostile tests

1. Installing \(\Xi\) as an entry of \(T_X\) is circular.
2. Using the endpoint-current column in place of the top exterior state
   confuses logarithm and determinant.
3. Choosing unrelated operators for \(P_1\), \(P_2\), and \(\det_3\) destroys
   the common determinant line.
4. A cutoff-dependent orientation factor can prevent descent despite unchanged
   finite zeros.
5. Finite invertibility with smallest singular value tending to zero permits a
   completion kernel.
6. A scalar determinant equality without a line isomorphism does not establish
   the \(\Xi\) bridge.

## Consequence for categorical RH

The finite multiplicative border \(D_{\Delta,X}\) is now canonical once the
complete source operator \(T_X\) and its orientation are given. It supplies the
correct zero-to-state bridge and carries a multiplicative action character.

The remaining constructive problem is sharply localized: assemble the actual
theta/Tate \(T_X\) from the logarithmic Euler translation carrier, seam and
endpoint complex, Gaussian line, and reciprocal sector link, then prove
relative-determinant descent and identify its completed line with \(\Xi\).

## Verdict

The RH-bearing finite border is the border of the top-exterior state of the
complete common operator. This corrects the additive-current border without
discarding it. Categorical RH now needs a source-derived complete operator and
a completion-stable determinant-line bridge, not another scalar determinant
identity.
