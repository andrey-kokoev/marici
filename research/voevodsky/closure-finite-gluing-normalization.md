# Normalization for arbitrary finite chain bracketings

## Constructed normalizer

`agda/ClosureFiniteGluingNormalization.agda` replaces size-specific bracketing comparisons with a recursive construction for arbitrary finite, nonempty linear gluing chains.

A system supplies labelled piece types, a boundary type for each pair of labels, and its two attachment maps. Distinct occurrence labels can encode any finite heterogeneous chain, even when some piece types coincide.

`Word` records a nonempty ordered chain, with its first and last labels retained in its indices. `Bracket` describes binary bracketings of a fixed word. These are finite syntax trees; their piece and boundary types need not be finite or truncated.

`Normal` is the explicitly right-associated homotopy gluing of the word. `rightBracket` constructs its canonical syntactic bracketing.

## Why endpoint preservation is essential

`appendFrame` normalizes a join of two already normalized chains. It recurses through the left chain using the actual three-piece associator, followed by a certified pushout comparison.

The accompanying `appendFirst` and `appendLast` laws preserve the chain's two external endpoint inclusions. They supply the homotopies needed when the normalized result is attached to another piece.

`normalize` then constructs an equivalence from every bracketed realization to `Normal`. Its recursive `normalizeFirst` and `normalizeLast` proofs supply the child attachment-square witnesses. Global realization frames are therefore derived, not independently assumed at each bracketing.

A small pushout-equivalence wrapper keeps inverse certification opaque while leaving the forward point and attachment computations transparent. All recursion is checked under `--safe`.

## Comparisons and routes

For bracketings p and q of the same word, the generated comparison normalizes p and unfolds q.

`changeIdentity` and `changeComposition` prove the expected identity and composition laws. `routeNormalForm` proves, by induction on any finite generated route, that its composite equals the direct endpoint comparison. `cycleReturns` returns every starting inhabitant along a generated closed route.

The constructed frames also instantiate the existing reference-operation model. Its compatible higher comparisons and null-homotopies for reference-based typed-operation cycles are available without adding a separate polygon proof at each chain size.

`normalizedPaths` provides the induced equivalence on path spaces. `reflectsNullLoop` proves that normalization cannot turn a genuinely nontrivial loop into reflexivity.

## One arbitrary operation

`Operations` accepts a map from the normal realization of one word to that of another. Input and output bracketings vary independently. It supplies their recursively constructed frames directly to the common-reference model.

Thus this increment is not restricted to identity operations or equal chain lengths. It generates presentations of any supplied root operation, with the required compatibility squares.

## Depth-eight regression

`agda/ClosureFiniteGluingNormalizationRegression.agda` constructs a nine-piece chain with eight two-point attachment boundaries. It checks three bracketings:

- left-associated, depth 8;
- right-associated, depth 8;
- balanced, depth 4.

A generated cycle through these three arrangements returns every value and has a null-homotopic typed-operation cycle.

A detector at the first boundary of the nine-piece normal form exhibits a nontrivial circle loop. Its pullback through the normalization equivalence on path spaces is proved nontrivial in the left-associated realization. The cycle returns this loop coherently along its basepoint return path, not by assuming that basepoint return is judgmentally strict.

The source loop is explicitly constructed by pulling back the detected normal loop. The regression does not claim that it has computed an independently chosen source attachment expression.

A further actual map collapses the remaining subchain of the nine-piece normal realization to obtain a two-piece realization, retaining the first attachment pair. The generated presentation at independently chosen source/target bracketings satisfies its checked operation square.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureFiniteGluingNormalizationRegression.agda`

Exit 0. Both added modules use `--safe --cubical --guardedness`, without holes or postulates. Their dependency closure includes the earlier explicit pentagon, reassociation, gluing, and dependent-boundary regressions. Existing source modules were not changed.

The initial helper-module name `Lift` collided with the Prelude record module and was renamed `LiftSpan` during incremental checking.

## Exact scope

The result covers arbitrary finite bracketings of nonempty **linear chains**, preserving the ordered pieces and their attachment data. It does not claim arbitrary finite gluing graphs, empty-chain unit laws, or unbounded-depth completions.

The recursively built normalizer uses the actual three-piece associator, but this alone does not identify every independently chosen local-rotation witness with the generated normal-form comparison. The next bridge is to admit such local rotations with their endpoint-reindexing and compatibility witnesses, then compare routes made from them.

The generic higher-coherence theorem applies to the resulting compatible presentations with their witnesses. It is not an assertion that all unframed tree paths or all internal topology are contractible. Analytical realization data remains a separate obligation.
