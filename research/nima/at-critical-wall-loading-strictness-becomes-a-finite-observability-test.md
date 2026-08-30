# At critical wall loading strictness becomes a finite observability test

## Critical normal form

At coherent wall strength \(\alpha=1\), use the coherent/disagreement basis and write

\[
H=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\]

The coherent coordinate is the pointwise radical; the disagreement coordinate is energetically observed.

Let the source-derived \(z\)-independent connection be

\[
A_0=
\begin{pmatrix}
a&b\\
c&-a
\end{pmatrix},
\]

the general real two-dimensional Hamiltonian generator in this frame.

The coherent radical is invariant under \(A_0\) exactly when

\[
c=0,
\]

because

\[
A_0
\binom10
=
\binom ac.
\]

Thus one matrix entry decides whether critical wall loading remains dark or is dynamically rotated into the observed disagreement channel.

## Observability Gramian

For a finite cell of length \(L\), define

\[
\mathcal O_L
=
\int_0^L
e^{uA_0^{*}}He^{uA_0}\,du.
\]

Then

\[
x^{*}\mathcal O_Lx
=
\int_0^L
\left|
P_{\mathrm{dis}}e^{uA_0}x
\right|^{2}\,du.
\]

Hence the integrated canonical energy is strictly positive on every nonzero state exactly when the pair

\[
(H^{1/2},A_0)
\]

is observable. In this two-dimensional critical normal form, the coherent vector is observable precisely when \(c\neq0\).

Equivalently, the finite observability matrix

\[
\begin{pmatrix}
0&1\\
c&-a
\end{pmatrix}
\]

has rank two exactly when \(c\neq0\).

## Two legitimate architectures

### Rotating radical

If \(c\neq0\), the coherent direction is pointwise dark but not dynamically dark. Every coherent state immediately develops an observed disagreement component. The integrated Wronskian energy can be strict without \(\alpha>1\).

### Protected dark line

If \(c=0\), the coherent line is invariant. It may still be legitimate if:

- it is an authorized gauge quotient;
- the endpoint-zero module excludes it;
- or it is the intended protected Feshbach line, with zeros produced by a separate reactive crossing.

In that case strict Hermite–Biehler phase cannot be claimed on the unreduced full state space from \(H\) alone.

## Completion margin

When the rotating-radical route is intended, pointwise \(c\neq0\) is insufficient. The relevant quantity is the smallest eigenvalue of the observability Gramian on the declared quotient:

\[
\inf_{X,s}
\lambda_{\min}
\left(
\mathcal O_{L,X}(s)
\big|_{\mathcal R_{\mathrm{reachable}}/\mathcal G}
\right)>0.
\]

A sequence \(c_X\to0\) gives valid finite observability while losing phase strictness at completion.

## Immediate source calculation

The next finite pilot should extract \(A_0\) in the coherent/disagreement frame and compute its lower-left entry \(c\). This is more informative than asking whether the critical coherent radical exists: it determines whether that radical is static, gauge, or dynamically observed.

The complete endpoint trace must then be appended to the observability matrix. A bulk-invariant coherent line may still be observed at the wall or archimedean endpoint.
