# Two source comparisons and two attachments: inverse-facing control

Owner: `marici.Strominger`. Net node: **`two-comparison-inverse-facing-control`**, scoped construction. The stronger `two-comparisons-two-attachments` node remains open for the forward/forward history-lift case.

- [Current net](contracts/wg-source-determination-conjecture-net.v1.json)
- [Full diagram and filler theorem](agda/TwoComparisonTwoAttachmentCoherence.agda)
- [Native higher admission and recovery](agda/TwoComparisonHigherAdmission.agda)
- [Fresh verification](results/two-comparison-coherence/verification.json)
- [Conservative dependency manifest](results/two-comparison-coherence/dependency-manifest.json)

## Exact result

Under the unchanged six-arrow incidence source, four endpoint seeds, twelve native schemas and target-side continuation convention, an explicit **inverse-facing pair of exchange comparisons** commutes with two dependent attachments up to equality of complete fillers. The higher witness is natively admitted in a faithful E envelope; projecting its path recovers exactly the constructed filler equality.

This is a two-row/two-attachment control, not two total native-rule applications: the retained interchange and envelope derivations contain additional comparison/reflexivity/E applications.

The selected attachment path is `AB; BC`. First exchange transports it to `BA; AD`; second exchange returns it to `AB; BC`. Final active port is **C**. Four actual existing interchange instances participate: `R.First`, `R.Second`, `K`, `K2`.

### Which second comparison?

Let `X` be the retained graph of the first comparison `seedBody A -> seedBody B`. `K` compares `X` back to `seedBody A` by the graph projection equivalence, with a proved exchange port law. This keeps the original comparison and its actual native history as an operand; it does not replace it with a fresh seed.

This is an explicitly constructed **inverse-facing** comparison. It is not a second application of `moveInitial` to arbitrary indexed native proofs. Vertex involution is used only in the vertex reader law. No involution of forward proof transport is inferred.

At attachment depth two, the second comparison equivalence `e2` is explicitly the first row's `R.sequential` followed by `K2.attachmentEquiv`. Thus its parameter origin is visible: it is constructed from the already implemented interchange terms, not chosen by matching endpoints after the fact. Its selected-point witness is normalized using proved local sethood; the original leg witnesses remain in the retained diagram.

## Routes and coherence

**Sequential route:** rebase the second comparison graph along the first row's repeated interchange, then apply the second row's two interchanges. Rebasing uses graph equivalences, not equality of native syntax.

**Fused route:** contract both comparison graphs, then lift the inverse pointed base equivalence through the two retained dependent attachments.

Both routes have explicit whole-carrier port laws. The target is an outgoing-witness family with a proved propositional loop fiber. The target reader is injective **for this exact carrier**, by `restore-target` and loop contractibility. This yields equality of the entire maps, then of equivalences, selected-value witnesses and port-law witnesses:

- `map-coherence`
- `filler-coherence : sequentialFiller ≡ directFiller`
- `native-history-coherence`, a dependent path between the corresponding comparison derivations.

The hidden-Boolean-fiber counterexample remains valid. Matching ports alone does not imply map equality when extra retained content destroys this locally proved injectivity.

## Higher admission and retention

`TwoComparisonHigherAdmission` reuses `HigherWitnessAdmission.PathAdmission` and the general contractible-fiber projection theorem. Each filler supplies a native comparison and a derived reflexivity branch. The E envelope is equivalent to the filler carrier because these branch fibers are proved contractible.

`admitted-higher` derives the lifted path under the unchanged `Seeds`; `path-recovery` recovers `filler-coherence` exactly. `bare-not-admitted` reuses the atomic-spine invariant to reject the literal bare atomic path package. Semantic equivalence of the envelope and filler carrier does not identify their Codes.

The reified payload retains all four interchange cells, the original and intermediate Bodies, both filler envelopes, their native histories and the admitted higher package. `recovery` is exact payload recovery. No global equality of raw histories or provenance erasure is asserted.

## Parameter ledger

| Parameter | Origin |
|---|---|
| Foundation, six arrows, four endpoint seeds | Previously declared source/foundation |
| All-outgoing request, stay/exchange menu, target reader | Previously declared task/interface policy |
| First comparison and its two interchanges | Existing checked `RepeatedInterchangeCoherence` implementation |
| Second base comparison | Explicit graph projection plus `backPorts`; inverse-facing choice |
| Depth-two second equivalence | Constructed composition `R.sequential ; K2.attachmentEquiv` |
| Point-witness normalization and full-filler equality | Proved local sethood/reader injectivity, not global proof irrelevance |
| Envelope index and uniform branch family | Explicitly supplied Agda family indexed by already constructed full fillers |
| Higher path | Constructed by this local theorem, then admitted; not searched for by native resolution |

The unrestricted native constructor language is unchanged. This ledger is not yet a certified source-program grammar for every parameter.

## Verification

```sh
python research/strominger/checkers/check_two_comparison_coherence.py
```

Fresh headless closure passes with `--ignore-interfaces`, explicit include roots, `--no-libraries`, safe/cubical/guardedness flags, Agda 2.8.0.1 and Cubical 0.9. Three intended negative modules fail with `UnequalTerms`:

1. Treating the envelope derivation as admission of the bare atomic package.
2. Replacing the comparison between routes by literal raw-package equality.
3. Assigning the final source Body port D instead of C.

The checker snapshots **1,819 source/library files** covering all declared include roots and Agda primitives, plus the compiler binary hash and commands. This is a conservative complete include-root inventory, not an exact import graph and not a claim that every inventoried file was compiled. Input hashes are checked unchanged across the run.

Disabling implicit library configuration exposes 49 distinct `UnsupportedIndexedMatch` warnings in Cubical dependencies, normally suppressed by that library's configuration. The receipt records them rather than hiding them. There are no repository-source warnings; unexpected or repository warnings fail the checker. Development encountered expensive elaboration of expanded proof terms; abstract proof boundaries and graph-equivalence rebasing avoid that expansion without axioms or rule changes.

## Remaining frontier

The inverse-facing control is constructed. **The forward/forward case and arbitrary native-history lift composition remain open.** The next task is `source-comparison-composition`: compare the actual chosen univalent endpoint paths and proof transports, establish their unit/composition comparisons or retain the exact residual. The larger diagram must not consume that law merely because both vertex actions are exchange.

General coherence induction, non-set witness fibers, parameter-program certification, policy classification, topology-changing interpretation and physical coverage remain open. Historical WG and parent-net verdicts are unchanged.
