# Local versus global polygon weight relations

## Question

How much of global channel-scale compatibility is detected by imposing multiplicative rank one on every codimension-one regional product?

## Claim boundary

Exact relation-space ranks are computed only for polygon sizes five through seven. No all-size quotient formula is inferred.

For each cut `c`, triangulations containing it form a product of regional triangulation sets. Anchored `2 by 2` logarithmic minors generate the complete rank-one relation space on that facet. Every such row lies in the left kernel of the global triangulation-channel incidence matrix, because channel-factorable weights restrict multiplicatively.

At five points both local and global relation ranks are zero. At six points, three generated local rows have rank three inside the rank-five global kernel, leaving a two-dimensional nonlocal quotient. At seven points, fourteen cuts generate twenty-eight local rows of rank twenty-one inside the rank-twenty-eight global kernel, leaving a seven-dimensional nonlocal quotient.

Thus adding more facet product tests does not close the global gap at the next stage: seven independent compatibility classes remain invisible to all codimension-one rank-one tests at seven points. The finite sequence of quotient dimensions `0,2,7` is evidence only; it is not promoted to a formula.

## Disposition

Global coefficient factorability must be checked independently of all local residue factorizations. For an owner packet at seven points, passing every facet minor still leaves seven global incidence-binomial tests modulo the local span. This separates local gluing from global coherence without treating either as source provenance.
