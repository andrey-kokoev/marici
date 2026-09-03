# Quadratic Gram weights lose signed source information

## Question

Can quadratic Gram weights reconstruct signed quarter-source terms and their Hall margins?

## Claim boundary

Not without external orientation data. Entrywise squares identify `(1,-1)` and `(1,1)` although their signed sums are `0` and `2`. Even the full rank-one Gram `zz^T` identifies `z=(1,2)` with `-z=(-1,-2)`, whose signed sums are `3` and `-3`. Quadratic scaling also changes linear margins: scaling source terms by `c` scales squared weights by `c^2`. Thus quadratic positivity alone cannot reconstruct signed terms or prove the required linear Hall margins. If an independent source theorem fixes a positive cone and square-root normalization, the ambiguity can disappear; none is presently derived.

## Disposition

Reject quadratic Gram weights as a standalone source-to-Hall mechanism. They solve positivity by quotienting precisely the sign information needed for source reconstruction and linear margins. The remaining distinct possibility is Gram data plus source-derived orientation anchors. Next determine the minimal anchors needed to lift the quadratic sign quotient and whether the existing source formula supplies them without assuming the desired sign law.
