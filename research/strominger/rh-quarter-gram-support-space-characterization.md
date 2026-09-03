# A single Gram range pair represents only rectangular coordinate support

## Question

Which bipartite coordinate-support graphs can equal the cross-block range space `U_A tensor U_B` of one singular Gram pair?

## Claim boundary

Exactly complete bipartite rectangles. If `U_A tensor U_B` equals the matrix space supported on a graph `G`, every matrix unit `e_i e_j^T` for an edge forces `e_i` into `U_A` and `e_j` into `U_B`. Tensor closure then includes every cross unit between represented rows and columns, so `G=I×J`. Conversely coordinate subspaces on `I,J` realize that rectangle. Hence diagonal, triangular, staircase, and other nonrectangular interlacing graphs cannot arise from one pair of endpoint range constraints. This theorem concerns equality with a coordinate-support space; it does not exclude sums of several tensor-range spaces.

## Disposition

Close the single-pair singular-Gram loophole. Any Gram representation of nonrectangular Hall support needs a sum of rectangular components or an explicit edge-indexed constraint, either of which carries additional combinatorial structure. Next test the minimal rectangle decomposition of interlacing support and whether it derives from source data rather than inserting the graph.
