# Natural label-ordered mass transport fails at fixed size eight

## Question

Do fixed `k=8` terminal terms satisfy cumulative oriented dominance in a natural source-label order?

## Claim boundary

No among four tested orders. Lexicographic and increasing-sum orders have prefix deficits in 3,551 of 3,584 terminal cases; reverse lexicographic and decreasing-sum orders fail in 3,556. Every order first fails for empty base and endpoints `(0,1)` at label `K={1}`, with an exact negative residual recorded in the result JSON. This refutes these natural total orders, not every partial-order transport certificate. Ordering terms by their observed sign would be circular and is excluded.

## Disposition

Reject lexicographic and sum-ordered cumulative dominance as bounded source certificates. Their failure is nearly universal, not exceptional. The next noncircular structure to test is the componentwise Gale order on equal-cardinality source labels: determine whether oriented sign and magnitude are monotone enough to admit an order-respecting positive-to-negative matching.
