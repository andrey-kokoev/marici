# Shared-leg DG realization and base-change coherence

## Differential on the actual assembly graph

Use the actual objects A,U,V,B, the11+11 arrow legs,4+4 state legs and the
independent direct reference d:A->B. Choose a base leg on each side of each
block. In the arrow block, freely adjoin degree-one witnesses

    delta(h_i)=x_i-x_0, delta(k_j)=y_j-y_0,
    delta(b)=y_0*x_0-d.

There is an analogous state block. Base-leg witnesses h_0,k_0 are zero. Extend
the differential by the graded Leibniz rule on composable paths. All original
maps have degree zero and zero differential, so delta^2=0.

The base-path witness b retains the discrepancy against the independent direct
reference. No factorization d=y_0*x_0 is required. The choice of roots and free
witness adjunction is a declared realization rule; the graph does not select a
preferred root or physical witness cost.

## All137 comparisons and their higher witnesses

Each slot comparison has two degree-one routes:

    sigma_first  = b + k_j*x_i + y_0*h_i,
    sigma_second = b + y_j*h_i + k_j*x_0.

Both have boundary y_j*x_i-d. Their difference is filled by

    K_ij=k_j*h_i,
    delta(K_ij)=(y_j-y_0)*h_i-k_j*(x_i-x_0)
               =sigma_second-sigma_first.

There are100 arrow-block and9 state-block nontrivial higher products. They now
live on the actual shared intermediate objects, using the original leg types.
This removes the need to compose the already-assembled parallel A->B maps.

The rectangle sum of the first-route witnesses simplifies to k_j*(x_i-x_0).
Its boundary is the nonzero formal mixed product (y_j-y_0)*(x_i-x_0). Thus that
rectangle is not itself a closed element of the free path DG model. K fills the
difference between two factorizations of that mixed boundary. This distinction
preserves the finite response instead of declaring it zero.

## Response evaluation

Evaluate each primitive witness by the matrix difference of its endpoint maps,
and each composable path by ordered matrix multiplication. Then both sigma
routes read exactly y_j*x_i-d. K reads

    (y_j-y_0)*(x_i-x_0),

the same mixed response as the four-slot rectangle. Its boundary's evaluated
response vanishes because the two factorizations agree. The137 normalized slot
responses reproduce the original assembly. Tests use an independent reference
2I and two different choices of base legs.

This is a graded record with a matrix readout, not a chain map into ordinary
matrices with zero differential: evaluating delta(h) gives the observed residual.
No identification of these witnesses with gauge equivalences is assumed.

## A concrete role for the higher cell: changing bases and returning

Change both base legs from(0,0) to(1,1), transporting b using the first-route
formula. Change back by that same convention. The returned witness is

    b_returned = b - delta(K_11).

Its boundary and matrix response agree exactly with those of b. The retained
history has changed by an exact term, with K_11 providing its higher comparison.
K_11 can have a nonzero mixed matrix readout. Thus the rectangle witness directly
controls base-choice coherence within the actual assembly.

This is a concrete reference-frame coherence result. A physical curvature or
gauge interpretation additionally requires transformations, observables and a
metric consistent with this frame dependence.

## Exact size and the next-level limit

The free DG category has31 degree-zero generating arrows and28 degree-one
generating witnesses. Its Hom(A,B) chain spaces have dimensions

| Degree | Dimension | Boundary rank |
|---|---:|---:|
| 0 | 138 | 0 |
| 1 | 246 | 137 |
| 2 | 109 | 109 |
| 3 | 0 | 0 |

Degree-zero paths are137 composites plus d. Degree-one paths include whiskered
leg witnesses and the two base-path witnesses. Degree-two paths are precisely
the109 products K. The degree-two boundary is injective; degree-one cycles are
all filled by those products.

Every original nonidentity path has at most two legs. Therefore there are no
three-witness composable paths in this graph and no nontrivial next cube from
this free construction. The original network supplies the square coherence;
further nontrivial ascent requires a specified network-extension or generator
rule. Whenever two degree-two chains have equal boundary here they already
coincide, so no additional nonzero cube is required for their equality.

These dimensions describe the free DG path realization, distinct from both the
additive cellular path-shadow complex and the earlier biclique complex. No
homology or filler dimensions are transferred between those models implicitly.

## Verification

    python research/nima/checkers/check_shared_leg_dg_realization.py

Exact rational checks: both137-slot witness routes, all109 degree-two fillers,
Leibniz boundaries and delta^2, chain dimensions/ranks, mixed matrix responses,
independent direct reference, two root contexts, and base-change/return coherence
in both blocks. No physical coupling or metric is assigned.
