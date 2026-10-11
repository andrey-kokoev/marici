# Matched refinement comparison

Date: 2026-10-06. Includes the follow-up reuse-against-reuse comparison. Result: equal capability; ordinary Cubical dependent-sum isomorphisms discharge the structural work. WG retains a domain-specific assembly convenience, not a demonstrated nontrivial proof advantage.

## Frozen task and rivals

Test `ComposableWitnessSpecialization.ProofDependentFixture`, not the weaker Wolfram rule compiler. The base flips a Boolean state. The first layer flips an admitted Boolean and emits its old value as an edge witness. The second layer flips another admitted Boolean and requires the retained first-layer witness to equal that old value. A third layer checks the same retained first-layer value after composition. Sources are the three lifted Boolean values true, false, true.

The obligation is **forward realization**, on this fixed Boolean fixture: retain every witness and source, flatten two layers, compare the two three-layer groupings, preserve endpoints and selected steps, and reject an incorrect first-layer payload. This includes arbitrary inhabitants of the edge types, not only generated examples.

Rivals: WG provides a capability missing from ordinary dependent records; WG packages routine structural proofs; or even its packaging adds little over an ordinary reusable library. The first rival predicts a failure or additional assumption on the matched baseline. Both implementations passing with definitionally equal data refutes that prediction for this fixture. The follow-up below tests the third rival by factoring the ordinary baseline through existing library isomorphisms.

## Implementations

All paths below are under `research/voevodsky/`.

- `agda/WGRefinementBaseline.agda`: independent ordinary dependent pairs, importing only Cubical foundations/data. Explicit nested and flattened edge types, generators, state and full-step isomorphisms, source projections, three-layer associator and source associator. It never imports the WG implementation.
- `agda/WGRefinementClient.agda`: independently states the same three leaf refinements, then calls `compose`, `Composite.correct`, `Composite.rebase` and `Associativity.associator`. It does not alias the existing fixture's solutions.
- `agda/WGRefinementComparison.agda`: checks equality of both implementations' carriers, edge families, generators, forward/inverse full-step maps and retained source values. Every comparison is `refl`.
- `agda/negative/WGRefinement{Baseline,Client}Bad.agda`: intentionally supplies `refl` after replacing the true first-layer payload with false, leaving endpoints and the original relation witness unchanged.

The ordinary implementation spells out the concrete third-layer groupings; the WG implementation obtains them generically from the supplied refinements. This compares hand-written local structure with an existing reusable API, not two equally optimized reusable libraries.

## Results

| Obligation | Ordinary dependent pairs | WG API |
| --- | --- | --- |
| Proof-sensitive second layer | Dependent sum indexed by first witness | `Extra` indexed by compiled witness |
| Two-layer flattening and inverse | Local tuple maps | `Composite` maps |
| All-step invertibility, endpoints, generated-step preservation | Local `Iso` fields and `refl` laws | `Composite.correct` |
| Both original sources retained | Pair with two `refl` projections | Generic source-recovery lemmas |
| Three-layer state/full-step associator | Local reassociation maps and `refl` laws | `rebase` and generic associator |
| Source associator preserves actual values | Pair reassociation and `refl` | Generic source associator |
| Incorrect payload | Rejected: `false != true`, exit 42 | Same rejection, exit 42 |
| Cross-implementation data/maps | Definitionally equal | Definitionally equal |

Fresh Agda 2.8.0 with Cubical 0.9 passed under `--ignore-interfaces --safe --cubical --guardedness`. The positive comparison and both intended negative rejections passed. Inputs were stable before/after all runs. The existing `TypedGeneratorLayers` import warning about `isPropIsContr` remains; no new holes or postulates were introduced.

Descriptive physical nonblank/noncomment counts, including imports and signatures: baseline **111**, WG client **48**, comparison **62**. The WG client imports a generic API file of **232** such lines, plus its dependencies. These are not development-time measurements, proof-complexity measurements or total implementation costs. The direct API file also contains unrelated declarations, so adding it to the client is not a clean total-cost comparison either.

