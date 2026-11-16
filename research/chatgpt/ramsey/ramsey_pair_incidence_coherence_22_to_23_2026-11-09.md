# Six-direction pair promotion, incidence transversals, and the Ramsey 22/23 frontier

Date: 2026-11-09  
Status: exact generative **22-vertex witness**; conditional necessary **23-vertex defect identity**; no new proof of the universal upper bound and no established Golay/2048 bridge.

## 1. Objective and origin

Seek a source-generated Ramsey incidence/obstruction law, not numerical matches to Golay code parameters. The seven-position `RGRGR00` binary rotation quotient contains six independent comparison directions (plus a seventh determined by their sum). Selecting six of those directions as a frame is an **explicit choice**, not yet a theorem of the original three-symbol composition calculus.

Starting with any named six-element frame `X`, this note derives a (3,7)-admissible graph of order 22 using independent pair promotion and a perfect matching between two classes of local constraints. No target 22x22 adjacency matrix is inserted. This reconstructs a classical Graver–Yackel/Kneser-pair construction in a different, fully source-explicit formulation.

The missing Ramsey theorem is the **universal** obstruction for 23 vertices; proving that a generated 22-vertex graph cannot be extended is only a lower-bound construction plus a special-case obstruction.

## 2. The duplex incidence system

Let `X=[6]`, and define:

- `P=C(X,2)`, fifteen **pair states** (duads).
- `Q=C(X,4)`, fifteen **four-set compatibility contexts**.
- `M`, fifteen partitions of `X` into three disjoint unordered pairs (**perfect matchings**, or synthemes).

Form a bipartite incidence graph `B` on `Q` and `M`: link `q` and `m` if `q` is the union of two blocks of `m`. This is equivalent to saying the complementary pair `X\q` belongs to `m`.

Every four-set admits exactly 3 internal pairings; every perfect matching has exactly 3 unions of two blocks. Therefore `B` is 3-regular on 15+15 vertices. By Hall's theorem **a perfect matching exists**.

Each incidence edge `(q,m)` identifies a unique red edge of the Kneser graph `KG(6,2)`: the two pair blocks of `m` whose union is `q`. Thus a perfect matching `mu: Q -> M` selects a set `D` of **fifteen Kneser edges** with precisely one selected edge per four-set and one per six-position perfect matching.

The fifteen triangles of `KG(6,2)` are exactly the fifteen perfect matchings of six positions; each Kneser edge belongs to exactly one such triangle. Therefore `KG(6,2)-D` is triangle-free.

### Forced balanced deletion degree

Fix one pair `a` in `P`. Exactly three perfect matchings `m` contain `a`. Their other two blocks form the **same** complementary four-set `q0=X\a`. The matching of contexts must assign `q0` to exactly one of these three `m`'s. This matched pair selects the Kneser edge joining the *other two blocks*, not incident with `a`. Each of the remaining two perfect matchings containing `a` selects an edge **incident with `a`**. Hence `deg_D(a)=2` for every pair state. The deletions automatically form a 2-factor, without any balancing condition imposed by hand.

Consequently, `H=KG(6,2)-D` is four-regular and triangle-free on fifteen pair states.

## 3. Elementary independence lemma

**Six-edge lemma.** If a simple graph `F` on six ground vertices has six edges and every edge `uv` satisfies `d_F(u)+d_F(v)>=5`, then `F` contains a four-cycle.

*Proof.* Let `Delta` be its maximum degree. `Delta<=2` is incompatible with the degree-sum condition.

- If `Delta=5`, the graph is a five-leaf star plus one further edge between two leaves. That edge has degree-sum 4.
- If `Delta=4`, let `v` be degree four. Its one nonneighbor cannot meet either of the two remaining edges, since it would create an edge with degree-sum at most four. The two remaining edges therefore lie among the four neighbors of `v`. They cannot be disjoint (degree-sum four), so they share a neighbor `a`, giving a four-cycle through `v`.
- If `Delta=3`, a degree-one vertex is impossible, since its incident edge has degree-sum at most four. With six edges, there are four, five or six nonisolated vertices. Four yield `K4`, containing a four-cycle. Five have degrees `(3,3,2,2,2)`: no edge can join two degree-two vertices, so all three degree-two vertices meet both degree-three vertices, containing `K_{2,3}` and a four-cycle. Six must all have degree two, contrary to the degree-sum hypothesis.

This exhausts the cases. QED.

**Corollary.** Every independent set in `H` has at most five vertices.

