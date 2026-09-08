# Quartic source: pole factorization versus coefficient quadrics

## Question

Does the source-derived cubic result survive a quartic interaction, or does the triangulation presentation insert extra structure?

## Claim boundary

Add -lambda phi^4/4! to the declared scalar Lagrangian. Retain the previous labelled planar-subset convention and strip the common -i from tree diagrams. Actual source coefficients are products g^v3 lambda^v4, since the vertices are -ig and -i lambda and a tree has one fewer internal edge than vertices. This is not a full identical-scalar amplitude or a positive-geometry embedding.

At four points A4=g^2/s+g^2/t+lambda. Pole residues fix g^2, not lambda. For any constant alpha the same expression has triangulation weights g^2+alpha lambda s and g^2+(1-alpha)lambda t. Thus constant triangle weights cannot encode the nonzero contact term as a rational identity in independent s,t, and a momentum-dependent refinement is not unique. No nontrivial rectangle quadric exists at four points.

### Six-point test

The source has 14 cubic diagrams with weight g^4, 21 one-quartic diagrams with weight g^2 lambda, and three two-quartic diagrams with weight lambda^2. A diagram with v4 quartic vertices has 2^v4 cubic refinements. Declare equal distribution across these refinements, multiplying by the canceled propagator variables. This reproduces the source rational function exactly but is a presentation choice, not a new source vertex.

The resulting 14 triangulation weights violate all three facet rectangle quadrics generically. For channel (0,3), the exact residual in the recorded ordering is

\[
w_{13}w_7-w_8w_{12}=\frac{g^2\lambda^3}{8}s_{03}(s_{02}-s_{13})(s_{04}-s_{35}).
\]

The other two residuals and all weights are retained in results/quartic_contact_source.json. This statement is a rational-function computation in formal channel variables (characteristic zero); it is not a claim on every fixed-dimensional physical kinematic locus.

On the channel divisor s03=0 the obstruction vanishes. The actual residue is exactly

\[
\left[g^2(s_{02}^{-1}+s_{13}^{-1})+\lambda\right]
\left[g^2(s_{04}^{-1}+s_{35}^{-1})+\lambda\right].
\]

It equals the two four-point source amplitudes, with A3=g and the four-point contact normalization lambda. The checker verifies this identity, all three residuals, their channel-divisor restrictions and the cubic limit lambda=0. An initial polygon-splitting implementation failed the residue test because rotated endpoint indices were unsorted; sorting those indices repaired it, restoring the 14/21/3 diagram counts and the unchanged residue test.

## Disposition

Source pole factorization does not imply off-pole rank-one identities for arbitrarily refined triangulation coefficients. In the pure cubic case a triangle is an actual cubic vertex with coupling g. Here a triangle produced by resolving a quartic vertex is bookkeeping: its apparent factors mix lambda, canceled propagators and a refinement convention. The displayed failure refutes this symmetric refinement as a global triangle-factor assignment; it does not prove no alternative rational refinement can factor.

The next bounded test is whether another refinement can remove these residuals without inserting denominators or moving the source normalization. That distinguishes a presentation-specific failure from a structural obstruction.

Operator prohibition: do not touch Git. No Git operations were performed after that instruction; it remains active for subsequent work.
