# Pivot extensions on the determinantal boundary face

## Question

Is the pole in one stratum section intrinsic, or can another pivot extend across it?

## Claim boundary

Arrange coefficients 35,36,40,41 as the rows of a two-by-two matrix W. Its face closure is det(W)=0. The four principal opens where one entry is nonzero cover precisely the punctured face. They allow additional coefficient zeros, unlike the fixed-support torus.

On the chart W_pq nonzero, set r_i=W_iq and c_j=W_pj/W_pq. Rank-one minors give W_ij=r_i c_j. Implement r_0,r_1 as triangle factors z035,z034 and c_0,c_1 as z013,z012; set the other five used triangle factors to one and unused factors to zero. Support closure ensures no excluded triangulation appears. These are regular sections on all four charts.

On an overlap with pivot (s,t), the new row factors are lambda times the old ones and the column factors are lambda inverse times the old ones, where lambda=W_pt/W_pq. The cross entry W_pt is invertible on the overlap because W_pt W_sq=W_pq W_st. Thus the transition remains regular even when some other entries vanish. The checker verifies four reconstruction identities and six pairwise transitions symbolically. The observed pole in one formula is therefore not an obstruction throughout its vanishing divisor.

## Disposition

Chartwise factor selection covers the punctured face. It cannot extend as a section near its vertex, even using arbitrary triangle lifts. Every one of the nine used triangle incidence columns is a row indicator, column indicator, or common indicator (verified by a targeted runpy assertion following the checker). Consequently the four coefficient map factors polynomially as h r c, including at all zero-fiber points. When h=0 its derivative has rank at most one; when h is nonzero, r c=0 forces r=0 or c=0, and the derivative rank is at most two. The face tangent dimension at its vertex is four. A differentiated section would require rank four, which is impossible.

This is not yet a proof that no global section exists on the punctured face: chart transitions may or may not be removable by regular changes of factors. The remaining question is the class of this multiplicative transition system, not another pivot computation. The rank argument is characteristic-independent. No physical source embedding is supplied.
