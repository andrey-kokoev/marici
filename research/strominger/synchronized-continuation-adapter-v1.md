# Native synchronized continuation presentation

`agda/SynchronizedContinuationAdapter.agda` gives synchronized requests their own native E adapter. Its index retains the source request, target request and actual synchronization path. The E/reflexivity derivation uses the preceding comparison's actual derivation, under unchanged Seeds and rules.

## Comparisons and recovery

For arbitrary existing Body comparison inputs and arbitrary synchronized request:

- derived pointed, full-reader carrier equivalences compare this presentation to the source- and target-indexed adapters;
- both comparisons are admitted by the native compare rule, with exact extraction of both operand closures;
- inverse laws recover the complete original tuple, including its target request and synchronization path;
- the old loop witness is unchanged and the full carrier value is recovered;
- direct target equivalence equals the composite through the source adapter;
- the existing native attachment interchange is bound to each comparison for every next edge.

Recovery is propositional, not judgmental. Projection to the source request has a canonical inverse, but its inverse law is the retained path back to the original tuple; an arbitrary synchronization witness is not silently replaced by reflexivity.

The direct/composite result is **equality of carrier equivalences**. It is not equality of native comparison packages or their higher admission witnesses. General native coherence remains separate.

## Scope

This completes the native presentations of source-indexed, target-indexed and synchronized requests considered so far. It does not admit independent pairs as synchronized requests: the prior AB/BC forgetful-map obstruction remains intact. Return ports are mode-adjusted. Raw-source-return policies need a different output contract.

The caller still supplies the original comparison operands, their equivalence/compatibility, and the synchronized request. No arbitrary new comparison filler is an adapter parameter. Inherited origins are not producer-certified, and no unique task/policy is selected. Existing Body operations and earlier packets are unchanged.

## Verification

    python research/strominger/checkers/check_synchronized_continuation_adapter.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,331-file manifest. Three `UnequalTerms` controls reject judgmental tuple recovery, an independent pair offered as a synchronized request, and a one-sided operand derivation offered as the synchronized package derivation. No repository-source warnings; Cubical dependency warnings are recorded.

Contract: `contracts/synchronized-continuation-adapter.v1.json`.
Receipt and manifest: `results/synchronized-continuation-adapter/`.

## Remaining policy gate

Freeze the bounded policy-family/task ledger using these three actual native presentations, their derived comparisons and the independent-pair obstruction. State which task and output contracts are supplied, which program alternatives are classified, and what additional observations could select among them. Do not claim exhaustiveness over arbitrary policies, unique selection, or native higher coherence merely from the carrier triangle.
