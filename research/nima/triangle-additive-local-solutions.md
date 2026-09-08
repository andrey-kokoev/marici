# Triangle-additive model for local coefficient gluing

## Question

What explicit functions on triangulations could realize the conjectured local-solution dimension `1+binomial(n-1,3)`?

## Claim boundary

Triangle-additive functions are proved to satisfy every local facet relation. Their generic rank and spanning property remain conjectural; ranks are tested only through `n=9`.

Assign a scalar `h_Delta` to every triple of polygon vertices. For a triangulation `T`, define

\[
f_h(T)=\sum_{\Delta\in T}h_\Delta,
\]

where the sum runs over its `n-2` triangular faces. If a cut decomposes `T` into regional triangulations `T_L,T_R`, its triangles partition between the two regions. Hence

\[
f_h(T_L,T_R)=f_h^L(T_L)+f_h^R(T_R),
\]

and every mixed anchored `2 by 2` difference vanishes. Thus triangle-additive functions lie in the local-gluing solution space for every polygon.

There are `binomial(n,3)` possible triangle weights, but the induced function space has tested rank

\[
1+\binom{n-1}{3}.
\]

Multi-prime ranks modulo `2,3,5,1000003` agree at every stage `n=5..9`, giving `5,11,21,36,57`. These equal the independently measured local-solution dimensions through `n=9`. The triangle-weight kernels have dimensions `5,9,14,20,27`.

## Disposition

The missing abstract basis has been replaced by an explicit triangle-additive candidate model with a generic locality proof. The local-rank conjecture would follow from two remaining theorems: the triangle-incidence rank formula and the converse that every locally factorizing triangulation function is triangle-additive. Finite modular equality does not prove either theorem.
