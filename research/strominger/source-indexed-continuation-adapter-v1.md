# A native source-indexed continuation adapter

## Result

`agda/SourceIndexedContinuationAdapter.agda` constructs a separately named source-indexed adapter for every actual `Body.compare m a b e p h`, compares it natively to the unchanged target-side attachment, and binds the existing native attachment interchange for every next edge.

This advances `policy-classification`; it does not select a unique task/policy or redefine Body.

## Exact inputs and routing

The inputs are the existing mode, actual Body operands and their supplied equivalence, point and compatibility witnesses. The additional request is an outgoing edge at the actual source reader of the selected comparison value. Its origin remains a declared request choice.

Routing composes the previously derived source/target request equivalence with transport along the actual comparison's alignment to `act m v`. No new equivalence, filler or port agreement is supplied by the caller.

The return law is

    act m (fst sourceRequest) = fst routedRequest.

Transport of an outgoing edge along a change of its source preserves its target label; path induction proves this for both transports in the route. This is a **mode-adjusted return**, not a raw-source-return policy. On the original exchange, AB is routed to a request ending at A rather than its raw endpoint B.

## Native construction and recovery

The source package is an E-package indexed by the source request type, with the same loop package over the actual preceding comparison. Its derivation uses the unchanged E/reflexivity rules and the actual `derivation old`; there is no fresh-root substitute.

`sourceBody` is a separately prepared Body whose reader routes its source index. `targetBody` is literally the old `attach old (route s)` operation. A derived dependent-sum equivalence maps the request and leaves the loop witness unchanged. Its selected-value and full reader squares commute. The inverse law recovers the full source value, not just its observed port.

`adapterComparison` is an actual native compare-rule application. `operands-retained` recovers both operand closures, including their derivations, by reflexivity.

For every next edge, the `Continued` module instantiates the existing `InternalComparisonInterchange.Interchange` and `Retention` results with this derived comparison. Both attach/compare orders have a native interchange and their actual closures are recovered. This is a scoped reuse/binding, not a newly claimed global Body functor or arbitrary-program coherence theorem.

## Scope and parameter ledger

- Existing Body operations, Seeds and native rules are unchanged.
- Mode, operand histories, equivalence and compatibility remain inherited inputs; their origins are not retrospectively producer-certified.
- The adapter equivalence, return law, comparison and next-edge interchange are derived.
- All loop values are preserved; no native-history sethood is assumed.
- Source-indexed routing is not raw-source-return semantics.
- Synchronized-pair native presentation and independent-pair task conditions are not constructed here.
- Task selection and global policy-program coherence remain separate.

## Verification

    python research/strominger/checkers/check_source_indexed_continuation_adapter.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable input hashes and a conservative 2,327-file manifest. Three `UnequalTerms` controls reject:

1. using the mode-adjusted return theorem as a raw-source return law;
2. using the source operand derivation instead of the native comparison derivation;
3. claiming source and target packages are judgmentally equal merely because their carriers are equivalent.

Only recorded Cubical dependency warnings remain; no repository-source warnings were reported.

Contract: `contracts/source-indexed-continuation-adapter.v1.json`.
Receipt and manifest: `results/source-indexed-continuation-adapter/`.

## Next boundary

Give the synchronized-pair request presentation its own native adapter and witness-preserving comparison to the one-sided presentations. Keep the independent-pair obstruction: admitting such pairs requires a different task or an explicit synchronization condition. Finish the bounded policy-family ledger without promoting these presentations to uniquely selected policies or certifying arbitrary inherited histories.
