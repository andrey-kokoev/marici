# No two vertices in a legal 35-vertex endpoint share five red neighbors

This is global: there is no assumption on singleton count, unsaturation, transitivity, or cube incidence. It uses 8-regularity of legal (3,9) endpoints and the complete 22-vertex (3,7) catalogue. The bound of four is attained by the known endpoint.

A red pair has no common red neighbor. Take a blue pair r,z with c common red neighbors. Their common blue neighborhood H has 17+c vertices, and it cannot contain a blue seven. Hence c<=5. Suppose c=5. Write C for the five shared red neighbors and U,V for the three private red neighbors on each side. Vertices of C cannot see C,U,V in red (triangles), so each has six red neighbors in H. U and V separately are blue. Put k=e_red(U,V); each private vertex has seven available red edges besides its root, so together they send 42-2k edges into H. By 8-regularity on the 22 vertices of H,

    2 e(H) = 8*22 - 5*6 - (42-2k),  hence e(H)=52+k.

Since k<=9, only the edge layers 60 (one graph) and 61 (six graphs) of the catalogue survive. The cross edges form K3,3 minus one edge, or all of K3,3. Thus H-support sizes on each side are (4,4,5) or (4,4,4), respectively. Each support is red-independent. Any two supports on one side must collectively hit every blue six in H: otherwise that six, the two private vertices, and the opposite root form a blue nine. The three together must hit every blue five for the same reason. (These tests are complete for this one-side (3,8) projection, not for the endpoint.) Finally each red cross edge forces the supports at its ends to be disjoint.

For every 61-edge graph there is **no** admissible one-side triple. For the unique 60-edge graph there are 116 triples, up to interchanging the size-four supports but with the catalogue vertices labeled. No two of them satisfy the eight disjointness tests. A separate SAT encoding that keeps both triples ordered and enumerates no panels gives the same exclusions. Thus c=5 is impossible. The stored endpoint has 105 blue pairs attaining four.

In the eight-singleton saturation problem this removes the entire profile with a five-label cell, even without assuming absence of a saturated region. The only remaining unsaturated possibilities with eight singletons are now 6, 7, or 8 pair cells, respectively followed by 12 triples; 10 triples + 1 quartet; or 8 triples + 2 quartets. The common-neighbor bound can also prune core colorings: if two cells already share s>0 labels, they are blue and may share at most 4-s red **core** neighbors.

[Panel census](results/ramsey_codegree_five_panels.json) · [Independent SAT results and positive control](results/ramsey_codegree_five_verify.json) · [Enumeration](checkers/ramsey_codegree_five_panels.py) · [Verifier](checkers/ramsey_codegree_five_verify.py).
