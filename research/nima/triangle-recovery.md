# Constructive triangle recovery

## Question

Can the audited converse recover triangle weights from locally separable function values without assuming channel factorability?

## Claim boundary

This is an exact six-point test of the reconstruction algorithm, not universal computational verification or a source-derived coefficient packet.

The checker builds the three local facet-minor rows and chooses a vector in their nullspace outside the channel-incidence image. In the recorded lexicographic diagonal ordering the input values are (1,1,0,...,0). All three local minors vanish, but augmenting the channel-incidence matrix by this vector raises rank from nine to ten.

All flips yield consistent context-free increments on fifteen quadrilaterals. Root contraction assigns h_ijk=g_0ijk away from vertex zero, with root-containing weights initially zero. The constant discrepancy at one reference triangulation is assigned to triangles incident to boundary edge (0,1). Summing the resulting triangle weights recovers all fourteen input values exactly.

A Kronecker function with nonzero local residual is rejected because two contexts give different increments for the same quadrilateral. Thus the algorithm tests its separability precondition rather than fitting a triangle expansion regardless of failure.

## Disposition

The constructive converse succeeds on a local-pass, channel-fail example. The results record every triangle weight and labelled triangulation. Further coefficient domains require explicit reduction or multiplicative reconstruction, not numerical logarithms or implicit root choices.
