# Channel root kernel inside triangle gauge

## Question

How does the finite channel kernel become trivial in the quotient by triangle gauge?

## Claim boundary

The maps are labelled monomial maps on complex tori for n>=4. They do not identify a source embedding or prescribe physical normalizations.

Let s_ij be one for a diagonal and zero for a polygon boundary edge. A common channel rescaling by zeta induces the triangle ratio h_ijk=zeta^(s_ij+s_jk). Define an edge cochain by u_0i=1 and u_ij=zeta^(s_0i+s_ij) for 0<i<j. Its coboundary equals h: on triples away from zero, the extra exponent is s_0j-s_ik=1-1=0; triples containing zero give the identity directly.

The boundary holonomy of u is zeta^(n-3). Therefore this cochain lies in triangle gauge exactly when zeta^(n-3)=1. The checker verifies all exponent identities through n=12 and rejects primitive (n-2)nd roots via their nonzero boundary exponent.

Conversely, a channel assignment mapping into triangle gauge evaluates to one on every triangulation. Comparing two triangulations differing by a flip forces the exchanged crossing channel scales equal. Connectivity of the diagonal crossing graph makes every channel scale the same zeta. One triangulation then imposes zeta^(n-3)=1. Thus no other channel kernel elements occur.

## Disposition

The channel-to-triangle-class map has exactly the diagonal root kernel mu_(n-3). This finite preimage kernel is compatible with the connected triangle-gauge torus: connectedness of the larger gauge does not imply injectivity of the comparison. The quotient of triangle-evaluation classes by the channel image remains a distinct object to construct.
