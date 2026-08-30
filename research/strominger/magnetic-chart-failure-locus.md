# The primary-chart failure locus is arithmetic, not spectral

Companion to `checkers/magnetic_chart_locus_checks.py` (7/7, exit 0) and
`results/magnetic_chart_locus.json`.

The two-chart census contained two superficially similar phenomena:

1. a canonical row-reduced chart can prefer a neighboring maximal minor;
2. the preferred Hall-selected maximal minor can actually vanish.

They are not equivalent.  A two-prime screen over

\[
2\le g\le15,\qquad 1\le q\le50,
\qquad 0\le k\le\min(30,\lfloor q/2\rfloor+5)
\]

examined 12,938 full-Hall blocks.  Exact integer determinants at every
candidate onset isolate the primary-chart zeros as

\[
(g,q,k)=(2r,4r+8,r+4),\qquad 1\le r\le7.
\]

Equivalently, at the first failed chart,

\[
\boxed{g\ \text{is even},\qquad q=2g+8,qquad a=2k=q-g=g+8.}
\]

At every such onset the preferred determinant is exactly zero, while the
same uniform target-row exchange

\[
1\longmapsto3
\]

has a nonzero exact determinant.  Thus the matrix is still injective.  The
vanishing is a singularity of one Plucker coordinate, not a singularity of
the underlying transport system.

This separates the explanatory mechanisms:

\[
\begin{array}{c|c|c}
\text{locus}&\text{local event}&\text{kernel effect}\\
\hline
a+g=q+1&\text{odd transfer factor vanishes}&\text{possible kernel birth}\\
q=2g+8,\ a=q-g&\text{preferred chart vanishes}&\text{none; adjacent chart survives}
\end{array}
\]

In the tested region, simultaneous failure of all maximal-minor coordinates
still occurs only at

\[
(g,q)=(2,1),\qquad (2,7).
\]

The earlier odd-grade row-reduced preferences, such as the grade-five
examples, are therefore harmless choices of canonical coordinates: their
preferred Hall determinants do not vanish.

## Explanation gained

The determinant atlas is behaving like a line bundle with local coordinates.
A zero of one coordinate need not mean that the transported subspace loses
dimension; it means only that this coordinate patch has reached its boundary.
The one-row exchange is the transition function to the neighboring chart.
Only simultaneous chart failure is spectral and creates a kernel class.

Accordingly, the search for exceptions should test rank or an atlas of
maximal minors, never a distinguished determinant in isolation.

## Scope

This is an exact finite-range classification of the first primary-chart
failure.  It does not yet prove that the arithmetic family is exhaustive for
all grades and component labels, nor derive its factor directly from the
source formula.  The next symbolic target is to factor the initial preferred
minor by the chart-boundary term

\[
q-2g-8
\]

and prove that the row-exchanged minor is nonzero on that divisor.
