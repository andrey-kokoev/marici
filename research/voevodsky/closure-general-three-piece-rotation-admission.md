# Three-piece rotation admission without invertible attachments

## Closed gate

`agda/ClosureGeneralRotationAdmission.agda` removes the invertible-left-leg hypotheses from admission of the three-leaf associator into the finite-chain normalizer.

The piece types, boundary types, and attachment functions are arbitrary. They need not be sets, contractible, empty, or equivalences.

This proves the normalizing square for the earlier independently constructed `Chain.associate`. It does not redefine the associator as a generated comparison.

## The missing coherence was on attachment paths

Even an identity span comparison is not judgmentally the identity on its pushout's attachment constructor: the comparison inserts unit path compositions.

`IdentitySpan.unchanged` supplies the homotopy to identity, including the full attachment case using the path-unit law.

For a two-leaf subtree, `Pair.framePath` compares its normalization equivalence with the identity equivalence. Crucially, `Pair.firstPath` and `Pair.lastPath` also compare its two endpoint-preservation witnesses along that frame path.

These endpoint squares justify replacing the child frame inside a parent pushout comparison. A comparison of the child functions alone would not do so.

## Native rotation square

For three leaves:

- `leftToAssociate` compares left-tree normalization with the actual associator;
- `rightToIdentity` compares right-tree normalization with identity;
- `rotationSquare` combines them to prove that normalizing after the native rotation equals normalizing its source.

The forward and inverse native maps are then admitted through the existing certified-edge interface. `nativeMatchesGenerated` compares the actual associator with the generated map, and `compatibleComparison` compares the complete compatible presentation, including the square witness.

Routes retaining these actual admitted maps inherit the existing endpoint normal form, closed type-route null-homotopy, and identity residual transport.

## Noninvertible regression

`agda/ClosureGeneralRotationAdmissionRegression.agda` returns to three point pieces with two Bool attachment boundaries. It proves explicitly that the attachment Bool->Unit cannot be an equivalence, so the previous positive admission theorem was genuinely inapplicable.

The new theorem admits the native rotation anyway. The regression reuses both previously detected nontrivial loops and checks their preservation. It also checks the full compatible comparison and the actual forward/backward type cycle's null-homotopy and identity residual action.

On the older circle-valued identity spans, the regression compares the newly constructed admission with the earlier invertibility-based one as complete compatible presentations. This does not assert proof irrelevance of their square witnesses considered separately.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureGeneralRotationAdmissionRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`, without holes or postulates. Their closure rechecks the previous admission, normalization, pentagon, reassociation, gluing, and dependent-boundary regressions. Existing source modules were not changed.

## Remaining scope

The theorem is for a rotation of three leaves, whose labels may carry arbitrary piece types. It is not yet admission of rotations of arbitrary variable subtrees in the existing finite-word syntax.

That extension must account for word-index reassociation and general endpoint-preserving frame homotopies. Treating larger subtrees as atomic piece types gives a three-block theorem, but does not by itself identify that block-level normalization with the previously defined normalization of the fully flattened word.
