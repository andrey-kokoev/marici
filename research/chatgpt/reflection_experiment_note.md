# Four tests of the outer-edge reflection construction

Date: 2026-10-28.

## Input protocol and choices

The requested sequence is: seed; clone-reflect across the white edge; clone-rotate the whole accumulated assembly by 120 degrees; clone-reflect the whole enlarged assembly across a newly exposed outer red edge; clone-rotate by 120 degrees again. Every original copy is retained at every cloning step. “Complete” here means carrying the entire accumulated assembly forward. It does not add arbitrary cells or filler relations.

The experiment fixes a triangular planar footprint and tests the undetermined rotation centers. The red direction stays fixed across all four variants; its actual supporting line is recomputed from the enlarged assembly. A supporting corner is not silently substituted for a supporting edge.

The supplied conversation does not define the five vertices, metric and full reflection hyperplanes of the intended Su-32 simplex. Two explicit, nonregular 4-dimensional simplex lifts are therefore tested as controls. Neither is claimed to be that native simplex.

## Exact coordinates

Use triangular coordinates `(u,v)` with Euclidean basis `(1,0),(1/2,sqrt(3)/2)`. The seed vertices are

    O=(0,0), A=(1,0), B=(0,1).

The Gram matrix is

    G = [[1,1/2],[1/2,1]].

The white mirror is `v=0`. Its reflection is

    W(u,v)=(u+v,-v).

The 120-degree linear rotation is

    R(u,v)=(-u-v,u).

Rotation about `c` is `R_c(x)=Rx+c-Rc`. The requested outward red direction is the covector `(1,1)`. For the current assembly its supporting line is

    u+v=h,  h=max(u+v) over every current vertex.

The reflection in this line is

    E_h(u,v)=(h-v,h-u).

The checker requires that this line contain an actual edge of at least one current triangle, not merely a corner or a convex-hull connector across a gap.

These are orthogonal reflections for the stated Gram matrix. The ordinary affine-reflection framework is described in Bill Casselman's *Coxeter groups*, Part I, section “Reflections”: https://personal.math.ubc.ca/~cass/coxeter/r.html. Counts, center choices and cycle results below are the present calculation, not results taken from that source.

## Four variants

All three completed runs retain 1, 2, 4, 8, 16 copy histories. Duplicate geometry is grouped for counting, never deleted from those records.

| Variant | First rotation center | Second rotation center | Distinct triangular footprints by stage | Final partial-overlap pairs |
|---|---|---|---|---:|
| A: shared white endpoint | (0,0) | (0,0) | 1,2,4,8,14 | 0 |
| B: white-reflected triangle centroid | (2/3,-1/3) | (2/3,-1/3) | 1,2,3,6,10 | 0 |
| C: move the second center | (0,0) | (1/2,1/2) | 1,2,4,8,16 | 15 |
| D: white-edge midpoint | (1/2,0) | not executed | 1,2,4; then refused | 4 at refusal |

A partial-overlap pair means two different triangular footprints whose interiors intersect. Identical footprints are counted as duplicates, not as partial-overlap pairs.

For A, B and C, the actual red supporting edge is the original segment joining `(0,1)` and `(1,0)`, now exposed on the enlarged assembly; its line is `u+v=1`. It is selected from the enlarged assembly, rather than assumed to be a conjugate of the white mirror.

For D, the required red supporting line is `u+v=3/2`. It meets the enlarged assembly only at `(1,1/2)`. There is no red edge there. The run stops before that reflection. Reflecting about a line through a corner would be a different protocol, and so would choosing a different edge direction.

## A: an actual central contact circuit

A has fourteen distinct non-overlapping footprints. Its shared-edge adjacency graph has fourteen vertices and fourteen edges and is connected, so its cycle rank is one. Exactly six triangles meet at O. They form the central six-cell circuit shown in blue in the viewer.

For each successive pair on this circuit, reflect in their shared edge. The checker verifies that this reflection maps the entire source triangle to the entire next triangle. It then multiplies all six affine transformations exactly. The result is

    S_6 S_5 S_4 S_3 S_2 S_1 = identity.

There is no residual translation and no residual linear rotation or reflection. This is whole-frame closure, not merely return of the contact vertex.

