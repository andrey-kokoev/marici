# Every weighted two-demand neighborhood reduces exactly to three capacities

## Question

Does varying Hasse topology obstruct use of the five-path transport algebra?

## Claim boundary

No for two demands. Every positive supply has one of three nonempty neighbor signatures:

\[
\{D_0\},\qquad \{D_0,D_1\},\qquad \{D_1\}.
\]

Summing capacities within each signature produces three aggregate supplies. Original-network feasibility is equivalent to the two singleton and collective Hall inequalities of the aggregate \(P-D-P-D-P\) model. Every aggregate flow lifts to individual supplies by distributing class flow within class capacities.

The checker exhausts 164,025 weighted four-supply networks, including absent signature classes, and separately verifies aggregate-flow lifting for all tested class capacities and totals.

## Disposition

This resolves topology variation for two demands: the twenty observed degree-sequence types share identical three-capacity cut algebra. The result does not prevent exponential growth for more demands. For three demands there are seven possible nonempty signatures. The next bounded test should census fixed-eight independent three-demand cuts, active signature counts, and whether a smaller source-specific compression survives.
