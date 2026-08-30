# Forced pivots leave an unbounded banded core

Companion to `checkers/magnetic_forced_core_checks.py` (8/8, exit 0) and
`results/magnetic_forced_core.json`.

## Falsified reduction

The proposed next step was to strip every degree-one row or column from a
Hall-selected square minor, factor its forced nonzero pivot, and reduce the
remaining determinant to one of finitely many small exceptional graphs.

This reduction is false. The family

\[
(g,q)=(2,2),\qquad A_k=\{0,2,\ldots,2k\}
\]

leaves a residual square core of order

\[
\boxed{2k-2}
\]

after exactly four forced pivots. Thus the residual order grows without bound.
At (k=2), the core is the previously identified mixed-sign block

\[
\begin{pmatrix}-10&100\\-30&60\end{pmatrix}.
\]

For every tested (2\le k\le30), the residual bipartite support is connected.
There is consequently no decomposition into a growing number of fixed local
exceptions.

## What survives

The failure is structured. For (k\ge3), the residual graph has exactly

\[
8k-14
\]

edges, and every residual row has degree at most four. Its order grows, but its
local width does not. All cores through order 58 are nonsingular modulo
(1{,}000{,}000{,}007), which proves their integer determinants are nonzero.

The corrected proof target is therefore a banded determinant recurrence or a
finite-state transfer matrix. Forced pivots still remove the two ends, but the
entire connected interior must then be propagated. The (2\times2) circuit is
the first member of this transfer family, not a standalone exceptional graph.

## Scope

The formulas above are exact computational statements for (2\le k\le30).
Their persistence suggests an arbitrary-(k) support theorem, but this packet
does not claim that unbounded theorem. It also does not prove a closed
determinant recurrence or reconnect to rational exactness.

## Verification

Run:

`uv run --with sympy python -u research/strominger/checkers/magnetic_forced_core_checks.py`

The checker passes 8/8 and records the actual residual sizes, connectivity,
edge counts, degree bound, and exact modular nonvanishing certificate.

