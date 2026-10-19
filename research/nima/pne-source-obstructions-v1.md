# Source-derived obstruction certificates — net iteration5

All nine packet patterns from the D2 completion planner now have impossibility certificates derived from source interfaces. The derivation does not query the atlas's certified-target list or Boolean completion formula. Those are used afterward for cross-checks.

## Results

| Mandatory packet core | Source certificate | Split nodes / leaves |
|---|---|---:|
|14|No possible exit path|—|
|3,18|Packet18 has no possible exit path|—|
|4,7|Packet7 has no possible exit path|—|
|4,19|Packet19 has no possible exit path|—|
|7,18|Exhaustive occupied/absent choices|5 / 3|
|13,18|No exit paths and no possible native witness for mandatory NN face at cells8/12|—|
|16,9|Exhaustive occupied/absent choices|131 / 66|
|18,19|Exhaustive occupied/absent choices|5 / 3|
|9,10|Exhaustive occupied/absent choices|109 / 55|

The four split trees total250 nodes and127 contradiction leaves. Their sizes reflect the current branching heuristic, not minimum proof sizes.

## Derivation

For mandatory core plus root:

1. Remove packets incompatible with the mandatory selection.
2. Build an **optimistic** graph of native and PE interfaces. An edge may be retained even when other optional edges cannot coexist with it. Mandatory occupancy and successor guards still apply.
3. Remove a candidate if it has no optimistic root path, no optimistic exit path, or requires a face whose native witnesses are all unavailable.
4. Repeat until a mandatory packet is eliminated or the relaxation stabilizes.

Elimination is sound by induction: every packet and edge of an actual certified extension must remain among the optimistic candidates. Each elimination condition is necessary for such an extension. Optional choices are deliberately allowed to conflict with each other, so failure of the optimistic graph is decisive while survival is only a residual.

For the four surviving cores, branch on one optional packet being selected or absent. Repeat the source relaxation in both branches. Every branch closes. The verifier replays the full tree with its accumulated selected/absent assumptions and checks both children at each split.

This separates two mechanisms:

- **Individual route/support obstruction:** the mandatory configuration has already excluded every route or face witness.
- **Joint-choice obstruction:** the relaxed graph contains routes, but no consistent selection realizes the needed routes together.

The latter is why unioning all individually possible connections was insufficient for four cores.

## Controls

- Every immediate proper subset has a source-replayed certified extension:17 controls in total.
- All698 D2 certified selections survive the source relaxation.
- The independently constructed guarded Boolean formula confirms all nine full cores have zero completions.
- Corrupted proof trees that split on the already mandatory root or omit an absent branch reject.

Core seeds were learned from the previous atlas. Their impossibility certificates are now produced without target membership. This supplies source-backed pruning lemmas for synthesis under the declared grammar.

## Origin dependence

The same marked packets were mapped into the D3 universe using species, geometric cell key, complete aliases, origin and coefficient map—not raw packet IDs. All nine cores survive the D3 optimistic test. That does not establish D3 completions; it shows the immediate D2 exclusion mechanism no longer suffices. The D2 certificates must not be reused as depth-independent bans.

## Next test

Build a **proof-carrying pruned D2 generator**: compile these nine certified cores as forbidden retained subsets, construct without consulting the completed target atlas, and compare the result afterward to the10,682 live states and698 certified states of the independent completion policy. This tests whether the new explanations produce a useful synthesis algorithm.

## Reproduction

```sh
node research/nima/checkers/check_pne_source_obstructions.mjs
```

[Source elimination module](pne-source-obstructions.mjs) · [Checker](checkers/check_pne_source_obstructions.mjs) · [Certificates, branch trees, controls and hashes](results/pne-source-obstructions/verification.json)
