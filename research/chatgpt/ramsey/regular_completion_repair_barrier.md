# A repair barrier in the 39-to-40 Ramsey transition

Date: 2026-11-09

## Result

An exact finite calculation excludes every 9-regular, triangle-free, 40-vertex Ramsey candidate obtainable from Exoo's published 39-vertex witness by deleting at most three of its original edges and adding arbitrary other edges. The original 39 vertices are retained, and the fortieth vertex is new. The calculation does not freeze a 35-vertex core, impose cyclic symmetry, or prescribe the new neighborhood.

Equivalently, under any identification of Exoo's 39 vertices with the vertices of G-v, a valid 9-regular (3,10;40) graph G would have to omit at least four of Exoo's 167 original edges. Since G-v has 171 edges, at least eight other old-to-old edges must then be inserted. Thus at least twelve of the pairs among those 39 vertices must change.

This is a local repair-distance result relative to one explicitly specified witness. It is not a nonexistence theorem for all regular 40-vertex graphs, is not a claim of novelty relative to the large published censuses, and says nothing decisive about nonregular 40-vertex graphs. No graph proving R(3,10)=41 was found.

## 1. The starting graph is an actual published witness

The input is Geoffrey Exoo's two-colour adjacency matrix at:

https://cs.indstate.edu/ge/RAMSEY/r3.10.39

Its zero entries off the diagonal give the sparse, triangle-free colour. The raw matrix is retained as `exoo_r310_39_matrix.txt`; its SHA-256 is:

`0efc627f51a2f230972e7abb8b23ab23d47ec81e0bf4cb8c7a5c47532707a6fb`.

The independent Python verifier checks symmetry, the diagonal, triangle avoidance, absence of independent 10-sets, and the following exact properties:

- 39 vertices and 167 edges;
- degree distribution: one vertex of degree 6, fourteen of degree 8, twenty-four of degree 9;
- 4,511 independent 9-sets.

The degree-six vertex is 35 in the retained zero-based labeling. Thus this witness does not already have the degree sequence required by deletion from a 9-regular graph on 40 vertices.

The published 43,146,537-graph partial census was not downloaded or searched. Angeltveit already used deletion and one-point re-extension to enlarge that census; the work here is not presented as the first proposal of such a method.

## 2. Exact regular-completion criterion

For a simple graph H on 39 vertices, define its degree-defect set

    S = {x : d_H(x)=8}.

There exists a 9-regular (3,10;40) graph whose deletion of its distinguished vertex is H if and only if all of the following hold:

1. H is triangle-free and has no independent 10-set.
2. Its degree sequence is nine eights and thirty nines.
3. S is independent.
4. H-S has no independent 9-set.

Proof. In a 9-regular graph, deleting a vertex lowers the degrees of exactly its nine neighbors. Its neighborhood is independent because the graph is triangle-free. An independent 10-set containing the deleted vertex corresponds exactly to an independent 9-set in H-S. Conversely, add a vertex adjacent precisely to S. These conditions give degree nine everywhere, exclude every triangle, and exclude independent 10-sets both containing and avoiding the new vertex.

This criterion does not assume that every (3,10;40) graph is regular. It is exact only for the regular branch.

## 3. Exhaustive repair construction

Write Q for the input graph and r for the number of original Q-edges that will be absent from H. Since |E(Q)|=167 and |E(H)|=171, precisely r+4 pairs not originally edges of Q must be added among the old vertices.

For each subset D of r original edges, form Q-D. Candidate additions are all original nonedges uv such that both endpoints currently have degree below nine and u,v have no common neighbor in Q-D. No other pair can be added in a triangle-free supergraph of Q-D with maximum degree nine.

Enumerate every subset of r+4 candidate additions, in a fixed increasing order. During the enumeration reject only:

- an edge that would raise an endpoint's degree above nine;
- an edge that would complete a triangle;
- an inability to raise all old degrees to at least eight using the remaining additions.

