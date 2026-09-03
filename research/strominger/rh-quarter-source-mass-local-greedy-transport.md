# Quarter source-mass local greedy transport

## Question

Do simple local relations support a greedy capacity transport from negatively oriented source terms to positive terms?

## Claim boundary

The test fixes lexicographic processing and four relations. Failure does not exclude a different ordering or a feasible global flow on the same graph.

## Disposition

No rule succeeds in all 769 upper interval-avoiding cases. Adjacent exchange succeeds in 601 cases; arbitrary single exchange and componentwise comparability each succeed in 604; interlacing succeeds in 661. The first interlacing failure has base \(\{1,2\}\), terminals \((3,4)\), 16 negative terms, and 15 positive terms. Since greedy failure can be an ordering artifact, the next leaf is `quarter-source-interlacing-max-flow`, testing exact rational max-flow feasibility and extracting a minimum-cut obstruction when infeasible.
