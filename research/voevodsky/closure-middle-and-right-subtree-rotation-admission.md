# Rotation admission with arbitrary middle and right subtrees

## Proved family

`agda/ClosureMiddleSubtreeRotationAdmission.agda` admits the actual rotation

`(A Q) R -> A (Q R)`

where A is a leaf and both Q and R are arbitrary finite bracketed subtrees. The comparison uses the existing normalizer of the fully expanded word, not an unrelated three-block reference object.

There are no invertibility or truncation assumptions on the attachment maps. The required component realization equivalences are constructed by normalization.

## Reusable comparison coherence

`agda/ClosureSpanComparisonCoherence.agda` adds two supporting results.

`MiddleRightNaturality` proves naturality of the native associator when the middle and right pieces are both replaced by equivalent realizations. It checks the point constructors and both attachment families, retaining the supplied commuting-square paths.

`RightComposition` compares two successive right-piece pushout comparisons with the comparison formed from their composite frame and composite square. The attachment case uses preservation of path composition, associativity, and reversal of a composite. It proves equality of the actual maps and of the resulting equivalences.

This composition law is proved explicitly rather than assumed as a coherence field.

## Normalization square

The normalization frame of `(A Q)` agrees with its underlying span-comparison frame. Its last-endpoint witness contains a trailing identity composition. `subLastPath` removes that trailing identity while retaining the actual endpoint path coming from Q; it does not declare Q's path trivial.

The two full normalization maps are then expressed through the span comparisons. Naturality moves reassociation across the component frames, and the composition theorem combines the right-side comparisons with the correct square.

The resulting `rotationSquare` admits the independently defined native associator. The inverse associator is admitted as well. The module proves equality with the generated comparison and compares the complete compatible presentation, including its witness.

## Word-reindexed form

The previously constructed `ReindexRotation` interface is also instantiated for this entire left-leaf family.

`reindexedSquare` follows the dependent path of normalization equivalences and the realization transport filler. It fills the interface's explicit normalization obligation and admits the actual reindexed native equivalence.

For a singleton left word, word associativity computes to reflexivity. Nevertheless, the proof retains the specified bracket and realization transport rather than silently deleting it.

## Twelve-piece regression

`agda/ClosureMiddleSubtreeRotationAdmissionRegression.agda` uses a two-piece middle subtree with a circle loop and a nine-piece right subtree of depth eight. The attachment maps are the noninvertible maps Bool->Unit.

The checks include:

- twelve pieces in the expanded word;
- source depth 9 and target depth 10;
- full compatibility of both the native and word-reindexed comparisons;
- null-homotopy of the actual native forward/backward type cycle;
- identity residual transport on every source inhabitant;
- preservation and nontriviality of loops inside both the middle and right subtrees;
- detectors that separately observe those two loops and ignore the other;
- agreement with the earlier arbitrary-right-subtree admission on their common specialization, as complete compatible presentations.

The right-subtree loop's basepoint identification remains explicit as a dependent path. The regression reuses the previously checked opaque large fixture and its exact system instantiation to avoid unnecessary expansion of its inverse certificates.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureMiddleSubtreeRotationAdmissionRegression.agda`

Exit 0. All three added modules use `--safe --cubical --guardedness`, without holes or postulates. The dependency closure includes the preceding subtree, admission, normalization, pentagon, gluing, and boundary regressions. Existing source modules were not modified.

## Remaining obligation

The first component A is still a leaf. Admission when the left component is itself an arbitrary variable subtree remains open. The general syntax, word-index reassociation, and native reindexed equivalence already exist; their general normalization square still needs the corresponding append-associativity and endpoint-coherence argument.

This is not yet a proof that every native local rotation, in every context, agrees with the generated normal-form comparison.
