# Comparing two gluing-tree arrangements

## Three-piece reassociation

`agda/ClosureGluingReassociation.agda` compares the two bracketings of a chain with three pieces A, B, C and two shared boundaries S, T:

`A <- S -> B <- T -> C`.

One realization first glues A to B, then attaches C. The other first glues B to C, then attaches A.

`associate` and `unassociate` are explicit maps of the nested homotopy pushouts. Their definitions cover every point inclusion and both attachment-path families. Their section and retraction laws are proved on those same constructors, yielding `reassociation : Left ≃ Right`.

The theorem allows arbitrary small types and attachment functions. It does not assume the pieces or boundaries are sets, or that either boundary is empty.

## Connection to actual refinement trees

The module builds both depth-two gluing trees. The left tree uses the constructed reassociation as its parent realization equivalence into the right-associated root; the right tree uses the identity parent equivalence.

Cuts now range over a dependent sum of the cuts of both arrangements. This extends the comparison beyond changing the frontier of one fixed tree.

Fully exposing a nested gluing tree reconstructs its attachment maps through child frames. Therefore its interpreted type must not simply be identified judgmentally with the original nested pushout. The comparison retains these refinements:

1. assemble the fully refined left tree into its raw left-associated pushout;
2. apply the independently defined reassociation map;
3. unfold into the fully refined right tree.

`throughReassociation` is this composite.

## Actual map and compatibility witness

The common-reference model uses the fully refined left realization as its fixed input, and the right-associated root as its common output realization.

The identity function is admitted as an independently given compatible presentation at the left arrangement. The reassociation composite is separately admitted at the right arrangement with its inverse-law compatibility square.

The module proves:

- `generatedIsReassociation`: the generated right-hand view is the actual framed reassociation composite;
- `changedIdentityIsReassociation`: changing the independently supplied identity presentation produces that same function;
- `changeMatchesReassociation`: the complete changed compatible presentation agrees with the independently admitted one, including its square witness;
- `cycleIsTrivial`: the reference-based typed cycle visiting cuts of both arrangements is null-homotopic.

The chosen frames deliberately use this constructed associator. These statements do not identify unrelated previously chosen universe paths or associator witnesses with the generated paths.

## Nontrivial topology regression

`agda/ClosureGluingReassociationRegression.agda` specializes the pieces to three points and both boundaries to Bool. Each two-point attachment boundary contributes a loop.

The regression checks that reassociation preserves both displayed loops. Two maps to the circle distinguish their behavior: the first detects the first loop and sends the second to reflexivity; the second does the reverse. Each loop is proved nontrivial using the earlier circle-monodromy obstruction.

This checks more than the point inclusions, without asserting a complete classification of the example's loop space. The loops are displayed at their respective vertices; no unjustified equality between differently based paths is used.

The generated comparison and cross-arrangement cycle theorem are also instantiated on this example.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureGluingReassociationRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`, without holes or postulates. Their closure rechecks the earlier gluing and dependent-boundary regressions. Existing source modules were not changed in this increment.

During incremental checking, a collision with the imported name `terminal` was fixed by renaming the local attachment function. Explicitly typed inclusion functions resolved ambiguous nested pushout constructor inference in the regression.

## Next coherence obligation

This constructs and integrates a three-piece reassociation. The next concrete obligation is a four-piece pentagon comparing composites of these actual reassociation maps. It is not supplied merely by naming the existing compatible-fiber coherence theorem.

Analytical realization data, arbitrary gluing diagrams beyond this chain pattern, identification with older independently chosen cofiber-pentagon witnesses, and unbounded-depth completions remain separate.
