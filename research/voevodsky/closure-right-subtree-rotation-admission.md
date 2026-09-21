# Native rotation admission with an arbitrary right subtree

## Proved family

`agda/ClosureSubtreeRotationAdmission.agda` admits rotations of the form

`(A B) R -> A (B R)`

where A and B are leaves and R is any finite bracketed subtree. No invertibility, truncation, or emptiness hypothesis is imposed on the attachment maps or piece types.

The normalization square uses the existing normalizer of the fully expanded word. It is not merely a three-block theorem with an independently selected block-level reference realization.

## Native associator naturality

`RightNaturality` compares reassociation before and after replacing the right piece by an equivalent realization, with an explicit square relating its attachment maps.

Its proof checks all point and attachment constructors. The first attachment uses the path-unit law; the second uses preservation of double path composition. The attachment-square adjustments remain in the formula.

For the subtree application, the replacement equivalence is the recursively constructed normalization of R. Its `normalizeFirst` witness supplies the attachment square.

## Parent endpoint coherence

The proof combines this naturality theorem with the earlier two-leaf frame contraction and its endpoint witnesses.

On the right-hand tree, the normalization frame of the subtree `(B R)` is compared with the corresponding span comparison. Its first-endpoint witness is contracted along that frame comparison, rather than discarded.

`leftToForm` and `rightToForm` expose both normalization maps in terms of these comparisons. `rotationSquare` then proves compatibility of the independently defined native associator with the expanded-word normalizer.

Both native directions are admitted. The complete compatible presentation agrees with the generated one, and actual admitted routes inherit the existing closed type-route and residual-action theorems.

## General word reindexing

The same module separately constructs `appendAssociative` for arbitrary nonempty words.

`ReindexRotation` takes three arbitrary bracketed subtrees. It constructs:

- the native left and right bracketings;
- the right bracketing transported back to the left word index;
- a dependent path of bracket syntax witnessing that transport;
- the corresponding realization-type path;
- the corresponding dependent path of normalization equivalences;
- the native associator followed by realization reindexing, as an equivalence at a common word index.

This construction does not yet provide the general normalization square. `NormalizationSquare` states that remaining obligation explicitly, and `admit` requires its proof. The regression does not fabricate such a proof or call `admit` for that unrestricted case.

## Eleven-piece regression

`agda/ClosureSubtreeRotationAdmissionRegression.agda` uses a nine-piece right subtree of depth eight and two additional point pieces. Attachment boundaries are Bool, with noninvertible maps to Unit.

The checked rotation changes the full tree depth from 9 to 10 while retaining all 11 pieces. The test checks its full compatible comparison, the null-homotopy of the actual forward/backward type cycle, and identity residual transport.

Detectors retain the two outer attachment loops and a previously proved nontrivial loop inside the large right subtree. The internal detector's basepoint identification is tracked by a dependent path; the proof does not assume that identification is judgmentally reflexive. A null-homotopic image of the internal loop is ruled out.

A separate instance checks the word-reindexed native equivalence for three larger subtrees. It is not presented as an admitted normalized rotation.

## Verification and proof-checking boundaries

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureSubtreeRotationAdmissionRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`, without holes or postulates. Their dependency closure rechecks the earlier admission, normalization, pentagon, reassociation, gluing, and boundary regressions. Existing source modules were not changed.

Initial checks timed out while expanding indexed transport and large instantiated proof terms. Indexed bracket transport, the derived rotation square, and the large checked fixture are kept abstract at their interfaces. The regression also reuses exactly the existing system instantiation rather than a separate definitionally equal attachment-function alias. Endpoint and loop facts remain explicitly proved and exported. With these boundaries, the final fresh closure check completed successfully. Temporary smoke-test files were removed.

## Remaining scope

Admission for rotations with arbitrary variable left and middle subtrees remains open. Their word reindexing and native equivalence now exist; the missing result is the normalization square with the required endpoint coherence.

This increment therefore proves an unbounded family of right-subtree rotations, not every rotation in an arbitrary gluing tree and not every higher associahedral relation.
