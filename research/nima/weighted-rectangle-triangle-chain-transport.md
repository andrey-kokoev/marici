# Weighted rectangle-to-triangle chain transport

## Explicit chain comparison

Use the full primitive four-label relation. Its bipartite incidence presentation
has8 vertices,12 edges and6 rectangle2-cells. Its Dowker presentation has4
vertices,6 edges and4 triangle2-cells.

Choose for each target t an adjacent source anchor a_t != t. Map source vertices
to themselves and target vertices to their anchors. With the signed incidence
boundary source-target, an edge (s,t) maps to the oriented simplicial edge
[a_t,s]. A rectangle with source pair(u,w) and target pair(v,z) maps to

    [a_v,u,w] - [a_z,u,w],

where repeated vertices give a zero simplex. The source triples are valid
Dowker triangles because each shares the indicated target neighbor. This gives
maps T0,T1,T2 satisfying both chain-map squares exactly.

The primitive integral rectangle cycle maps to the primitive integral triangle
cycle with degree +/-1 according to the initial orientation convention.

## Transport the metric and complementary records

For the cyclic anchor choice a_t=t+1 mod4, T2 has rank4 and a2-dimensional
kernel. With unit source rectangle cost, define

    G=(T2*T2^T)^-1,
    L=T2^T*G,
    residual=(I-L*T2)*x.

Then every source2-chain has the lossless representation

    y=T2*x,
    x=L*y+residual,
    ||x||^2=y^T*G*y+||residual||^2.

Here G=I4. All729 source vectors with coefficients in{-1,0,1} pass exact
reconstruction and cost checks.

## Closedness is part of the promoted edit type

For the primitive sphere cycle z:

    source cost6 = unconstrained target quotient cost4 + residual cost2.

The unconstrained minimum lift L*T2*z is NOT closed in the source complex.
Its boundary is nonzero even though its image is a target cycle. Restoring the
retained residual cancels that boundary and recovers z.

Thus the target cycle condition alone does not determine source admissibility.
The complete promoted state must satisfy

    d2_source*(L*y+residual)=0.

There is no nonzero chain simultaneously in ker(T2) and ker(d2_source), so the
residual of a closed source lift is unique in this primitive example. Its cost
is forced by closure. On the target cycle line the transported closed-class
cost equals3/2 times its unit-triangle norm, giving cost6 again. This fixes the
metric on that line; it does not uniquely specify a metric on all target cells.

## Independence from anchor choices

There are3^4=81 admissible anchor assignments. The checker constructs every
chain map and finds the same oriented class image and closed-class cost6.
The ranks of T2 vary:

| Rank | Anchor assignments | Unconstrained class-image cost | Residual cost |
|---:|---:|---:|---:|
| 2 | 3 | 2 | 4 |
| 3 | 48 | 3 | 3 |
| 4 | 30 | 4 | 2 |

For rank-deficient maps the quotient cost is on their target image. The
complementary cost accounts for the rest in every case. All chain-map identities
and primitive-class images are checked. This provides a concrete witness-family
calculation: presentation maps vary, while the complete closed-class budget is
unchanged.

## Structural consequence

The required promotion contract has three parts:

1. Retained content reconstructs the source record.
2. The transported metric includes the complementary record's cost.
3. Admissibility constraints are imposed on the reconstructed source.

Keeping the target value and assigning it a metric alone can select an invalid
source edit and undercount its cost. This refines the earlier mean-plus-residual
rule to a chain-level, state-constrained return contract.

The next extension is the two-factor comparison complex. Its chain maps must
transport both independent degree2 classes, their metric, and the source closure
constraints. That tests whether the primitive budget law composes through the
actual comparison hierarchy.

## Verification

    python research/nima/checkers/check_weighted_rectangle_triangle_transport.py

Exact Fraction chain maps, primitive class normalization,729 source-cell
reconstructions, induced quotient Gram, orthogonal residual projector, closure
negative control, scaled class returns, and all81 anchor choices. No cost scale
is fitted: the initial unit rectangle cost is transported through the explicit
map and retained residual.
