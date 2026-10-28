# Transport-compatible partial correspondence: first checked assembly

## Result

`agda/TransportObservationPartialCorrespondence.agda` binds actual retained executions to a declared observation and constructs either a certified image factor from a compatibility proof or a refusal from a separating collision.

This is a bounded successor to the falsified universal-existence proposal. It does not promise a realization for every observation task or decide compatibility automatically.

## Explicit signature and source

The assembly reuses `SeedGeometricResponseState.FromA`: the existing six-arrow free geometric interpretation, initial based path refl at A, and the explicitly declared `RetainedTransportResolution.Extension`. Every endpoint-typed directed word is executed from that one initial package; its raw route remains retained.

This selects the already available unary extension. It is **not** an admission theorem in the original twelve-rule Resolve calculus. No native rule or other-owner source was changed.

## Acceptance and refusal on the actual executions

For each endpoint v and declared Boolean probe on `State(v)`, `At` defines the observation by reading the actual compiled native execution, not by substituting a standalone mathematical evaluator. Its execution square proves agreement with the existing geometric effect interpreter. Route recovery remains exact.

For a supplied word summary:

- `certify` constructs a factor through its admissible image when every summary collision preserves the observed bit;
- `necessary` extracts that compatibility from any proposed factor;
- `Accepted` retains the factor, the same actual native executions and its readout square;
- `Collision` supplies two merged words with different actual observations;
- `refuse` proves that no image factor exists for such a collision.

The constructive image-descent theorem is reused from the existing observer development. The new work binds it to these actual execution packets and concrete source routes. It does not claim a new general descent theorem.

## Concrete negative instance

Use the existing mathematical `ReturnProbe`, which flips across BA and transports unchanged across the other five edges. The two complete runs

    A --AB--> B --BA--> A
    A --AB--> B --BC--> C --CA--> A

read true and false respectively. A constant summary merges them, so `no-forgotten-factor` rejects every proposed factor for that summary.

This is a dependent, comparison-sensitive probe. It is not the impossible global map from the realized graph into the discrete vertex set, and is not asserted to be a source-selected physical detector.

## Concrete positive instance, for all words

An independently defined two-state word interpreter flips its bit exactly at BA. `step-reading` and `run-square` prove agreement with geometric transport, and `native-parity` proves agreement with the actual native readout for every directed A-to-A word, without a length bound.

`parity-accepted` therefore certifies a finite observation summary while retaining the full executions separately. This is stronger than defining the summary to be the native readout and accepting it by tautology.

The parity summary is sufficient for this one probe, not a reconstruction of the source history. Empty traversal and ABC traversal have the same parity but different retained words. Other probes need their own compatibility checks.

## Verification

Run:

    python research/strominger/checkers/check_transport_observation_partial_correspondence.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, implicit libraries disabled, stable inputs and a conservative 2,438-file manifest including the observer source directory.

Two expected `UnequalTerms` controls reject:

1. accepting the constant summary by reflexivity without compatibility;
2. promoting equal parity to identity of retained words.

The runner explicitly records Cubical dependency warnings and the pre-existing `TypedGeneratorLayers.agda` unused `isPropIsContr` import warning. No warning-free claim is made. During checker development, the strict warning policy caught that known import and a negative control initially failed for a clashing name; both were corrected before the final fresh passing run.

Contract: `contracts/transport-observation-partial-correspondence.v1.json`.
Receipt, logs and dependency manifest: `results/transport-observation-partial-correspondence/`.

## Remaining gates

- An original-twelve-rule bridge if that signature, rather than the selected extension, is required.
- Anchor/source-mode and product comparisons at this new interface.
- Larger observation languages and independent source-separation results.
- Physical receiver/probe authority, calibration and empirical tests.

The revision-27 completed local theorem and its pins remain unchanged. This partial baseline does not close its three broader blocked obligations or revive the refuted unconditional conjecture.
