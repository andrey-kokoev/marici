# D8 port gluing: first realized target

## Construction

For each alternating square in a complete red/blue graph, take the verified local D8 model: four positions, eight framed ports, eight directed perimeter arrows. Give its four local positions the physical vertex labels of that square.

Glue position occurrences with equal physical labels. Glue port occurrences **only** when their directed source and target labels agree. Ports at the same node pointing to different nodes remain distinct. This realizes the proposed state–arrow correspondence globally without forcing each physical node to have only two outgoing directions.

Each square remains an injectively embedded patch. Its two color moves commute at the level of endpoints. Attach a square 2-cell imposing the corresponding path relation. Arrow reversal, source/target maps, and fixed red/blue colors descend to the quotient.

For a shared directed arrow with local states s_i,s_j, use the D8 transition

g_ji = s_j s_i^{-1}.

This maps the framed state and its arrow endpoints correctly; it also maps the reversed arrow with the same transition. Since the physical color is fixed, these transitions lie in the V4 subgroup. On triple shared-port overlaps the group products satisfy the cocycle identity.

These are **port-overlap transitions**, not one rigid coordinate change for every shared bare position. The distinction is essential: a bare vertex may appear in two patches with no shared outgoing port there. Requiring a single D8 coordinate change across their entire bare-position intersection is stronger and fails for every pair of distinct C5 charts in this construction. The checker records those failures rather than claiming a rigid global D8 atlas.

## Tested assemblies

| Quantity | Five-cycle coloring | Six-node red matching |
|---|---:|---:|
| Physical nodes | 5 | 6 |
| Alternating square patches | 5 | 6 |
| Local position occurrences | 20 | 24 |
| Local flag occurrences | 40 | 48 |
| Glued framed ports | 20 | 30 |
| Glued directed arrows | 20 | 30 |
| Basic port gluing | Pass | Pass |

The agreed incidence/state–arrow rules **do not reject the matching counterexample**. Both admit consistent quotients. D8 alone has not supplied the missing Ramsey obstruction.

C5 has 20 pairwise shared-port transition checks and no triple shared-port overlaps, so its triple condition is vacuous. The matching has 24 nonvacuous triple-overlap cocycle checks. These are local overlap checks, not an assertion of trivial transport on all global loops.

### Node minimum: what was and was not optimized

For each prescribed assembly, every pair of physical nodes lies in at least one patch. Any further node identification would collapse two distinct vertices inside a patch. Thus the displayed quotients have minimum node counts five and six **with these prescribed seams and patch embeddings**.

This is not a minimization over every possible way to glue abstract square charts. The original endpoint incidences are input constraints. The numbers cannot be advertised as deriving the Ramsey threshold from D8 alone.

## A geometric distinction: closed square surfaces

Separately test an optional stronger target:

1. Every undirected edge belongs to exactly two square faces.
2. Every vertex link is one connected cycle.

These are the standard local conditions for this finite square complex to be a closed surface. They were measured separately, not silently included in basic gluing.

### Five-cycle: a torus

Each of its ten edges belongs to two faces. Every vertex link is a four-cycle. Face orientations can be chosen compatibly. The connected square complex therefore is a closed orientable surface with

V=5, E=10, F=5, χ=0.

By surface classification it is a **torus**. The independently computed F2 Betti numbers are (1,2,1).

This is a concrete global object: five local Klein-four squares glue to a toroidal carrier with a bijection between 20 global ports and 20 directed arrows. The global port space is not itself the eight-state D8 torsor; D8 remains local chart structure.

### Six-node matching: boundary and branching defects

Its twelve blue edges belong to only one square each. Its three red edges belong to four squares each. Each vertex link is a four-leaf star rather than a cycle.

Thus it has exposed blue boundaries and branching along red edges; it is not a closed surface. Its Euler characteristic is −3 and F2 Betti numbers are (1,4,0).

This gives a genuinely geometric way to distinguish the two examples, without explicitly prohibiting monochromatic triangles. But the choice to require a closed surface is an **additional hypothesis**.

## Immediate asymmetric limitation

Every face alternates red and blue. A closed vertex link must therefore alternate incident red and blue edges, forcing

d_R(v)=d_B(v)

at every physical node. Globally, closed edge incidence likewise forces equal numbers of red and blue edges.

If the one-skeleton is a complete graph on n nodes, then n−1 must be even. In particular, **no eight-node complete coloring can form this closed alternating square surface**, regardless of how its alternating faces are selected or repeated while retaining closed manifold incidence.

Therefore the closed-surface condition cannot be a universal gluing criterion for R(3,4): it excludes all the critical eight-node colorings already enumerated. It is a meaningful symmetric carrier target, not the sought general Ramsey law. An asymmetric extension would need an independently motivated boundary or incidence structure, not just the same surface rule with a new numerical threshold.

## Reproduction

```sh
python research/chatgpt/ramsey/check_state_transport_d8.py
python research/chatgpt/ramsey/check_d8_port_gluing.py
```

The second checker writes `d8_port_gluing_results.json`: explicit charts and transition elements, port/node counts, rigid-overlap failures, vertex links, edge incidences, orientability and homology counts. It uses only the Python standard library. Earlier audits are unchanged.
