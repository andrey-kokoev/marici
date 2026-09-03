# Three deterministic Gale greedy flows fail despite max-flow feasibility

## Question

Does a simple deterministic Gale-comparable greedy rule realize the successful fixed-eight transport?

## Claim boundary

No among three tested rules. Lexicographic demand/supply order fails in 736 of 3,584 cases, largest-demand with largest-supply first fails in 2,714, and most-constrained demand with largest-supply first fails in 1,070. Every rule has an exact first unmatched negative mass. Since exact max flow succeeds in all cases, these are allocation failures rather than Hall deficits. The result refutes these greedy constructions, not canonical optimization-defined flows.

## Disposition

The bounded mechanism is genuinely global: local greedy choices consume supply needed by later demands. An all-order proof must establish weighted Hall inequalities or provide an augmenting-path construction, not a one-pass rule. The missing parameterized `A_k,B_k` constructor now blocks extension beyond eight. Send the common-architecture owner the sharpened acceptance request: derive Gale-comparability weighted Hall inequalities for every negative-label subset from the complementary minors, reproducing the fixed-eight zero-deficit census.
