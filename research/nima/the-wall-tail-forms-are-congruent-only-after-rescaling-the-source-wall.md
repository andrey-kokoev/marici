# The wall–tail forms are congruent only after rescaling the source wall

## Purpose

The causal multiplier audit rules out vanishing of the shifted-history
wall–tail cross term on every nonzero incidence vector.  This note performs
the next finite-dimensional calculation: the exact congruence between the
independent wall/tail block forms.

It also identifies why abstract positive-form congruence is not yet the
first-Adams theorem: eliminating the cross term while retaining the saturated
wall coefficient necessarily rescales the wall coordinate.

## The two block forms

Write an independent wall/tail vector as \((w,t)\), and abbreviate
\(M=M_\Phi>0\).  The shifted-history graph energy is

\[
\|w\|^2+\|Mw+t\|^2,
\]

with block matrix

\[
G_{\rm hist}=
\begin{pmatrix}
1+M^2&M\\
M&1
\end{pmatrix}.
\]

The Fourier-saturated zero-cross-term prescription is

\[
(1+M^2)\|w\|^2+\|t\|^2,
\]

with

\[
G_{\rm sat}=
\begin{pmatrix}
1+M^2&0\\
0&1
\end{pmatrix}.
\]

These formulas concern the independent two-port block.  Pulling back along
\(t=Bw\) recovers the nonzero causal cross term found in the preceding audit.

## Exact unconstrained congruence

Set

\[
s=\sqrt{1+M^2},
\qquad
S=
\begin{pmatrix}
s&0\\
-Ms&1
\end{pmatrix}.
\]

A direct multiplication gives

\[
S^*G_{\rm hist}S=G_{\rm sat}.
\]

Equivalently, this congruence changes coordinates by

\[
(w,t)\longmapsto (sw,t-Msw).
\]

Thus there is no inertia or positivity obstruction between the two abstract
forms.

## Wall-normalized triangular congruence fails

Suppose instead that source normalization requires the wall coordinate and
the tail quotient to remain fixed.  The most general scalar triangular shear
with those two associated-graded maps equal to the identity is

\[
S_c=
\begin{pmatrix}1&0\\c&1\end{pmatrix}.
\]

Then

\[
S_c^*G_{\rm hist}S_c=
\begin{pmatrix}
1+M^2+2M\operatorname{Re}c+|c|^2&M+\overline c\\
M+c&1
\end{pmatrix}.
\]

Zero cross term forces \(c=-M\).  At that unique value,

\[
S_{-M}^*G_{\rm hist}S_{-M}=I,
\]

not \(G_{\rm sat}\).  The wall coefficient drops from \(1+M^2\) to \(1\).
Therefore no wall-normalized unit-diagonal triangular shear converts the
history form into the saturated form.

More generally, for

\[
S_{a,c}=\begin{pmatrix}a&0\\c&1\end{pmatrix},
\]

zero cross term forces \(c=-Ma\), after which the wall coefficient is
\(|a|^2\).  Matching \(G_{\rm sat}\) forces

\[
|a|^2=1+M^2.
\]

The required wall rescaling is therefore unavoidable in this triangular
class.

## First-Adams consequence

The remaining question is no longer whether some congruence exists.  It is
whether the completed first-Adams edge authorizes the specific rescaling

\[
w\mapsto \sqrt{1+M_\Phi^2}\,w
\]

and compensating tail shear

\[
t\mapsto t-M_\Phi\sqrt{1+M_\Phi^2}\,w
\]

without changing:

- the canonical tensor-unit counit;
- even-wall and odd-jump normalization;
- the ordered primitive reconstruction;
- reflection covariance;
- radical descent and cutoff maps;
- prime-uniform form bounds.

If the tensor-unit counit freezes the wall map as the identity, this exact
triangular comparison is not source-authorized.  One must then either locate
an additional metric-bearing port whose Schur return restores the missing
\(M_\Phi^2\) wall energy, or prove that the target completed Green form is the
history form rather than the saturated diagonal form.

## Status

The abstract block-congruence calculation is closed.  The source-natural
congruence is not.  The earliest unresolved datum is now the wall
normalization of the completed quadratic edge: does its tensor-unit map allow
the factor \(\sqrt{1+M_\Phi^2}\), or is an additional Schur port required?
G1.1 remains open.
