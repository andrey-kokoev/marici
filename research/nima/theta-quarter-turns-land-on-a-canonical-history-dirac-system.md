# Theta quarter-turns land on a canonical history Dirac system

## Status

Exact geometric construction and revised candidate architecture. Rotating the
full source-incidence graph through its conormal produces the adjoint arrow.
Combined with Fourier, sector, spectral, and port rotations, the mechanism
becomes a selfadjoint Dirac system or an equivalent skew-adjoint conservative
flow. The scalar zero-to-spectrum bridge remains unproved.

## 1. Incidence graph rotation

Let

\[
H:\mathcal C\supset\operatorname{Dom}H\longrightarrow\mathcal S
\]

be the closed, densely defined full-history synthesis from coefficient packets
to the seam state. Its graph is

\[
\Gamma(H)
=
\left\{
(c,Hc):c\in\operatorname{Dom}H
\right\}
\subset
\mathcal C\oplus\mathcal S.
\]

A vector \((d,g)\) is orthogonal to this graph exactly when

\[
\langle d,c\rangle_{\mathcal C}
+
\langle g,Hc\rangle_{\mathcal S}
=
0
\]

for every \(c\in\operatorname{Dom}H\). Hence

\[
d=-H^*g
\]

and

\[
\Gamma(H)^\perp
=
\left\{
(-H^*g,g):g\in\operatorname{Dom}H^*
\right\}.
\]

After swapping the two factors, this is the graph of \(-H^*\):

\[
\mathsf S\Gamma(H)^\perp
=
\Gamma(-H^*).
\]

Thus the adjoint arrow is generated canonically by a quarter-turn from a
relationship to its conormal, followed by exchange of source and target axes.

This construction uses the full graph and both source metrics. Scalar
conjugation cannot replace it.

## 2. Exact theta history pair

For the moving seam history,

\[
(Hc)(t)
=
\int_t^\infty
\Phi(q-t)c(q)\,dq.
\]

Its Hilbert adjoint is

\[
(H^*g)(q)
=
\int_0^q
\Phi(q-t)g(t)\,dt.
\]

The first is anti-causal history synthesis; the second is causal backreaction.
Both have cutoff-growing rank. The adjoint is not a reflected rank-one source
port.

## 3. Dirac and Hamiltonian rotations

On

\[
\mathcal C\oplus\mathcal S
\]

define

\[
\mathscr D_H
=
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix}
\]

with domain

\[
\operatorname{Dom}H\oplus\operatorname{Dom}H^*.
\]

For closed densely defined \(H\), the block operator \(\mathscr D_H\) is
selfadjoint.

The dynamical quarter-turn is

\[
\mathscr K_H
=
\begin{pmatrix}
0&-H^*\\
H&0
\end{pmatrix}.
\]

It is skew-adjoint and generates a unitary conservative flow when its domain
conditions are satisfied.

Their squares expose the positive source and seam Gramians:

\[
\mathscr D_H^2
=
\begin{pmatrix}
H^*H&0\\
0&HH^*
\end{pmatrix}.
\]

Therefore adjoint completion, conservative backreaction, and positive Gram
formation are three rotations of one full-history incidence.

## 4. Rotation in scale and frequency

Fourier transformation rotates logarithmic translation into phase
multiplication. The anti-causal and causal history operators acquire conjugate
Hardy boundary values. Schematically,

\[
\mathcal F H\mathcal F^{-1}
=
M_{\overline h}
\]

and

\[
\mathcal F H^*\mathcal F^{-1}
=
M_h,
\]

with the appropriate half-line Hardy projections retained.

The projections are essential. Dropping them falsely identifies a Toeplitz or
Hankel compression with full-line multiplication.

Grothendieck's audit of

\[
\mathcal F H\mathcal F^{-1}
\]

against \(H^*\) is therefore a test of whether Fourier–Tate sewing implements
the graph-conormal rotation or only changes the multiplier chart.

## 5. Rotation in spectral space

The centered variable

