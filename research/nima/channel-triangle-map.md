# Root-free channel-to-triangle comparison

## Question

How can channel weights be represented by triangle factors without distributing square roots across both incident faces?

## Claim boundary

Fix the ordered cyclic vertex labels, abelian unit channel weights, and boundary-edge weights equal to one. The construction is a labelled monomial comparison, not source authority.

For i<j<k set

\[
h^+_{ijk}=\lambda_{ij}\lambda_{jk},\qquad h^-_{ijk}=\lambda_{ik}.
\]

The oriented boundary of an increasing triangle traverses ij and jk increasingly and ik decreasingly. Each internal diagonal is traversed in opposite directions by its two incident triangles. It is therefore assigned exactly once by either convention. Boundary factors are one, so either triangle product equals the product of all triangulation channel weights.

The ratio is

\[
h^+_{ijk}/h^-_{ijk}=\lambda_{ij}\lambda_{jk}/\lambda_{ik}=\delta\lambda.
\]

Its boundary holonomy is one, so the two lifts differ by precisely the previously classified triangle gauge. They define the same class of triangle factors modulo that gauge. Neither lift is asserted invariant under unrecorded relabelling.

## Disposition

The formal-exponent checker verifies both products and their gauge ratio through n=9. Assigning every internal edge to both triangles instead produces exponent two, giving a deliberate failure. No roots are needed, and the channel-to-triangle comparison is explicit. Its kernel after quotienting triangle gauge remains to be matched constructively with the channel root-of-unity kernel.
