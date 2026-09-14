# The Suzuki Toeplitz complex retains kernel and cokernel as a signed harmonic boundary

## Motivation

Projection onto

\[
V=\ker L
\]

retains only one side of the generalized-inner Toeplitz geometry. In finite models, a forbidden denominator excess appears instead in

\[
\operatorname{coker}L\simeq\ker L^*.
\]

The smallest source-defined object retaining both is the two-term Hilbert complex

\[
0\longrightarrow H_+
\xrightarrow{L}
H_+
\longrightarrow0,
\]

where `L` denotes the linearized conjugate-Toeplitz leakage.

## Supersymmetric doubling

On

\[
\mathcal H=H_+^{even}\oplus H_+^{odd},
\]

define

\[
\mathcal D=
\begin{pmatrix}
0&L^*\\
L&0
\end{pmatrix},
\qquad
\Gamma=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix}.
\]

Then

\[
\mathcal D=\mathcal D^*,
\qquad
\Gamma\mathcal D+\mathcal D\Gamma=0,
\]

and

\[
\boxed{
\mathcal D^2=
\begin{pmatrix}
L^*L&0\\
0&LL^*
\end{pmatrix}
\succeq0.
}
\]

Thus the doubled bulk energy is an unconditional positive square.

## Harmonic boundary

The harmonic space is

\[
\ker\mathcal D
=
\ker L\oplus\ker L^*.
\]

Its two components are exactly

\[
H^0=\ker L,
\qquad
H^1=\ker L^*\simeq\operatorname{coker}L
\]

when the range is closed. The grading induces the signed harmonic form

\[
Q_{harm}(u,v)=\|u\|^2-\|v\|^2.
\]

Therefore the complete Toeplitz complex naturally carries

\[
\boxed{
\text{positive bulk }\mathcal D^2

\quad+
\text{signed boundary }(\ker L)-(\ker L^*).
}
\]

This is the correct abstract structure for retaining a divisor obstruction instead of projecting it away.

## Finite-Blaschke check

For

\[
L=T_{\bar S B},
\qquad
m=\deg S,
\quad n=\deg B,
\]

the previous index calculation gives

\[
\dim H^0=\max(m-n,0),
\qquad
\dim H^1=\max(n-m,0).
\]

Hence the graded harmonic dimension is

\[
\operatorname{sdim}\ker\mathcal D
=\dim H^0-\dim H^1
=m-n
=\operatorname{ind}L.
\]

The supersymmetric complex reproduces the exact Toeplitz index orientation.

## Heat regularization

For `t>0`, the positive heat operator

\[
e^{-t\mathcal D^2}
=
\begin{pmatrix}
e^{-tL^*L}&0\\
0&e^{-tLL^*}
\end{pmatrix}
\]

is source-defined from `L`. In finite-rank or trace-class-relative settings, its graded trace satisfies the McKean--Singer identity

\[
\operatorname{Str}(e^{-t\mathcal D^2})
=\operatorname{ind}L.
\]

Thus positive heat evolution in each parity sector retains a signed, time-independent boundary index after terminal graded polarization.

This resembles the completed endpoint--gamma--prime architecture more closely than an ordinary projection: positive bulk pieces can cancel under a final signed trace while the cokernel remains visible.

## Why this is not yet Weil positivity

The grading form is indefinite whenever `ker L*` is nonzero. Supersymmetric doubling explains and preserves the sign; it does not turn it positive. To identify the construction with the Weil functional, one still needs a source Green identity of the form

\[
Q_W(f,g)
=
\langle A_{even}f,A_{even}g\rangle
-
\langle A_{odd}f,A_{odd}g\rangle,
\]

with the odd harmonic sector corresponding exactly to the forbidden divisor contribution.

Eliminating the odd sector would require

\[
\ker L^*=\{0\},
\]

or a source differential pairing it acyclically with an additional positive state. In the finite-Blaschke model, `ker L*=0` is equivalent to `deg B<=deg S`, not to absence of every forbidden pole; index alone is too weak.

## Required refinement beyond index

Off-axis zero pairs have net index zero but nontrivial Krein signature `(1,1)`. A scalar Toeplitz index can therefore miss them. The complex must retain the full harmonic spaces and their evaluation representation, not collapse them to

\[
\dim H^0-\dim H^1.
\]

A valid arithmetic comparison must match individual divisor multiplicities and conjugation orbits before taking a supertrace.

## Candidate endpoint completion

The only genuine repair available in this language is to enlarge the complex by a source-derived boundary differential

\[
R:H^1\longrightarrow E_{endpoint}
\]

such that the odd harmonic sector becomes exact while its image contributes a positive endpoint norm. For this to prove positivity, `R` must be:

1. injective on every forbidden divisor mode;
2. defined from endpoint--gamma--prime data rather than the zero list;
3. compatible with conjugation and translation;
4. bounded in the completed source norm.

The earlier translation argument shows that a bounded covariant `R` cannot absorb an off-axis exponentially growing character. Therefore such an acyclic repair would itself force spectral confinement.

## Disposition

The full source-defined Suzuki object should be the Toeplitz complex, not only its kernel projection:

\[
\boxed{
0\to H_+\xrightarrow{L}H_+\to0,
\qquad
\ker\mathcal D=\ker L\oplus\ker L^*.
}
\]

It provides an unconditional positive supersymmetric bulk and faithfully retains the signed kernel/cokernel boundary. This is an abstract factorization of the obstruction, not a positivity proof. The missing endpoint differential is now precisely typed and is blocked by the same bounded-covariant growth theorem unless off-axis modes vanish.