\[
z=s-\frac12
\]

rotates to

\[
\lambda=-iz.
\]

The critical seam becomes the real \(\lambda\)-axis. A skew-adjoint flow
generator \(\mathscr K_H\) becomes the selfadjoint spectral operator

\[
i\mathscr K_H.
\]

Thus conservative scale evolution and real spectral support are quarter-turn
descriptions of the same operator law.

## 6. Rotation in port space

The impedance variables \((u,y)\) rotate to incoming and outgoing waves:

\[
a_{\mathrm{in}}
=
\frac{u+y}{\sqrt2},
\qquad
a_{\mathrm{out}}
=
\frac{u-y}{\sqrt2}.
\]

The supply form becomes

\[
2\operatorname{Re}(\overline u,y)
=
|a_{\mathrm{in}}|^2-|a_{\mathrm{out}}|^2.
\]

This rotation diagonalizes boundary flux. It does not construct \(H^*\); that
comes from graph-conormal rotation.

## 7. Rotation in sector space

Direct and reciprocal sectors rotate into common and difference coordinates:

\[
G_c=\frac{G_++G_-}{\sqrt2},
\qquad
G_d=\frac{G_+-G_-}{\sqrt2}.
\]

This separates trace-like bulk from orientation-sensitive flux. As earlier
Clark calculations showed, sector rotation can cancel spin-two cross terms
when both sectors are already in one source frame. It cannot by itself reverse
the variance of a source incidence.

## The combined rotated mechanism

The rotations organize into one typed chain: source incidence graph, conormal
adjoint graph, Dirac block, Hamiltonian flow, and real spectral problem.

The durable operator is

\[
\mathscr D_H
=
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix}.
\]

This is the first adjoint-complete object derived from an already constructed
theta source map rather than from the scalar completed section.

## Connection to the puncture complex

The Dirac square gives

\[
\ker\mathscr D_H
=
\ker H\oplus\ker H^*.
\]

Thus unpaired states are genuine kernel/cokernel defects of the source-history
incidence. This recovers the earlier Koszul/Fredholm puncture intuition in a
forward-derived form.

However, a scalar theta zero is not yet known to produce a vector in
\(\ker\mathscr D_H\) or an eigenvector of a shifted Dirac operator. That bridge
must be constructed, not inferred from the attractive geometry.

## Immediate finite compiler

At cutoff \(X\), build the actual history matrix \(H_X\) and form

\[
D_X
=
\begin{pmatrix}
0&H_X^*\\
H_X&0
\end{pmatrix}.
\]

Verify:

\[
D_X^*=D_X,
\]

\[
D_X^2
=
\operatorname{diag}(H_X^*H_X,H_XH_X^*),
\]

and compare the Fourier–Tate candidate backreaction with \(H_X^*\) before
scalar compression.

The first nonzero residual

\[
R_X^{\mathrm{FT}}
=
B_X^{\mathrm{FT}}-H_X^*
\]

distinguishes source Fourier–Tate adjunction from formal Hilbert adjunction.

## Hard gates

The construction fails to explain RH if:

1. \(H\) is not closed or densely defined in the source completion;
2. the formal adjoint does not preserve arithmetic typing;
3. Fourier–Tate sewing differs from \(H^*\) by a nonzero boundary or measure
   residual;
4. the Dirac graph loses selfadjointness under restricted-product completion;
5. scalar zeros do not map to characteristic states of the Dirac system;
6. hostile prime perturbations preserve the same Dirac characteristic data;
7. the determinant bridge is fitted backward from \(\Xi\).

## Verdict

Rotating every independent axis does not magically prove RH, but it changes
the missing-constructor diagnosis. The adjoint arrow need not be guessed from
a reflected copy: it is canonically generated from the conormal of the full
history-incidence graph. The resulting Dirac system is selfadjoint by
construction. The decisive remaining question is whether Fourier–Tate sewing
selects this canonical adjoint and whether the completed scalar zero is a
characteristic state of the resulting source-derived Dirac operator.
