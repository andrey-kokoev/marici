# Hall-contact composition and arbitrary-order missing fillers

## Exact contact identity

Color the complete graph using A for graph edges and B for nonedges. Let L be a B-clique of size l and H=V\L. For u in H put S(u)=N_A(u) ∩ L. For every A-independent T⊆H, its B-completion in L is L\S(T). Thus

    alpha_A(G)=l + max_{T⊆H, T A-independent} (|T| - |S(T)|).

In particular, when l=m−1, absence of a B-K_m is equivalent to independent-set Hall expansion |S(T)|≥|T| for all A-independent T⊆H. This is an equivalence, not an additional Ramsey axiom.

## Relative filler law

Let T be an A-independent old-vertex set, with slack f(T)=|S(T)|−|T|≥0. Consider a set J of new births that are mutually B-connected and B-connected to all of T. Let P_j⊆L be their A-contact sets. To avoid a B-K_m it is necessary and (relative to this T) sufficient that

    f(T)+ |(⋃_{j∈J}P_j)\S(T)| ≥ |J|.

The same inequality must hold for every subset J'⊆J. If f(T)=0, Hall's theorem makes the allowed birth sets J exactly the independent sets of the transversal matroid on the bipartite incidence graph from births to the unused contacts L\S(T). In particular, minimal failed completions are circuits of that matroid. Different old T impose simultaneous conditions, and the global compatibility system is not generally a single matroid.

## A full arbitrary-order missing simplex

For integers m≥3, 1≤t≤m−2, let r=m−1−t. Set L={l_1,...,l_{m−1}}, a B-clique. Adjoin t old vertices u_1,...,u_t, where each u_i has exactly one A-neighbor l_i; there are no A-edges among the u_i. Create r+1 potential newborn vertices z_1,...,z_{r+1}, each with the same A-neighbors l_{t+1},...,l_{m−1}; there are no A-edges between newborns or old u_i.

For j newborns present, the A-graph is the disjoint union of t copies of K_2 and one K_{r,j}; every edge is between L and its complement. It is triangle-free, and

    alpha_A(G_j)=t+max(r,j).

Hence for every j≤r the coloring avoids a B-K_m, while j=r+1 creates a B-K_m consisting of all t old u_i and all r+1 newborns. Its family of admissible newborn subsets is precisely the full boundary ∂Δ^r, with integral reduced homology H_{r−1}=Z.

Concrete case: m=6,t=2,r=3. Four potential births yield 4 vertices, 6 edges, 4 triangles, and no filled tetrahedron in the completion complex, so H_2=Z. Every proper subset of births is individually and jointly admissible; all four are forbidden.

This construction does **not** have a Hamiltonian A-cycle (its A-graph is disconnected). Therefore it gives an obstruction in unrestricted Ramsey colorings, not a counterexample to a theorem that explicitly assumes Hamiltonian A and B traversals. It also does not show that the completion complex has intrinsically nontrivial infinity-groupoid higher homotopy: the simplicial homology claim concerns the admitted-birth subset complex.

## General local B-simplex link inequality

For any pure B-simplex W of k vertices, its common B-link is V\(W∪N_A(W)). In a triangle-free graph without B-K_m, it has at most R(3,m−k)−1 vertices when 1≤k≤m−2. Thus

    |⋃_{w∈W}N_A(w)| ≥ N−k−R(3,m−k)+1.

For a putative 23-vertex (3,7) graph, k=1,2,3,4,5 gives lower bounds on neighborhood-union sizes 5,8,12,14,16 respectively, using R(3,6)=18, R(3,5)=14, R(3,4)=9, R(3,3)=6, R(3,2)=3. For k=6 the contact union has all 17 exterior vertices, and the stronger Hall constraints must hold on every exterior B-simplex.

## Limitation and research objective

Hall expansion is mathematically equivalent to avoiding forbidden B-simplices, so it is not an independent source of Ramsey values. The new structural information is the complete relative matching description, the resulting matroid circuits, and existence of minimal missing faces in arbitrarily high dimensions as m grows. A predictive explanation of Ramsey thresholds must bound which contact matroids and circuits are realizable by the proposed native simplex composition operations rather than impose Hall as an extra axiom.
