# Iteration 1: actual potential complex and realization pullback

## Scope and declared contract

This replaces the identity-glue and independent holonomy proxies with an actual potential complex, two explicit interface maps and their full geometric pullback.

The category is PL polyhedra with PL maps. The chosen fold grammar is the complete barycentric flag subdivision, with inward radial contraction to the barycenter. It is not an isometric origami law and is not asserted to exhaust every possible meaning of an inward fold. The common interface is normalized inward depth. These choices are explicit hypotheses, not uniquely forced by particle terminology.

The unchanged 1836-arrow source is included and reverified. No electron identity, charge, mass or new coefficient operator is assigned by the construction.

## 1. Potential complex and all its declared inward folds

Take the potential tetrahedron C = sd(Delta^3), in its own barycentric coordinate chart. Its body barycenter is b=(1/4,1/4,1/4,1/4). Its vertices are barycenters of all 15 nonempty vertex subsets. The 24 maximal tetrahedra are precisely all flags

```text
vertex < edge < face < body.
```

They refine four primary face-to-body inward cones. None is discarded when b is realized.

For y in C define

```text
h_C(y) = 1 - 4 min(y_i).
```

The body barycenter has height zero; the entire boundary has height one. This map is affine on each retained flag tetrahedron. The inward contraction R_s(y)=(1-s)y+s b stays inside each cone and satisfies h_C(R_s(y))=(1-s)h_C(y).

## 2. Actual host and interface maps

Select the existing oriented outer triangle AB=(F_ABC,A,B). Subdivide it barycentrically:

```text
T = sd(Delta^2), with six vertex < edge < face flags.
q = its barycenter = (7/9, 1/9, -1/9) in the source spatial chart.
```

In triangle barycentric coordinates q=(1/3,1/3,1/3). Define h_T(x)=1-3 min(x_i). The common interface is I=[0,1]. Both maps send their central barycenter to 0 and every proper-face barycenter to 1.

The source surface is conformingly refined, including the three adjacent triangles affected by the new edge midpoints. The refined surface has 12 vertices, 30 edges and 20 triangles, remains an oriented sphere and retains volume 8/3. The new realized point really is a vertex on the selected outer triangle, not a detached outward apex.

This geometric refinement does not silently retarget or duplicate the original coefficient arrows.

## 3. The full pullback—not just a named point

Construct the commuting square

```text
P  --p_C-->  C
|           |
p_T         h_C
|           |
v           v
T  --h_T-->  I
```

with P={(x,y): h_T(x)=h_C(y)}.

The zero-depth fiber is exactly the single vertex r=(q,b). Its projections identify the potential barycenter with the new host vertex. But the whole pullback is much larger than that fiber.

For any compatible pair of positive depth t, there are unique boundary directions u and v:

```text
x = (1-t)q + t u,     u in boundary Delta^2,
y = (1-t)b + t v,     v in boundary Delta^3.
```

Conversely these formulas produce every compatible pair. At t=0 all direction pairs meet at r. Therefore

```text
P is PL-homeomorphic to cone(S^1 x S^2).
```

The explicit triangulation has 6 host boundary edges times 24 potential boundary triangles. Each edge-times-triangle prism has three compatible staircase tetrahedra; coning gives 432 four-simplices. The counts are:

| Complex | f-vector |
| --- | --- |
| Full pullback | (85, 600, 1380, 1296, 432) |
| Link of the realized vertex | (84, 516, 864, 432) |

All 144 host/potential flag pairs and all 24 potential fold flags remain present. Every maximal pullback cell has exact affine dimension four. The vertex link has mod-2 Betti numbers (1,1,1,1), not those of a three-sphere.

This is an information-space dimension, not a claim of an extra physical spatial dimension. In particular, retaining only r would forget the requested inward-fold data; the rich pullback is not a three-dimensional tetrahedral complex merely because its potential factor is one.

### Universal property and executable mediator

