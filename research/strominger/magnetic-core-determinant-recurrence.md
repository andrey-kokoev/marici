# The growing magnetic core has a quartic determinant ratio

Companion to checkers/magnetic_core_recurrence_checks.py (7/7, exit 0)
and results/magnetic_core_recurrence.json.

## Exact recurrence

Let \(D_k\) be the determinant of the residual core obtained from the
Hall-selected \((g,q)=(2,2)\), \(A_k\) block after exhaustive degree-one pivot
stripping. For every integer \(k\ge2\),

\[
\boxed{D_2=2400,\qquad
D_k=80k(k-1)(2k-1)(2k+1)D_{k-1}.}
\]

Consequently,

\[
D_k=2400\prod_{j=3}^{k}80j(j-1)(2j-1)(2j+1)>0.
\]

## Proof

Order the residual target rows recursively as
\[
-3,-4,\ldots,-2k
\]
and start the source columns with \((2,-),(4,+)\). At step \(k\), append
\((2k-2,-),(2k,+)\). The old columns have no support on the two new rows
\(-(2k-1),-2k\). Therefore
\[
C_k=\begin{pmatrix}C_{k-1}&B_k\\0&Q_k\end{pmatrix}.
\]

Substitution in the grade-two cubic path law gives
\[
Q_k=\begin{pmatrix}
-2(k-1)(12k^2-20k-3)&2k(12k^2-20k+17)\\
-2(k-1)(2k-1)(2k+1)&2k(2k-1)(2k+1)
\end{pmatrix}.
\]
Direct symbolic reduction yields
\[
\det Q_k=80k(k-1)(2k-1)(2k+1).
\]

Block triangularity proves the recurrence. Exact construction through
\(k=20\) independently cross-checks the symbolic theorem.

## Interpretation and scope

The connected core grows as \(2k-2\), but its determinant transfer is scalar
and positive. The \(2\times2\) mixed-sign circuit with determinant 2400 is the
initial condition.

The coherent Plucker gauge is genuinely bipartite: neither row-only nor
column-only raw sign assignments work in the first cyclic examples. A closed
source-parity formula remains open.

This is an arbitrary-\(k\) theorem only for the \((g,q)=(2,2)\) component. It
does not yet provide transfer matrices for general \(g,q\).

