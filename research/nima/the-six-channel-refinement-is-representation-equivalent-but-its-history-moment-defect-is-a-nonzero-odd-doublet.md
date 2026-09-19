# The six-channel refinement is representation-equivalent, but its history/moment defect is a nonzero odd doublet

## Exact six-channel action

The fixed-seam common packet

\[
(B_0,Q_0,M,J,A_0,C_0)
\]

carries an exact Fourier order-four action. Both the endpoint-moment and
history packets are equivariant projections.

The history extension splits algebraically after defining

\[
\widetilde A_0=A_0-\frac12Q_0.
\]

Then

\[
\mathcal F:
\begin{pmatrix}\widetilde A_0\\C_0\end{pmatrix}
\longmapsto
\begin{pmatrix}
0&-(2\pi i)^{-1}\\
2\pi i&0
\end{pmatrix}
\begin{pmatrix}\widetilde A_0\\C_0\end{pmatrix}.
\]

The moment odd pair obeys

\[
\mathcal F:
\begin{pmatrix}M\\J\end{pmatrix}
\longmapsto
\begin{pmatrix}
0&-2\pi i\\
(2\pi i)^{-1}&0
\end{pmatrix}
\begin{pmatrix}M\\J\end{pmatrix}.
\]

These two odd representations are isomorphic. One intertwiner is

\[
\widetilde A_0\leftrightarrow M,
\qquad
C_0\leftrightarrow-4\pi^2J.
\]

## Source defect

Representation equivalence does not make the source functionals equal. Define

\[
D_1=A_0-\frac12Q_0-M,
\qquad
D_2=C_0+4\pi^2J.
\]

For general Schwartz functions, `(D_1,D_2)` is nonzero. It forms a closed
Fourier-odd doublet. Therefore the history-to-moment comparison obstruction is
not failure of Fourier typing; it is the nonvanishing of this source defect
pair.

## Consequence for the Clark chain map

The six-channel common refinement supplies compatible Fourier actions and
canonical transpose columns. A direct chain equivalence between the two
four-port quotients exists only after accounting for `(D_1,D_2)`.

A higher compensator may retain this odd doublet as an auxiliary state and map
its boundary into the relative Clark kernel. Quotienting it away merely
because the two representations are abstractly isomorphic would erase source
information.

## Finite next test

Evaluate the Clark codiagonal on the defect doublet. There are two outcomes:

1. it lands in `ker S_Cl`, so scalar Clark outputs agree while the cone stores
   the defect;
2. it survives Clark projection, directly obstructing even the output-level
   chain square.

Either way, the full cone comparison must retain the doublet until a
source-derived null-homotopy is constructed.