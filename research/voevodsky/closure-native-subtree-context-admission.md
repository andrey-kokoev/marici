# Unrestricted native subtree rotations under finite contexts

## Closed gate

`agda/ClosureNativeSubtreeContextAdmission.agda` constructs a complete `Coherent` value for the native rotation of **three arbitrary subtrees**, including its actual word-index transport. Both external port paths and their higher normalization cells are retained.

`Native.Trees.contextual` then admits this rotation beneath arbitrary finite one-hole contexts, with arbitrary finite siblings, using `ClosureCoherentContextAdmission`.

No attachment equivalence, truncation, caller-supplied append square, or caller-supplied port coherence is required. The theorem remains within the existing finite nonempty chain model.

## Construction

### 1. Dependent endpoint naturality

`agda/ClosureDependentEndpointNaturality.agda` proves a general transport square for a dependent family of maps and a dependent endpoint path.

Its explicit two-dimensional filler interpolates between the actual transport filler and the supplied endpoint path. Applying the dependent map and `fromPathP` gives the factorization of the moving image path. A supplied dependent normalization witness then provides the full boundary square.

The endpoint path and normalization witness need not be reflexive. The lemma does not require its maps to be equivalences.

### 2. Actual bracket-index transport

`agda/ClosureRotationIndexPortCoherence.agda` applies that lemma to the existing `ReindexRotation.treePath` and `normalizationPath`.

It constructs the first and last ports of the **actual native reindexed equivalence**, together with their coherence along the index-transport segment of normalization. In particular, abstract bracket transport is not replaced by an identity map.

### 3. Transfer the paired word square

`agda/ClosureSubtreeAppendPortCoherence.agda` precomposes the paired append square with the subtree normalization comparison.

The bridges from actual subtree endpoints to word endpoints explicitly retain `normalizeFirst p` and `normalizeLast r`. Whiskering the complete word-square cell by these bridges transfers both endpoint coherences. The top-level construction supplies the already proved arbitrary-word induction; callers supply no witness.

### 4. Compose in the complete endpoint state

The native construction packages a map together with its first and last normalization-port paths. It composes:

1. bracket-index transport;
2. the right normalization factorization and associator naturality;
3. the paired word square transferred to subtree ports;
4. the inverse left normalization factorization.

The factorization segments retain their port paths. Explicit distribution and associativity laws align the selected endpoint witnesses at the joins. Projecting the resulting path gives the normalization square and both higher cells simultaneously.

The resulting frame is the existing `nativeEquivalence`; the two ports are the existing tree-path transport witnesses.

## Witness boundary

The normalization square is newly constructed in the complete endpoint state. Equality with the earlier unpointed `ClosureRotationAppendReduction.Trees.rotationSquare` is **not** asserted.

Nor is equality with the earlier three-leaf normalization witness asserted after specializing the generic construction. Those earlier results remain available separately.

This follows the useful architectural lesson of the prime-cube observer note: retain the complete typed data before invoking functorial reconstruction. No linear-observer theorem from that note is used as a substitute for dependent higher coherence.

## Regression

`agda/ClosureNativeSubtreeContextAdmissionRegression.agda` checks:

- all three rotating subtrees are two-piece trees;
- two alternating contextual ancestors, also with two-piece siblings;
- ten circle-valued pieces altogether;
- provably noninvertible Unit-to-circle attachments;
- exact root-frame retention and contextual-frame retention;
- computation of the contextual action on the **entire rotating realization**, including native index transport;
- comparison of the complete compatible presentation;
- admission of the inverse and closure of the forward/inverse type route;
- preservation of a detected nontrivial circle loop;
- a separate dependent transport square with a nonreflexive endpoint path and a source normalization witness that varies dependently from the circle generator to reflexivity.

This is not a separate strict implementation on every surrounding attachment constructor. That stronger implementation comparison remains the separately checked three-leaf regression; it is not needed for the unrestricted contextual admission theorem.

## Verification and elaboration

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureNativeSubtreeContextAdmissionRegression.agda`

Exit 0, no warnings, **7 minutes 42 seconds**, under a 1200-second bound. The final incremental check took approximately 1 minute 52 seconds, including recompilation of the native construction.

Earlier broad-alias attempts expired, including a 600-second regression run. An instantiation-only probe isolated the problem: indiscriminate module aliases copied the large helper namespaces. Restricting aliases with `using` reduced that probe to 31 seconds. The final construction makes implementation aliases private, and the regression selects its public modules explicitly. The temporary probe was removed.

All five added modules use `--safe --cubical --guardedness`, without holes or postulates. The fresh closure includes both append inductions, dependent transport, subtree reduction, contextual fork lifting, and imported gluing regression dependencies. It does not rerun every separate historical regression entrypoint.

## API

Instantiate `ClosureNativeSubtreeContextAdmission.Native` with the piece and attachment families. Its public `C` is the coherent contextual API; `Trees p q r` exposes `coherent`, the native `change` and ports, `Hole`, and `contextual`.

For concrete instances, prefer bounded module aliases, for example `using (module C; module Trees)` and then `using (module R; change; coherent; module Hole; contextual)`.
