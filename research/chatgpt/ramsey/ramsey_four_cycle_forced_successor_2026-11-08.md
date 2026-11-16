# A source-selected four-cycle forces bipartite Ramsey completion

8 November 2026. Computational classification for all seven 17-vertex extremal Ramsey(3,6) graphs, with a general implication theorem. The exact standalone checker is `ramsey_forced_sector_successor_2026-11-08.py`.

## Problem

Given an extremal triangle-free graph G on 17 vertices with independence number 5, seek an attachment construction for Ramsey(3,7), using only the current graph's incidence data and not a supplied 22-vertex target. Determine whether the prior `13 → 17 → 22` quarter-turn / `K_{2,3}` pattern extends across all seven graph types.

## Exact first-stage observation

All seven 17-vertex critical graphs have independence number 5 and are unextendable at parameter 6: for every independent S ⊆ V(G), α(G−S)=5. Consequently every independent S is an allowed neighborhood for a *first* new vertex at parameter 7. There are, for the seven graph types respectively, 645, 642, 675, 645, 675, 609, and 615 choices. One-vertex admissibility does not select the successor.

For *two* new vertices with independent old neighborhoods S,T, a red edge between them is possible exactly when S∩T is empty; a blue edge is possible exactly when α(G−(S∪T))≤4. We study the first nontrivial **blue** compatibility, minimizing |S|+|T|. This is a stated selection rule, not a consequence of Ramsey admissibility alone: a disconnected red pair with empty neighborhoods is also allowed.

## Source-selected four-cycle theorem: seven-graph classification

For every one of the seven extremal 17-vertex graphs, the minimum blue-pair neighborhood support is 4. Every minimizing pair has |S|=|T|=2, S∩T=∅, and S∪T is an induced red C4 with S and T its opposite vertex pairs.

Removing that C4 leaves a graph isomorphic to the unique 13-vertex extremal Ramsey(3,5) graph C13(±1,±5). Conversely, these residual-core C4s are exactly all minimum blue-pair neighborhoods.

| Parent 17-vertex graph (McKay order) | All induced C4 | C4 whose deletion gives extremal 13-core | Independent neighborhoods |
|---:|---:|---:|---:|
|1|38|2|645|
|2|37|2|642|
|3|34|1|675|
|4|39|2|645|
|5|33|2|675|
|6|42|2|609|
|7|44|3|615|

The decompositions are source-local and do not require a global order-four automorphism of the parent graph. Six of the seven graphs do not have one.

## Forced neighborhood identity

Fix one qualifying C4, write its opposite pairs as A and B, and let C=G−(A∪B), isomorphic to the unique 13-vertex critical graph. Add two vertices a,b, with a blue edge ab, red neighborhoods A and B in G. Call the resulting 19-vertex graph H. Direct integer-bitset enumeration, on **every one of the 14 qualifying decompositions**, proves

    E_7(H) = { {a,b} ∪ U : U is independent in C },

where E_7(H) is the set of red neighborhoods that permit a one-vertex extension while preserving triangle-freeness and α≤6.

The equality is of the actual families, not merely of cardinalities. In generating-function form,

    sum_{S∈E_7(H)} z^|S| = z² I_C(z)
                              = z² (1+13z+52z²+78z³+39z⁴).

There are exactly 183 eligible neighborhoods, distributed by size 2–6 as `(1,13,52,78,39)`. In particular, **every later vertex must be joined in red to both a and b and to no old vertex of the selected four-cycle**.

### General propagation theorem

Let H be an induced subgraph of any further admissible extension K. For each additional vertex x, the restriction of its red neighborhood to V(H) must lie in E_7(H), because H+x is an induced admissible subgraph of K. Hence each additional vertex is red-adjacent to a,b. Any red edge joining two such vertices would create a red triangle through a. Thus all later vertices form a blue independent set and the red subgraph on `{a,b}` and them is necessarily the complete bipartite graph `K_{2,t}`.

This propagation statement is general; it uses only the established identity E_7(H), not any property of a 22-vertex target. **The K_{2,t} shape is forced *conditional on selecting the initial minimum blue pair*.**

## Complete source-only continuation

Let U_1,...,U_t⊆C be the independent red neighborhoods of the later vertices in the old G. Their mutual blue edges and red edges to a,b are now forced. The enlarged graph has α≤6 exactly when, for every nonempty J⊆{1,...,t},

    |J| + α(G−⋃_{j∈J} U_j) ≤ 6.

