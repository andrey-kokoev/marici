# Six-label obstruction: elementary degree cases

Let F be a graph on six vertices with at least six edges, no 4-cycle, and no three disjoint edges. A trapped edge xy is one for which every pairing of the other four vertices contains an edge of F.

Maximum degree at most two: six edges forces all six degrees to be two. The graph is a six-cycle or two triangles (a four-cycle is forbidden). The six-cycle has three disjoint edges. In two triangles any edge is trapped: the complementary four vertices contain a triangle, meeting every pairing.

Degree five at v: among its five neighbors, the induced graph has maximum degree one, or there is a four-cycle through v. Two such edges together with v joined to the remaining neighbor would give three disjoint edges. Hence at most one extra edge exists. At least six edges forces exactly one; that extra edge is trapped because the complementary four vertices contain a three-edge star.

Degree four at v: name its neighbors a,b,c,d and its nonneighbor w. The edges inside {a,b,c,d} form a matching, and w has at most one neighbor among these four (otherwise a four-cycle through v). Writing t for the number of internal edges and s for the edges from w, we have t<=2, s<=1, and t+s>=2.
- t=2,s=1 is impossible: use the w-edge, an edge from v to the other endpoint of that internal matched pair, and the other internal edge to form three disjoint edges.
- t=2,s=0 gives two triangles sharing v and isolated w. Either internal matched edge is trapped: its complement has a triangle plus an isolated vertex.
- t=1,s=1: write the internal edge ab. If w attaches to c or d, there are three disjoint edges. Thus it attaches to a or b. Its edge, say wa, is trapped because its complement contains the star from v to b,c,d.
These cases also bound the total edge count by six.

## Maximum degree three

If triangle-free, take a degree-three vertex v with independent neighbors a,b,c. The other vertices d,e are not neighbors of v. Each has at most one neighbor among a,b,c, by four-cycle exclusion. Thus there are at most six edges: three at v, at most two from {d,e} to {a,b,c}, and de. Equality requires all these edges. The two external neighbors must be distinct, otherwise de forms a triangle with their common neighbor. Rename them a,b. Then vc,ad,be are three disjoint edges, a contradiction.

If there is a triangle abc, each of its vertices has at most one external neighbor. No external vertex can meet two triangle vertices, since those four vertices would contain a four-cycle. Thus cross edges form a matching of size t. Let s be the number of edges on external vertices d,e,f. We need t+s>=3.
- t=3 already gives three disjoint edges.
- t=2: write the cross edges ad,be. Any external edge incident to f, together with the other cross edge and a suitable triangle edge, gives three disjoint edges. The only possible external edge is de; it creates the four-cycle a-d-e-b-a. Hence t+s cannot reach three.
- t=1: write the cross edge ad. The external edge ef is impossible because ad,bc,ef would be disjoint. Thus s>=2 forces exactly de,df. Edge bc is trapped: its complement has the star centered at d with leaves a,e,f.
- t=0: s>=3 forces the second triangle def; triangle edges are trapped.

This completes the six-label lemma: at least six duads, with no four-cycle and no three disjoint duads, force a trapped duad.

## Independent sets in the 22-vertex construction

For the duads in an independent set, a four-cycle or three disjoint duads are impossible by the partition deletion rule. A trapped duad is also impossible: each of its three incident partitions would have to select a different duad, contradicting its required matching partner. The lemma therefore bounds the number of independent duad vertices by five.

If the independent set contains the root, it contains no label vertices and has size at most 1+5=6. Without the root, let k be the number of label vertices. The duads must avoid those k labels. For k=0 or 1, the five-duad bound gives total at most six. For k=2, the remaining four labels admit at most four edges without a four-cycle, giving 2+4=6. For k=3, at most three duads remain, giving six. For k>=4, the bound k+binomial(6-k,2)<=6 suffices. Thus every independent set has size at most six, for every incident perfect matching.
