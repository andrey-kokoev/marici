# Three-spoke seed through the shared retained assembler

## Result

The seed AB, AC, AD assembles into a **full tetrahedral path/coherence package** through the existing shared constructor. The input has three primitive occurrences. The output retains those three spokes and derives BC, BD, CD; it contains four triangular faces and their tetrahedral filler.

This run goes beyond checking the abstract missing-face theorem: it constructs the actual occurrence table, invokes shared table grouping/recovery, supplies an explicit path interpretation, constructs a retained request, and calls `RetainedTetrahedralPackage.Cells.build`. The same output is proved to be returned by the shared `Cells.WG.generate` transition.

No shared machinery was modified. No proton-specific assembly rule was added.

## Exact pipeline

1. `Seed.seed`: the table has exactly the three constructors AB, AC, AD with source A and targets B, C, D.
2. `TableFibrationCycle.group-from/unpack` and `four`: their existing table-isomorphism theorems retain the original labels and endpoints.
3. `Seed.Realization`: the established free-realization pattern from `SeedTetrahedronBridge` adds a node per vertex and a path per primitive occurrence. It adds **no face constructors**. This is an explicit interpretation, not an assertion that every primitive directed WG relation already has path typing.
4. `RootedSpokePathCompletion.FromSpokes`: inverse/composition and cancellation construct the three branch paths and root faces; existing `unique123` supplies the BCD face with coherence.
5. `Cells.build`: assemble the retained horn ABC, BCD, ABD into `Cells.Full`. The constructor's ACD face and filler are checked **as a dependent pair** against the previous cancellation face and filler, using the existing `unique023` contractibility theorem.
6. `Seed.result`: retain the primitive occurrence table alongside the completed package and its request-recovery witness.

The extra inverse paths are not added as primitive directed rows. The primitive count remains three, even though the assembled edge record has six slots.

## Checked retention

- Original AB, AC, AD preserved by reflexivity in the actual completed edge record.
- BC = inverse AB followed by AC, BD = inverse AB followed by AD, CD = inverse AC followed by AD.
- The full shared request is recovered unchanged.
- All six shared-edge equations include endpoints and the actual path witness.
- The supplied ACD cancellation face agrees with the assembler's generated face; filler agreement is correctly dependent on that face comparison.
- A nontrivial Boolean-negation path fixture confirms the generic adapter retains the original spoke's payload action, not just its incidence.

## Controls and verification

Fresh safe Cubical checks, with `--ignore-interfaces`:

- `RootedSpokeSharedAssembly`: accepted.
- `RootedSpokeAssemblyBadErasure`: rejected when it tries to erase the retained Boolean-negation spoke action.
- `SpokeBadDirectedCompletion`: rejected when it treats an original directed AB occurrence as a BC comparison.
- Source/compiler/import-closure hashes unchanged throughout the run.

The positive check has the existing `TypedGeneratorLayers` unused-import/export warning (`isPropIsContr`); it is successful elaboration, not a warning-free claim.

```sh
python research/strominger/checkers/check_rooted_spoke_shared_assembly.py
```

Source: `research/strominger/agda/RootedSpokeSharedAssembly.agda`.
Receipt: `research/strominger/results/rooted_spoke_shared_assembly.json`.

## Comparison with the proton route

The shared output has the same tetrahedral package structure: four vertex slots, six edge slots, four faces and a filler. The three-star route retains a different primitive occurrence record from the proton's two-triangle seed.

This run supplies no metric, leaf rotation, phase or proton coefficient protocol. It therefore establishes the shared tetrahedral assembly route, not equality with the full proton record or a regular Euclidean realization. The meaningful next comparison is between retained edge/face histories of the two routes, rather than between their silhouettes.