Every independent U_j extends to a size-four maximum independent set of C; enlarging any U_j only helps these inequalities. It is therefore sufficient to examine the **39** maximum independent four-sets of C, a source-determined finite family.

Create the compatibility graph on those 39 sets, with edge UV iff α(G−(U∪V))≤4. For all 14 decompositions, the set of three-way compatible triples equals the set of triangles of this graph: every pairwise-compatible triple also satisfies α(G−(U∪V∪W))≤3.

| 17-vertex graph | Valid triple counts for its qualifying C4s | Maximal total graph sizes in this selected family |
|---:|---|---|
|1|4, 4|22, 22|
|2|4, 4|22, 22|
|3|0|21|
|4|0, 0|21, 21|
|5|4, 4|22, 22|
|6|4, 4|22, 22|
|7|4, 4, 0|22, 22, 21|

For each of the ten successful decompositions, the four compatible triples have one common set, and their other entries form two two-element choices: the triple hypergraph is `{c,x_i,y_j}`, i,j∈{0,1}. The four choices form a square. No quadruple has all its triple subfamilies compatible, so no fourth right-side vertex can be added. For each successful triple, the resulting 22-vertex graph is independently verified triangle-free with α=6.

The four unsuccessful decompositions cannot be completed to 22 vertices **after the selected blue pair**, even if later old neighborhoods and their internal edge colors are initially left unrestricted. The forced-neighborhood/forced-bipartite theorem reduces all such continuations to the triple search above. This does **not** prove those 17-vertex graphs lack some other 22-vertex successor through a different initial pair.

## Structural interpretation and limits

The construction produces the sequence

    17 = 13 + 4
      → 19 = 17 + 2   (a minimal blue-compatible pair)
      → 20, 21, [22]  (forced bipartite right-side additions).

The first four-cycle is source-selected by minimum blue-pair incidence support. From that point the internal `K_{2,t}` structure is forced, and the right-side continuation is selected by the compatibility graph. At depth three, its four solutions form a two-by-two grid around one common independent set, consistent with the proposed formation of mutually constrained symmetry sectors.

The remaining, essential selection question is **why use a minimum-cost blue pair at all**, and whether there is a comparable intrinsic selection rule for other values of k. This is a complete conditional generator/classification for the seven 17-vertex critical graphs, not a complete universal generator or formula for R(3,k). The number 22 was not supplied to the continuation search; the maximum 21 or 22 emerges from the compatibility hypergraph.

## Reproduction and source

Run:

    python ramsey_forced_sector_successor_2026-11-08.py

The self-contained checker embeds the seven graph6 records and the unique 13-vertex graph6 record from McKay's public catalogue. It verifies the minimum blue-pair census, every residual core isomorphism, equality of the complete neighborhood families for all 14 cases, the 39-node pair/triple compatibility structure, the two-by-two square decomposition, all 22-vertex witness triangle and independence checks, and the absence of fourfold right-side continuations.

Catalog: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html

## Counterexamples at the next level

A source-dependent construction cannot be promoted to a general formula merely because it produces all successful continuations after a selected four-cycle. We tested the first 20 graphs in McKay's catalog of 191 extremal 22-vertex Ramsey(3,7) graphs. Eighteen have an induced red K_{2,3} whose removal leaves one of the seven extremal 17-vertex Ramsey(3,6) graphs. Two do not. Both are perfectly valid 22-vertex Ramsey graphs (triangle-free, independence number six), so the K_{2,3} predecessor form is **not universal**.

A more intrinsic counterexample test minimizes |S|+|T| for an admissible *blue* pair at the next Ramsey parameter (k=8). Among the 20 catalog graphs, nineteen have minimum support five; one requires six. The most common minimum five-vertex support induces K_{2,3}, but exceptions occur. In particular:

- McKay 22-vertex catalog graph #2 has minimum blue-pair support **6**, and no induced K_{2,3} whose removal is a 17-vertex extremal core.
- McKay 22-vertex catalog graph #9 has minimum blue-pair support **5**, but likewise no induced K_{2,3} whose removal is a 17-vertex extremal core.

The accompanying checker embeds both graph6 records and verifies these claims exhaustively. The other 18/20 figure is a sample test, not a census of all 191. The two explicit counterexamples suffice to falsify universal K_{2,3} decomposition.

Accordingly, the next mathematical unknown is the *selection and branching policy before the minimum pair is fixed*, not another count of higher comparison cells inside the successful branch.