These rejections are monotone or necessary degree bounds. They do not exclude any completion under the stated deletion limit. At a leaf, check the degree sequence, independence of the now-determined set S, and the Ramsey conditions.

Original edges in D are not reinserted. A graph in which one of them were reinserted belongs to an earlier, smaller deletion radius and has already been covered. This keeps the exact-radius enumeration unambiguous.

## 4. Complete integer results

All entries below are labeled counts, not numbers of isomorphism classes.

| Original edges deleted | Deletion sets covered | Triangle-free H with target degrees | H with independent S | Those also avoiding independent 10-sets |
|---:|---:|---:|---:|---:|
| 0 | 1 | 33 | 0 | 0 |
| 1 | 167 | 4,035 | 0 | 0 |
| 2 | 13,861 | 286,790 | 65 | 0 |
| 3 | 762,355 | 15,544,413 | 5,146 | 0 |
| Total | 776,384 | 15,835,271 | 5,211 | 0 |

For the first two radii, independence of S already fails. At radii two and three, every one of the 5,211 candidates passing that condition already has an independent 10-set inside H. These are explicit certificates, not solver timeout inferences. Consequently the last condition, alpha(H-S)<=8, is not even reached in this family.

Each surviving candidate is recorded by its removed edges, inserted edges, and an independent 10-set in `radius2_rejections.jsonl` or `radius3_rejections.jsonl`. The separate Python verifier reconstructs each graph and checks its degree sequence, triangle-freeness, independent defect set, and displayed independent 10-set. It also rejects duplicate records and checks the recorded totals.

The exhaustive coverage argument is the one in Section 3, implemented in `exact_repair.cpp`. The separate certificate verifier checks the individual rejections, not an independently formalized completeness proof for the C++ enumeration. No Agda, Lean, SAT/DRAT or other proof-assistant certificate was generated.

## 5. An exact rule for which single-edge replacements are possible

The search suggests a useful general diagnostic, independent of any selected metric or geometric interpretation.

Let H have no independent k-set and let e=uv be an edge. Define

    W_e(H) = {I subset V(H) : |I|=k and E(H[I])={e}}.

These are exactly the independent k-sets created by deleting e. If f is a nonedge of H, then

    alpha(H-e+f) < k
        iff f is contained in every I in W_e(H).

When W_e is nonempty, the condition is equivalently

    endpoints(f) subset intersection_{I in W_e(H)} I.

Proof. Any independent k-set of H-e must have used e as its only original edge; adding f destroys it exactly when both endpoints of f lie in it. Conversely, adding an edge cannot create an independent set. Triangle-freeness and degree conditions on H-e+f must still be checked separately.

If that intersection is exactly {u,v}, then no different single edge f can compensate for deleting e. This gives a small, checkable obstruction to a one-edge replacement. It does not prohibit a coordinated replacement involving multiple deleted and inserted edges.

For Q, 160 of its 167 edges are individually critical for independent-ten avoidance. For 41 edges, explicit witness families have intersection exactly the endpoints of the edge. `locked_edge_certificates.json` retains such small families. The independent verifier checks that every witness contains exactly one Q-edge and that its family's intersection is precisely that edge. Hence the 41 single-replacement barriers do not depend on trusting a computed independence number or a numerical optimization status.

The relation above is elementary. Its value here is operational: it states precisely what an allowed repair must accomplish, rather than guessing a symmetry or a coherence rule.

## 6. Constructive searches outside the certified family

The exact result is not the only work performed. Several bounded searches allowed more general changes.

### Ramsey-valid 39-vertex walks

Starting from a 171-edge supergraph of Q, use two types of moves:

- two-edge switches, preserving every degree;
- a deficit transfer: replace uv by uw when v has degree nine and w has degree eight, preserving the degree multiset while replacing w by v in S.

