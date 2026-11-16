# Facet attachment, retriangulation, and the first coherence cells

**Research note — 2026-11-09**  
**Status:** Self-contained combinatorial arguments and exact finite Python checks. No native Marici constructor added; no new formal Agda compilation; no Ramsey threshold derived.

## Problem and typing

The conjecture is that an R simplex tree, an opposed B structure, and coherence G might emerge together from one primitive. Prior tests based on a free directed edge source found no forced 2-cells. This note changes the carrier to actual abstract simplicial complexes and refuses to conflate three kinds of objects:

- **Spatial complex** `K`: an abstract collection of finite nonempty vertex sets closed under taking nonempty subsets. Its 2-faces are actual triangles.
- **Assembly states**: complexes reached by legal attachment operations; distinct histories can have equal final states.
- **Comparison cells**: cells in a separate space of assemblies or triangulations. Their existence does not, without a realization map, add a spatial triangle to `K`.

No metric, unitary effects, G filler, point reflection, degree uniformity, or final manifold is an input to the first test.

## Test 1 — Two independent triangle attachments

Start with `K0 = <012>`, the full triangle on vertices `0,1,2`. A legal elementary facet attachment along an exposed boundary edge `F` adds a full triangle `F ∪ {x}` with a **fresh** vertex `x`. Existing cells are never removed.

Let `a` attach `<013>` along `01` and `b` attach `<124>` along `12`.

- Both orders remain legal and yield the exact same abstract simplicial complex, `K_ab = K_ba = K_a ∪ K_b`.
- Its f-vector is `(5 vertices, 7 edges, 3 triangles)`; Euler characteristic 1; first homology mod 2 vanishes; all vertex links are intervals or circles. Its boundary has five edges and it is a disk.
- The edge `34` is absent. No face of either attachment includes both new vertices, so no mixed simplex can be derived by closing under subfaces.

A separate optional triangle `<134>` would add the **new** edge `34`, yielding `(5,8,4)`, also a disk. **That addition is not a legal move of the unchanged fresh-vertex facet-attachment grammar**: it uses an existing vertex and meets the existing complex along two edges. It is a countermodel to a uniqueness inference from incidence/manifoldness, not a claim that the facet-attachment grammar produced G.

**General conservativity statement:** If `K_a` and `K_b` are formed by gluing a simplex with new vertex `x` or `y` to the same `K`, and `x != y` are fresh, the canonical generated union `K_a ∪_K K_b` contains no simplex involving both `x` and `y`. Proof: every simplex of the union belongs to one of the two pieces; neither piece has both vertices. Thus mixed spatial simplices require a further constructor or relation.

## Test 2 — Attachment conflicts and source-defined admissibility

Attach `<013>` and `<014>` independently along **the same** exposed edge `01` of `<012>`. Each branch separately yields a disk. Their union has three triangular cofaces at edge `01`, violating the 2-manifold boundary/interior condition that an edge have one or two cofaces. This failure is monotone: adding more triangles cannot reduce that coface count. The two-step composite is correctly refused by the facet-attachment rule after either first attachment.

This is a genuine local-to-global obstruction obtained from elementary incidence **plus the stated manifold-preserving admission rule**. It is not an obstruction intrinsic to abstract simplicial complexes: their unrestricted union still exists as a nonmanifold complex.

## Test 3 — Three independent branches

Attach `<013>`, `<124>`, `<025>` to three distinct boundary edges of `<012>`, each with a new vertex.

- All `3! = 6` orderings are legal and result in the same complex.
- The spatial f-vector is `(6,9,4)` with six boundary edges: a four-triangle disk whose dual graph is a three-leaf star.
- The partial-assembly state set is the Boolean lattice `2^{\{a,b,c\}}`, with 8 states. Its order complex has f-vector `(8,19,18,6)` and is a triangulated 3-ball (six tetrahedra). The four-state Boolean lattice for two branches has f-vector `(4,5,2)` and triangulates a square.

All higher incidence comparisons among the **assembly states** are canonical because every subset determines one union of specified cells. They do not create missing triangles in the **spatial** simplicial complex. This is a typed distinction between assembly-level and space-level coherence.

## Test 4 — Replace facet growth by local retriangulation

To obtain nontrivial higher comparison shapes, consider a distinct, actual simplicial operation: a diagonal flip of the two triangles comprising a convex quadrilateral. It changes the triangulation but preserves the underlying polygonal region.

Enumerating every maximal set of noncrossing diagonals and all legal single flips yields:

| Convex polygon | Triangulations | Flip edges | Comparison structure |
|---|---:|---:|---|
| 4-gon | 2 | 1 | interval |
| 5-gon | 5 | 5 | one pentagonal cycle |
| 6-gon | 14 | 21 | 3D associahedron |
| 7-gon | 42 | 84 | 4D associahedron |

