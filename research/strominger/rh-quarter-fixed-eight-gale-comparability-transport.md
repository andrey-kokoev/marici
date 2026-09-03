# Undirected Gale-comparability transport certifies every fixed-eight terminal sum

## Question

Can positive oriented source mass cover all negative mass when transport is allowed between Gale-comparable labels in either direction?

## Claim boundary

Yes for all 3,584 fixed `k=8` terminal cases. Exact bipartite max flow finds zero failed cases and no unmatched negative mass. This is stronger than total-sum positivity because transport edges are restricted to comparable equal-cardinality labels, but it is weaker than either directed Gale mechanism, both of which failed. The result is a finite-size existence certificate; it neither gives a canonical flow nor proves the property for parameterized source matrices.

## Disposition

Retain undirected Gale comparability as the first surviving source-labelled cancellation mechanism. Before promoting it beyond a bounded theorem, audit nontriviality and extract exact Hall inequalities: count incomparable positive-negative pairs, record minimum cut slack, and determine whether a canonical equivariant flow can be defined from source labels rather than solved separately from observed weights.
