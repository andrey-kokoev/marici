# Six-port obstruction for R(3,7): complete catalogue verification

Date: 2026-11-09  
Status: **complete computer-assisted certificate for the known equality R(3,7)=23, conditional on the established completeness of the 16- and 17-vertex (3,6)-graph catalogues.** The fractional obstruction is verified on every relevant graph, not only a generated component. No graph-independent generator theorem is asserted.

## 1. Inputs, integrity, and scope

Input `r36_16.g6.gz` is a 2,576-record graph6 catalogue of the 16-vertex triangle-free graphs of independence number at most five. SHA-256 of the compressed file:

`5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25`

This matches the independently published checksum previously located in the repository metadata for the same graph6 catalogue. A standalone, standard-library verifier parses all 2,576 records and checks every graph for triangle-freeness and absence of independent six-sets.

The edge distribution is:

| Edges | Graphs |
|---:|---:|
| 32 | 5 |
| 33 | 39 |
| 34 | 200 |
| 35 | 547 |
| 36 | 803 |
| 37 | 634 |
| 38 | 275 |
| 39 | 62 |
| 40 | 11 |

All 39 of the 33-edge graphs satisfy the residual degree restriction 2 through 5. Every one is isomorphic to precisely one of the earlier 39 rewiring-closed cases, and the 39 catalogue graphs are pairwise nonisomorphic. These comparisons use exact NetworkX graph isomorphism, not graph hashes.

The seven supplied 17-vertex (3,6) graphs were also independently checked: two have 40 edges with five degree-4 and twelve degree-5 vertices; three have 41 edges with three degree-4 and fourteen degree-5 vertices; two have 42 edges with one degree-4 and sixteen degree-5 vertices.

## 2. Reduction of the hypothetical 23-vertex graph

Adopt the convention that graph edges are red; an independent k-set is a blue K_k. Suppose there exists a triangle-free 23-vertex graph G with alpha(G) <= 6.

For any vertex v, N_G(v) is independent, hence d(v) <= 6. If d(v) <= 4, the 22-d(v) >= 18 nonneighbors of v contain an independent six-set because R(3,6)=18; together with v this is an independent seven-set. Thus 5 <= d(v) <= 6.

**Exclude degree five.** Assume d(v)=5, write S=N(v), and let H be the other 17 vertices. H is one of the seven 17-vertex (3,6) graphs. Every s in S has at least four neighbors inside H, giving at least 20 S-H edges. Every w in H has room for at most 6-d_H(w) such edges.

* If e(H)=42, the total capacity is 18 <20.
* If e(H)=41, the total capacity is exactly 20, forcing all fourteen degree-5 vertices of H to have one port in S. For each s, the degree-5 vertices whose only port is s are mutually nonadjacent, so three of them together with S\{s} would form an independent seven-set. Each of five ports accommodates at most two, contradicting fourteen.
* If e(H)=40, the total capacity is 22. Let a be the number of degree-5 vertices having no port, and b the number of degree-4 vertices having exactly one port. A deficit of at most two from capacity gives a+b<=2. The at-most-two-per-singleton-port rule yields 12-a+b<=10, hence a>=b+2. Therefore a=2,b=0, with no other deficits. There are exactly two zero-port vertices, ten one-port vertices (two for each s), and five two-port vertices. The zero-port vertices must be adjacent (otherwise S plus these two is independent). Each zero-port vertex must also be adjacent to at least one of the two one-port vertices for each of five s, or those two plus the zero-port vertex and S\{s} are an independent seven-set. This requires at least six distinct neighbors inside H, contradicting the zero-port vertex's H-degree five.

Thus **every vertex has degree six**.

Choose v, let S=N(v), |S|=6, and H=G-(S union {v}), |H|=16. The six-port regularity forces

    e(H) = (23*6/2) - 6 - 6*5 = 33.

H is triangle-free with alpha(H)<=5. Each port s has exactly five neighbors T_s=N_H(s) in H; each T_s is an independent five-set. For each w in H, the degree-cover relation is

    sum_{s in S} 1_{T_s}(w) = 6-d_H(w).

Our final exclusion does **not** need this degree-cover relation: it uses the weaker condition that the T_s are six independent five-sets.

## 3. Fifth-order incidence obstruction

Let F=I_5(H), the family of all independent five-sets in H. Define

    D[I,T] = 1  iff  I cap T = empty,   I,T in F.

