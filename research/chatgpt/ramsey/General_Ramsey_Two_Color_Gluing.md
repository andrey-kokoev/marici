# Two-color incidence gluing for arbitrary R(r,s)

## Scope

The rooted neighborhood construction used for R(3,t) generalizes exactly to all two-color clique Ramsey problems R(r,s). The substantive change is that the root's red neighborhood is no longer independent: its internal red and white graphs must both be retained. This is a standard neighborhood-gluing construction, not a new Ramsey theorem or a new threshold formula.

The accompanying script verifies the identities and threshold criterion, checks a 17-vertex R(4,4) lower-bound witness, and retains two negative controls. It does not perform an exhaustive general Ramsey-graph generation, a new R(4,5) computation, or proof-assistant verification.

## 1. Rooted data

Let G be the red graph. White pairs are its nonedges. Fix a vertex v and define the induced graphs

- B = G[N_G(v)], the red neighborhood;
- H = G[V(G) minus (N_G(v) union {v})], the white neighborhood.

For each b in B retain the attachment S_b = N_G(b) intersect V(H). Reconstruct G from B, H and the S_b by making v red-adjacent to every vertex of B, white-adjacent to every vertex of H, and b red-adjacent to exactly S_b inside H. The reconstruction is exact with vertex labels retained.

Write omega(X) for the largest red clique in X and alpha(X) for the largest white clique (independent set). Both values are zero on the empty graph. Allow the empty set as both a clique and an independent set.

For C subset B, set

    H_R(C) = H[ intersection over b in C of S_b ],
    H_W(C) = H - union over b in C of S_b.

The empty intersection is V(H), and the empty union is empty.

## 2. Two exact identities

For every finite simple graph G, not only Ramsey graphs,

    omega(G) = max( 1 + omega(B),
                    max over red cliques C in B of [ |C| + omega(H_R(C)) ] ).

    alpha(G) = max( 1 + alpha(H),
                    max over white cliques J in B of [ |J| + alpha(H_W(J)) ] ).

Proof of the first identity: a red clique containing v lies in {v} union B. A red clique not containing v splits into its red clique C in B and a red clique in H that is adjacent to every member of C. The latter lies precisely in H_R(C). Conversely, every such choice gives a red clique, so both maxima are attained. The white proof is identical with common nonneighbors in place of common neighbors; a white clique containing v lies in {v} union H.

No symmetry, group action, averaging, regularity, or preferred cyclic ordering is assumed.

## 3. Necessary and sufficient gluing criterion

Fix r,s >= 2. Then G avoids both a red r-clique and a white s-clique if and only if all the following hold:

1. B avoids a red (r-1)-clique and a white s-clique.
2. H avoids a red r-clique and a white (s-1)-clique.
3. For every nonempty red clique C in B,

       |C| + omega(H_R(C)) <= r-1.

4. For every nonempty white clique J in B,

       |J| + alpha(H_W(J)) <= s-1.

The proof is the pair of identities above. Equivalently, conditions 3 and 4 forbid a red (r-|C|)-clique or a white (s-|J|)-clique in the respective common-neighbor graph.

Keeping every clique witness is sufficient; keeping just attachment cardinalities is not. There is no assertion that singleton or pairwise checks are sufficient at every threshold.

The operations obey

    H_R(C union D) = H_R(C) intersect H_R(D),
    H_W(C union D) = H_W(C) intersect H_W(D),

where intersection means induced intersection of vertex sets. The definition is independent of r and s. The thresholds only change the maximum permitted total clique size.

## 4. Recovery of the R(3,t) rule

For r=3, B must avoid a red 2-clique, so B is independent. Every subset of B is consequently a white clique, and its only nonempty red cliques are singletons.

Condition 3 becomes omega(H[S_b]) <= 1: each S_b is independent. Condition 4 becomes

    |J| + alpha(H - union over b in J of S_b) <= t-1

for every subset J of B. This is exactly the attachment law used by the earlier R(3,7) construction.

Thus the previous method is a specialization, not a different mechanism.

## 5. Complete finite recursive construction

Let Rcal(r,s;n) denote the class of n-vertex graphs avoiding the two specified cliques. For every d=0,...,n-1, enumerate

    B in Rcal(r-1,s;d),
    H in Rcal(r,s-1;n-1-d),

then enumerate the possible cross-edge attachment records and retain exactly those satisfying Section 3. Add v as specified in Section 1. Every avoiding graph appears by choosing any vertex as v. Conversely, every accepted assembly is avoiding. Relabeling duplicates may be removed only with justified isomorphisms.

