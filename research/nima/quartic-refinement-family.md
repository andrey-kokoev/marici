# No universal constant quartic split restores the six-point quadrics

## Question

Was the symmetric-refinement failure merely a poor choice of one half?

## Claim boundary

Take the source and graph conventions in quartic-contact-source.md. For each quadrilateral with sorted labels q0<q1<q2<q3, allocate fraction alpha to diagonal (q0,q2) and 1-alpha to (q1,q3). Use the same constant alpha at every quartic vertex, multiplying allocations when a graph has two quartic vertices. Canceled propagator variables turn the allocation into polynomial triangulation weights, with no new poles. This ansatz is label-dependent except at the symmetric value; no cyclic covariance is claimed.

The exact source amplitude is preserved for every alpha: summing all refinements of each original graph gives (alpha+1-alpha)^v4=1. Therefore the source coefficients g^4, g^2 lambda, lambda^2, the normalization A3=g and the four-point contact lambda are unchanged. Source residues remain unchanged as rational functions.

## Disposition

No value of alpha makes all three off-pole six-point rectangle quadrics vanish as identities in generic formal channel variables and couplings. In the (0,3) residual, the coefficient of g^2 lambda^3 s03 s02 s04 is alpha^3. In the (2,5) residual, the coefficient of g^2 lambda^3 s25 s15 s35 is -(alpha-1)^3. Simultaneous vanishing would require alpha=0 and alpha=1. The checker independently computes the gcd of all coefficient constraints as one and rejects both endpoints. No root search or positive sampling is used.

This rules out the entire declared one-parameter family, not all polynomial refinements. The pure cubic limit remains an exact positive control. The interpretation is correspondingly bounded: one universal constant rule for replacing a quartic vertex by triangles cannot turn its source coefficients into global rank-one triangle weights. This is not a failure of tree-level pole factorization or of the source interaction.

A next discriminating test is locality rather than another universal scalar: permit one parameter for each of the 15 labelled quadrilateral faces at six points, shared whenever that face occurs in a larger diagram, and test whether the resulting exact source-preserving identities admit a solution. An inconsistent subsystem would establish failure of context-independent constant vertex allocation; a solution would identify precisely how the universal rule was too restrictive. Momentum-dependent or context-dependent allocations remain outside that test.

Git prohibition remains active. No Git operations were performed in this turn. The checker reruns the source checker and refreshes its owned result as a prerequisite.
