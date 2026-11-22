# Understanding Ramsey Systems

Color every pair of vertices red or blue. A $(3,k)$ system avoids two configurations: three vertices with every pair red, and $k$ vertices with every pair blue. Draw only the red edges. The first condition says the graph is triangle-free; the second says its largest independent set has fewer than $k$ vertices.

A construction and an upper bound answer different mathematical problems. Building a $(3,7)$ system on 22 vertices proves that $R(3,7)$ is at least 23. Showing that this graph cannot take another vertex explains why this particular construction stops. To prove the upper bound one must exclude *every* graph on 23 vertices, not just extensions of this one.

## What the project understands by case

$R(\ell,k)$ is the least number of vertices on which every red–blue coloring contains either a red clique of size $\ell$ or a blue clique of size $k$. Swapping the colors gives $R(\ell,k)=R(k,\ell)$. The number column is background: established values or published inclusive bounds, not claims of discovery. The other columns distinguish what the project constructed, checked or explained from what the same work does not establish.

| Case | Established $R(\ell,k)$ | Project result | Limit of that result |
|---|---:|---|---|
| $(2,k)$ | $k$ | Baseline only: forbidding a red edge forces all pairs blue. | No project computation is needed. |
| $(3,3)$ | 6 | The pentagon is a building block in either color. In each color, a directed edge has a unique continuation without immediate reversal. | That continuation describes the witness; it does not exclude order six. |
| $(3,4)$ | 9 | Glue two pentagons along two vertices. Sharing a red edge permits 12 labeled fillings giving all three eight-vertex types; sharing a blue edge permits none. | Exhaustive for the specified overlap. It explains the eight-vertex outputs, not the upper bound. |
| $(3,5)$ | 14 | On the cyclic 13-vertex witness, exchanging vertices in independent four-sets produces a four-set missed by any proposed independent neighbourhood. No fourteenth vertex can attach. | Terminality of one graph is not a general upper-bound argument. |
| $(3,6)$ | 18 | Across all seven 17-vertex cores, independent five-sets that meet a neighbourhood in exactly four vertices, but are not neighbourhoods, already force three new independent ports to overlap. | The row test is catalogue-wide at order 17, not universal at the next size. |
| $(3,7)$ | 23 | A six-point incidence rule constructs a 22-vertex witness on the empty set, singletons and pairs. Separately, weighted independent five-sets obstruct six simultaneous attachments in each of 39 residual cases for order 23. | The obstruction relies on the completeness of the residual classification. The inequality is uniform; its weights are not. |
| $(3,8)$ | 28 | The four-port square rule constructs 26-vertex witnesses from 69 of the 191 order-22 cores. A different seven-label wiring search constructs a 27-vertex witness. | The square rule stops short of 27; the wiring search takes the address system as input. |
| $(3,9)$ | 36 | On 32 held-out order-27 cores, using an eight-vertex block alongside pentagons raised the number yielding a 30-vertex witness from one to 14. | This tests transfer, not extremality. Unrestricted disjoint supports succeeded on 30 of the 32. |
| $(3,10)$ | 40–41 | A pentagon description reconstructs Exoo’s 39-vertex witness. A search from the target alone reaches 38 and excludes 39 within the tested cyclic class. | Recovering offsets from a witness is not deriving them. Neither result decides whether a 40-vertex witness exists. |
| $(4,4)$ | 18 | A 17-vertex witness validates the two-color gluing checker beyond triangle-free graphs. | An implementation check, not an exhaustive generation. |
| $(4,5)$ | 25 | External comparison only: a formal proof shows how splitting at a vertex and checking all gluings can certify an upper bound. | The project did not reproduce that computation. |
| $(5,5)$ | 43–46 | Overlapping neighbourhoods give a quadratic consistency check that rejects incidence data admitted by the tested linear relaxation. | This separates two tests, not two Ramsey bounds. It does not exclude all 45-vertex candidates. |

## Three link colors can specify a wiring

For the fixed seven-label $(3,8)$ address table, the readout `[02;13,34,36]` means: at reference `02`, read the colors of the links to `13`, `34`, and `36`, in that order. With red as 1 and blue as 0, the eight legal labeled wirings give the eight binary triples exactly once. This is more than a lookup key: given those three bits and the table constraints, a decoder recovered the other 77 link colors in every case by testing hypothetical colors up to two levels deep. The vector specifies a **wiring on a given table**, not a vertex position or a way to derive the table from $(3,8)$ alone.

The same notation exposes a difference between cases. For $(3,7)$, even *all* link colors at one reference fail to distinguish the 288 legal labeled wirings of the six-label table. For $(3,9)$, `[2;4,5,26]` distinguishes eight transported wirings in the cyclic chart. Two triples differing in one, two, or three bits correspond respectively to wirings differing on 42, 74, or 96 of the 193 candidate links.

## The cost of adding a vertex

Call a new vertex a *port* and its set of old red neighbours its *support*. The support must be independent: a red edge inside it would close a triangle through the port. But a support cannot simply be made small. Every old independent set it misses can grow by taking the port. If two ports are red-adjacent, their supports must also be disjoint; a common neighbour would close another triangle.

