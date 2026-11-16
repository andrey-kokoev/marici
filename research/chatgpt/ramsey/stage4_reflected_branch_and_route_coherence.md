# Stage 4 — Reflected branch order, canonical green collar, and its limits

**Date:** 2026-11-09  
**Status:** Exact finite enumeration (2–6 operations), mathematical identification with a known Coxeter complex, and a conditional construction. No new Marici-native comparison has been derived; no Agda compilation claimed.

## Question

Given a red simplex tree (R), its point reflection (B), and a proposed coherence completion (G), can one fixed local rule generate G and force global triangulation without fitting its faces, degree or topology?

This stage changes translation domain to **execution orders and their partial-state incidence**. The symbols R, B and G here label route subcomplexes, not Marici P/E/N particles, nor the independent edge-color classes of a Ramsey graph. In particular, a *star of simplices* is not necessarily a graph-theoretic tree of simplices.

## 1. Six antipodal geometric endpoints

Place the vertices at ±e1, ±e2, ±e3 in three-dimensional Euclidean space. Prescribe the two disjoint triangles R=(+e1,+e2,+e3), B=(-e1,-e2,-e3). Enumerate every choice of four reflected pairs of triangular faces, including R/B. With V=6, a closed triangulated 2-sphere must have E=12 and F=8.

Exact enumeration of all C(9,3)=84 candidate reflected face-orbit choices yields **10** closed simplicial 2-spheres with connected circular vertex links. Nine use two antipodal edges, and exactly one uses none. Since straight antipodal edges are diameters through the center, the nine cannot give embedded complexes with these specified Euclidean coordinates: distinct edges intersect away from their vertices. The sole embedding-compatible choice is the octahedral boundary, with R/B plus six mixed faces G.

The uniqueness assumes 3D coordinates, a closed embedded surface, and no extra vertices. Neither reflection nor native operation composition alone proves those conditions.

## 2. A no-fitting route generator

Let n reversible independent operations be indexed by [n]. A partial execution state is the subset S of operations already executed. Initial state is ∅; final state is [n]. A route is any permutation of [n], with its n−1 nonempty proper prefix subsets. Define K_n by:

- vertices: all nonempty proper subsets S of [n];
- a k-simplex: k+1 such subsets forming a strict inclusion chain;
- local generator: interchange two adjacent independent operations in a route; retain all intermediate subsets, entire route history, and the comparison question between orders.

This is the order complex of the proper part of the Boolean lattice B_n. It is the **Coxeter complex of type A_(n−1)**, the barycentric subdivision of the boundary of an (n−1)-simplex. Hence K_n is a triangulated sphere S^(n−2). This general theorem is known mathematics, not a newly proven result.

Reflection acts by complement S ↦ [n]\\S. It reverses the inclusion order and maps every chain to a chain. A geometric realization is available in the sum-zero hyperplane H={x in R^n:sum x_i=0}: map S to the ray through 1_S−(|S|/n)·1. Complement sends this vector to its negative; radial projection yields central inversion on S^(n−2). Its quotient is RP^(n−2).

A maximal simplex corresponds to one of n! execution routes. K_n has 2^n−2 vertices. It is combinatorially dual to the permutohedron Π_n, whose vertices represent permutations and facets represent nonempty proper subsets. For n=4, Π_4 has six square and eight hexagonal faces; its coherence is *not* exclusively pentagonal.

| n | f-vector of K_n | Topology |
|---|---|---|
| 2 | (2) | S^0 |
| 3 | (6, 6) | S^1 |
| 4 | (14, 36, 24) | S^2 |
| 5 | (30, 150, 240, 120) | S^3 |
| 6 | (62, 540, 1560, 1800, 720) | S^4 |

The f-vectors, codimension-one face multiplicities, reflection involution and face counts have been checked exhaustively. Sphericity is established by the known barycentric-subdivision theorem, not inferred from the counts.

## 3. A reflected dependency and its interface

Let a precede b in R, with all remaining operations independent. For B reverse the precedence. R and B now admit half the permutations each, and complement maps R to B. Their route subcomplexes are balls, each of dimension n−2, and their common intersection is K_(n−1), a sphere of dimension n−3: in the intersection the operations a and b are either both completed or both uncompleted, so they behave as one composite operation.

Thus R∪B=K_n, and the common interface has been generated from the shared admissibility states without adding any spatial angles or triangulations. Exact tests for n=3..6 confirm the face-level identities.

An important obstruction: a poset's collection of order ideals is closed under complement **if and only if** the poset is an antichain. If a<b, the complement of ↓a contains b but not a, hence it is not an ideal. Reflection of a dependent execution domain therefore naturally leads to the opposite precedence domain, not to a symmetry of one domain.

