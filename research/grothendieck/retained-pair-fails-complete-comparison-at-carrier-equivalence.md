# Retained pair fails complete comparison at carrier equivalence

## Question

Can the actual AB versus AD;DB pair enter Strominger's complete-comparison interface through the existing native attachment interpreter, retaining its original observations?

## Claim boundary

`agda/RetainedPairComparisonAdapter.agda` maps all four vertices and six occurrences of `ActualSeedEndpointTable` into `NativeExtensionFamilyAudit`, respecting their typed endpoints. `run` interprets each actual free path by successive `Body.attach` constructors. `adapt` stores the original history, resulting Body, and realization equality; `history-recovery` is reflexivity. Both routes therefore have native Body representations with their original words retained separately.

The conjecture that these two attachment representations admit a complete comparison is false. Its first required field, a carrier equivalence, is impossible:

- Direct AB has carrier `Out A` paired with a loop at the seed value. Explicit AB and AD alternatives give two distinguishable carrier points.
- Indirect AD;DB has carrier `Out D` paired with a loop at the preceding attachment value. `Out D` is propositional by its sole DB constructor. The preceding carrier is a set, by the existing outgoing-edge and vertex sethood results, so its loop type is propositional. Hence the entire indirect carrier is propositional.
- An equivalence would identify the two distinguishable direct points. `no-carrier-equivalence` derives the contradiction using its inverse and retraction paths.

`ComparisonAttempt` spells the stay-mode contract: carrier equivalence, selected-value preservation, and equality of every port reading. `no-complete-comparison` rejects even its first field. This is stronger than an endpoint mismatch and different from the earlier diagonal-history obstruction. Both Bodies have active endpoint B.

## Disposition

The native attachment adapter exists and preserves original histories in its outer record, but does not land this pair in a complete comparison. The exact obstruction is the asymmetric carrier interface, not absence of higher coherence machinery. Strominger's repeated-interchange theorem compares maps between fixed matching interfaces; it does not imply equivalence between these different interfaces.

A different source-authorized interface or a non-equivalence comparison could change the problem, but neither is constructed or authorized by this result. Adding a Boolean coordinate merely to equalize cardinalities would not supply its source derivation, port laws, or history compatibility. No universal impossibility of higher comparison is claimed.

Fresh Agda 2.8.0.1 safe cubical closure check exited 0:

```sh
agda --ignore-interfaces --transliterate --safe --cubical --guardedness --no-libraries -i /tmp/marici-pair-adapter.AasMgq -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 /tmp/marici-pair-adapter.AasMgq/RetainedPairComparisonAdapter.agda
```

The temporary include directory contains copied Nima and Strominger `.agda` sources and the new module; a separate content comparison found no differing-content filename collisions between the two source directories. Their original source/interface files were not edited. Imported indexed-match computation warnings remain; no holes or postulates were introduced. This fresh check includes the imported repeated-interchange source, not every prior research checker. Files remain uncommitted.
