# Quarter-source rank-gap-left recurrence obstruction

## Question

Does adding absolute left endpoint to source rank and endpoint gap determine canonical bounded transport data?

## Claim boundary

Across all 769 exact cases, signatures were grouped by `(rank,gap,left endpoint)`. The first collision occurs at `(1,1,2)`: base `(0)` gives signature `(5,0,3,3)`, while base `(1)` gives `(13,0,7,7)`. Thus absolute endpoint placement does not repair rank-gap state compression. This rejects only recurrences omitting base configuration or induced source weights.

## Disposition

Reject `(rank,gap,left endpoint)` as sufficient recurrence state. Any surviving recurrence must retain base-shape data or a compressed statistic proved faithful to the induced source-weight profile. The next nonredundant test is whether the ordered gap profile of the base determines canonical transport signatures.
