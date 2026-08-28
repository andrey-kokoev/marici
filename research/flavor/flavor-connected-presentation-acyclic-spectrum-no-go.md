# Connected Presentation Does Not Select the Acyclic Spectrum

## Question

Can WP831's vectorlike threshold fiber be removed by requiring the finite
source complex to be connected or indecomposable rather than a visible direct
sum?

## Split and connected presentations

The visible stabilization is

\[
B\oplus(1)=
\begin{pmatrix}
2&-1&0&0\\
3&0&-1&0\\
0&0&0&1
\end{pmatrix}.
\]

Its support graph exposes a separate contractible component. Compare it with

\[
B_c=
\begin{pmatrix}
2&-1&0&1\\
3&0&-1&1\\
1&1&-1&1
\end{pmatrix}.
\]

Every row and column of \(B_c\) has support degree at least two, and its
bipartite support graph is connected. Nevertheless,

\[
B_c(1,2,3,0)^T=0,
\]

its rank is three, its cokernel is trivial, and its Smith form is identical to
that of \(B\oplus(1)\): three unit invariant factors and one kernel generator.

Thus split support and connected support are two integral presentations of the
same module type. Support connectedness does not detect the contractible
stabilization.

## Physical decoration survives

The extended primitive current retains cubic anomaly 36. The hidden acyclic
sector can still carry an anomaly-neutral vectorlike decoration \((r,-r)\),
which changes the current spectral index by \(2r^2\). Its mass remains a
continuous spectral datum detected by

\[
2e^{-\tau m^2}.
\]

Neither the Smith type nor support connectedness fixes \(r\) or \(m\).
Consequently the WP831 response fiber survives unchanged:

\[
(S,e)=(14,1),
\qquad
(S,e)=\left(16,\sqrt{\frac78}\right).
\]

## Typing consequence

“Connected quiver,” “dense incidence,” and “no isolated node” are presentation
conditions. They can rigidify a chosen matrix without selecting a physical
spectrum. A genuine repair must state irreducibility invariantly in the
physical category and prove that it forbids or fixes every interacting
anomaly-neutral sector and its mass.

This packet does not prove that every categorical irreducibility principle
fails. It proves that graph-support connectedness and permutation-level matrix
indecomposability are insufficient substitutes.

## Smallest exact falsifier

The pair \(B\oplus(1)\) and \(B_c\) has identical Smith data, primitive
current, anomaly, kernel, and cokernel. One visibly splits; the other has
connected support with no leaf row or column. The same vectorlike spectral
decoration and Ward-response fiber attach to both.

## Disposition

Negative connectedness result. Presentation indecomposability does not make
the full spectral completion unavoidable and therefore cannot fix portal
magnitude, RG coefficients, thresholds, or readout.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp832_connected_presentation_acyclic_spectrum_no_go.py
```
