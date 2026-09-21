# Arbitrary-left rotation: endpoint admission and word-only reduction

Update: the unrestricted root-rotation theorem is now proved in [Arbitrary-subtree root rotation admission](closure-arbitrary-subtree-rotation-admission.md). The record below describes the preceding stage, when that gate was still open: endpoint-restricted admission and reduction to word-only coherence.

## Admission with an equivalent final-piece inclusion

`agda/ClosureEndpointRotationAdmission.agda` considers three arbitrary finite subtrees P, Q, and R. It uses the existing native associator followed by the actual word-index realization transport.

`nativeLast` proves preservation of the final-piece inclusion through that transport. Together with the constructed normalizers' endpoint witnesses, this proves the normalization square on the final piece.

If its inclusion into the source realization is an equivalence, the square extends to every source inhabitant. This admits the native reindexed equivalence and its inverse.

`InvertibleLeft.lastIsEquiv` supplies that hypothesis recursively when every left attachment map is an equivalence. The right attachment maps are arbitrary. This is a sufficient hypothesis, not an assertion that arbitrary attachments satisfy it.

The regression uses circle-valued identity spans with four pieces in the left subtree, two in the middle, and four on the right. It checks full compatible presentation, retention of the native equivalence, the closed forward/inverse type cycle, identity residual transport, and preservation of a nontrivial final-piece circle loop.

It also proves that the final-piece inclusion cannot be an equivalence in the earlier noninvertible Bool->Unit regression: such an equivalence from Unit would contract the source and contradict its detected middle loop. The endpoint theorem therefore cannot silently bypass the noninvertible case.

## General comparison coherence

`agda/ClosureGeneralSpanCoherence.agda` proves:

- associator naturality when all three realization frames change;
- composition of pushout comparisons when both component frames change;
- equality of the resulting comparison equivalences.

All attachment-square witnesses are retained. The constructor proof combines five paths using explicit composition, associativity, and reversal laws. It does not assume that these paths are reflexive.

A circle-valued regression instantiates the composition theorem with nontrivial attachment-square witnesses and proves that its chosen twist is not reflexive.

## Unrestricted reduction to a word-only square

`agda/ClosureRotationAppendReduction.agda` factors normalization on both sides of a rotation of three arbitrary subtrees.

The component-normalization stage is separated from the stage that appends the three normal words. Composition of comparisons is proved by the new coherence theorem. Trailing unit compositions in the endpoint witnesses are removed together with their frames, without discarding the endpoint paths themselves.

For words u, v, and w, `Words.AppendSquare` is the remaining obligation: appending the normal blocks on the right, after native reassociation and return to the left word index, must agree with appending them on the left.

`Trees.rotationSquare` converts this word-only witness into the full native reindexed normalization square, for any bracketings P, Q, and R of those words. `recoverAppendSquare` constructs a witness in the other direction from a native normalization square for those bracketings.

These are checked transfers of witness data in both directions. Their being mutually inverse as higher data is not asserted, and square witnesses are not declared proof-irrelevant.

## Proved base and regression

`SingleLeft.square` proves the singleton-left-word base directly. It retains both identity-span attachment corrections and constant-family transport.

Combining that base with the general reduction reconstructs the entire earlier left-leaf/arbitrary-middle-and-right family without importing its admission theorem. The regression compares this independent derivation with the earlier admission as complete compatible presentations. It also exercises recovery of the word square and readmission from it.

A separate instance checks both normalization factorizations with non-leaf left, middle, and right subtrees. It deliberately does not supply an unproved append square or claim unrestricted admission for that instance.

## Remaining step

The non-singleton induction step for `Words.AppendSquare` is still missing. It must relate append-frame associativity, endpoint witnesses, and the dependent word-index transport under a leading word constructor. The existing native pentagon is available, but its compatibility with those recursive frames is not being assumed.

Thus arbitrary left subtrees are now admitted under the endpoint-equivalence condition. Arbitrary noninvertible attachments with arbitrary left subtrees remain an open gate.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureEndpointRotationAdmissionRegression.agda`

Exit 0. Its dependency closure checks all five added modules and the preceding regression chain. All added modules use `--safe --cubical --guardedness`, without holes or postulates. Existing source modules were not modified.

Added sources:

- `agda/ClosureGeneralSpanCoherence.agda`
- `agda/ClosureRotationAppendReduction.agda`
- `agda/ClosureRotationAppendReductionRegression.agda`
- `agda/ClosureEndpointRotationAdmission.agda`
- `agda/ClosureEndpointRotationAdmissionRegression.agda`
