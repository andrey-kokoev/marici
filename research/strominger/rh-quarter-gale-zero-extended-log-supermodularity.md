# Fixed-eight source weights are fully log-supermodular after zero extension

## Question

Do support-boundary zeros obstruct the nonzero Gale-diamond log-supermodularity certificate?

## Claim boundary

No at fixed \(k=8\). Across all 3,584 terminal cases, the exact checker tested 211,680 Gale cover diamonds, including 102,124 with at least one zero weight. Every diamond satisfies

\[
w(K)w(K_{ab})\geq w(K_a)w(K_b)
\]

when absent source terms are assigned weight zero. Together with the prior 109,556 four-nonzero audit, this gives a complete finite zero-extended log-supermodularity certificate for the absolute source weights.

This is stronger than support convexity but remains bounded to the supplied \(k=8\) matrices. It does not imply the signed Hall inequalities without a compatible organization of positive and negative labels.

## Disposition

The MTP2-type rival survives its strongest immediate boundary falsifier. The next test is sign geometry: determine whether terminal source signs are single-crossing along Gale covers, or whether positive and negative regions interlace. A monotone sign boundary combined with log-supermodular magnitudes could support a source-derived coupling; exact sign inversions would identify the additional structure still required.
