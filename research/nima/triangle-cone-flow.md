# Triangle cone as nonnegative interval flow

## Question

Is every seven-point triangle cone face coordinate-induced?

## Claim boundary

The coordinates below are real nonnegative weights on labelled triangles, not physical flow or time. Interval containment is a combinatorial partial order. No external polyhedral package is needed: an exact decomposition proves the cone identity.

Root the polygon at edge (0,n-1). A triangle (i,j,k) has parent interval (i,k) and child intervals (i,j),(j,k). For each internal diagonal e impose balance: the sum of weights of triangles whose parent is e equals the sum of weights of triangles having e as a child. Let H be this balance matrix. Every triangulation incidence vector satisfies H v=0.

Conversely, take any nonzero nonnegative balanced v. A positive triangle whose parent is not the root forces a positive containing triangle by balance. Strict interval enlargement ends at the root, so some root triangle is positive. Select one such triangle, then recursively select a positive triangle for each internal child interval. Balance guarantees that choice exists. Strictly shorter child intervals ensure termination and give one full triangulation of positive triangles.

Subtract the minimum selected weight times that triangulation incidence vector. Balance and nonnegativity remain, and at least one positive coordinate disappears. Repeat. At most binomial(n,3) subtractions suffice because zero coordinates never become positive. Thus every balanced nonnegative vector is a nonnegative combination of triangulations, proving

\[
C=\ker(H)\cap\mathbb R_{\geq0}^{\binom n3}.
\]

Since span(C) is contained in ker(H), this also gives C=span(C) intersect the nonnegative orthant. Every face of a cone defined within its span solely by coordinate nonnegativity is coordinate-induced. By the face-lifting criterion every toric support admits a Boolean triangle lift. At seven points the already proved local/toric ideal equality therefore promotes this to all locally admissible Boolean supports, without enumerating 2^42 subsets.

## Disposition

The checker verifies seven-point balance rank 14, incidence rank 21, and an exact 21-term decomposition of a rational test vector. An unbalanced nonnegative vector is rejected. The general decomposition argument, rather than that sample, proves the cone statement. Arbitrary coefficient lifting on boundary strata remains separate; the next issue is the integral lattice of each retained triangle map. These source-independent cone facts do not supply the deferred physical embedding.
