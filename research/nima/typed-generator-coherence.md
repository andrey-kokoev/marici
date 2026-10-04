# All-dimensional preservation and relative coherence

## Checked claim

Formal source: `agda/TypedGeneratorCoherence.agda`.

For every admitted Layers 1–4 stack and each pair of execution endpoints, certified compaction preserves iterated identity types in every finite dimension. For a fixed compact boundary, complete recovery packages and every iterated comparison type over them are contractible.

`certify` has type `(stack : Stack4 ...) → Coherent4 stack`. `Coherent4` states these two conclusions for every endpoint-indexed reduction in that stack. Earlier history, execution, and reduction-composition laws remain supplied by the existing interfaces; this certificate does not add composition to an arbitrary original witness relation.

Active SCC obligations: forward realization, route/coherencer compatibility, and readout descent.

## Dimensions and boundaries

The implementation reuses `GradedBoundaryCoherence.Tower` instead of introducing a second tower. Here `Cell` names its boundary-indexed `Fill` type, not its total boundary-and-filler package.

These are the defining cases:

- Dimension zero has the unit boundary and the original type as its cell type.
- A dimension n+1 boundary consists of a dimension n boundary and two cells over that same boundary.
- Its cell type is the path type between those two cells.

Thus all higher comparisons have well-typed, parallel endpoints. A boundary's formation alone does not imply an inhabitant of its cell type.

`boundaryMap` and `cellMap` apply an actual supplied function recursively. At dimension zero the cell map is that function. At each successor dimension it is congruence of the preceding cell map.

## Preservation theorem

For an equivalence between types, `map-is-equivalence` proves that every induced cell map is an equivalence. The proof is structural induction on an arbitrary natural number n, using the library theorem that congruence of an equivalence is an equivalence.

`AllDimensions.preservation` specializes this result to the actual `Reduction.compact` function. This fixes which map is certified; it does not merely assert the existence of some unrelated equivalence.

The certificate exposes the resulting cell equivalences, inverse cell maps, and both source and target recovery paths. Target cells have the image of the supplied source boundary as their boundary.

## Relative coherence theorem

For a fixed compact boundary b, Layer 4's `Recovery b` contains a source record together with a path from its compact view to b. Layer 4 already proves this complete package type contractible.

`cell-contractible` proves by induction that every iterated comparison type over a contractible type is contractible. `AllDimensions.relative-coherence` applies this to every complete recovery fiber.

Both components of a recovery package vary in this statement. It does not contract arbitrary source types or arbitrary fixed-endpoint comparisons in them.

## Certification itself

`certify-reduction` constructs `AllDimensions` for every supplied certified reduction. `certificate-contractible` additionally proves that, for a fixed reduction, the complete certificate type is contractible. Its two fields are families of equivalence and contractibility proofs.

This does not identify different reduction policies or different source presentations.

`certify` applies the result to every reduction in an admitted `Stack4`. Concrete terms instantiate it for the canonical execution view and for the previously checked two-stage reduction.

## Controls

- The empty and two-turn execution records still have no comparison path, although their Boolean outputs coincide.
- `no-score-preservation` shows that an all-dimensional preservation certificate for the score function would already fail in dimension one: inverting the shared score comparison would produce the forbidden history comparison.
- Identity and Boolean flip remain distinct paths between the same universe terms. The resulting dimension-two boundary has no filler.
- The negative compiler controls attempt an arbitrary false/true filler and an unjustified lift of a shared score comparison to source history observations. Both are rejected with the expected false/true mismatch.

## Verification

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module TypedGeneratorCoherence -ReceiptStem typed-generator-coherence -NegativeModules CoherenceBadGlobalFiller,CoherenceBadScoreLift
```

Fresh safe Cubical compilation and both intended rejections passed. Execution reference: `structured_command_execution:e_25120_1791074448411871100_263`.

- Formal receipt: `results/typed-generator-coherence-formal-audit.json`.
- Source-bound checker: `checkers/check_typed_generator_coherence.py`.
- Audit result: `results/typed-generator-coherence.json`.
- SCC model: `nima-typed-generator-coherence`.

## Scope

“All-dimensional” means a uniform theorem for every natural-number dimension, proved by induction rather than sampling finitely many dimensions. “Universal” ranges over admitted stacks, their supplied certified reductions, and well-typed boundaries.

The result preserves the retained records' identity structure and supplies relative coherence inside recovery fibers. It makes no assertion of universal fillers for arbitrary relations or boundaries, transfinite dimensions, or a general infinity-category/simplicial interface. The geometric refinement experiments are not dependencies.
