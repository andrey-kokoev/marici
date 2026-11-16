# Doubleton port capacity and the five-port obstruction

5 November 2026. Ramsey convention: red graph `G` is triangle-free and
`alpha(G) <= k`; the excluded blue clique has order `k+1`. Results below
are elementary necessary conditions. Nothing here determines `R(3,10)`.

## Port model

Choose `v` with red degree `k`, put `A=N(v)`, `B=V(G)\N[v]` and
`P_x=N(x) intersect A` for `x in B`. Every red-independent `T` in `B`
satisfies `|union_{x in T}P_x| >= |T|`. Red-adjacent exterior vertices must
have disjoint supports. Every exterior vertex has red degree at most `k`;
therefore its degree in `G[B]` is at most `k-|P_x|`.

Doubletons `P_x={a,b}` are edges of a multigraph on port labels. Their
transversal matroid is the *bicircular matroid* of the label multigraph:
matching to port labels corresponds to a pseudoforest (at most one cycle
per connected component). A minimal failure is a bicycle. This observation
is established background about bicircular matroids; the inequalities below
are derived for the Ramsey port model.

## Four-port theorem

For each 4-label subset `U={a,b,c,d}`, let `n_ab` be the multiplicity of
exact support `{a,b}` among exterior vertices, and let `h_U` count exterior
vertices with exact supports of size 3 or 4 contained in `U`. Singleton
supports elsewhere are allowed; only vertices of support size at least two
are used for this argument.

Every admissible Ramsey port system satisfies

    h_U + max(n_ab,n_cd) + max(n_ac,n_bd) + max(n_ad,n_bc) <= 4.     (1)

Proof: In the induced exterior graph on vertices whose supports lie in `U`
and have size >=2, every vertex with >=3 ports is isolated. Doubleton
vertices can be red-adjacent only in the three complementary-pair
bipartite blocks. Select the larger side of each block, and all vertices
with support >=3. They form an independent set whose entire port union is
contained in `U`; Hall gives the bound 4. No assumption about chosen
red edges or global regularity is used.

Put `q_U=sum_{ab subset U}n_ab`. All red edges inside the restricted local
graph join two doubleton vertices with complementary supports, hence their
combined support is exactly `U`. Every doubleton-to-doubleton red edge
belongs to precisely one 4-label block. Because an independent set of
vertices in the `U`-restricted graph has size at most four, its edge count
is at least `(q_U+h_U-4)_+`. Summing yields

    sum_{|U|=4} (q_U+h_U-4)_+ <= e(G[D]) <= (k-2)*n_2/2,           (2)

where `D` is the set of all exact-doubleton exterior vertices and
`n_2=|D|`. The second inequality follows from the individual degree bound
`deg_{G[D]}(x)<=k-2`. Both inequalities hold with duplicate supports and
with singleton supports elsewhere.

Equation (1) is a support-only obstruction. Equation (2) is a global
capacity obstruction. They are valid in all parameters `k`.

## Complete doubleton saturation theorem

Assume for every pair of port labels `ab`, there is an exterior vertex
with exact support `ab`. Choose one such vertex for every pair, forming
`D_0` of size `binom(k,2)`. Restrict (2) to `D_0` and omit other supports:
for each 4-label set, all six pair types appear, requiring at least two red
edges. Thus

    2*binom(k,4) <= e(G[D_0]) <= (k-2)*binom(k,2)/2.

For k>=4 this simplifies to `k<=6`. This theorem assumes neither global
regularity nor absence of additional exterior vertices.

For k=6, equality holds at both ends. Every selected vertex has exactly
four red neighbors in `D_0` and its two red neighbors in `A`, exhausting
the red degree bound six. If an additional exterior vertex `z` existed, it
would be nonadjacent to every vertex of `D_0`. For any port a, the five
vertices with supports `{a,b}` form an independent set. Together with `z`
and the central vertex `v`, they would give an independent set of size 7,
a contradiction. Hence `B=D_0` and `|V(G)|=22`.

This explains a distinguished family of critical `R(3,7)` constructions,
not all such constructions. The full-pair premise cannot hold in a
hypothetical 9-port/30-exterior-vertex system simply because
`30 < binom(9,2)=36`; the saturation theorem alone offers no new bound on
`R(3,10)`.

## Verifications on known critical Ramsey graphs

The bundled verifier audits every degree-six center of the 191 McKay
`R(3,7;22)` graph6 entries, i.e. 3,249 centers. The four-port lower edge
bound is positive at 2,121 of them. Exactly three centers have one vertex
of each of the fifteen doubleton types: (catalogue entry 190, vertices 0
and 5) and (entry 191, vertex 0). Each has 30 doubleton-to-doubleton red
edges, exactly the four-port lower bound, and exactly two red edges inside
each of the fifteen four-label blocks.

The verifier also checks the four-port theorem at all 35 saturated centers
of the known 35-vertex `R(3,9)` critical graph.

## Why four-port closure is not enough at nine ports

For a hypothetical 9-regular 40-vertex `R(3,10)` coloring, the exterior
port system would have 30 vertices and 72 port incidences. If it has no
singleton supports then at least 18 are doubletons. The archive includes
an explicit test system with exactly 18 doubleton and 12 tripleton supports,
with each of 9 port labels occurring exactly 8 times. Its 18 doubletons
form a bipartite label graph (`K_{4,5}` minus two edges).

There is an explicit 99-edge red graph on these 30 exterior vertices such
that:

- Exterior red degrees equal `9-|P_x|` exactly.
- The exterior graph is triangle-free; red edges join disjoint supports.
- Every actual 4-label Hall test passes; not merely inequality (1).
- Every two port fibers satisfy the eligible-pair perfect matching test.

Nonetheless its exterior graph contains a red-independent set of size ten.
The first port-subset Hall failure occurs already on five labels. One
minimal circuit is the following six exterior supports:

    {0,1,8}, {1,6,8}, {0,6}, {2,6}, {0,8}, {2,8}.

They use only labels `{0,1,2,6,8}` and every proper five-support subset
can be matched to distinct labels. In the test graph the six vertices are
red-independent, violating Hall. The only three eligible red pairs inside
this circuit join (support positions 1,4), (3,6), (4,5), using one-based
positions in the displayed support list. Thus the 6-element circuit is a
necessary genuinely five-port exclusion, invisible to 4-port tests.

Within five port labels, exact-doubleton types form the vertices of the
Petersen graph `KG(5,2)` under disjointness. A tripleton can have a red
edge only to a doubleton with complementary support, while vertices with
support size 4 or 5 are isolated among support-size >=2 vertices.
This supplies a small, parameter-independent local structure for the next
layer of weighted circuit-capacity inequalities.

This test system is **not** a Ramsey graph; the independent ten-set
proves failure. It establishes the limitation of four-port and pair-fiber
tests, not the existence of a 40-vertex counterexample.

## Next target

Construct a weighted five-port bicircular/Petersen-spike inequality which
charges all six-element circuits against per-vertex degree capacities and
triangle exclusions. It must combine overlapping five-label subsystems:
individual four-label constraints, even when all hold exactly, do not
exclude the 9-port case.

## Reproduce

Run `python3 ramsey_doubleton_capacity.py` in this folder. It uses only the
Python standard library and the accompanying graph6/edge-list input files.
All graph and degree computations are red-graph computations.

Public provenance: Brendan McKay's Ramsey graph catalogue,
https://users.cecs.anu.edu.au/~bdm/data/ramsey.html ;
Vigleik Angeltveit, *R(3,10) <= 41*, Electronic Journal of Combinatorics
(2025), https://doi.org/10.37236/12936 .