The trivial bases r=2 and s=2 are edgeless and complete graphs of the permitted orders. The parameter sum r+s decreases in each class-generation recursion. This yields an exact finite procedure, not an efficiency guarantee or a closed expression for the threshold.

## 6. Degree identities must also be generalized

The old triangle-free deficiency identity cannot be copied unchanged. For an arbitrary graph with n vertices, m red edges, degrees d_v and tau red triangles,

    e(H_v) = m - sum over u in N(v) of d_u + e(B_v),

    sum_v e(H_v) = n*m - sum_v d_v^2 + 3*tau.

The neighborhood degree sum counts edges internal to B_v twice, whereas removing N[v] should remove them once. Adding e(B_v) corrects the count. Each red triangle contributes once to e(B_v) at each of its three vertices. When tau=0 these reduce to the previously used identities.

## 7. R(4,4) test

Construct the graph on Z/17Z whose red differences are

    {1,2,4,8,9,13,15,16} = {+/-1,+/-2,+/-4,+/-8} modulo17.

The script constructs this graph directly. Exact results:

- 17 vertices, 68 red edges, all red degrees eight;
- maximum red clique three, maximum white clique three;
- 68 red triangles;
- zero red four-cliques and zero white four-cliques, checked directly on all 2,380 four-subsets;
- both general identities and all gluing inequalities pass at each of 17 roots.

At every root B and H each have eight vertices; B has twelve red edges and H has sixteen. No local graph is replaced by an independent set.

For the upper bound, the already established R(3,4)=R(4,3)=9 implies |B|<=8 and |H|<=8 in any (4,4)-avoiding graph. Hence n<=17. Combined with the verified construction this gives the known R(4,4)=18. This upper bound is the elementary Ramsey recurrence, not a new higher-overlap obstruction.

## 8. Negative controls

### Red-pair compatibility is necessary

Use five vertices with root0, B={1,2}, H={3,4}. Make 0-1 and0-2 red and make every edge among1,2,3,4 red. The two local subgraphs satisfy their (3,4) and (4,3) requirements. Every singleton attachment condition passes. However S_1=S_2={3,4}, and their common red neighborhood contains the red edge3-4. The red pair1-2 therefore completes the forbidden red four-clique1,2,3,4. The general red-pair check rejects it.

### Pairwise checks do not suffice in general

Use five vertices with root0, B={1,2,3}, H={4}. The only red edges are0-1,0-2,0-3, so all S_i are empty. Local subgraphs and all red/white attachment checks involving at most two B vertices pass. But the white triple1,2,3 has the common white neighbor4, giving a white four-clique. The triple check rejects it.

These are direct counterexamples to restricted checks, not a claim that both failures occur in every degree-restricted extremal class.

## 9. Executed verification

Command:

    python verify_general_ramsey_gluing.py --atlas --output general_gluing_receipt.json

Actual checks:

- 1,099 labeled nonempty graphs through five vertices;
- 5,405 rooted choices and 86,480 tests of the iff criterion for r,s in{2,3,4,5};
- all 1,253 graphs in the NetworkX atlas through seven vertices, with 8,475 rooted identity checks;
- corrected degree identities on every tested graph;
- the Paley17 construction and all 17 rooted tests;
- both negative controls.

All passed. The written decomposition proves the identities for arbitrary finite graphs; these finite tests check the implementation, not the universal theorem by sampling. The receipt binds the script hash. The standard-library tests require no external package; only --atlas requires NetworkX.

## 10. Attribution and next discrimination

Neighborhood splitting and gluing already apply beyond triangle-free graphs. A formal proof of R(4,5)=25 in HOL4 uses a splitting vertex, complete coverage of the two neighborhood classes, and certified unsatisfiable gluing problems. This is direct evidence that the mechanism extends beyond3, not merely a conjectured analogy.

R(4,4) validates the implementation but its upper bound already follows from the basic recurrence. R(4,5) is a stronger next test for retained-incidence pruning, with established computational and formal proofs available for comparison.

Sources:

- Thibault Gauthier and Chad E. Brown, A Formal Proof of R(4,5)=25 (2024), especially Sections3 and5: https://arxiv.org/html/2404.01761v1
- Brendan McKay, Ramsey Graphs, catalogues of (4,4) and (4,5) graphs: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
- Prior generated note, R37_Automated_Incidence_Proof.md, Section1, for the exact triangle-free specialization.
