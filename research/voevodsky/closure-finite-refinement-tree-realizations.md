# Finite split refinement trees generate coherent cut presentations

## Constructed structure

`agda/ClosureRefinementTrees.agda` adds finite binary input and output refinement trees to the existing reference-operation model.

Each input fork carries a local equivalence from the sum of its two child types to the parent. Each output fork carries a local equivalence from the parent to the product of its two child types. Leaves need no further refinement.

These are split sum/product trees, not arbitrary homotopy-gluing or dependent-family trees. The constructors require the actual local equivalences; a branching shape does not manufacture them.

## Cuts are independently pruned frontiers

For a fixed tree, a cut either stops at a node or exposes both children with independently selected cuts. Thus different branches can stop at different depths.

`InputAt` interprets an exposed input fork as a sum of its child presentations. `OutputAt` interprets an exposed output fork as a product. A stopped node keeps its parent type as one visible component.

This follows the selected interpretation "for every input index, a function": inputs are alternatives, not a tuple of all input values consumed jointly.

Although trees contain type labels and live in Type1, the cuts of any fixed tree are small types. They can therefore be passed directly to the previously checked framed-cut machinery without changing its universe assumptions.

## Local-to-global realization frames

`inputFrame` and `outputFrame` recursively derive equivalences between each cut presentation and the root type. They use closure of sums/products under equivalence and composition with the local node equivalence.

Global equivalences for every cut are not separately assumed. They are constructed from the local tree data.

`Realization` takes one root operation F:A->B and the two trees. It instantiates `ClosureReferenceNormalForm.Model` with the automatically generated cut types and frames. Consequently:

- every pruning has a generated presentation of F;
- compatible independently constructed presentations can be normalized;
- finite cut routes have typed-realization normal forms;
- the reference-based closed cycles are null-homotopic;
- all finite globular coherence levels are available for compatible presentations.

The local node equivalences remain real mathematical obligations. No analytical realization has been assumed by deriving the global frames.

## Actual depth-eight test

`agda/ClosureRefinementTreeRegression.agda` builds right-growing trees recursively for arbitrary natural-number depth. At each input fork, the left branch stops while only the right branch continues.

The concrete root types are actual cofibers from the earlier pointed-target construction. Its input target is a nested sum of nine circles; its output target is a nested product of three circles. The underlying map is the already constructed canonical cofiber transport induced by a function sending the first input circle to the first output circle and sending the other input components to the base output.

The first node frames come from the checked pointed-target cofiber equivalences. The deeper nodes expose the sum/product structures of the chosen target types by identity equivalences. This is a controlled inhabited example, not a discovered splitting of an unspecified analytical object.

The regression proves:

- input structural depth = 8;
- output structural depth = 2;
- fully exposed input frontier width = 9;
- fully exposed output frontier width = 3;
- a cycle through root-only, partially exposed, and fully exposed cuts is null-homotopic as a typed-realization loop;
- the fully refined actual operation maps an entire circle loop to the corresponding output loop;
- the all-finite-globular-level theorem is available at every pruning.

Thus depth eight is actual tree nesting, not eight homotopy dimensions and not uniform insertion of eight indices on every branch. The two sides need not have equal depth.

## Invalid local split is excluded

The `SplitGate` regression proves that Unit cannot be assembled equivalently from Unit + Unit. Such a local input fork therefore cannot enter the construction merely because its binary shape can be drawn.

This is separate from the positive example, where every required local equivalence is supplied by an actual construction.

## Verification

Fresh check of the final source:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureRefinementTreeRegression.agda`

Exit 0. Both new modules use `--safe --cubical --guardedness`, with no holes or postulates. Existing source modules were not modified.

## Scope and remaining work

This supplies arbitrary finite binary tree shapes with certified split nodes, independently pruned cuts, and their connection to the existing common-reference/coherence architecture.

Still separate are dependent or infinite branching, non-split homotopy-gluing node constructors, and analytical evidence for the intended local decompositions. Routes here move among prunings of fixed trees; identification with previously chosen cut-pentagon witnesses or tree-reassociation paths remains an explicit comparison task rather than an automatic relabelling.
