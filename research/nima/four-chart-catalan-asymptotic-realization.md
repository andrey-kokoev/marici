# Four-chart Catalan realization and its finite boundary defect

Let `P_n` denote one forced-channel projection in the full Catalan module `H_n`. Its normalized trace is

\[
\tau_n(P_n)=\frac{C_{n-3}}{C_{n-2}}
=\frac14+\frac{3}{4(2n-5)}.
\]

If four chart rotations carry `P_n` to four equal-rank projections, their total unnormalized trace is `4 C_(n-3)`. At finite `n` this exceeds the full rank:

\[
4C_{n-3}-C_{n-2}
=\frac{6}{n-1}C_{n-3}>0.
\]

Normalized by the full Catalan trace, the exact defect is

\[
\frac{4C_{n-3}-C_{n-2}}{C_{n-2}}
=\frac{3}{2n-5}\longrightarrow0.
\]

Therefore four forced-channel charts cannot be a disjoint finite-degree partition. They can become a trace partition only asymptotically. Any exact realization functor must place the positive finite defect on chart overlaps/shared faces rather than treating the four sectors as orthogonal summands.

This fits the eight-lattice architecture: four tetrahedral chart directions share lower-dimensional faces. A precise comparison should seek projections `P_(i,n)` satisfying an inclusion-exclusion or Cech identity

\[
\sum_{i=1}^4 P_{i,n}-I=\text{face-overlap correction},
\]

with normalized trace `3/(2n-5)`. Showing that the correction is carried by the triangular/tetrahedral boundary relations would identify the Catalan quarter-limit with the four-chart realization cycle.

`check_four_chart_catalan_trace_defect.py` verifies the exact identities through `n=100`.
