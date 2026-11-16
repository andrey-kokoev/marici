# Partial-Orbit Successors: The Four-Cycle, Its Pendant Completion, and a Second Forced Five-Vertex Type

Date: 2026-11-08  
Project: Ramsey  
Status: exact finite classifications and explicit counterexample; no general closed-form Ramsey theorem

## Problem

Test whether a rule derived from the internal incidence of an extremal 17-vertex triangle-free graph with independence number five determines its successor at parameter `k=7`. In particular, test whether the previously constructed minimum-cost blue pair and forced `K_{2,3}` completion works across all seven 17-vertex critical graphs **without selecting one globally symmetric predecessor**.

This experiment separates three statements:

1. A low-cost *compatible pair* exists.
2. A low-cost pair *supports three further vertices* in a specified blue-pair continuation.
3. All five-vertex continuations *must* have that form.

Statements 1 and 2 are computed exactly below. Statement 3 is **false**.

## Exact matrix formulation

Represent red edges by the symmetric zero-diagonal binary matrix `A`. The graph is admissible for `R(3,7)` when it is triangle-free and `alpha(G) <= 6`.

For new vertices with red neighborhoods `N_0,...,N_4` in the old graph, and internal red adjacency `F`, the new matrix is

```
A' = [ A   X ]
     [ Xᵀ  F ]
```

where column `i` of `X` indicates the old neighbors of new vertex `i`.

For every independent set `J` of the internal red graph `F`,

```
alpha(A') = max_J ( |J| + alpha(G - union(N_i, i in J)) ).
```

Triangle-freeness requires each `N_i` independent, `F` triangle-free, and `N_i ∩ N_j = empty` whenever `ij` is red in `F`.

All tests are integer/bitset calculations. The example checks independently reconstruct `A'` and compute its exact independence number.

## Stage 1: Source-compatible blue pairs

Let the first two new vertices `a,b` be joined by a **blue** edge, with independent red neighborhoods `S,T` in old graph `G`. The pair is admissible if

```
alpha(G - (S ∪ T)) <= 4.
```

Define the old-neighborhood support cost `c(S,T)=|S|+|T|`. Exhaustive search of all independent `S,T` with `c<=5` yields:

| 17-vertex predecessor | Cost-4 pairs | Cost-5 pairs | Least cost of a pair supporting a K2,3 completion | Number of winning pairs at that cost |
|---:|---:|---:|---:|---:|
| 1 | 2 | 61 | 4 | 2 |
| 2 | 2 | 59 | 4 | 2 |
| 3 | 1 | 45 | **5** | 2 |
| 4 | 2 | 62 | **5** | 2 |
| 5 | 2 | 53 | 4 | 2 |
| 6 | 2 | 69 | 4 | 2 |
| 7 | 3 | 77 | 4 | 2 |

Every cost-4 blue pair consists of opposite two-sets of an induced red `C4`. In graphs 3 and 4, all cost-4 pairs fail to permit three further vertices in this continuation family.

For graphs 3 and 4, exactly **two** cost-5 pairs in each graph support three further vertices. In all four winning cases, the five old vertices in `S∪T` induce **`C4` with one pendant vertex**. Merely having this shape does not suffice: among the 45 cost-5 blue pairs in graph 3, 34 have `C4+leaf` shape and only two succeed; among 62 in graph 4, 46 have that shape and only two succeed.

Thus a *source-support defect of one vertex* repairs the two failing branches. This is a finite observation, not a universal law for all `k`.

## Stage 2: What the pair forces

For every winning pair, let `H=G+{a,b}` with `ab` blue. The complete set of admissible neighborhoods for one more vertex satisfies

```
E_7(H) = { {a,b} ∪ U : U independent in G-(S∪T) }.
```

This is an equality of *sets of neighborhoods*, checked by full enumeration; it is stronger than equality of their cardinalities.

Consequences:

- Every subsequent new vertex must be joined in red to **both** `a` and `b`.
- Two subsequent new vertices cannot be connected in red, as that would create a triangle through `a` or `b`.
- All five new vertices therefore induce `K2,t`, conditional on the chosen starting pair; for a three-vertex continuation, `K2,3` is **forced**.

This forcing applies to all 14 cost-4 candidate pairs and all four *winning* cost-5 pairs tested here. It is **not** true of every cost-5 compatible pair: some admit third neighborhoods excluding one or both members of `a,b`.

## Stage 3: Three-way coherence of residual neighborhoods

Fix one of the winning blue pairs and define `C=G-(S∪T)`. For three subsequent right-side vertices, each red to both `a,b`, choose independent neighborhoods `U_1,U_2,U_3` inside `C`.

The exact conditions on the old graph are

```
alpha(G-(U_i ∪ U_j)) <= 4       for each pair i != j;
alpha(G-(U_1 ∪ U_2 ∪ U_3)) <= 3.
```