## 4. The R/G/B collar construction

Designate one independent operation a. Let R contain all routes with a first, B all routes with a last, and G all routes with a in an interior position. Define each route's simplex from its n−1 proper prefix subsets. The local adjacent-interchange rule propagates from R through successive positions of a and generates *every* route, and hence all green maximal simplices.

| n | Red maximal simplices | Blue | Green | Union |
|---|---:|---:|---:|---|
| 3 | 2 | 2 | 2 | S^1 |
| 4 | 6 | 6 | 12 | S^2 |
| 5 | 24 | 24 | 72 | S^3 |
| 6 | 120 | 120 | 480 | S^4 |

For every n≥3, R and B are opposite (n−2)-balls (closed stars of antipodal vertices); G is a complementary collar S^(n−3)×[0,1]. R∩B is empty, while R∩G and B∩G are two copies of S^(n−3). This is exact combinatorial topology and follows geometrically from splitting the spherical Coxeter arrangement by the position of a.

The n=4 finite test gives R=(7 vertices, 12 edges, 6 triangles), B the same, G=(12 vertices, 24 edges, 12 triangles), with two six-edge boundary cycles. The assembled sphere has (14 vertices, 36 edges, 24 triangles).

**Precisely what is generated:** all route words, intermediate-state simplices, and their incidence under local interchanges. **What is not generated:** an equality of different retained word histories, a nonzero physical comparison, a preferred phase, or a native source authorization for every swap.

## 5. Controls preventing overclaim

**Dependence:** With three operations a,b,c and a<b, while c is free, the proper-ideal order complex is a path of four vertices and three edges (a ball), not S^1; complement is not an internal operation. Pairwise diamonds cannot force the missing joint state. Reflected domain B must use the reverse dependency to glue a second ball along its boundary.

**Phase selection:** For three independent reversible operators with labeled central commutation signs ε_ab, ε_ac, ε_bc ∈ {±1}, all eight sign assignments are algebraically consistent. Each of the six orderings is a distinct retained history; the hexagon of adjacent swaps has trivial total *sign* holonomy for all eight assignments. Therefore global route closure does not determine the three local comparison signs. This recovers the phase-selection obstruction in `research/nima/phase-selection-from-coherence.md`.

**Dimension:** The n=3 octahedral surface is S², while the n=3 route-coherence complex is S¹. They are linked by indexing mixed octahedral facets with intermediate subsets, but are not identical complexes. In general the boundary of the n-dimensional cross-polytope is S^(n−1), while the route complex K_n is S^(n−2). Never silently identify these two topologies.

**Topological quotient:** At n=5, K_5=S³ with complement reflection has quotient RP³, not the Poincaré homology sphere. The latter requires a different finite group action and cannot be derived from a single antipodal involution.

**Ramsey translation:** No map has been proved from generated route/incidence simplices to complementary edge colorings, so this does not compute R(3,7).

**Native source:** The free six-arrow Marici seed retains `AB` versus `AD·DB` as distinct histories. The repository's `SeedFaceObstruction` explicitly rules out the corresponding face in its original free realization. Our conditional adjacent-interchange operation is additional unless a source constructor admitting its comparison is identified.

## 6. New sharp research target

Identify, within Marici's typed source, a **source-admitted adjacent interchange** of two extensions that:

1. preserves distinct histories and correct endpoints;
2. admits reversal and transport under all authorized continuations;
3. produces the square comparisons and the three-operation braid/hexagon coherence, including any retained residue;
4. gives the same local rule at n=4 without assuming it will fill a sphere;
5. fails or reports an obstruction for explicitly dependent operations rather than inventing their permutations.

If such an operation exists natively, the Coxeter/permutohedron construction becomes a candidate generator for route-level G. If it does not, this construction remains a conditional model explaining exactly which extra admission law is needed.

### Reproduction

```
python reproduce.py
```

All tests use Python standard library. Data are saved in `results.json`. A complete finite test is not a new Cubical Agda proof.

### Literature

- Coxeter complex as barycentric subdivision of simplex boundary: https://link.springer.com/article/10.1007/s41468-022-00104-7
- Permutohedron face indexing, facets, and adjacent swaps: https://academic.oup.com/imrn/article/2023/19/16748/7005645
- Permutohedron square/hexagon coherence faces: https://circles.math.ucla.edu/circles/lib/data/Handout-4318-4106.pdf
- Marici source free-realization obstruction: https://github.com/andrey-kokoev/marici/blob/main/research/nima/seed-native-promotion-binding-gate.md
- Marici independent phase-selection control: https://github.com/andrey-kokoev/marici/blob/main/research/nima/phase-selection-from-coherence.md
