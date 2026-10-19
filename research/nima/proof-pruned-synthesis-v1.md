# Proof-carrying pruned synthesis — net iteration6

Source-derived obstruction certificates now drive the generator directly.

| Quantity | Unpruned D2 family | Proof-pruned D2 family |
|---|---:|---:|
| Selected configurations |243,034|10,682|
| Exit certificates |698|698|
| Labelled transitions |7,018,785|224,537|

The generator avoids232,352 dead configurations, a **95.6% reduction**, while preserving every certified configuration and every transition between completable configurations.

## What the search uses

Before generation, the admission step replays all nine obstruction certificates: five direct contradictions and127 leaves from four occupied/absent split trees. It binds the resulting core predicates to the source hashes, universe fingerprint, experimental mode and maximum origin2.

The generator then uses interface records, compatibility masks, incremental connection updates and the nine proved subset exclusions. It reads neither completion-policy memberships nor the certified-target atlas during construction. Those artifacts are opened only after generation to compare results.

The nine patterns were originally discovered using the atlas. This experiment demonstrates source-verified use of those learned patterns, not automatic discovery of all needed patterns from scratch.

## Exact comparison

Every original configuration is checked: membership in the new family agrees exactly with nonnegative distance in the independently computed completion policy.

Every retained state passes direct source compatibility and rootedness checks; all698 exit certificates survive. Stored parent additions reconstruct the new state and interface activity.

All224,537 labelled transitions match the induced live-state subgraph of the original graph, including:

- 174,055 revisit/self-loop transitions;
- 4,834 PE transitions;
- 2,157 accepted transitions that disable a previous shortcut while preserving a replacement route.

No target-membership oracle was used to select these states or transitions during generation. The check first obtains the generated family, then reads the old graph and policy.

The search rejected31,664 distinct encountered candidate masks by core predicates and2,108 by rootedness. These are encountered-candidate statistics, not total counts of all excluded subsets. The nine core counters are retained in the receipt.

## Proof and artifact controls

Six controls reject wrong origin budget, wrong mode, changed source hash, changed universe fingerprint, a missing absent branch in a proof, and a configuration-resource stop treated as completion.

The first graph-comparison run encountered forward references in the interleaved source archive: an edge can precede its target configuration row. The decoder was corrected to infer and later verify the target mapping from its packet mask. The final fresh run passes exact state and edge comparison.

The generated compressed graph was decompressed and checked against its state/edge counts and complete footer. Native generator files and previous scientific receipts remain unchanged.

## Next test

The D2 obstruction rules are deliberately budget-bound. All nine survive optimistic D3 continuation analysis. Next, use source-guided guarded search to seek **actual D3 certified extensions** retaining each marked core, without enumerating the full D3 atlas. Record a reconstructed witness, a source impossibility proof, or a resource stop for each core.

This distinguishes restrictions caused by insufficient origin depth from restrictions that persist when the available interfaces expand.

## Artifacts

[Proof admission and pruned generator](proof-pruned-synthesis.mjs) · [Checker](checkers/check_proof_pruned_synthesis.mjs) · [Receipt](results/proof-pruned-synthesis/verification.json) · [Pruned graph](results/proof-pruned-synthesis/D2-pruned-graph.jsonl.gz)

```sh
node research/nima/checkers/check_proof_pruned_synthesis.mjs
```