## Follow-up: reuse against reuse

The original baseline and tests remain in place. `agda/WGRefinementLibraryBaseline.agda` implements the same fixture using Cubical 0.9's `Σ-assoc-Iso` and `Σ-cong-iso-snd`, together with `compIso` and `invIso`. `agda/SigmaReassociation.agda` provides a **14-line** generic helper, `totalAssoc`, assembled solely from those library isomorphisms. It lifts strict reassociation through an arbitrary dependent result family and contains no graph, generator, source or WG concepts. It is new glue, not falsely attributed to Cubical itself.

The library version contains no hand-written forward/inverse reassociation implementations or inverse-law proofs. Its two-layer full-step isomorphism is a composition of `totalAssoc` with a fiberwise associator. Its three-layer full-step isomorphism adds one outer dependent-sum layer. State and source isomorphisms come directly from the library. Endpoint and selected-generator compatibility remain explicit `refl` laws.

`agda/WGRefinementLibraryComparison.agda` is identical to the original comparison except for the module name and baseline import; the checker enforces this textual equality. All its proofs remain `refl`, including both inverse full-step maps. `negative/WGRefinementLibraryBad.agda` fails with the same intended Boolean mismatch. Thus the obligations were not weakened to accommodate the library implementation.

Fresh runs pass both positive comparisons and all three negative controls. Current counts: handwritten baseline **111**, library baseline **101**, ordinary reusable helper **14**, WG client **48**, each comparison **62**. The new helper is included separately rather than treated as free infrastructure. These counts do not establish that either implementation is optimal: the baseline explicitly names each concrete state/edge/generator presentation, whereas WG derives those presentations from a refinement record. The 14 helper lines plus 101 client lines do not give a one-fixture size saving over the handwritten version; they do remove hand-written inverse proofs and make the structural construction reusable.

## Interpretation and decision

Ordinary dependent-sum machinery now supplies the same reusable structural proof work. WG's remaining convenience is **assembling state/edge families and selected generators from refinement records, and packaging endpoint/selected-step compatibility into a named certificate**. The ordinary baseline spells out those presentations and names the compatibility laws separately. This is an interface/organization distinction, not missing expressive power or a difficult theorem solved only by WG.

The comparison is settled for this fixture: no nontrivial proof advantage remains demonstrated after factoring the baseline. Do not call the implementations equally short, claim the helper is globally minimal, or extrapolate to every refinement. Nevertheless, the present evidence supports an **expository formalization**, with a modest domain-specific API convenience, rather than a research-level abstraction breakthrough. No additional theorem or case study is needed to reach that bounded disposition.

Units, four-layer pentagon coherence, runtime performance, automated inference of refinements, arbitrary sources and broader application coverage were not compared. The checker imports only the composition root, not the later pentagon module. This experiment supplies a stronger-composer example separately from Wolfram; it does not turn Wolfram into such an instance.

## Reproduction and evidence

```text
python research/voevodsky/checkers/check_wg_refinement_comparison.py
python research/aspect/scc/scc.py check wg-refinement-comparison
```

The checker is dependency-free Python; override `AGDA` and `CUBICAL_DIR` for another installation. Default paths use the local Agda 2.8.0/Cubical 0.9 installation. Each compiler run is bounded to 240 seconds. It requires all three negative failures to have exit 42 and the specific Boolean mismatch, not merely any error.

Receipt: `research/voevodsky/results/wg-refinement-comparison.json`. Logs: `wg-refinement-{comparison,library-comparison,baseline-erasure,library-erasure,wg-erasure}.log` in the same directory. The receipt records commands, source/compiler hashes, before/after stability and descriptive counts. The inventory is broader than the import closure; it excludes compiler builtin data as a separately unpinned dependency. SCC's `checks_passed` is an exit-code-based orchestration result, not a novelty certificate.