It suffices to search **inclusion-maximal** independent sets `U_i` of `C`: any valid `U_i` can be enlarged within `C` without harming the conditions (the residual independence number can only decrease).

For the cost-4 `C4` source case, `|V(C)|=13`, `C` is the unique 13-vertex extremal graph for `R(3,5)`, and the 39 maximal independent sets permit four compatible triples. These form one square of alternative completions.

For each cost-5 `C4+leaf` winning pair in graphs 3 and 4:

```
|V(C)| = 12;
I_C(z) = 1 + 12z + 45z² + 64z³ + 30z⁴;
number of inclusion-maximal independent sets = 30;
compatible pairs among these 30 sets = 69;
triangles in this pairwise compatibility graph = 2;
fully Ramsey-compatible triples among those triangles = 1.
```

For all 152 independent subsets of `C` (not just maximal ones), the pairwise compatibility graph has 307 edges. Thus the more selective count 69 above refers specifically to the 30 maximal independent sets.

The two successful residual-carrier types are distinct: a 13-point residual carrier with **four** compatible triples, and a 12-point residual carrier with **one** compatible triple.

Every winning pair in the table generates an explicit 22-vertex triangle-free graph with independence number six. This verifies a lower-bound witness from **each of the seven predecessors**. It does not prove the upper Ramsey bound.

## Stage 4: Unrestricted five-vertex shape disproves universality

The preceding search restricts attention to a blue starting pair and later `K2,t` continuations. To test whether `K2,3` is universal, an independent mixed-integer search allowed **all remaining three neighborhoods and all other internal red/blue edges to vary**. It found a different valid five-vertex internal graph in predecessor 1.

Use graph 1 of the seven `G17_G6` records in the companion checker. Five old neighborhoods are:

```
N0 = {2,4,6,9}
N1 = {12}
N2 = {1,2,3,5,14}
N3 = {1,8,10,15}
N4 = {7,11,13}
```

Of all `2^10=1024` internal red/blue assignments, **exactly one** is triangle-free and has `alpha <= 6`:

```
red internal edges:
(0,3), (0,4), (1,2), (1,3), (1,4).
```

Its degree sequence is `(1,2,2,2,3)`: a red **`C4` with one pendant vertex**, *not* `K2,3` (which has six red edges and degree sequence `(2,2,2,3,3)`). The old five-vertex support `N0∪N1` induces the red **star `K1,4`**. The new full graph has 22 vertices, 63 red edges, no red triangles, and exact independence number 6.

The 1024-pattern classification and independent 22-vertex graph verification appear in the companion script; no optimizer is needed to recheck the resulting counterexample.

This **disproves** the conjecture that every low-cost five-vertex successor is a forced `K2,3`, even when the preceding graph is one of the seven extremal 17-vertex graphs.

## Scope and interpretation

Established in this finite search:

- All seven 17-vertex critical Ramsey graphs admit a five-vertex extension to a valid 22-vertex `R(3,7)` lower-bound witness.
- The restricted cheapest **completable** blue pair has cost four for five graphs and cost five for two graphs.
- The cost-five repair shape in the two failing branches is `C4+leaf` on the **old support**.
- For the selected winning blue pairs, the complete frontier forces `K2,3` among the five new vertices.
- Another valid successor has `C4+leaf` among the **new vertices**; thus the internal shape is not universal.

Not established:

- An attachment-size selection law. The search **asked for three vertices beyond the initial blue pair**, so the five-vertex successor size was supplied as the test horizon.
- A universal `k -> k+1` successor, especially for high `k`.
- A characterization of *all* 22-vertex extensions of each predecessor or of all 22-vertex extremal graphs.
- An extremality upper-bound proof, or a closed formula for `R(3,k)`.

## Productive conjecture

The source-level selection rule should retain the **entire pair-extension frontier**, not only the cheapest pair or a prescribed `K2,3` target. The five-point source carriers `C4+leaf` and `K1,4` are explicit competing completions of an insufficient four-point carrier. Their possible common origin would be a source-determined transformation between local red-neighborhood incidence and internal five-vertex adjacency.

The next discriminating test is to derive the *attachment-support transformation* from the zero pattern of the old adjacency matrix. Its output should predict whether the next internal sector is `K2,3`, `C4+leaf`, or another structure before evaluating the complete graph. Do not infer a universal generator from these finitely many 22-vertex witnesses.

## Reproduction

```
python ramsey_partial_orbit_successor_audit.py
```

Requires NetworkX; uses exact bitset independent-set dynamic programming and independently checked maximum independent sets. The companion program embeds the seven input graph6 strings, enumerates compatible pairs, constructs the two restricted source-support types, checks all resulting 22-vertex graphs, and verifies the unrestricted-shape counterexample by all 1024 internal assignments.

Historical comparison/checker: `ramsey_forced_sector_successor_2026-11-08.py`. Full shape-free mixed-integer discovery of the counterexample was independently replayed using SciPy MILP; the final certificate does not depend on the optimization software.
