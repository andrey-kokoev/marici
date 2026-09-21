# Dependent refinement trees retain genuine boundary twisting

## Extension

`agda/ClosureDependentRefinementTrees.agda` extends the local-to-global tree construction from binary sums/products to indexed dependent families.

Every node is explicitly labelled:

- `sigmaNode`: retain an index i and a value of its dependent fiber B(i);
- `piNode`: supply a value of B(i) for every index i.

Both kinds require a local equivalence between the displayed dependent type and the parent type. The label's meaning is not inferred from whether the node occurs on the input or output side. In particular, a Sigma boundary inside an output is not silently replaced by a product.

The natural-number parameter is a depth bound. A leaf may stop at any bound; each non-leaf consumes one level. Indices can be arbitrary small types, including the circle. Thus depth is bounded, but the node count or branch-index type is not asserted to be finite.

## Cuts and global frames

A cut either stops at a node or supplies a cut for each child. For a higher index type, that choice is a dependent function and must respect its paths; it is not an arbitrary disconnected list of choices.

`At` interprets the selected cut. `frame` recursively derives the equivalence from that cut to the root, using dependent-sum or dependent-product congruence on the family of child frames.

`sigmaObservation` checks that the selected base index is preserved, up to the explicitly supplied local equivalence. No uniformity of the fibers is needed.

`Realization` supplies these derived frames to the existing reference-operation model. Generated views, finite-route normal forms, compatible higher coherence, and triviality of the reference-based cut cycles remain available.

## Mixed output example

`agda/ClosureDependentRefinementRegression.agda` first builds a depth-bounded output tree with a Pi node over Bool and a Sigma node inside each output.

Each output contains a family value p:Bool->Bool together with a boundary R(p). Depending on p(false), that boundary is Unit or Bool. This reuses the earlier checked dependent-boundary model rather than assuming the residual is independent.

The root is an actual cofiber realization of this output type. The operation is the previously constructed cofiber transport induced by swapping the two output columns.

The regression computes both columns of the fully refined output, including their differently typed residuals. It also checks a cycle through a partially refined cut, where only one output's dependent boundary has been exposed.

## A genuinely higher-indexed, twisted boundary

The second example defines a family Cover over the circle:

- Cover(base) is Bool;
- transport around the circle loop is Boolean negation, specified by univalence of the swap equivalence.

The Sigma total type has a point (base,false) and an actual cofiber realization. A Sigma tree node unfolds that realization without changing the base observation.

The checked results include:

- `monodromy`: transport around the base loop swaps the boundary value;
- `liftedBaseLoop`: a path in the dependent total type from (base,false) to (base,true);
- `realizedLiftedLoop`: that path retained in the actual cofiber realization;
- `basePreserved`: the unfolded tree frame preserves the circle-valued observation;
- `noSection`: no global choice of one boundary value over every base point exists;
- `noCoherentTrivialization`: no coherent family identifying all fibers with one fixed Bool exists;
- `noProductAtRoot`: no product replacement with any constant residual type can preserve the selected circle observation of this cofiber realization.

The no-section proof extracts a hypothetical chosen section's path around the circle, obtaining a fixed point of Boolean negation. That contradicts true≠false. A product replacement would supply such a section by selecting a residual value from the inhabited total space, so it is excluded as well.

This is an obstruction over the chosen base observation. It is not a claim that the unlabelled total type has no other product representation.

## Why this does not contradict cut coherence

Presentation changes and motion inside the observed boundary family are different directions.

The common-reference construction removes avoidable ambiguity in the chosen presentation routes. It does not replace a dependent family by a constant one or erase its internal monodromy. A cut can unfold the twisted family faithfully while reference-based changes between those cuts remain coherent.

The indexed node metadata also does not manufacture inhabitants of a dependent product. The same example proves a product of all boundary choices is uninhabited, even though its dependent total space is inhabited.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureDependentRefinementRegression.agda`

Exit 0. Both new modules use `--safe --cubical --guardedness`, without holes or postulates. An initial incremental check caught a local name collision with the imported `section`; renaming it to `forbiddenSection` resolved the issue. Existing source modules were not modified.

## Remaining node types

The trees now support bounded-depth dependent Sigma/Pi refinement. General homotopy-pushout or gluing nodes with shared boundaries remain separate. Adding them requires the actual span maps, their attachment paths, and compatible comparison data—not treating a glued decomposition as a disjoint sum. Unbounded-depth completions and analytical realization maps also remain separate.