For any PL maps a:X->T and d:X->C satisfying h_T a=h_C d, the only possible mediator is z |-> (a(z),d(z)). The equality ensures its image lies in P. This map is PL after the compatible subdivision induced by the staircase cells. Both projections recover a and d, and uniqueness follows because a point of P is precisely its ordered projection pair.

The checker implements a rational mediator, not only the commuting square. For t>0 it computes u and v, decomposes them into barycentric flag simplices, and uses monotone interval coupling to locate their product in a staircase simplex. Projection reconstructs the exact original pair. At t=0 it returns r. Shared-face chart representations can differ; the geometric mediator remains unique.

Checks cover all 2647 compatible pairs in two rational grids and an interior point of every one of the 432 cells. These finite checks support the explicit general construction above; they are not presented as a formal proof-assistant verification of the universal quantification over X.

## 4. What is actually derived about the belt?

The link of q in the fully flagged host triangle is the six-cycle

```text
vertex 0 -> edge 01 -> vertex 1 -> edge 12 -> vertex 2 -> edge 02 -> vertex 0.
```

Cutting the six inward host sectors between depths 1/2 and 1 constructs a genuine six-quadrilateral annulus, with 12 vertices, 18 edges and two six-edge boundary loops. It is stored with exact barycentric coordinates and checked for incidence and nondegeneracy.

This belt is around the **new realized barycenter of the selected triangle**. It is not silently identified with the earlier six-belt around an original tetrahedral corner.

The annular neighborhood follows from the punctured host disk. Six panels follow specifically from retaining its vertex-edge-face flags. Topology alone does not require six: a three-sector stellar subdivision gives the same depth map and underlying disk. Likewise, a particular truncation radius is not forced.

## 5. Nontrivial transport does not follow

Away from r the pullback is globally the product of a positive depth interval, the host direction circle and the potential direction sphere. Potential directions and all their fold charts can remain fixed during a circuit around the host vertex. No permutation is forced by either interface map. The checker follows all 24 potential charts around the six-cycle.

There is also an extension obstruction to the previous odd C2 transport. Any flat two-sheet transport extending across the center must satisfy, on each radial triangle,

```text
boundary_bit_i = radial_bit_i XOR radial_bit_(i+1).
```

Summing around the boundary gives zero: all radial bits cancel. Exhausting the 64 radial assignments finds two extensions for zero boundary labels and none for a single odd boundary swap. This radial disk is present in the actual pullback by holding one potential boundary direction fixed.

Thus nontrivial belt transport is not a consequence of this realization. If demanded, it cannot extend as an everywhere locally constant two-sheet system across the realized center. It requires additional data such as a branch locus, a singular/nonflat transport law or removal of the center. None is inserted under the name neutron.

## Verification, limits and executable continuation

All 31 tests passed, including full source-bound packet replay and honestly rehashed mutations of the realization point and interface map. The saved packet includes the original proton witness, both complexes, interface maps, all pullback cells with fold provenance, conforming host refinement and the derived belt.

```text
python research/voevodsky/checkers/check_potential_complex_pullback.py
```

- `research/voevodsky/checkers/potential_complex_pullback.py`: construction, projection maps, mediator and exact combinatorics.
- `research/voevodsky/checkers/check_potential_complex_pullback.py`: source-bound verifier and controls.
- `research/voevodsky/results/potential_complex_pullback_store.json`: retained construction.
- `research/voevodsky/results/potential_complex_pullback.json`: check receipt.

This is one explicit realization contract, not a uniquely derived electron. In particular, normalized depth matching deliberately leaves the two angular directions independently retained; it has not yet imposed a coefficient-port attachment law.

The next nonredundant step is a witness-preservation audit of the projections and candidate compressed interfaces: determine exactly which fold information is lost by a point-only or host-only view, and specify the smallest retained interface that can reconstruct this actual pullback. Only then should coefficient-port maps and H-1/H-2 arrow counts be proposed. The earlier conditional 1908/1944 counts and the independent 72-arrow holonomy experiment are not costs of this new object.
