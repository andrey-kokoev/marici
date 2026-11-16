# Ramsey one-defect repair: exact local certificate

## Definitions

Let `G` be the RED graph of a red-blue coloring of a complete graph, with
no red triangles, independence number `alpha(G)=k`, and vertex set `V`.
The BLUE maximum cliques are maximum red-independent sets of size `k`.
Let `H={u:degree_G(u)=k}` be the set of saturated red vertices. Every
`N_G(u)` for `u∈H` is a maximum BLUE `K_k`.

An `H`-transversal `U ⊆ H` meets every maximal RED-independent set. It
implies a cover of the independence complex by the complementary induced
subcomplexes `Ind(G[V \ N_G(u)])`, for `u∈U`, and prevents any new vertex
from being attached without a red triangle or a blue `K_{k+1}`.

## The local forcing lemma (proved)

For `C⊂V`, let `S` be a maximal red-independent set disjoint from `C`,
with `w∈S`. If `z∉C` satisfies

    N_G(z) ⊆ N_G(w) ∪ C,

then `z∈S`: independence excludes all of `N_G(w)` from `S`, avoidance
excludes all of `C`, so `z` has no red neighbor in `S`. Maximality forces `z`.

Let `v∈H`, put `C=N_G[v]∩H` and `T=N_G(v)\H`. For every `w∈T`, find
`z_w∈H\C` with `N(z_w)⊆N(w)∪C`. Every maximal independent set meets `C`
or includes some `w∈T`, whence includes `z_w`. Thus

    U = C ∪ {z_w : w∈T}

is an `H`-transversal with `|U|≤ k+1`. This proof uses only adjacency.

## Simplicial fold interpretation (proved)

Let `X=V\C`, `K_C=Ind(G[X])`. The condition is precisely the simplicial
vertex domination criterion: every facet of `K_C` containing `w` also
contains `z_w`. Equivalently `link_{K_C}(w)` is a cone with apex `z_w`.
Deleting `w` is an elementary strong collapse. Since all `z_w` are in
`V\N[v]`, distinct from every deficient neighbor, all of `T` can be
removed in sequence. Consequently the local criterion proves

    Ind(G[V\C])  strong-collapses onto  Ind(G[V\N[v]]) = link_{Ind(G)}(v).

This is a homotopy-level interpretation of local repair. It does NOT imply
a general upper bound for Ramsey numbers or prove repair for all critical
colorings. The strong-collapse interpretation is not needed for the
transversal proof.

## Finite findings

The supplied source `r37_22.g6` contains 191 known critical `R(3,7)` red
graphs on 22 vertices, in catalogue order. They all have `alpha=6`,
checked by the script.

Pure neighborhood-inclusion certificates are found for 190 graphs:

- 146 saturated closed neighborhoods (no repair),
- 39 centers with exactly one deficient neighbor, locally repaired,
- 5 centers with exactly two deficient neighbors, both locally repaired.

Graph 124 has such a certificate after selecting center 10. The remaining
graph, index 57, requires collective reasoning: choose
`U={8,9,11,12,13,15,20}`. In `W=V\U` the four demands `Q={8,11,12,13}`
have available red-neighbor sets

    N(8)∩W = {2,10,19}
    N(11)∩W = {7,14,17}
    N(12)∩W = {1,17,21}
    N(13)∩W = {0,14,16}.

No independent set can hit all four; for each omitted demand an independent
set does hit the remaining three. The verifier checks these facts by at
most 3^4 neighbor selections, rather than enumerating all maximal independent
sets. It follows that `U` is an H-transversal.

The proof therefore certifies all 191 via graph adjacency: 190 with
neighborhood inclusions and one with four-way inconsistency.

## Counterexamples to unrestricted repair conjectures

The 4-vertex path `P4` is triangle-free with `alpha=2`, but a saturated
vertex has one deficient neighbor that no saturated vertex repairs.

Maximal triangle-freeness is **also not sufficient**. A 13-vertex
triangle-free graph has `alpha=5`, `H={0,1,2,4,5,6,7,10}`, and a saturated
vertex 0 with exactly one deficient neighbor 11. It is *maximal*
triangle-free, yet `S={3,8,11,12}` is a maximal independent set disjoint
from all of `H`. Thus no H-transversal exists at any cardinality. Its
adjacency masks are given and fully verified in the code.

That graph has order 13, below the critical `R(3,6)` order 17. The
restrictions on extremal graph order cannot be dropped from the proposed
universal conjecture.

## Reproduce

    python ramsey_one_defect_local_forcing.py

No third-party dependencies. The script verifies triangle-freeness,
independence number, all local inclusion certificates, the exceptional
four-way obstruction, and both counterexamples. It writes
`ramsey_one_defect_local_forcing_witnesses.json` with all explicit vertex maps.

Data: <https://users.cecs.anu.edu.au/~bdm/data/ramsey.html>.
