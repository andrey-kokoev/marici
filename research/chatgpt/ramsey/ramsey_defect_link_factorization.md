# Defect clauses can be constructed directly from small endpoint-link graphs

There is now an exact incidence factorization, not just a faster completed-output test.

Let S be k vertex-disjoint two-edge switches. A genuinely k-switch-born independent seven must contain exactly TWO vertices from each switch support, and those two must be endpoints of one of its deleted edges.

Reason: minimal birth requires at least one original red edge to be removed by each switch. Three vertices from a four-vertex support would contain an edge of its newly added perfect matching, contradicting independence. Hence exactly two endpoints occur per support; all remaining vertices lie outside the supports.

Construction:
1. Choose one of the two deleted edges from each switch (2^k choices).
2. Reject the endpoint set if it has any original red edge other than the chosen deleted ones.
3. Form L: vertices outside ALL selected supports, originally nonadjacent to every chosen endpoint.
4. Choose an independent (7-2k)-set in G[L]. Adjoin the2k endpoints.

This constructs exactly the genuinely k-switch-born sevens, with no completed switched graph needed. Conversely every constructed set is independent after allk switches but not after any proper subcollection, because a chosen original edge remains.

Consequences:
- singleton defects = deleted edge + independent FIVE-set in its endpoint link;
- pair-born defects = two deleted edges + independent THREE-set in their common link;
- triple-born defects = three deleted edges + ONE common nonneighbor.

For a triangle-free6-regular22-vertex source, each single-edge link has at most TEN vertices. Adjacent endpoints have disjoint red neighborhoods; each can have at most one additional neighbor among the other two support vertices (otherwise a triangle). Outside the four-vertex support, at least eight vertices are excluded by endpoint adjacency, leaving at most18-8=10.

ramsey_defect_link_constructor.py constructs the clauses this way and independently verifies them against completed-output enumeration for all80 singles,1450 disjoint pairs and7005 disjoint triples of Hall191. Exact matches:550 singleton defect occurrences,6895 pair-born occurrences,4455 genuinely triple-born occurrences. Observed link sizes:9..10 for singles,3..7 for pairs,1..5 for triples. These are occurrence counts, not unique seven-set counts.

This resolves the locality puzzle precisely: the earlier support/core profiles ignored edges BETWEEN external vertices; those are exactly the edges in G[L] that determine the residual independent sets. For the dead/viable local twins, first-edge links are both10-vertex graphs but have three versus four independent-five residues; second-edge links each have two. The viable switch has MORE initial defects, so defect count alone still cannot determine repairability. The actual residue sets and their repair incidences matter.

The existing repair-rule compiler can therefore be supplied from original-graph link incidence, rather than discovering clauses by building switched22-vertex graphs and enumerating independent sevens. Independence enumeration remains, but only on bounded smaller links (five-sets or triples); we have not eliminated it entirely or classified every link by a closed-form motif.

Proof scope: factorization holds generally for disjoint two-edge switches and minimal defect birth; the link-size bound uses the particular degree/order conditions. Full candidate-family completeness and subsequent repair propagation retain their earlier finite scope.

Artifacts: ramsey_defect_link_constructor.py/JSON. Construction function link_defects() does not construct completed outputs; its main verification loop does so only as an independent check.
