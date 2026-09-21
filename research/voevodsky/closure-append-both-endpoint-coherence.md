# Append coherence with both external endpoints

## Closed word-level gate

`agda/ClosureAppendBothEndpointInduction.agda` constructs the append normalization square together with **both** first- and last-endpoint coherence, for arbitrary nonempty words and arbitrary attachment maps.

The non-singleton step is proved recursively, not supplied as a hypothesis. The subsequent transfer to arbitrary subtree realizations and finite contexts is now complete; see [unrestricted native contextual admission](closure-native-subtree-context-admission.md).

## Moving right-hand transport

`agda/ClosurePushoutMovingPortCoherence.agda` extends the existing pushout transport comparison on its changing right-hand piece.

For an arbitrary path of piece types and attaching functions, and an arbitrary dependent endpoint path, it proves coherence between:

- transport of the endpoint inside the whole pushout;
- the right inclusion of the endpoint's component transport witness.

The theorem uses the existing `FixedLeft.framePath`; it does not silently substitute a different frame comparison. Its proof accounts for the computation path of the earlier path induction and the inverse/unit cancellations at the constant diagram.

A further `sourcePort` theorem allows a nontrivial source-side endpoint witness before the dependent endpoint path. Neither witness is assumed reflexive.

## Both-endpoint state and induction

`agda/ClosureAppendBothEndpointCoherence.agda` defines the stronger state, proves its singleton base, and supplies the last-endpoint correction for prefix index transport.

The singleton last-endpoint proof uses naturality of constant-family transport along `appendLast`; it does not assume that this path is judgmentally trivial for variable words.

The recursive proof carries the last-endpoint field alongside the first-aware map state through the actual append factorizations and native pentagon. The right-hand transport correction handles the only factorization step whose value on the final piece is not constant. The induction hypothesis then supplies the lower last-endpoint cell.

Both endpoint witnesses remain present when the factorization paths are composed.

## Relation to the earlier square

`agda/ClosureAppendEndpointErasure.agda` projects the new state to the earlier first-aware **interface**, retaining the newly constructed square.

It does **not** assert equality with the earlier `ClosureAppendInduction.coherentAppend` witness. Adding dependent fields changes transport computation; an attempted judgmental identification did not establish that equality. No proof irrelevance for normalization squares is assumed.

The new square still concerns exactly the existing append maps. Its projection can be passed to the previously checked tree reduction, retaining the actual native reindexed equivalence.

## Regression

`agda/ClosureAppendBothEndpointRegression.agda` checks a four-piece example with a non-singleton left word, circle-valued pieces, and provably noninvertible Unit-to-circle attachments.

It checks both endpoint cells and transfers the new square to admission of the actual reindexed tree rotation, retaining its native equivalence and comparing its complete compatible presentation.

A separate instance simultaneously varies the attaching-function family, the right-hand endpoint, and its source-side port path. The endpoint path is the provably nontrivial circle generator.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureAppendBothEndpointRegression.agda`

Exit 0, no warnings, approximately 10 minutes 22 seconds under a 1200-second bound. An earlier 600-second fresh run expired and was not counted as verification. The final regression uses four pieces; an earlier six-piece version had passed incrementally but is not the final checked fixture.

All five added modules use `--safe --cubical --guardedness`, without holes or postulates. The closure includes the old and new append inductions and their transport, reduction, and gluing dependencies. It does not rerun every separate contextual or arbitrary-root regression.

## Subsequent gate: closed

`ClosureNativeSubtreeContextAdmission` now transfers **both** endpoint coherences through arbitrary-subtree normalization and bracket/realization word-index transport, producing a complete `Coherent` value for the actual native root rotation. It feeds `ClosureCoherentContextAdmission` for arbitrary finite ancestors.

The choice of normalization-square witness remains explicit: the construction composes in the paired-port state and does not assign its coherence to an independently selected old square. See [the construction and fresh ten-piece regression](closure-native-subtree-context-admission.md).
