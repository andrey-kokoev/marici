# Five-symbol Ramsey primitive: exact orbit, Petersen decoder, and the missing vertex-creation operation

9 November 2026. Source-first finite test of `R G R 0 0`, without supplying the 13-vertex extremal graph during generation. Companion exact checker: `ramsey_five_symbol_primitive_test.py`.

## 1. Source transformations

Index the five positions by `F_5`. The row `x=RGR00` has red-marked positions `{0,2}`, green-marked position `1`, and two empty positions `{3,4}`. Define the cyclic translation `T(j)=j+1` and the quarter-turn root `P(j)=1+3(j-1)` mod 5. Then `P²(j)=2-j` mod 5, the reflection about the green midpoint, and `P⁴=I`. The source row is invariant under `P²`, so the orbit of `x` under `P` alone contains only two distinct literal rows.

The group `<T,P>` is the complete affine group `AGL(1,5)`, order `5·4=20`. Its orbit of the un-oriented, un-phased literal row has ten elements. The red positions in each row range over all `binom(5,2)=10` unordered pairs `{a,b}`. The green position is always their midpoint `(a+b)/2` mod 5; the other positions are zero. The two-red/one-midpoint structure and ten-row orbit are forced by the stated positional operations; no graph adjacency has yet been defined.

The ten rows are identified naturally with the edges of `K_5`. A distinct orientation/phase register would distinguish histories collapsed by the literal row representation, but has not been supplied by this ten-state construction.

## 2. Conditional adjacency decoder

Test the intrinsic rule: two row-states are red-adjacent iff their *red-position pairs* are disjoint. This produces the Kneser graph `KG(5,2)`, the Petersen graph, with 10 vertices, 15 red edges, no red triangles, and independence number 4. Every independent family consists of pairwise-intersecting two-element subsets of a five-element set; its size is at most 4. Its five maximum independent sets are the four-pair stars `M_i={{i,j}:j!=i}`.

The natural action of `S_5` on unordered pairs preserves disjointness. Conversely, every Petersen automorphism permutes the five uniquely characterized size-four independent stars. Since a pair `{i,j}` is the unique intersection `M_i∩M_j`, the resulting action is faithful. Therefore `Aut(KG(5,2))=S_5` (order 120). The source *generator* is the proper subgroup `AGL(1,5)` (order 20); `S_5` emerges as the full symmetry of this particular decoded graph.

The red-disjointness decoder is **additional** to the original row transformations. It is not implied just by the labels `R/G/0`.

## 3. Exhaustive equivariant decoder census

On the ten states, the 20-element source group has exactly four orbits on unordered pairs of distinct row-states, with sizes `10,20,5,10` (the two disjointness orbits have sizes `10+5`; the two intersection orbits `20+10`). Therefore exactly `2^4=16` undirected binary red-edge rules are invariant under every source transformation.

Testing all 16 by exact triangle and independence enumeration gives **four** triangle-free graphs with `alpha<=4`: two labelled instances of `C_5 ⊔ C_5` (10 edges), and two labelled instances of the Petersen graph (15 edges). The decoded incidence is consequently **not uniquely selected** by symmetry plus Ramsey admissibility.

## 4. Exhaustive valid one-vertex extension

At fixed Ramsey parameter `k=5`, any new vertex with red neighborhood `S` must satisfy `S` independent and `alpha(G-S)<=3`.

- `C_5 ⊔ C_5` has no valid new vertex. An independent neighborhood in each component misses an independent pair of that component. The union of the two disjoint missed independent pairs is a size-four independent set disjoint from the proposed neighborhood.
- The Petersen graph has exactly **five** valid new-vertex neighborhoods, precisely the five stars `M_i` (size four). All five extensions are mutually isomorphic.
- No valid second vertex can be added after a star `M_i` is attached. Let its new vertex be `v`, joined red to `M_i`. A second new vertex `w` would need an old-Petersen neighborhood `M_j` to hit all five old maximum independent stars. If `vw` were red, then `M_i∩M_j` would create a red triangle (always nonempty). If `vw` were blue, the remaining Petersen graph after removing `M_i ∪ M_j` has independence number 3, so `v,w` and that independent triple give a forbidden independent five-set. Both colors fail.

Hence the entire four-rule *source-equivariant* construction, followed by arbitrary legal one-vertex extensions without retaining symmetry, reaches **at most 11 vertices**, not the 13-vertex lower-bound witness required for `R(3,5)=14`. This is a source-first negative result, not an upper bound on `R(3,5)`.

## 5. Independent comparison with the 13-vertex critical graph

The known `C_13(±1,±5)` graph has 13 distinct red four-cycles, whose vertex sets are translations of `{0,1,5,6}`. Each old vertex lies in four of those cycles. Removing any three vertices destroys at most 12 of the 13 four-cycles, so every 10-vertex induced subgraph retains a red four-cycle. The Petersen graph has girth five. Thus the known 13-vertex graph has **no induced Petersen subgraph**. This separately rules out the simplest addition of three vertices to the Petersen decoder.

The known 13-vertex graph was not used to generate the ten row states, select candidate red-edge orbitals, or test their terminality.

## 6. Meaning of the obstruction

The five-symbol row and the literal position operations determine a ten-state affine orbit, not a 13-state graph. Decoding disjointness produces a genuine triangle-free Ramsey-compatible graph with `S_5` symmetry, but the seed alone does not choose that decoder, and *all* invariant decoder options stop by vertex 11. New vertex creation or a different incidence construction must enter **before** the 13-vertex threshold.

The literal permutation square-root of the analogous natural reflection on six positions also fails: it would square to an involution with three transpositions, impossible for any permutation of the six positions. A signed/continuous phase lift is possible, but is a different representation and does not itself generate binary incidence.

**Next discriminating target:** derive an *incidence-producing, vertex-creating operation* on the five-symbol source that is not equivalent to taking only the single affine orbit of ten two-point states. Test its graph outputs with the same unchanged red-triangle and independent-set constraints; do not insert the order 13 or the `C_13` graph as inputs.