The same six maps, extended by the identity on the two hidden coordinates, map the full five-vertex simplex to the next full simplex for BOTH 4D lifts below. All six full-cell matches are separately checked for each lift. Their product is the identity in four dimensions, so every geometric vertex label returns after the whole circuit.

These are geometric seam-reflection maps. Their admission as native P/N/E transport, or their action on additional proof/history data, has not been established. The six-cell adjacency cycle is not an unfilled hole in the union: the planar union has no hole. No nontrivial bundle follows from this identity return.

## B: exact overlaps depend on all five vertices

B gives ten planar footprints, although there are fourteen distinct affine transformations and sixteen retained histories. Some transformations arrive at the same triangle with different inherited vertex orderings. Its shared-edge adjacency graph is a tree; there is no six-cell central circuit. The planar union has no hole.

To check the four-dimensional significance, use the first three vertices

    O=(0,0,0,0), A=(1,0,0,0), B=(0,1,0,0).

Two possible choices for the remaining vertices are:

    centered lift:
      D=(1/3,1/3,1,0), E=(1/3,1/3,0,1);

    asymmetric lift:
      D=(1/4,1/4,1,0), E=(1/2,1/4,0,1).

Both edge matrices have determinant one in these coordinates, so both are genuine 4-simplexes. Both project to the identical seed triangle, since the projections of D and E lie strictly inside it. The metric is the planar triangular Gram matrix plus the Euclidean metric in the two hidden directions.

Extend every planar affine map by keeping the last two coordinates unchanged. Count geometric 4-simplexes by their complete unordered sets of five 4D vertices. Keep ordered vertices and construction histories separately.

| Variant | Centered-lift 4-simplexes | Asymmetric-lift 4-simplexes |
|---|---:|---:|
| A | 14 | 14 |
| B | 10 | 14 |
| C | 16 | 16 |
| D, stopped | 4 | 4 |

Thus four apparent geometric identifications in B depend on how the two remaining vertices are placed. The triangular drawing alone does not certify them. In B's asymmetric lift, distinct 4-simplexes can share the same projected triangle. This is not a claim that generic coordinates are native or physically preferred; it is a comparison of two explicit lifts.

These reflections fix supporting 3-hyperplanes in 4D whose intersection with each affected simplex is an edge. They are not claimed to reflect across tetrahedral facets. The distinction matters for any extension to a facet-glued four-dimensional tessellation.

## Why the midpoint choices differ

For `c=(u,v)`, the rotation translation is

    c-Rc=(2u+v, v-u).

The rotation preserves the unshifted triangular lattice exactly when both components are integers. This criterion follows directly from the displayed integral matrix for R and its inverse.

A and B satisfy the criterion. The white midpoint `(1/2,0)` and the red midpoint `(1/2,1/2)` do not. Their rotated copies occupy shifted triangular lattices, and the actual tested assemblies have partial interior overlaps. Lattice preservation alone does not prove the desired contact topology: B satisfies it but has no central six-cell circuit.

## Consequence for the proposed mechanism

A supplies a closed geometric comparison circuit from the declared reflected copies. No final arbitrary closing map is added. B supplies a distinct overlap pattern; its interpretation is sensitive to the unprojected vertex data. C and D distinguish a usable outer-edge assembly from interior crossing and from an unavailable requested edge.

The successful local result is the exact six-seam identity in A, valid for both tested 4D lifts. It is not an established fibration or an unfilled higher-dimensional boundary. It provides a concrete geometry and complete maps against which native packet interfaces can be tested.

## Evidence

`check_reflection_variants.py` uses only Python's standard library and exact `Fraction` arithmetic. It checks affine inverses, metric preservation, reflection involutions, order-three rotations, supporting-edge admission, absence of cross-seam interior overlap at admitted reflection steps, exact triangular intersections, copy identity, five-vertex 4D cell identity, and the complete central return.

The browser uses floating point only for rendering. Its comparison views, stage navigation, inspector and 4D-lift selector were tested in headless Chromium. No Agda/Lean run or native Su-32 execution was performed. The source construction under test is explicitly the protocol and coordinates above.