*Proof.* An independent six-set of pair states in `H` can be viewed as a six-edge graph `F` on the six ground positions. Every edge of `F` is disjoint from at most two other edges of `F`, because any disjoint pair must be a deleted edge and `D` is a 2-factor. For every edge `uv` of `F`, the number of its disjoint partners is `7-d_F(u)-d_F(v)`. Hence `d_F(u)+d_F(v)>=5`. The lemma supplies a four-cycle in `F`. Its two opposite-edge decompositions are **two distinct Kneser edges supported on the same four-set**. To make the chosen six pair states independent in `H`, both would have to lie in `D`, contradicting the one-deletion-per-four-set condition. QED.

A five-element star of pairs containing one fixed ground position is independent in `H`, so `alpha(H)=5` exactly.

## 4. Full 22-vertex Ramsey graph and proof

Define `G` on `{p} U X U P`, of cardinality

`1+6+C(6,2)=22`.

Red edges are:

1. `p -- x` for all six ground positions `x`;
2. `x -- {i,j}` iff `x in {i,j}`;
3. edges of `H=KG(6,2)-D` among the fifteen pair states.

**Theorem.** For every perfect matching `mu` of the above bipartite incidence graph, `G` is 6-regular, triangle-free, and `alpha(G)=6`.

*Degree.* `p` has degree six. Every ground `x` meets `p` and five incident pair states, so has degree six. Every pair state meets two ground vertices and four other pair states in `H`, so has degree six. Hence `e(G)=66`.

*Triangle-freeness.* Ground vertices have no mutual red edges, and pair states incident with the same ground vertex intersect as pairs, hence have no mutual Kneser edge. The pair-induced graph `H` is triangle-free by Section 2. All possible triangle types are excluded.

*Independence.* An independent six-set exists: the six ground vertices. For the upper bound, an independent set containing `p` can use no ground vertices and at most five pair states, so has size at most six. An independent set excluding `p` with `r` ground vertices can use only pair states from the remaining `6-r` ground positions.

- `r=0,1`: at most five pair states, by `alpha(H)=5`, so total at most six.
- `r=2`: among the six pair states of a remaining four-set, Kneser adjacency is three independent edges. Exactly one is deleted by the quartet transversal, leaving two edges. The resulting independence number is four; total at most `2+4=6`.
- `r>=3`: the trivial upper bound is `r+C(6-r,2) <= 6`.

Thus `alpha(G)=6`. QED.

This is a **nontrivial, checkable lower bound** `R(3,7) >= 23` derived from pair incidence and Hall matching, not an imported adjacency matrix. It remains conditional on interpreting six binary comparison directions as the ground frame and on the displayed incidence semantics.

## 5. Exact finite structure of matching choices

The 15x15 bipartite graph has exactly **288** perfect matchings. Every selected 15-edge set `D` is a 2-factor of `KG(6,2)`. Its cycle-type distribution is:

| Selected deletion 2-factor | Count | Relabeling orbit under `S6` |
|---|---:|---:|
| Single 15-cycle | 144 | One orbit of size 144 |
| 5-cycle plus 10-cycle | 144 | One orbit of size 144 |

The two classes yield **nonisomorphic 22-vertex graphs** (checked separately). The earlier explicit 15-cycle

`56,12,35,26,13,46,23,14,25,34,15,36,45,16,24,56`

is one representative; it is **not** a free, unexplained adjacency choice in the Hall construction.

The quartet-syntheme 15x15 incidence matrix has **rank 10 over F2**; its image has `2^10=1024` elements. Neither this rank nor the number 288 supplies the Golay `2^11=2048` syndrome space without further structure. Do not silently relabel this as an eleven-phase proof.

## 6. One-vertex terminality, and its limitation

For the displayed Hamiltonian-deletion representative, exact bitset enumeration produces independent-set counts

`(1,22,165,550,870,612,137)` for sizes `0..6`, respectively.

A new vertex has a triangle-free red neighborhood `S` iff `S` is independent in the old graph. To keep the enlarged independence number at most six, `S` must intersect every one of the old 137 independent six-sets. **No such `S` exists** among the 2,357 independent subsets. A short explicit certificate comprises **ten** independent six-sets, one symmetry orbit: every independent `S` is disjoint from at least one of the ten. The independent-set and symmetry checks are exact in the companion checker.

This proves this particular 22-vertex graph is terminal under induced one-vertex extension. **It does not prove the universal absence of 23-vertex Ramsey graphs**; a different 22-vertex graph could conceivably extend. The known upper bound `R(3,7)<=23` is a separate classical theorem.

