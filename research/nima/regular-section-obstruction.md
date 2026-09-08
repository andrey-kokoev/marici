# No regular triangle section at the seven-point vertex

## Question

Can the proved pointwise triangle lifts be chosen by a regular section of the monomial map?

## Claim boundary

Let X be the seven-point coefficient variety and pi:A^35 -> X its triangle monomial parameterization over a field k. There is no regular section on any open neighborhood of the coefficient vertex 0, hence no global regular section. This does not prohibit regular sections on locally closed support strata.

The conjecture of a global regular factor choice competes with a vertex tangent obstruction. A misleading rival argument would assume every lift of the vertex is the parameter origin and use vanishing derivatives of degree-five monomials there. That assumption is false: setting one triangle coordinate to one and all others to zero also maps to the vertex. The checker verifies this control.

All 63 generators of the defining ideal of X are homogeneous quadrics. Thus the ideal has no linear terms, and the tangent space T_0 X has dimension 42 over every field. For any hypothetical section s near 0, put a=s(0). Affine 35-space is smooth at every a, so T_a A^35 has dimension 35. Differentiating pi composed with s equal to the identity gives

\[
d\pi_a\circ ds_0=\operatorname{id}_{T_0X}.
\]

The left side has rank at most 35, while the right side has rank 42. The deficit is at least seven regardless of which lift a is chosen. This rules out the proposed section without assuming anything about the zero fiber's geometry.

## Disposition

Pointwise surjectivity does not extend to a global regular choice of factors. The exact checker verifies generator homogeneity, both dimensions, and the nonorigin zero-fiber control. Existence over each field is unchanged. A remaining constructive question is a regular section on each fixed-support torus, with the complement choices and transition ambiguities recorded; the tangent obstruction does not address those lower-dimensional domains.
