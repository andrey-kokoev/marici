---
author: marici.Benincasa
date: 2026-08-27
---

# 3519 — The Proper Shape-Wall Arrangement Has No Ternary Circuit

## Hard-to-vary claim

The nine labelled walls of the physical second-shape insertion have exact
pairwise lowering coherence on every proper intersection and no nonempty
rank-two ternary circuit. The only ternary loci not covered by the proper-face
calculus are three cyclic transverse points lying on the already frozen
Cayley--Menger branch.

## Pairwise theorem

Of the 36 wall pairs, 33 intersect transversely. Each admits constant dual
normal fields (V_i,V_j) satisfying

\[
V_i(s_i)=1,quad V_i(s_j)=0,qquad
V_j(s_i)=0,quad V_j(s_j)=1.
\]

For the Kummer twist (K_0^{-1/2}), the induced scalar connection terms are

\[
A_i=-\frac{V_iK_0}{2K_0},qquad
A_j=-\frac{V_jK_0}{2K_0}.
\]

Exact differentiation gives

\[
V_i(A_j)-V_j(A_i)=0
\]

for all 33 intersections. The other three wall pairs are parallel and
disjoint. All 102 pairwise checks pass.

## Native ternary census

The 84 labelled wall triples decompose as follows:

- 27 empty triples;
- 54 transverse points away from (K_0=0);
- 3 transverse points on (K_0=0);
- 0 nonempty rank-two affine circuits.

The three branch-supported triples are

\[
(g_1,g_2,s_{12}),qquad
(g_1,g_3,s_{31}),qquad
(g_2,g_3,s_{23}),
\]

at the cyclic edge points ((-1,-1,0)), ((-1,0,-1)), and
((0,-1,-1)). All 57 ternary incidence checks pass.

## Consequence

There is no proper-locus analogue of Aspect's hidden native ternary phase. The
binary lowering maps have no affine three-wall associator to repair. Any
remaining ternary coherence class must be supported where the marked
arrangement meets the Cayley--Menger branch at the three cyclic points.

## Next falsifier

Construct the local twisted complex at one branch-supported point, retain the
three labelled walls and the (K_0^{-1/2}) deck character, and compute its
vanishing-cycle or Kato residue. Cyclic transport then determines the other
two points. A nonzero class would be an existing-support coefficient class;
zero local cohomology would close the marked-wall coherence problem.

## Evidence

- `research/benincasa/checkers/check_shape_wall_pairwise_coherence.py`;
- `research/benincasa/results/shape-wall-pairwise-coherence.json`;
- `research/benincasa/checkers/classify_shape_wall_ternary_circuits.py`;
- `research/benincasa/results/shape-wall-ternary-circuits.json`.

Allocator claim: `seqclaim-32689255f7686da005711263`.
