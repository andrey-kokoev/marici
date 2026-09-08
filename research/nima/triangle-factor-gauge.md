# Multiplicative triangle-factor gauge

## Question

Which changes of triangle factors leave all triangulation products unchanged?

## Claim boundary

Factors are units in an abelian group. Connectedness and dimension below refer to the complex algebraic torus, not to real points or physical gauge authority.

If triangle factors h evaluate to one on every triangulation, comparing the two diagonals in any four-vertex quadrilateral gives delta h=1. Every crossing pair extends to a polygon flip. Multiplicative simplex contraction therefore gives an edge cochain u such that

\[
h_{ijk}=u_{jk}u_{ij}/u_{ik}.
\]

The product over a triangulation cancels every internal oriented edge and equals

\[
H(u)=\frac{\prod_{i=0}^{n-2}u_{i,i+1}}{u_{0,n-1}}.
\]

Thus the kernel is exactly edge coboundaries with H(u)=1. Two edge representatives give the same h precisely when related by a vertex coboundary u_ij -> u_ij v_j/v_i.

Fix all root edges u_0i=1 using vertex gauge. The remaining binomial(n-1,2) edge variables obey the single equation product_{i=1}^{n-2} u_{i,i+1}=1. Solve for u_12 using exponent one. The kernel is consequently isomorphic to a torus of dimension binomial(n-1,2)-1=n(n-3)/2, with no disconnected finite factor over the complex numbers. This differs from the finite diagonal root kernel of channel-scale evaluation.

## Disposition

Exact rational examples through n=8 verify nontrivial triangle gauge invariance and vertex-gauge cancellation. Breaking one boundary-edge factor makes every triangulation product equal two, detecting the holonomy condition. Triangle recovery selects a representative of this continuous gauge; it is not unique without such a choice.
