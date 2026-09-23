# Common lifting over polyhedral domains has finite compatibility certificates

## General scalar-fiber criterion

Let Q be a fixed nonempty compact rational polytope of public parameters. A history has scalar fine coordinate h constrained by finitely many rational affine bounds

    l_i(y)<=h<=u_j(y), y in Q.

Assume both bound families are nonempty and include the complete source-relative admission constraints. For a group of histories with this same public domain, a common lift exists pointwise iff every combined lower/upper pair obeys

    l_i(y)<=u_j(y) for all y in Q.

Each obligation is a rational linear optimization question over Q. It can be certified by a dual bound or refuted by a feasible public point where l_i>u_j. A verified vertex presentation of Q provides an alternative finite certificate: affine inequalities hold throughout Q iff they hold at every vertex.

If all obligations pass, define

    l_G(y)=max_i l_i(y), u_G(y)=min_j u_j(y),
    s_G(y)=(l_G(y)+u_G(y))/2.

Finite maxima/minima of affine functions are continuous and piecewise affine; hence s_G is an explicit continuous common selection. It remains source-admitted because the source bounds are included. Straight-line contraction of the COMMON intersection fiber to s_G preserves every participating history at that y. It does not contract a history's entire larger fiber while preserving other histories it did not originally satisfy.

For any fixed norm, maxima/minima inherit the largest affine Lipschitz bound of their pieces; the midpoint has the corresponding averaged bound. Translating h back to source coordinates introduces the norm of that inverse coordinate map. This is not a uniform conditioning statement over changing source parameters.

## Why this is stronger than one-point grouping

Compatibility must hold throughout Q. Failure at one public point prevents a shared lifting state even if most fibers overlap. Conversely the explicit midpoint construction shows that, in this finite affine interval class, pointwise common nonemptiness has no additional continuity obstruction. This conclusion is specific to the class; it should not be generalized to arbitrary parameterized witness spaces.

For finite intervals, pairwise intersection at each y implies total intersection. Therefore, for histories with interval fibers on the SAME Q, group compatibility is equivalent to all pairwise compatibilities holding over Q. Construct an incompatibility graph on histories: an edge has a certified public point where their fibers are disjoint. Minimum common-lifting state count is the chromatic number of this graph, with color classes given the common midpoint section. This is a structural characterization, not an efficient graph-coloring algorithm or a general higher-dimensional Helly claim.

It differs from transitive quotienting: compatibility remains nontransitive. A chosen partition into compatible groups induces states; the compatibility relation itself is not an equivalence.

## Owning varying-domain control

Use m=3 and source coordinates

    x(p,h)=(p-h/128, 1+129h/128, 1-h),
    1<=p<=2, 0<=h<=1.

These obey the owning atom caps. Their public moments are

    U=p+2, V=p+1/128+1/16384,

independent of h. Fix that public segment and include the displayed h bounds as source-relative linear evidence. With h=1-x_2, the two moment equalities recover the displayed source formula uniquely. All extra affine bounds below are therefore rational linear evidence in the original public moments and raw atom audit.

Define histories A,B,C by

    A: 0<=h<=1/2,
    B: (p-1)/4<=h<=3/4,
    C: (p-1)/2<=h<=1.

All three have the entire public segment as image. Their common fibers are

    (p-1)/2<=h<=1/2,

with continuous shared section h=p/4. The endpoint p=2 gives a singleton common fiber, so the control includes a rank collapse without a discontinuity.

Define D by p/2<=h<=1. It too has the same public image. A and D overlap at p=1 but are disjoint for every p>1; p=2 gives a strict compatibility obstruction. A lift procedure valid only at the first public boundary would miss this failure.

For the four histories A,B,C,D, at least two lifting states are needed because A and D are incompatible. Two suffice, for example grouping A,B,C together and D alone. Every history still shares one public-answer state; their distinct fine relations require four states for exact fine re-exposure in this frozen family.

## Verification and scope

The exact checker verifies all lower/upper obligations for A,B,C at both public vertices. It checks midpoint and source reconstruction identities at rational controls, verifies the obstruction at p=2, and checks the endpoint common-fiber collapse. The continuum proof is affine vertex checking plus max/min continuity, not sampling.

    python research/voevodsky/checkers/check_common_lifting_domain.py

Artifact: `results/common-lifting-domain.json`.

No general LP optimizer, graph-coloring implementation or separate packet verifier is delivered by this control. It does not freshly replay upstream analytical admission. The result is a reusable finite certificate criterion and continuous selection construction for complete scalar affine-bound fibers.
