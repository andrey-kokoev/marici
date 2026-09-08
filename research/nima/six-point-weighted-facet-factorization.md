# Six-point weighted facet factorization

## Question

How must triangulation coefficients restrict on each polygon facet if they arise from channel scales and respect regional gluing?

## Claim boundary

The checker uses one algebraically distinguished prime assignment to channel scales. It tests the factorization law exactly but does not supply source coefficients or provenance.

For a cut `c`, triangulations containing it are products of regional triangulations `T_L,T_R`. If global coefficients arise from channel scales, then

\[
w_{T_L\cup\{c\}\cup T_R}
=\lambda_c w_{T_L}w_{T_R}.
\]

Consequently the coefficient matrix indexed by `T_L,T_R` has multiplicative rank one. Every `2 by 2` minor obeys

\[
w_{ij}w_{k\ell}=w_{i\ell}w_{kj}.
\]

At six points all nine channel facets are checked. Short cuts split a triangle from a pentagon and have a `1 by 5` coefficient array. Long cuts split two quadrilaterals and have a `2 by 2` array, yielding a nontrivial cross-ratio test. Distinct prime channel scales prevent accidental equalities from hiding incorrect channel assignments.

A deliberate failure doubles one coefficient in a long-cut `2 by 2` matrix. Its cross-product residual is recorded and nonzero, localizing the gluing failure to that facet.

## Disposition

Weighted residue factorization has an executable local test independent of solving all global scales. An owner six-point packet must pass both the five global incidence binomials and every regional rank-one condition; the latter identifies which cut fails when coefficients do not glue.
