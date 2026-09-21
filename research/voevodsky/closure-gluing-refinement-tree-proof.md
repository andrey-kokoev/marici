# Gluing nodes with independently refined shared boundaries

## Implemented extension

`agda/ClosureDependentRefinementTrees.agda` now includes `glueNode` alongside dependent Sigma and Pi nodes.

A gluing node supplies:

- a left type L, shared-boundary type M, and right type R;
- attachment maps f:M->L and g:M->R;
- a proved local equivalence Pushout(f,g)≃A to the parent realization;
- child refinement trees for L, M, and R.

A cut can stop at the parent or expose the gluing while choosing the three child cuts independently. Thus the shared boundary is itself refinable, not frozen or discarded.

The gluing is a homotopy pushout. Every boundary value contributes an attachment path. It is not a disjoint sum or a set quotient.

## How the refined span is constructed

`agda/ClosurePushoutRefinement.agda` gives the reusable span construction. Let eM, eL, eR be the child frames from the refined boundary and pieces to the original ones.

The new attachment maps are:

- refinedLeft = inverse(eL) composed with f composed with eM;
- refinedRight = inverse(eR) composed with g composed with eM.

The inverse laws of eL and eR provide the two commuting-square witnesses. The library pushout-equivalence theorem then constructs the equivalence between the refined and original pushouts.

`onAttachment` exports its full action on a gluing path: the original attachment is surrounded by the left and right frame-adjustment paths. Those adjustments cannot generally be dropped, because the endpoints only agree by homotopy.

The equivalence witness is kept abstract to avoid expensive unfolding of large inverse proofs. The forward map and its point/path constructor equations remain transparent.

## Recursive interpretation

`At` and `frame` in the dependent-tree module are now mutually recursive on strictly smaller child trees. The interpreted type of a gluing cut needs the child frames to construct its attachment maps. The resulting pushout equivalence, composed with the local parent equivalence, supplies its global frame.

Agda checks this recursion under `--safe`; no termination bypass was added. The node uses the existing depth-bound discipline.

The common-reference views, cut-route normal forms, compatible higher comparisons, and null-homotopies for reference-based closed cycles are inherited from the same model as the Sigma/Pi cases.

## Circle regression

`agda/ClosureGluingTreeRegression.agda` uses the span

`Unit <- Bool -> Unit`.

Its homotopy pushout is equivalent to the circle. The boundary Bool is refined into two labelled point slots by a Sigma node, while the left and right pieces stay points. The resulting tree therefore mixes gluing with a dependent-sum refinement.

The test proves:

- the forward action on each refined attachment;
- the composite of one attachment with the reverse of the other maps to the circle loop;
- that composite is not reflexivity;
- a cut cycle exposing the gluing, refining its boundary, and returning is null-homotopic as a typed-realization cycle;
- no map to Bool can retain distinct false/true tags on the two glued vertices, since even one attachment would force false=true.

The nontrivial-loop proof reuses the previously checked circle-indexed Boolean-swap family. Thus the previous dependent-boundary regression is also rechecked in this test's dependency closure.

The original circle's loop survives inside the realization while changes of presentation have coherent return paths. These are different kinds of paths, not contradictory claims of contractibility.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureGluingTreeRegression.agda`

Exit 0. The helper and regression modules use `--safe --cubical --guardedness`; the extended tree module retains those options. No holes or postulates were added.

The initial incremental regression caught named implicit arguments to `leaf` in the wrong order. Reordering them resolved the elaboration issue. The previous dependent-family and twisted-boundary tests passed after the datatype extension.

Changes consist of two new Agda modules and the extension of `ClosureDependentRefinementTrees.agda`; earlier comparison modules were not rewritten.

## Scope

The model now supports bounded-depth trees mixing dependent sums, dependent products, and shared-boundary homotopy gluing. Global cut frames are derived from local realization equivalences and the actual attachment maps.

Local spans and their parent realization equivalences still need mathematical evidence. The code constructs the refined spans by canonical transport through child frames; comparison with independently supplied analytical attachment maps is an additional theorem.

Arbitrary re-association maps between distinct gluing trees, their identification with previously chosen cofiber-pentagon witnesses, unbounded-depth completions, and analytical realization functors remain separate tasks.