For a hexagon, the exact flip graph has **three square cycles and six pentagonal cycles**; each is characterized as the set of triangulations containing one fixed diagonal. A short diagonal partitions the hexagon into triangle + pentagon, giving five refinements (six diagonals of this type). An opposite-vertex diagonal partitions it into two quadrilaterals, giving four refinements (three diagonals of this type). These 9 cycles are the 2-faces of the associahedron and satisfy `V-E+F = 14-21+9=2` on its boundary.

The higher-comparison cells here arise from the **partial triangulation/refinement poset**, which determines the associahedron, not from the bare flip graph. In particular, the pentagon flip graph by itself has `π1 ≅ Z`: an explicit 2-cell/contractibility interpretation is needed to fill it. The conventional associahedron supplies precisely that interpretation. This construction is established mathematics, not a newly discovered generator.

## Test 5 — Point reflection on genuine triangulations

For the convex hexagon use the geometric half-turn `i → i+3 mod 6`, a genuine point reflection about its center. It acts by an involutive automorphism of the flip graph.

- Exactly 6 of the 14 triangulations are fixed by this point reflection.
- The other 8 form 4 reflected pairs.
- Three reflected pairs are separated by two flips, each with two distinct shortest flip histories. One pair is separated by four flips, with six shortest histories.

Thus point reflection does not always produce a *different* B, and it does not select a unique green comparison path even where R and B differ. In the filled associahedron all such paths represent the same relative-endpoint **homotopy class** (it is contractible), but the explicit histories remain distinct. Strict uniqueness of a selected word and uniqueness up to coherent higher comparison are different statements.

## Proof-level distinctions

1. **Necessary incidence-level relation:** For two independent fresh-vertex facet attachments, union is commutative/associative and order-independent (as a labeled complex). This gives an incidence-level comparison square.
2. **Necessary incidence-level obstruction under an explicit admission contract:** Two distinct cells added along the same previously exposed facet overfill that facet and violate the manifold condition.
3. **Not necessary:** Mixed spatial simplex between fresh branch vertices. It is absent from the free union.
4. **Necessary comparison boundary, not a filled cell:** The five triangulations of the pentagon form a 5-cycle under local flips. The 2-cell requires the established associahedral partial-subdivision interpretation.
5. **Not necessary:** Unique reflection partner different from R, unique shortest comparison history, a natural norm, closure to a manifold without boundary, or any Ramsey threshold.

## Falsifiable next theorem

Define an interpretation from an **incidence/retriangulation comparison calculus** into the user-intended spatial or operational coherence calculus. State:

- which facet attachments and flips are permitted by source rules;
- which partial-subdivision comparisons become actual 2-morphisms and higher coherences;
- whether reflection acts covariantly or contravariantly and what it preserves;
- how distinct retained histories remain distinguishable even when their geometric regions are identical;
- exactly when a 2-dimensional comparison becomes a **new spatial simplex**, instead of a relation between two triangulations.

The high-value discriminator is whether the *same unchanged realization rule* generates a green simplex for some branching source and refuses it for another, without imposing a target triangulation or Ramsey number.

## Relation to existing Marici research

- `research/nima/typed-generator-layer-2.md` retains path histories but requires separately supplied interpretation algebra.
- `research/strominger/source-incidence-selects-the-coherence-nerve.md` distinguishes simplicial, cubical and globular source incidence; the present calculations provide explicit examples of cubical attachment commutation and associahedral flip coherence.
- `research/nima/seed-native-promotion-binding-gate.md` blocks source-preserving filling of the original six-arrow free realization; this note does **not** replace that source with a claimed native filled primitive.

## Literature

- Garoufalidis, Hodgson, Rubinstein, Segerman, *Geometry & Topology* 19 (2015), Theorem 6.32: associahedron 2-cells are squares and pentagons; all flip-path differences are generated by those relations. https://msp.org/gt/2015/19-5/gt-v19-n5-p05-p.pdf
- *Connectivity of Triangulation Flip Graphs in the Plane*, *Discrete & Computational Geometry* (2022): polygon flip graphs are 1-skeleta of associahedra and partial triangulations describe higher faces. https://link.springer.com/article/10.1007/s00454-022-00436-2

## Reproduction

Run (Python standard library only):

```bash
python check_simplicial_composition.py
python check_flip_coherence.py
python check_reflected_flip_paths.py
```

The scripts check all reported finite counts, equality of attachment orders, boundary incidence, 2-manifold vertex links, mod-2 homology of the configuration order complex, diagonal-flip graphs, 4- and 5-cycles, and reflected shortest-path multiplicities. No Agda checking or physical interpretation is claimed.
