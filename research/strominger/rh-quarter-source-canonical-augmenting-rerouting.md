# Quarter-source canonical augmenting rerouting

## Question

Does canonical exact interlacing transport require global residual rerouting, or can every bounded case be solved by forward-only allocations?

## Claim boundary

A lexicographically ordered exact Edmonds–Karp construction transports all negative demand in all 769 bounded cases. Reverse residual edges occur in 108 cases; the first is base `(1,2)`, endpoints `3,4`, with 30 augmentations. The maximum observed augmentation count is 68. Thus the canonical construction is globally coordinated in those cases. Algorithmic feasibility and rerouting do not supply an all-order source recurrence or a positive planar factorization.

## Disposition

Reject forward-only local allocation as an explanation of the canonical exact flow. Retain globally coordinated augmenting transport as a bounded constructive backend. The next nonredundant problem is to derive the augmenting choices and termination from a uniform source recurrence rather than finite graph search.
