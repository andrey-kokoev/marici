# The Logarithmic Integer Comb Is Not an Ordinary Hilbert Boundary Trace

## Logarithmic carrier

The unitary map

\[
(Uf)(q)=e^{q/2}f(e^q)
\]

identifies

\[
L^2(\mathbb R_+,d\rho)
\]

with

\[
L^2(\mathbb R,dq)
\]

and turns the centered dilation generator into ordinary momentum.

Under this map, integer-comb evaluation becomes

\[
B\psi
=
\sum_{n\geq1}
n^{-1/2}\psi(\log n).
\]

## Translation witness

Choose a nonnegative smooth function \(\psi\) of compact support with

\[
\int_{\mathbb R}e^{t/2}\psi(t)\,dt>0,
\]

and translate it:

\[
\psi_R(q)=\psi(q-R).
\]

Every translation-invariant Sobolev norm is constant along this family. In
particular,

\[
\lVert\psi_R\rVert_{H^1(\mathbb R)}
=
\lVert\psi\rVert_{H^1(\mathbb R)}.
\]

But the comb trace is

\[
B\psi_R
=
\sum_{n\geq1}
n^{-1/2}\psi(\log n-R).
\]

As \(R\) tends to infinity, the labels in the translated support have density
of order \(e^R\), while each label has weight of order \(e^{-R/2}\). The
Riemann-sum asymptotic is

\[
B\psi_R
\sim
e^{R/2}
\int_{\mathbb R}
e^{t/2}\psi(t)\,dt.
\]

Therefore

\[
|B\psi_R|\longrightarrow\infty
\]

while the \(H^1\) norm remains fixed.

## Boundary-triple obstruction

The integer comb is not a bounded trace functional on the natural
translation-invariant form domain of the carrier Dirac operator. Consequently
it cannot be inserted as an ordinary finite-energy boundary condition for
\(\mathcal Q\).

The obstruction is source-derived label accumulation at logarithmic infinity:

\[
\log(n+1)-\log n\sim\frac1n.
\]

The arithmetic boundary becomes exponentially dense in the carrier
coordinate.

## Stronger test-space warning

Ordinary Schwartz decay in \(q\) is polynomially controlled and need not defeat
the exponential label density. Thus the logarithmic comb is not automatically
a tempered distribution on the standard Schwartz rigging.

A faithful test space must retain exponential seminorms, a discrete label
port, or an equivalent relative boundary coordinate.

## Consequence

The canonical carrier operator

\[
L=H^2+\frac14
\]

and the canonical integer comb do not meet inside an ordinary Hilbert boundary
triple. Their interaction is inherently rigged or relative.

This identifies the first real construction obstacle for the proposed
arithmetic extension:

Build a Fourier-compatible exponential test-space rigging on which both
momentum transport and the logarithmic comb trace are continuous.

## Falsifier

Any claimed ordinary Sobolev boundary realization must bound

\[
|B\psi|\leq C\lVert\psi\rVert_{H^1}.
\]

The translated packet \(\psi_R\) disproves such a bound.