## 7. Universal necessary defect at the hypothetical 23rd vertex

Assume for contradiction a triangle-free graph `G23` on 23 vertices with `alpha<=6`. The neighborhoods are independent, so `Delta<=6`. The nonneighbors of each vertex induce a triangle-free graph with independence number at most five; since `R(3,6)=18`, every degree is at least five. The handshake lemma then shows an **odd positive number of vertices of degree six**.

Choose a degree-six vertex `v` and write `A=N(v)` (six independent vertices), `B=V\(A U {v})` (sixteen vertices). Let `t_b=|N(b) intersect A|`. Since `A U {b}` would otherwise be an independent seven-set, `t_b>=1`. Put `n_j=number of b in B with t_b=j`, and let `m` count degree-five vertices in `A`.

Counting red incidence from `A` to `B` in two ways gives

`sum_{j=1}^6 j n_j = sum_{a in A}(deg(a)-1)=30-m`, while `sum_j n_j=16`.

Subtracting twice the second identity yields the exact **defect equation**

`n_1 = 2 + m + sum_{j=3}^6 (j-2)n_j`.

Therefore every degree-six reference vertex in any hypothetical 23-vertex counterexample has **at least two nonneighbors sharing exactly one red neighbor with it**. High codegree states and degree-five neighbors force even more singleton states.

At 22 vertices the same calculation has no leading `+2`. The balanced six-frame witness realizes the zero-defect pair configuration at its distinguished reference `p`.

This is a **genuine universal necessary incidence constraint**, not a proof of nonexistence: singleton and triple-codegree states already occur in other valid 22-vertex graphs.

## 8. A second local-to-global obstruction: global uniformity is impossible already at 22

Suppose, more strongly, that a six-regular triangle-free graph on 22 vertices had **exactly two common neighbors for every nonadjacent pair**, as our distinguished reference `p` does. With adjacency matrix `A`, counting two-walks forces

`A^2 + 2A - 4I = 2J`.

On the 21-dimensional space orthogonal to the all-ones vector, the two possible eigenvalues of `A` are `-1+sqrt(5)` and `-1-sqrt(5)`. Since `A` is integral, these irrational conjugate eigenvalues must occur with equal multiplicity, impossible in **odd dimension 21**. Thus no strongly regular graph with parameters `(22,6,0,2)` exists.

This proves that local two-fold pair completeness cannot hold at **every** reference simultaneously. The explicit witness exhibits nonneighbor codegree counts:

`codegree 1: 35 pairs; codegree 2: 95 pairs; codegree 3: 35 pairs`.

The deviations from uniformity are globally balanced. This is a rigorous symmetry/coherence obstruction, but not by itself the 23-vertex Ramsey impossibility.

## 9. Where the 2048-cycle stands

The previous eleven-dimensional Golay field and `I+T` map do provide a 2047-state nonzero orbit plus a fixed zero, with an extra nonlinear splice making one 2048-cycle. That arithmetic is exact, but this incidence construction independently gives a 10-dimensional GF2 image and 288 perfect matching choices. **No source-defined homomorphism** identifies these objects or makes the 2048-cycle impose the 23-vertex Ramsey obstruction.

The immediate mathematical target is now much sharper than fitting 23: **show that the forced singleton defects in Section 7 cannot be made globally compatible with the pair/matching constraints of every vertex**. That would be a real proof of the upper bound using the same kind of mechanism as the Hall-transversal witness. Test the incompatibility for all degrees 5 and 6; do not require the hypothetical graph to contain this particular 22-vertex witness as an induced subgraph.

## 10. Reproduction

`python check_ramsey_six_direction_bitransversals.py`

- Builds all 288 compatible transversals without a given adjacency matrix; confirms cycle types and the two `S6`-orbits; tests the resulting 22-vertex graph representatives, and computes the GF2 incidence rank.

`python check_ramsey_pair_cycle_coherence.py`

- Builds the explicit Hamiltonian representative; checks 66 edges, degree six, no triangles, alpha six, the independent-set distribution, no valid single-vertex extension, the compact ten-set obstruction, codegree defect spectrum, and the six-edge lemma for all 5,005 six-edge graphs on six positions.

Source context: Graver and Yackel, *Some graph theoretic results associated with Ramsey's theorem* (1968), for classical R(3,7) constructions and the upper bound; contemporary graph collections of B. McKay list 191 maximal 22-vertex Ramsey(3,7) graphs. Neither existing result is presented as a theorem newly discovered here.
