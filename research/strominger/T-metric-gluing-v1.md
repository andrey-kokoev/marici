# T as a four-simplex with three reader facets

## Metric result

The proposed abstract C0/M2 seam works metrically for **all 24** saved hydrogen
reference embeddings. Keep the intrinsic lengths in each P/N/E tetrahedron and
identify the two seam labels in the abstract glued object. Every shared edge
receives the same length from its incident reader facets.

The resulting five-point distance matrix has a positive-definite rank-four
Gram matrix in every case. This proves that it has a Euclidean realization as
a nondegenerate **4-simplex** (pentachoron), rather than merely a combinatorial
quotient. The exact determinant is 4 in the squared-distance normalization of
the checker. Distances there are proportional to physical squared distances
because the source coordinates are barycentric in a regular simplex.

This is an intrinsic gluing construction. C0 and M2 remain distinct in the
original unfolded three-dimensional assemblies; the new abstract object glues
their boundary presentations. It preserves each reader's intrinsic tetrahedral
metric, not the entire original six-point distance matrix.

## The three facets

Let u=C1, v=M1 and a=[C0~M2], b=M0, c=C2. Then

```
T has vertices {u,v,a,b,c}.
P = {u,v,a,b} : barycentric coordinate c = 0
N = {u,v,b,c} : barycentric coordinate a = 0
E = {u,v,c,a} : barycentric coordinate b = 0
```

The three tetrahedral facets meet along the same u/v edge. Its link in the
4-simplex is the triangle with vertices a,b,c. Thus the proposed three-section
picture has an actual geometric realization: three three-dimensional facets
of one four-dimensional object, each fixing a different coordinate to zero.

T also has two other tetrahedral facets, omitting u or v. Their role in a full
assembly theory has not been specified. The present result identifies three
selected reader facets, not a complete five-facet dynamics.

## Configuration-coordinate assignment

A candidate assignment compatible with the previously tested reversal is

```
a = realization coordinate R
b = M coordinate
c = C coordinate
```

It gives:

| Reader | Held fixed | Varying named coordinates |
|---|---|---|
| P | C | R,M |
| N | R | M,C |
| E | M | C,R |

The motivation is that a is the seam class fixed by reversal, while b and c
exchange as M0/C2. Reversal also exchanges u/v. This is a coordinate naming
proposal; identifying it with the earlier physical/configuration M,C,R spaces
requires compatible transition, index and coefficient laws.

## Symmetry distinction

Cycling a->b->c->a cycles the three facets combinatorially. It is an isometry
in **none** of these 24 supplied metrics. The reader facets need not be congruent
for them to be facets of one object.

The P/E-exchanging reflection a->a, b<->c, u<->v preserves the metric in the
8 regular-E examples and changes it in the 16 split-E examples. This exactly
matches the earlier rigid P/E exchange classification. Generic chart changes
therefore require metric-aware transport, not an assumption of rigid symmetry.

## What has and has not been established

Established: an explicit seam, compatible intrinsic reader metrics, a rank-four
Euclidean realization, three coordinate-zero facets and their common edge/link.

Still open: the seam's role/occurrence/coefficient transition, the interpretation
of the two remaining facets, the common object's relationship to native 12/3
channel spaces, and whether the selected facet dynamics yields the occupied
support-contraction rule. In particular the five-slot coefficient reference
omits M2; the metric quotient does not supply its coefficient identification.

Production and viewer remain unchanged.

```sh
node research/strominger/checkers/probe_T_metric_gluing.mjs
```

Evidence: `results/T-metric-gluing/verification.json`, with all ten edge lengths,
exact Gram matrices, positive-principal-minor tests and symmetry outcomes.
