# A 35-vertex Ramsey core and its possible eighth pentagon

**Date:** 2026-11-09  
**Objective:** Find a 40-vertex triangle-free graph with independence number at most nine, thereby proving \(R(3,10)=41\).  
**Status:** Exact finite structural reduction and an exhaustive transversal certificate. **No 40-vertex graph has been found, and this extension family has not been excluded.**

## 1. Core and unrestricted five-vertex attachments

Let \(H\) be the 35-vertex circulant graph on \(\mathbb Z_{35}\) with edges at differences \(\pm1,\pm7,\pm11,\pm16\). This is the unique 35-vertex \((3,9)\) Ramsey graph (published classification). It is 8-regular, triangle-free and has independence number eight.

Look for a triangle-free 40-vertex graph \(G\) containing this **fixed induced** copy of \(H\) with \(\alpha(G)\le 9\). Let \(F\) denote the five new vertices, and \(S_i\subseteq V(H)\) the old neighbors of new vertex \(i\).

Every old vertex has degree eight, and every vertex of \(G\) must have degree at most nine because its neighbors form an independent set. Consequently **the five sets \(S_i\) are pairwise disjoint**. They must each be independent in \(H\), and have size at most seven once the new five vertices form a pentagon.

## 2. Why the new five vertices must form \(C_5\)

Enumerate all maximal independent sets of \(H\): there are 3,360 of size eight and five of size seven. For maximal independent sets \(M,N\), declare them compatible when every independent 8-set \(I\) meets \(M\cup N\). The resulting graph has **3,365 vertices, 191,100 edges, and no triangles**; no vertex is compatible with itself. These counts were regenerated directly from the explicit 35-vertex adjacency rule.

If three new vertices were mutually nonadjacent, their three independent attachment sets would satisfy the pairwise hitting condition. Extending these sets to maximal independent sets would give a triangle (allowing repeated vertices would require a self-compatible maximal set). Contradiction. Hence the graph induced by the five new vertices has no independent triple. It also has no triangle. The only five-vertex graph with both properties is \(C_5\).

This is a conditional theorem for extensions **containing the specified 35-core**. It is not a classification of all 40-vertex potential Ramsey graphs.

## 3. Exact joint extension problem

Index the new pentagon by \(0,1,2,3,4\), with edges \(i\sim i+1\pmod5\). The entire extension exists exactly when one can choose \(S_0,\ldots,S_4\subseteq \mathbb Z_{35}\) satisfying:

- each \(S_i\) is independent in \(H\);
- sets are pairwise disjoint;
- \(3\le |S_i|\le7\) (the lower bound three uses the known exclusion of degree-four vertices, or the induced 35-vertex residual argument);
- for each of the five nonadjacent pentagon pairs \((i,j)\), every independent 8-set of \(H\) meets \(S_i\cup S_j\).

The condition is necessary and sufficient: independent 10-sets in \(G\) must contain two nonadjacent new vertices and eight old vertices, since \(\alpha(H)=8\) and \(\alpha(C_5)=2\).

Put Boolean variable \(x_{v,i}=1\) when old vertex \(v\) connects to new vertex \(i\). The formulation uses **175 Boolean variables**, 35 disjointness constraints, 700 triangle-freeness constraints, five new-degree constraints, and **16,800 independent-eight hitting constraints**. One symmetry break \(x_{0,0}=1\) is valid because \(H\) and \(C_5\) are vertex-transitive and some attachment is mandatory.

## 4. New exact transversal bound

Let \(\mathcal I_8(H)\) denote the 3,360 independent 8-sets. Define the transversal number

\[
\tau_8(H)=\min\{|T|:T\cap I\ne\varnothing\ \text{for every }I\in\mathcal I_8(H)\}.
\]

**Exact result:** \(\tau_8(H)=9\).

An independent, standard-library C++ verifier enumerated every independent 8-set, then examined **all \(\binom{34}{7}=5,379,616\) eight-subsets containing vertex 0**. None intersects all independent 8-sets. Every eight-subset of \(H\) can be rotated to contain vertex 0, so this excludes all size-eight transversals and, consequently, all smaller ones. The program also verifies that

\[
T=\{0,2,6,7,11,18,19,25,26\}
\]

meets every independent eight-set. The script outputs both bounds and exits nonzero if either fails.

