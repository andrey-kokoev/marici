# The diagonal neutral compression cancels the Krein residual but cannot contain the physical reciprocal sections boundedly

## Neutral graph

After solving the Clark cross block, the remaining doubled residual is

\[
\mathcal T
=
\begin{pmatrix}
T&0\\
0&-T
\end{pmatrix}.
\]

The diagonal graph

\[
\Lambda_{\rm diag}
=
\{(f,f):f\in\mathcal H_\Phi\}
\]

is neutral for every self-adjoint \(T\):

\[
\langle
\mathcal T(f,f),(f,f)
\rangle
=0.
\]

Thus diagonal matching cancels the residual algebraically.

## Physical reciprocal sections

The physical doubled spectral state is

\[
\left(
 e^{-su},e^{su}
\right).
\]

To place all these states in a graph compression, one would need an operator \(U\) satisfying

\[
Ue^{-su}=e^{su}
\]

for every relevant \(s\).

On the analytic polynomial core, this map is forced by Taylor expansion to act as

\[
U(u^n)=(-1)^n u^n.
\]

It is half-line analytic reflection.

## Norm obstruction

Assume that \(U\) extended boundedly on

\[
\mathcal H_\Phi
=
L^2(\mathbb R_+,\Phi(u)du).
\]

Then for every positive real \(s\),

\[
\int_0^\infty
 e^{2su}
\Phi(u)du
\le
\|U\|^2
\int_0^\infty
 e^{-2su}
\Phi(u)du.
\]

The right integral is an ordinary decaying Laplace transform and is concentrated near \(u=0\). It has at most polynomial decay in \(s\).

The left integral has an interior saddle moving to infinity. Using the leading theta decay

\[
\Phi(u)
\asymp
\exp
\left(
\frac92u-
\pi e^{2u}
\right),
\]

the exponent

\[
2su+
\frac92u-
\pi e^{2u}
\]

is maximized near

\[
u_s
\sim
\frac12
\log
\frac{s}{\pi}.
\]

Its value grows on the scale

\[
s\log s-O(s).
\]

Consequently,

\[
\frac{
\|e^{su}
\|_{
\mathcal H_
\Phi}
}{
\|e^{-su}
\|_{
\mathcal H_
\Phi}
}
\longrightarrow
\infty.
\]

No bounded \(U\) can perform reciprocal analytic reflection on all spectral sections.

## Consequence

The simplest neutral compression succeeds algebraically but fails physical-state admission. More generally, a bounded graph relation on the raw theta-tail Hilbert space cannot implement

\[
e^{-su}
\mapsto
e^{su}
\]

uniformly over the spectral parameter.

The reciprocal sheet must therefore be handled through one of:

1. an unbounded closed boundary relation with a separately controlled graph norm;
2. a Hardy dilation in which reflection is represented as boundary conjugation rather than half-line analytic continuation;
3. a parameter-dependent family followed by a source-derived positive quotient;
4. a rigged or pro-Hilbert carrier with asymmetric weights.

## Control interpretation

The required feedback is not a bounded static controller on the raw theta-tail state space. It is an unbounded reciprocal boundary condition.

This explains why finite packet realizations are benign while a single global bounded graph is unavailable: on every finite packet, analytic reflection has a finite interpolation norm, but that norm diverges as the spectral packet escapes to large positive real parameter.

## Disposition

Diagonal neutral compression is not the missing universal constructor. It cancels the Krein residual but cannot admit the complete physical reciprocal family as a bounded graph.
