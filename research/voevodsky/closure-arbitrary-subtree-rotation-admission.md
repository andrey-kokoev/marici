# Arbitrary-subtree root rotation admission

## Closed gate

`agda/ClosureArbitrarySubtreeRotationAdmission.agda` proves admission of the native rotation

`(P Q) R -> P (Q R)`

for three arbitrary finite subtrees, with the necessary word-index realization transport. There are no invertibility, endpoint-equivalence, truncation, or emptiness assumptions on the attachment maps or piece types.

The comparison is with the existing normalizer of the fully expanded nonempty word. Neither an append square nor a native normalization square is supplied by the caller.

Both the native reindexed equivalence and its inverse are admitted. The module proves agreement with the generated map, retains the native equivalence, and compares the full compatible presentation.

## Why a stronger induction was needed

The earlier word-only append square compared functions. To lift its induction hypothesis through a parent pushout, the first-endpoint witness must move along with that function comparison.

`agda/ClosureAppendEndpointCoherence.agda` therefore packages an append square together with this endpoint coherence. Its singleton base includes the higher cell relating the unit compositions and constant-family transport; it does not treat those operations as judgmental identities.

## Transport is an actual span comparison

`agda/ClosurePushoutTransportCoherence.agda` compares transport along a path of right-hand piece types and attachment functions with the corresponding `LiftSpan` equivalence.

Path induction carries the map homotopy and its left-endpoint coherence together. The result includes a path of equivalences and a dependent path contracting the endpoint witness along that frame path.

The word-prefix specialization identifies return-index transport under a leading word constructor with the required pushout comparison. No attachment invertibility is used.

## The non-singleton step

`agda/ClosureAppendInduction.agda` proves the previously missing induction step.

For a leading piece A and the three remaining normal blocks:

1. Factor the left append map through the component comparisons and native reassociations.
2. Factor the right append map through the corresponding comparisons and the actual index transport.
3. Use the existing constructor-defined four-piece pentagon to put both composites over the same intermediate source.
4. Lift the endpoint-aware induction hypothesis through the outer pushout.
5. Restore the prescribed endpoint witnesses.

The factorization paths live in a space of maps paired with their first-endpoint witnesses. Their composition therefore retains the higher cell needed by the next induction step. Pointwise equalities are not silently promoted to coherence of independently chosen witnesses.

`coherentAppend` now handles every nonempty left word. Its square projection discharges the earlier unrestricted word-only obligation. The previously checked reduction then transfers it to arbitrary choices of all three subtrees.

## Fifteen-piece noninvertible regression

`agda/ClosureArbitrarySubtreeRotationAdmissionRegression.agda` uses:

- a four-piece left subtree;
- a two-piece middle subtree;
- a nine-piece right subtree;
- Bool attachment boundaries with constant maps to Unit.

The regression proves these attachment maps are not equivalences. It checks all 15 pieces, source depth 9, and target depth 10, including depth preservation through the explicit bracket reindexing.

It checks the full compatible comparison, the actual forward/inverse closed type route, and identity residual transport.

Separate detectors observe nontrivial loops inside the left, middle, and right subtrees and ignore the other two contributions. Reflection through the actual realization-index equivalence proves that none of those loops collapses after reindexing. The right-subtree detector retains its explicit basepoint path.

The regression also compares the new complete admission with the earlier endpoint-restricted admission on circle-valued identity spans. A separate transport instance uses a provably nonreflexive circle-valued attachment-family witness and checks its endpoint coherence.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureArbitrarySubtreeRotationAdmissionRegression.agda`

Exit 0. The final fresh closure took approximately seven minutes with a 600-second timeout. An earlier 200-second bound expired; that run was not counted as verification.

All five added modules use `--safe --cubical --guardedness`, without holes or postulates. The closure rechecks the preceding normalization, reduction, subtree, endpoint, pentagon, reassociation, gluing, and boundary regressions.

## Scope still not implied

This theorem admits a root rotation of three arbitrary subtrees in the finite nonempty linear-chain model. It does not by itself certify every separately implemented contextual whiskering of a rotation under additional ancestors, nor arbitrary independently selected higher associahedral witnesses.

Follow-up: [Selected higher admission](closure-selected-higher-admission.md) supplies an exact lift criterion in all finite globular dimensions and a checked counterexample to automatic higher-witness admission. Contextual whiskering remains the constructive gate.

Empty-chain units, arbitrary gluing graphs, unbounded completions, and analytical realization obligations remain outside this result. Presentation-cycle null-homotopy does not erase the realization's internal topology.

## Added sources

- `agda/ClosurePushoutTransportCoherence.agda`
- `agda/ClosureAppendEndpointCoherence.agda`
- `agda/ClosureAppendInduction.agda`
- `agda/ClosureArbitrarySubtreeRotationAdmission.agda`
- `agda/ClosureArbitrarySubtreeRotationAdmissionRegression.agda`