If the six port neighborhoods T_1,...,T_6 existed, then for each I in F at most **one** T_s could be disjoint from I. Otherwise two ports, neither of which is adjacent to any vertex of I, together with I form an independent seven-set. Consequently the *rank-five compatibility graph* on F, joining two **distinct** members T,U when no I in F is disjoint from both, must have a six-clique, unless some chosen T is repeated. A repeated T is possible only when T has no disjoint independent five-set.

**Catalogue theorem.** For all 39 33-edge H in the exhaustive catalogue, the rank-five compatibility graph has no six-clique and every T in F has some disjoint independent five-set. Consequently no such six-port construction exists.

Check results:

| Test | Result |
|---|---:|
| 33-edge residual graphs | 39 |
| F-size range | 72 through 90 |
| Graphs with a compatibility K5 | 13 |
| Graphs with a compatibility K6 | 0 |
| Graphs permitting a repeatable port neighborhood | 0 |

These facts give a direct finite obstruction independent of the numerical LP solver.

## 4. Rational fractional certificates and exact inequality

For each H, a stronger reusable certificate is a vector of nonnegative rational weights y_I indexed by F, satisfying

    for every T in F: sum_{I disjoint T} y_I >= 1;
    sum_{I in F} y_I < 6.

**Proof of exclusion.** Summing six inequalities for six chosen port neighborhoods gives a lower bound of six. Reversing summation, every I contributes at most once by the independent-seven obstruction, hence the sum is at most total weight, strictly less than six. Contradiction. Repeated neighborhoods are excluded by the same argument.

All 39 certificates were regenerated directly on the uploaded catalogue labels using a linear-programming solver, rounded *up* to numerators with denominator 1000, and independently verified using integer arithmetic without consulting solver output. Every one meets both the coverage and strict-total bounds. The largest exact rational certificate mass is 5.775.

The largest numerical LP optimum over the 39 graphs is 75/13. This value is **also certified exactly** on catalogue graph 20 by independent, nonnegative integer primal and dual vectors, each with denominator 26 and total numerator 150:

    min 1^T y subject to D y >= 1, y>=0;
    max 1^T z subject to D z <= 1, z>=0.

Both inequalities, feasibility, and equality of the two objectives were verified using integers. The other 38 graphs have independently certified rational feasible covers of weight below 75/13, so 75/13 is the exact maximum of the 39 optimum values.

## 5. Conclusion and mathematical limits

From the complete catalogue and the degree-five exclusion, no 23-vertex triangle-free graph with independence number at most six exists. Any of the independently checked 22-vertex graphs with no red triangles and alpha=6 establishes the lower bound. Hence **R(3,7)=23**, via a catalogue-dependent recursive proof.

This is not a new Ramsey-number value, and no claim is made that the proof or fractional certificate method is absent from prior literature. The achievement of the current investigation is an exact, independently reproducible translation of the 23-vertex obstruction into the disjointness geometry of independent five-set families, with all needed finite instances verified.

**The remaining generative target:** prove directly, without using the 39-class catalogue, that every 16-vertex triangle-free H with e(H)=33 and alpha(H)<=5 admits a nonnegative rational weight vector satisfying D y>=1 and 1^T y<6. Better still, construct y(H) by a fixed local rule rather than optimizing separately for each H. Tests of uniform weights and simple disjointness-degree power weights fail on these 39 cases; the observed weights are substantially nonuniform. Another route is a structural K6-exclusion theorem for the compatibility graph based on residual graph invariants.

## 6. Verification files

* `ramsey_r37_full_catalogue_audit.py`: generate all 39 fractional witnesses with SciPy; independently check the 39 records using Python integer arithmetic and the K6 search.
* `ramsey_r37_full_catalogue_certificates.json`: all 39 rational certificates, in the original uploaded graph6 labels.
* `ramsey_r37_recursive_proof_verify.py`: **standard library only**; validates all 2,576 16-vertex inputs, all 39 certificate inequalities, all seven 17-vertex controls, and five 22-vertex lower witnesses. Classification completeness is assumed, not reconstructed.
* `ramsey_r37_extremal_lp_check.py` and `ramsey_r37_extremal_fractional_primal_dual.json`: exact matching integer primal/dual for graph 20, giving 75/13.
* Original supplied inputs: `r36_16.g6.gz`, `ramsey36_all7.g6`, `ramsey37_first5.g6`.

Primary catalogue reference: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