For three mutually nonadjacent ports the tradeoff is exact. Suppose the largest old independent set has size $a$, and the enlarged graph must have independence number at most $a+1$. Every old independent $a$-set must meet at least two supports, and every independent $(a-1)$-set must meet at least one. Indeed, an old independent set can take precisely those ports whose supports it misses. An $a$-set can afford to miss one port, an $(a-1)$-set can afford to miss two, and a smaller set can afford all three. This argument does not assume the supports are disjoint.

## When supports must overlap

On all seven catalogued 17-vertex $(3,6)$ cores, any three disjoint supports leave an independent five-set meeting fewer than two of them. Even a restricted family of five-sets forces this failure: those for which some old vertex sees four members but none sees all five. The same obstruction does not persist at every size. Of the 191 catalogued 22-vertex $(3,7)$ cores, 28 admit disjoint supports meeting every independent six-set at least twice. Only 17 of those also meet every independent five-set at least once.

Sharing a vertex spends degree. In a triangle-free graph the neighbours of each vertex are independent, so a graph of independence number six has maximum degree at most six. In the observed five-port attachments shaped like $K_{2,3}$ minus one edge, the endpoints of the missing edge share an old vertex of degree four. Those two incidences take its degree to six. The three ports on the same side also need an overlap, and the vertex already at degree six cannot supply it. This accounts for the failure on a 17-core with only one degree-four vertex. The first shared vertex is a catalogue observation; it is not a theorem about every missing-edge attachment.

## A shortage of distinct neighbours

For disjoint supports, let $R$ be the old vertices left outside all three. Write $\alpha(U)$ for the independence number on a vertex set $U$. The port test is equivalent to two bounds: $\alpha(R)\le a-2$, and $\alpha(R\cup S)\le a-1$ for each support $S$. The first excludes a large set missing every support. The second excludes a maximum set meeting at most one.

Fix an independent subset $J$ of $R$. The largest independent set in $R\cup S$ whose leftover part is exactly $J$ consists of $J$ and every vertex of $S$ with no neighbour in $J$. Thus if $|S|=a-1$, the second bound says precisely

$$|N(J)\cap S|\ge |J|.$$

One leftover vertex needs one neighbour in each support. Two leftover vertices cannot both rely on the same sole neighbour: sharing that neighbour makes them nonadjacent, so they can enter an independent set together. The shortage need not appear in a pair. Four independent vertices can collectively see only three members of a support even when every three see enough.

The difference is measurable on the 22-vertex cores. Reserve seven leftover vertices containing three disjoint edges and partition the other fifteen into independent fives. Across the catalogue, 7,541 core–leftover choices admit a partition satisfying the neighbour bound through pairs; 127 admit one satisfying it through triples; 31 admit one satisfying it through fours. Three disjoint edges leave room for at most four independent vertices among the seven, so there is no fifth test.

## Smaller Ramsey graphs as building blocks

A shortage disproves a proposed support. A partition can prove one works: the independence number of a region is at most the sum of the independence numbers of its blocks, regardless of any additional edges between blocks.

Start with $K_4$ and replace two opposite edges by paths of length three. The resulting eight-vertex graph is triangle-free and has independence number three. Its four original vertices induce a four-cycle. If an independent set uses at most one original vertex, it can add at most one internal vertex from each path. If it uses two, they are the endpoints of one replaced edge; neither internal vertex of that path can be added. Together with two disjoint edges, this graph therefore bounds the independence number of a twelve-vertex region by five.

The same block gives a forward construction at the next level. On a 27-vertex core of independence number seven, choose two disjoint independent six-vertex supports. Their complement has fifteen vertices. If it contains a partition into the eight-vertex block, a pentagon and an edge, its independence number is at most $3+2+1=6$. Three disjoint pentagons give the same bound. Either partition certifies that no old seven-set misses both supports.

Now find three supports for which every pair has such a certificate. If the nine leftover vertices contain four disjoint edges, their independence number is at most five. The seven-set and six-set obligations are both met: adding the ports gives a triangle-free graph on 30 vertices with no independent nine-set.

On 32 held-out cores, pentagons alone gave a construction on one. Allowing the eight-vertex block gave constructions on 14. An unrestricted disjoint-support search succeeded on 30. The difference between one and 14 demonstrates a use for the smaller Ramsey graph beyond describing a finished example. The remaining 16 successes that the block rule missed do not, on their own, establish that another block is needed: support size and the reserved matching were restrictions too.

## Construction versus reconstruction

A pattern in a finished witness need not explain how to choose it. In a trace of local moves, for example, the same observations admitted two histories: in one the labels stayed fixed; in the other they followed a change of starting point. Replaying the sequence could not distinguish those histories. A symmetry visible after a graph has been built can have the same ambiguity.

The block construction makes a narrower claim that can be tested: choose supports by a rule fixed before seeing the target, then check the graph it produces. A successful tiling proves an extension exists. A failed tiling rules out that certificate, not the extension. Keeping those conclusions separate is what makes the rule useful on the next core.