Every accepted graph is checked for triangle-freeness and independent-ten avoidance. Two-edge switches alone cannot change S, which is why deficit transfers are necessary for this approach.

The initial best simple augmentation had two edges inside S and 286 independent 9-sets in H-S. A completed bounded walk found another valid 39-vertex graph with the same target degree sequence, still two edges inside S, and 240 independent 9-sets in H-S. It differs from Q by three original-edge deletions. It is not extendible by the required ninth-degree vertex. The exact repair result explains why repairing S cannot succeed anywhere within that deletion radius.

### Unrestricted regular 40-vertex switches

A separate search allowed every edge of the 40-vertex graph to change while keeping the graph triangle-free and 9-regular. It used both ordinary switches and coordinated repairs aimed at common-neighbor blockers. No 35-vertex core was frozen. The 70-independent-ten baseline from the earlier construction was not improved. A second run from an integer-model candidate reduced 440 independent 10-sets to 180, still worse than that baseline.

These are bounded heuristic outcomes, not lower bounds on what unrestricted switching can attain.

### Integer search beyond the repair barrier

An incremental mixed-integer model uses all 780 pair variables, degree-nine equations, all triangle exclusions, and dynamically added independent-ten clauses. It may delete or add any old edge. For the Exoo-started run, the verified repair barrier was incorporated as the valid inequality that at most 163 of Q's original 167 edges may remain.

The starting cut family comprises all 4,511 known independent 9-sets of Q, each joined to the proposed fortieth vertex. Returned integer candidates are independently checked and their newly discovered independent 10-sets added as clauses. Two returned 40-vertex candidates were triangle-free and 9-regular but contained 1,120 and 890 independent 10-sets. A later timed solve returned no candidate. None is a Ramsey witness, and no MIP time limit is treated as infeasibility.

`cut_search.py` is a discovery program using the HiGHS bindings bundled with SciPy 1.17. Its numerical optimizer is not used in the exact repair certificate.

## 7. What is established, and what is not

The construction target remains one triangle-free 40-vertex graph with independence number nine. The literature upper bound of 41 would turn such a graph into a proof that R(3,10)=41.

This run establishes an explicit repair barrier around one known witness and a general exact edge-replacement test. It does not show that every 39-vertex Ramsey graph has the same barrier, that no regular 40-vertex graph exists, or that nonregular graphs can be discarded. A different 39-vertex source could have different repair behavior.

Any continuation of this particular seed search must permit at least four coordinated original-edge deletions, or move to a substantially different starting graph. The barrier identifies a restriction to remove; it does not select the correct next construction or imply that a construction exists.

## Reproduction

From this directory:

```sh
c++ -O3 -std=c++17 exact_repair.cpp -o exact_repair
./exact_repair exoo39.adj 0 radius0
./exact_repair exoo39.adj 1 radius1
./exact_repair exoo39.adj 2 radius2
./exact_repair exoo39.adj 3 radius3
python verify_transition.py
```

The exact search and final verifier require only a C++17 compiler and standard-library Python. The supplied JSON receipts record `complete: true`; an optional time limit on the search produces `complete: false` if it interrupts enumeration and must not be used as an exhaustive certificate.

## Primary sources

Geoffrey Exoo, published Ramsey adjacency matrix, https://cs.indstate.edu/ge/RAMSEY/r3.10.39 . The precise matrix, rather than an undocumented database sample, is retained in the bundle.

Vigleik Angeltveit, *R(3,10) <= 41*, Electronic Journal of Combinatorics 32(4) (2025), P4.30; https://arxiv.org/html/2401.00392v2 . Section 7 describes the large partial census and the unresolved regular branch. Its graph files were not searched here.

Geoffrey Exoo, *On Some Small Classical Ramsey Numbers*, Electronic Journal of Combinatorics 20(1) (2013), P68; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i1p68/pdf . It already reports near-solutions with one triangle and describes local search with varying forbidden-subgraph weights. No claim of inventing that strategy is made here.
