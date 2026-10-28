# Reconstructing Sulfur's four-stage operation skeleton

**Result: a concrete incidence skeleton for the four-stage hypothesis, not yet its operation law or completed wiring.** No route, coefficient meaning or phase action was added.

## 1. What prior research actually supplies

The current operator recollection proposes:

1. split by additivity;
2. split by multiplicativity;
3. split quartic effects;
4. reconcile quartic effects.

The reviewed Sulfur specification records directional separation, four cross-pairings and shared-reference comparisons. It does not use the additive/multiplicative/quartic terminology or define a quartic algebra. Thus this review treats the recollection as a hypothesis to reconstruct, not a quotation independently recovered from that document.

A relevant earlier source was recovered:

- `research/nima/binary-arity-square-is-the-duoidal-skeleton.md` supplies rooted substitution and cut coaction as two distinct composition actions, with a mixed Beck–Chevalley interchange.
- `research/nima/gray-coherence-cube-refactors-the-arity-tetrahedron.md` distinguishes those actions, comparison of their two orders, and coherence of that comparison.
- `research/strominger/primitive-packet-type-instance-v1.md` explicitly warns that constructor position does not establish quadratic/cubic/quartic degree.
- `research/strominger/routing-and-quartic-experiments-v1.md` distinguishes four-input structure, quartic interaction energy, cubic response and fourth-order correlations.

The duoidal source offers an actual four-input comparison schema:

```
(a box b) tensor (c box d)
        ->
(a tensor c) box (b tensor d).
```

Its two operations are not automatically the operator's addition and multiplication. Its strict law holds on a marked transverse occurrence system; Sulfur's shared references do not by themselves establish that hypothesis. The inspected small source checker uses a disjoint-labelled-union fixture, not a Sulfur adapter. No other-owner theorem or fixture was silently imported as a native filling.

## 2. Separate operations from slices

Sulfur has nine cell-centre slices and eight successive interfaces. The entrance-to-middle half has four interfaces, between slices 1 and 5. This provides positions for four functional stages without claiming four stages equal four isolated cells or four independent signal orders.

The fresh checker examines actual coordinates and incidences, for all six readings of both edge three and edge five. Transverse grid dimensions are verified as Cartesian sets, not guessed from counts.

### Proposed Sulfur alignment

| Functional stage | Native restriction | Established operands/outputs | Missing operation |
|---|---|---|---|
| 1: additive separation | Slice 1 N to slice 2 P/E | One incoming N; two P and two E reference occurrences | A source-defined additive splitting map and its ownership/retention law |
| 2: multiplicative separation | Slice 2 to slice 3 N | Four N occurrences, exactly one for every P-reference/E-reference pair | A source-defined multiplicative pairing/refinement operation; not merely a count of four |
| 3: quartic-effect separation | Slice 3 to slice 4 charged cells | Eight outer single-input cells plus four central shared-reference comparisons | What 'quartic' denotes, and the maps carried by these comparisons |
| 4: reconciliation | Central slice-4 comparisons to slice 5 N | All four central comparison cells meet one common N endpoint | A simultaneous reconciliation witness, including compatibility with the retained outer branch data |

The last two rows are a proposed operational reading, not a recovered equation. The eight outer cells remain in the obligation inventory; the central comparison subdiagram does not replace the full carrier or its peripheral routing.

## 3. The first joint layer is a real reference product

At slice 2 there are two P references and two E references. The four slice-3 N cells realize every reference pair exactly once.

For each joint N there are two actual two-interface presentations:

```
incoming N -> its P reference -> joint N
incoming N -> its E reference -> joint N.
```

These are four native incidence diamonds. They give a concrete place to test two-order comparison, but their arrows have not yet been identified with the two operations of the duoidal source.

At slice 4, comparisons connect joint N occurrences sharing one reference and differing in the other. This is stronger than a four-way count: the actual operand/reference identities are retained.

## 4. Reconciliation has a specific boundary

The four central slice-4 comparison cells have a unique common N neighbour in slice 5. At edge three this is the carrier's central N.

Between the incoming N in slice 1 and that endpoint lie exactly the already identified:

- 16 four-interface presentations;
- 20 elementary comparison-context moves;
- 14 cells: 4 P, 6 N, 4 E;
- native vertex-link sphere-sweep boundary.

This reconnects the four-stage hypothesis to the earlier sphere result **without** introducing Hopf phases or spatial charges. The sphere supplies the shape of a reconciliation obligation, not its answer.

Sulfur has six such residual cones over the entire carrier. In any one reading their starting-slice counts are:

```
slice 1: 1 cone
slice 3: 4 cones
slice 5: 1 cone.
```

Thus the entrance cone and its exit-side counterpart are not the whole global problem. Four additional cones overlap the middle. A reconciliation law must work on that common incidence simultaneously; checking one entrance-to-middle cone is insufficient.

The prior six-peripheral-channel incidence assignments do not force the central N to be exclusively unused ground, nor do the present comparison incidences establish a physical use for it. Reconciliation support and payload routing remain distinct questions.

## 5. Extension to edge five: what is justified now

The positive-half grid pattern is

```
N: 1x1 -> 2x2 -> 3x3 -> 4x4 -> 5x5,
```

with intermediate P/E rectangles of sizes `(k+1)xk` and `kx(k+1)`, up to exchanging transverse axes and roles with the reading.

The same first four-interface comparison cone still ends at slice 5. But slice 5 is now **before** the physical middle, which is slice 9. The four-stage local boundary therefore does not require changing its arity merely because the side increases.

Across the full edge-five carrier, the 44 residual cones begin at slices

```
1, 3, 5, 7, 9, 11, 13
```

with counts

```
1, 4, 9, 16, 9, 4, 1.
```

This supports a candidate generalization: reuse the source-bound four-stage comparison law on a larger, overlapping incidence system and impose its overlap coherence. It does **not** prove that law exists, that repeated application constructs the global object, or that larger sides automatically introduce eighth-/sixteenth-order interactions. Nor may the carrier be replaced by independent copies of the entrance cone.

## 6. The next source adapter, now specified

Before numerical or route construction, supply:

1. The additive and multiplicative constructors on the retained signed-pair object, including domains and output/ownership types.
2. A map from their operations and operands to the two reference-family refinements in the four native diamonds.
3. The four-input effect/comparison object and what 'quartic' means in its grading or operation type.
4. The reconciliation map on the actual 16-presentation boundary, preserving lower records and outer-branch compatibility.
5. The source theorem's hypotheses on every overlapping cone. If the relevant cut/factor incidences are nontransverse, a strict identity from the transverse theorem cannot be substituted for the required witness.

This is a global specification task followed by local restriction checks, not a return to greedy local route generation. All six Sulfur cones and the complete boundary remain in scope from the outset.

## Replay

```sh
node research/strominger/checkers/check_sulfur_operation_reconstruction.mjs --record
```

Receipt: `results/sulfur-operation-reconstruction-v1/verification.json`.

It retains all twelve size/reading cases, complete half-carrier grid coordinates via cell identities, the four entry diamonds, actual shared-reference operands, retained outer cells, the first four-interface cone and all cone-start populations. `constructionAdmitted`, `operationBindingAdmitted` and `quarticMeaningEstablished` remain false. The older source theorem checkers were inspected, not freshly rerun or modified.
