# Ramsey (3,10): variable-degree overlap certificates and an exact branch exclusion

## Status

The target remains undecided: no 40-vertex (3,10) graph was constructed, and no universal nonexistence certificate was obtained. The current verified interval remains 40 <= R(3,10) <= 41.

Two independently checked steps were completed in this run:

1. A new finite-overlap calibration certificate proves R(3,6) <= 18 without supplying five-regularity or any fixed-degree assumption. It uses only the smaller known R(3,j), j <= 5, triangle avoidance, independent-six avoidance, induced-pattern restriction identities, rooted capacity inequalities, and finite overlap positivity.
2. An exact compatibility-kernel computation excludes degree four in a hypothetical (3,10;40) graph, conditional on the published uniqueness of the (3,9;35) graph. This is an independent reconstruction of an exclusion also reported elsewhere in 2026, not a new Ramsey bound or a claim of priority.

## 1. Uniform variable-degree capacities

For an induced pattern H, choose disjoint independent subsets A and B. Let C(A,B) be vertices outside A union B that are adjacent to all of A and nonadjacent to all of B.

In a triangle-free graph with independence number below t:

- If A is nonempty, C(A,B) is independent. Together with B it is independent, so |C(A,B)| <= t-1-|B|.
- If A is empty and B is nonempty, the induced graph on C(A,B) has independence number below t-|B|. Hence |C(A,B)| <= R(3,t-|B|)-1 whenever that Ramsey bound is supplied.

The internal part of C(A,B) is already visible in H. Averaging the external part gives a linear inequality between frequencies of H and its one-vertex extensions. Root pairs are grouped only by automorphisms of H; their incidence information is retained.

For patterns through seven vertices, the generalized template has 172 triangle-free unlabelled patterns, 4,206 rooted capacity rows, and 218 rooted five-vertex flags. Three labeled roots and two unordered witness vertices give seven moment blocks of sizes 50, 32, 32, 24, 32, 24, 24. Products retain zero-, one-, and two-witness collisions.

## 2. Exact calibration without regularity

For n=18, t=6, patterns containing an independent six-set are set to zero. The surviving catalogue has 164 patterns. The delivered certificate uses:

- 31 exact equality multipliers (normalization and deletion consistency);
- 96 nonnegative rooted-capacity multipliers;
- 11 nonnegative finite mean-square multipliers.

Its contradiction margin is greater than 1/2, verified with Fraction arithmetic. No fixed-degree equation occurs in the certificate format or verifier. An explicit 17-vertex graph is also checked, recovering R(3,6)=18 from the stated smaller Ramsey values.

The numerical optimizer was used for discovery only. The verifier regenerates the relevant counts and checks completeness of the allowed catalogue by comparing independently enumerated labeled graphs with the summed isomorphism-orbit counts.

Commands:

    python -m pip install networkx
    python verify_no_regularity_certificate.py

## 3. Exact degree-four obstruction at order 40

Assume G is triangle-free, has 40 vertices, and has no independent ten-set.

Every degree is at most nine, since neighborhoods are independent. R(3,9)=36 gives minimum degree at least four. Suppose d(v)=4. Its 35 nonneighbors induce a triangle-free graph H with no independent nine-set. By Goedgebeur--Radziszowski's uniqueness theorem, H is the cyclic graph on Z/35 with differences +/-1, +/-7, +/-11, +/-16.

Let the four neighbors of v be u_1,...,u_4, and let S_i=N(u_i) intersect V(H). Each S_i is independent in H. For every i != j, H minus (S_i union S_j) cannot have an independent eight-set, or that set together with u_i,u_j would be independent of size ten.

Extend each S_i to a maximal independent set M_i in H. Enlarging S_i can only preserve the necessary pair-compatibility condition. Define a graph B on the maximal independent sets of H by

    M adjacent to M' iff no independent eight-set of H avoids M union M'.

Any valid attachments would require a four-clique in B, allowing repetition only if a maximal set were self-compatible. The checker verifies that no maximal set is self-compatible.

Independent exact calculations give:

    maximal independent sets of H: 3365
    of size 8: 3360
    of size 7: 5
    edges of B: 191100
    triangles of B: 0
    clique number of B: 2

Therefore even three pairwise-compatible maximal attachments are impossible. Four are impossible in particular. Degree four is excluded, and every hypothetical (3,10;40) graph has degrees in {5,6,7,8,9}.

The verifier uses two independent algorithms for maximal-independent-set enumeration, verifies alpha(H)=8, and checks that every compatibility edge has no common compatibility neighbor. It uses only integer bitsets and standard-library Python.

    python verify_degree4_obstruction.py

This also shows H cannot be the nonneighbor graph of a vertex having three or more neighbors in any (3,10) graph. The result does not classify the possible 30- through 34-vertex nonneighbor graphs.

External assumption: the uniqueness theorem for H is cited, not independently reproved by our verifier. The exclusion of degree four was also reported by Unsolved Lab and hraness/algal-lab in September--October 2026; their claims were not substitutes for our exact check.

## 4. A nonregular branch reduction for the remaining 40-vertex case

Set w(v)=9-d(v) and D=sum_v w(v). Then e(G)=180-D/2. For a vertex v of degree d,

    e(G - N[v]) = e(G) - sum_{u in N(v)} d(u)
                 = 180 - 9d - D/2 + epsilon(v),
    epsilon(v) = sum_{u in N(v)} w(u).

If D>0, there is a vertex with w(v)>0 and epsilon(v)<=D/2. To see this, look at the subgraph on positive-weight vertices. If it is edgeless, epsilon=0 on it. Otherwise, choose one of its edges xy. Triangle-freeness makes the two weighted neighbor sets disjoint, so epsilon(x)+epsilon(y)<=D. One endpoint works.

Consequently, every non-9-regular candidate has at least one vertex with:

| Degree d | Nonneighbor order | Upper bound on its edges |
|---:|---:|---:|
| 5 | 34 | 135 |
| 6 | 33 | 126 |
| 7 | 32 | 117 |
| 8 | 31 | 108 |

If the candidate is 9-regular, every nonneighbor graph has exactly 30 vertices and 99 edges. This is the even-order adaptation of the weighted-deficit reduction used by Angeltveit. The table is an existence-of-a-useful-root reduction, NOT a bound asserted at every vertex of an arbitrary nonregular graph.

## 5. What the large-target computation did not prove

The variable-degree seven-vertex model was tested at n=40 and n=41. Several rounds of numerical eigenvector cuts were generated. No exact infeasibility certificate was obtained. Intermediate candidate moment matrices still had negative eigenvalues, so those candidates are NOT feasible semidefinite solutions and are NOT graph constructions. We have not proved that this relaxation is feasible or that seven-node overlaps are fundamentally insufficient.

The next unsolved cases are the four nonregular branches in the table and the 9-regular branch. No assumption that all hypothetical graphs are regular is justified.

## Sources

- Vigleik Angeltveit, R(3,10) <= 41, Electronic Journal of Combinatorics 32(4) (2025), P4.30. https://doi.org/10.37236/12936 ; https://arxiv.org/html/2401.00392v2
- Jan Goedgebeur and Stanislaw P. Radziszowski, New Computational Upper Bounds for Ramsey Numbers R(3,k), EJC 20(1) (2013), P30, Theorem 3 (uniqueness and cyclic steps of H). https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i1p30/pdf
- Bernard Lidicky and Florian Pfender, Semidefinite Programming and Ramsey Numbers. https://arxiv.org/abs/1704.03592
- Unsolved Lab, October 2026 report (self-published, explicitly not externally reviewed): https://unsolvedlab.com/problems/ramsey-r310