For every new pentagon nonedge \((i,j)\), \(|S_i|+|S_j|=|S_i\cup S_j|\ge9\). Summing the five inequalities gives \(2\sum_i|S_i|\ge45\), so \(\sum_i|S_i|\ge23\).

**Any 40-vertex counterexample containing this 35-core has at least \(140+5+23=168\) red edges.** A 9-regular construction would have 180 edges and \(|S_i|=7\) for all five new vertices.

The bound nine is tight for one individually compatible pair under the additional independence requirements. For example,

\[
S_0=\{0,4,9,12,21,27,29\},\qquad S_2=\{5,28\}
\]

are disjoint independent sets whose union meets all 3,360 independent 8-sets. This does not extend to five mutually compatible attachments.

## 5. Why the compatibility-graph shortcut does not solve it

The maximal-independent-set compatibility graph is triangle-free but **contains 5-cycles**. One explicit 5-cycle has maximal-independent sets

```
[0,5,10,13,22,25,27,30]
[6,9,11,14,19,24,29,32]
[2,8,10,16,20,25,28,33]
[0,9,12,17,22,27,30,32]
[1,3,7,11,16,24,28,34]
```

The ordered neighboring pairs cover all independent 8-sets. But these maximal sets intersect each other; the actual old-to-new attachment sets must be pairwise disjoint. Hence the compatibility 5-cycle is necessary evidence of pairwise consistency, **not a 40-vertex witness**.

## 6. Constructive search so far

The complete linear relaxation is feasible. A full integer model was attempted but not resolved within the allotted run. A smaller iterative integer search with independent-set cuts completed four rounds, assigning between 32 and 35 old vertices in the best returned candidates; every candidate retained forbidden independent 10-sets, and the fifth round reached the solver time limit without a solution. This is *not* an UNSAT certificate.

In the 9-regular subfamily, all 120 relabelings of the residue-class partition were checked. Their numbers of forbidden independent 10-sets range over \(70,294,406,630\), so none is valid. A balanced Kempe-swap heuristic searched asymmetric proper 5-colorings but did not improve the best score of 70 in the recorded run. That is a bounded heuristic, not a proof that 70 is optimal.

A candidate checker builds the 40-vertex graph from any 35-character assignment, tests all triangles, and checks all five ways to extend an old independent eight-set to a forbidden independent ten-set. A zero-violation candidate would immediately provide a reproducible graph6 witness proving \(R(3,10)=41\).

## 7. Research conclusion

The earlier seven-pentagon structure leads to an **exact, symmetry-free five-way incidence problem**. We proved that the eighth pentagon is forced within the induced-core model, that its five attachment sets are disjoint, and that each of its nonadjacent pairs must cover all maximal independent eight-sets. The new exact transversal invariant provides a 23-edge cross-incidence lower bound.

We did **not** prove or disprove the existence of the full five-way assembly. This restriction may be too severe: a 40-vertex Ramsey graph, if it exists, need not contain the unique 35-vertex extremal graph. The 39-vertex Exoo witness was not available as an adjacency record in this audit, so we did not verify whether it contains this core.

The next high-value action is a certifying integer/SAT search of the full 175-variable extension problem, and independently a structural deformation/search beginning with known 39-vertex witnesses. In neither case should the target be presumed to exist.

## Reproduction

```
python verify_core_compatibility.py
c++ -O3 -std=c++17 transversal_exact.cpp -o transversal_exact
./transversal_exact
python verify_candidate_40.py 14203142031420314203142031420314203
```

The last command deliberately checks a triangle-free, 9-regular near-candidate and reports its 70 forbidden independent 10-sets.

Optional exploratory scripts (`analyze.py`, `lazy_joint_search.py`, `regular35_plus5.py`, `kempe_search.cpp`) are not proof certificates for nonexistence.

### Sources

- Goedgebeur and Radziszowski, *New Computational Upper Bounds for Ramsey Numbers R(3,k)*, Electronic Journal of Combinatorics 20(1), P30 (2013). https://doi.org/10.37236/2824
- Angeltveit, *R(3,10) <= 41*, EJC 32(4) (2025), P4.30. https://doi.org/10.37236/12936
- Prior project investigation: `ramsey_310_progress_note.md`, especially its degree-four exclusion and 35-core compatibility graph.
