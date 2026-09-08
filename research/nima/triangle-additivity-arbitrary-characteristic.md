# Division-free triangle additivity

## Question

Is characteristic zero needed in the local-factorization converse?

## Claim boundary

This strengthens the additive theorem to any field. It does not carry the characteristic-zero formula for the quotient by channel functions unchanged into other characteristics.

The prior proof represented a residual constant by assigning its value divided by n-2 to every triangle. That choice fails when the characteristic divides n-2. Fix instead one polygon boundary edge e and assign the constant to triangles containing e and zero to all other triangles. Exactly one triangle of every triangulation contains e, so its triangle sum is the required constant without division.

All preceding steps of the converse use additive differences, context independence under facet separability, the alternating pentagon identity, and the contracting homotopy of the full simplex. The simplex contraction works over any coefficient field. Flip connectivity then leaves a constant handled by the boundary-edge construction. Thus local separability equals triangle additivity in arbitrary characteristic.

The triangle-incidence kernel proof also remains valid: vertex coboundaries have rank n-1, and the polygon-boundary functional is nonzero in every characteristic (one edge evaluates to one). Consequently the local-solution dimension remains 1+binomial(n-1,3).

However, the channel-incidence rank is F-1 when the field characteristic divides n-3 and F otherwise, by the integer Smith theorem. The quotient of global channel relations by local relations therefore has dimension 1+binomial(n-1,3)-rank(A), not uniformly the characteristic-zero expression with F.

## Disposition

The characteristic-zero restriction was an artifact of the constant representative. The new checker verifies every boundary edge through n=9 and exhibits the failure of uniform weights at (n,p)=(4,2),(5,3),(7,5). These tests verify the replacement step, not the complete proof by computation. The original characteristic-zero packet remains a valid restricted theorem; this packet supplies its extension.
