# Ramsey degree-six obstruction via independent-neighborhood compatibility

2026-11-09. Exact identities and verified finite witness; universal compatibility conjecture OPEN.

## 1. General port-deficiency identity

Let `G` be triangle-free, `v` a vertex of degree `d`, `S=N_G(v)` its (independent) port set, and `H=G[V\(S ∪ {v})]` the residual graph. For an independent `I⊆V(H)`, write `N_S(I)={s∈S : s has a neighbor in I}`. Define

`δ_S(H)=max_{I independent in H} (|I|-|N_S(I)|)`.

**Theorem (exact):** `α(G)=max(1+α(H), d+δ_S(H))`.

**Proof.** An independent set containing `v` consists of `v` and an independent set of `H`. An independent set not containing `v` comprises an independent `I⊆H` plus an arbitrary subset of `S\N_S(I)`. The largest such set for fixed `I` has `|I|+d-|N_S(I)|` vertices. Taking maxima proves the identity.

Consequently `G` avoids independent `k`-sets iff

`α(H) ≤ k-2` and `δ_S(H) ≤ k-1-d`.

When `d=k-1`, these are the restricted Hall inequalities `|N_S(I)| ≥ |I|` for every independent `I` in `H`. By Hall's theorem, every independent set of `H` is matchable injectively into `S`. This is an inclusion of the graph independence complex into the independent sets of the transversal matroid defined by the S–H bipartite incidence graph. This mathematical reformulation does not by itself give a closed formula for `R(3,k)`.

## 2. Specific six-port reduction

By the earlier 17-vertex exclusion and the known classification of all seven `(3,6;17)` graphs, a hypothetical `(3,7;23)` graph would be 6-regular. Fix a root `v`. Then `|S|=6`, `|H|=16`, `e(H)=33`; each `T_s=N_H(s)` is an independent five-set in `H`. Degree balance reads:

`sum_{s∈S} 1_{T_s}(w)=6-d_H(w)` for every `w∈H`.

Conversely, any triangle-free `H` with `α(H)≤5` and six independent five-sets satisfying the degree-cover equation builds a triangle-free 6-regular graph `G` of order 23. It avoids independent seven-sets **exactly** when all restricted Hall inequalities hold.

## 3. Exact falsifier for low-rank Hall sufficiency

The accompanying `ramsey_port_hall_witness.py` uses a 16-vertex graph `H` with 33 edges, `α(H)=5`, and six independent five-sets that satisfy the degree-cover equations. The resulting 23-vertex `G` is triangle-free, 6-regular, and has `α(G)=8`.

For independent subsets `I⊆H`, the exact numbers of restricted Hall violations are:

| `|I|` | independent `I` | Hall violations |
|---:|---:|---:|
| 1 | 16 | 0 |
| 2 | 87 | 0 |
| 3 | 203 | 0 |
| 4 | 208 | 14 |
| 5 | 76 | 25 |

The first exhibited violation is `I={0,1,2,11}`, whose port neighbors are exactly `{0,1,2}`. It gives the independent seven-set `I ∪ {port_3,port_4,port_5}`. Thus restricted Hall through size three, even combined with residual independence number five, complete six-degree balance, and triangle-freeness, is **not sufficient**.

## 4. Rank-five Hall reduces to pairwise compatibility on neighborhoods

Let `F=I_5(H)`, the family of independent five-subsets of `H`. Define a graph `K(H)` on `F`, joining distinct `T,U` exactly when **no** `I∈F` is disjoint from both `T` and `U`, equivalently `α(H-(T∪U))≤4`.

For any six selected port neighborhoods `T_1,...,T_6`, restricted Hall for all `I∈F` requires every pair of selected neighborhoods to be adjacent in `K(H)`. It also forbids repeating a neighborhood `T` when some `I∈F` is disjoint from `T`. In the exact fixture, every `T∈F` has at least one disjoint `I`; `K(H)` has 76 vertices, 851 edges and clique number four. Hence *the rank-five constraints alone* preclude six ports for that residual graph, without using the degree-cover equations.

This is a natural local-to-global obstruction on the *space of candidate neighborhood sets*, rather than on the original graph edges. It is still a reformulation of constraints, not a new proof of Ramsey thresholds.

## 5. Strong testable conjecture (not established)

For every 16-vertex triangle-free `H` with `α(H)=5`, `e(H)=33`, and `2≤d_H(w)≤5`, the rank-five compatibility graph `K(H)` has no six-clique, and every `T∈I_5(H)` has an independent five-set disjoint from it.

If true, this stronger statement excludes the 6-regular 23-vertex case immediately. The smaller claim that *no six-clique satisfying degree balance exists* would suffice even if the stronger conjecture fails.

McKay's complete `(3,6;16)` catalogue contains 2,576 isomorphism classes (https://users.cecs.anu.edu.au/~bdm/data/ramsey.html). An independently generated sample of ten 33-edge residual graphs had compatibility clique numbers four (six graphs) or five (four graphs). This **is not** a census and is **not** evidence that no other graph has a six-clique. The `ramsey_six_port_catalogue_check.py` verifier takes the full downloadable `r36_16.g6.gz` catalogue as input; its full-catalogue execution was **not** performed in this session because the gzip source could not be retrieved into the execution environment.

The decisive question is therefore no longer about `esd7`: **does pairwise compatibility of maximal independent neighborhoods universally obstruct six-port composition at 16 residual vertices?** The answer must come from a full catalogue run and, ideally, an invariant proof independent of the catalogue.
