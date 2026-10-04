# Layer 2: retained histories and coherent composition

## Checked interface

Formal source: `agda/TypedGeneratorLayers.agda`.

Active SCC obligations: forward realization and route/coherencer compatibility.

`Layer1` now has a formal record with a state type, witness relation and generator. `Layer2 L` is a dependent record over a fixed Layer 1 term L. `extend` constructs the stack. `layer1-recovered` recovers L by reflexivity.

Layer 2 represents finite histories by a type family equipped with an equivalence to the explicit history datatype. This preserves intermediate states and the individual relation witnesses. The equivalence has checked recovery maps in both directions.

The construction additionally uses finite inductive families and natural numbers from the adopted type theory. These are declared foundation inputs.

## General histories

A history is either empty at a state or consists of a witnessed edge followed by a history. The datatype's indices enforce matching endpoints.

| Operation or law | Formal declaration |
|---|---|
| Include one witnessed transition | `Histories.single` |
| Join matching histories | `Histories.join` |
| Left and right unit laws | `Histories.left-unit`, `Histories.right-unit` |
| Associativity | `Histories.associative` |
| Generate n successive transitions | `Histories.generated` |
| Retain exactly n steps | `Histories.generated-length` |
| Recover histories through another representation | `Layer2.decode-encode`, `Layer2.encode-decode` |
| Preserve composition through the representation | `Layer2.composition-preserved` |
| Unit and associativity laws for represented histories | `Layer2.left-unit`, `Layer2.right-unit`, `Layer2.associative` |

The canonical Layer 2 uses the explicit history datatype itself.

## Interpretation into the original relation

`Composition L` separately supplies identities, composition, unit laws and an associativity witness for L's original relation. `Interpret.fold` uses that structure to interpret a history as one relation witness. `fold-single` and `fold-join` prove preservation of single transitions and composition.

Layer 2's histories exist for every Layer 1. The original relation may lack a composition operation. This boundary is proved by the Boolean-flip example: two flips form a retained history from false to false, while the flip relation has no such single edge. `no-universal-composition` excludes a construction supplying `Composition L` for every Layer 1.

The general `Composition` record contains the listed finite laws. It makes no assertion of a complete infinite coherence structure for arbitrary relations.

## Path specialization and generated tetrahedron

`path-layer` instantiates Layer 1 with paths as witnesses. `path-composition` supplies the required interpretation algebra from the existing path laws.

For any such generator and starting state, `GeneratedPaths.edges` constructs four successive state occurrences and all six edges. Three edges are generated transitions. The others are their explicitly parenthesized composites.

Faces 012, 123 and 023 are reflexive comparisons with the constructed composite edges. The prior marked-tetrahedron theorem constructs face 013 together with the tetrahedral filler. All six edges and the other three faces remain fixed.

`GeneratedPaths.At.certificate` proves contractibility of the type containing this fourth face and its filler. `higher-certificate` certifies the resulting certificate type. The completion space permits the fourth face to vary; it is not the filler space of an arbitrary boundary with all four faces already fixed.

`GeneratedPaths.naturality` proves the square comparing generation before and after a supplied input path.

## Retention control

Even an identity path generator can produce histories of different lengths. `no-history-decoder` proves that a composite path cannot recover every original history. The source histories remain part of Layer 2's representation.

The two deliberate rejection controls attempt:

1. to replace two flips by a single edge of the flip relation;
2. to classify a two-step identity history as empty.

Both are rejected with the expected false/true mismatch.

## Verification and scope

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module TypedGeneratorLayers -ReceiptStem typed-generator-layers -NegativeModules GeneratorBadComposition,GeneratorBadHistoryErasure
```

Fresh safe Cubical compilation and both controls passed. Execution reference: `structured_command_execution:e_25120_1791066075241289200_242`.

- Receipt: `results/typed-generator-layers-formal-audit.json`.
- Source-bound checker: `checkers/check_typed_generator_layers.py`.
- SCC model: `nima-typed-generator-layers`.

Layer 2 is complete at this declared scope: retained finite histories, their representation and composition laws, optional interpretation, and generated path coherence through a tetrahedron. [Layer 3](typed-generator-layer-3.md) now connects these histories to dependent payload transport and the circle-cover machine. An explicit all-dimensional simplicial interface remains open.
