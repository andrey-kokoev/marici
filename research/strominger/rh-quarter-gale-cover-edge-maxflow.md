# Gale Hasse edges support every fixed-eight signed transport

## Question

Are long comparable jumps necessary, or can branching transport remain local on the Gale Hasse graph?

## Claim boundary

Exact max flow using only opposite-parity Gale cover edges satisfies every negative demand in all 3,584 terminal cases. No longer comparable edge is required at fixed \(k=8\).

This is stronger than the prior all-comparability certificate. It reconciles the failed edgewise, three-term, and interval decompositions: individual blocks can have negative residual while a branching cover-edge network splits and reroutes mass globally. Combined finite structure is:

1. source signs are a case-dependent checkerboard parity character;
2. zero-extended absolute weights are log-supermodular on every Gale diamond;
3. a feasible signed flow exists on the Hasse graph alone.

The result is a finite exact network theorem. It does not derive cover-edge Hall inequalities for arbitrary order or provide the missing parameterized source matrices.

## Disposition

The remaining all-order target is now sharply local: derive weighted Hall inequalities for negative parity subsets using only their opposite-parity Hasse neighbors, from source-minor total positivity or log-supermodularity. Send this stronger acceptance condition to the common-architecture owner together with the fixed-eight checker paths.
