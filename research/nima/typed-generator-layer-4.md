# Layer 4: certified presentation and simplification

## Checked interface

Formal source: `agda/TypedGeneratorPresentation.agda`.

`Layer4 T` is a dependent record over a fixed Layer 3 term. `Stack4` retains all four layers, and `layers-recovered` recovers the original Layer 1–3 stack by reflexivity.

Active SCC obligations: forward realization, route/coherencer compatibility, and readout descent. No coordinate system, metric, subdivision, or barycentric experiment is required.

## The reduction rule

For a source type A and retained boundary type B, `Reduction A B` requires:

- a dependent remainder `Hidden` over B;
- a supplied equivalence presenting A as the dependent pair of a boundary and its remainder;
- a contractibility certificate for the remainder at every boundary.

`compact` exposes the boundary. `recover` reconstructs a representative using the certificate's center and the inverse presentation map.

Both round trips have checked paths. Consequently `compact` is an equivalence, and every supplied observation of the original record is preserved by recovery. Recovery is up to paths in the declared types, rather than a promise of identical serialized syntax or identical computation cost.

This licenses omission of the certified dependent component. It supplies neither a general method for finding contractibility certificates nor permission to forget arbitrary components.

| Obligation | Checked declaration |
|---|---|
| Source recovery | `Reduction.source-recovered` |
| Boundary recovery | `Reduction.boundary-recovered` |
| Equivalence and injectivity | `Reduction.equivalence`, `Reduction.injective` |
| Preservation of observations | `Reduction.observations-preserved` |
| Complete recovery-package contractibility | `Reduction.recovery-certificate` |
| Contractible comparisons between recovery packages | `Reduction.recovery-comparisons` |
| Higher certificate | `Reduction.higher-certificate` |

A complete recovery package contains a source record together with its comparison to the boundary. Both components vary in the contractibility statement. Arbitrary fixed-endpoint comparison types are not asserted to be contractible.

## Identity, composition and coherence

`contractRemainder` constructs the direct dependent-pair reduction from a supplied certificate.

`fromEquivalence` presents a certified equivalence by its contractible fibers. This supports identity reductions and `then`, the composition of two certified reductions.

- `compact-identity` checks identity compaction.
- `compact-composes` checks direct versus successive compaction.
- `recover-composes` compares direct versus successive recovery.
- `compact-associative` checks rebracketing of three reductions.
- `Associativity.recovery-agreement` compares the two complete recovery packages, including their boundary comparison witnesses.
- `after4` applies another certified reduction to an existing Layer 4 view while keeping the same underlying Layer 3.

These are laws for specified reductions. The interface does not choose a reduction strategy or prove confluence of arbitrary proposed rewrite rules.

## Canonical Layer 3 instance

For fixed execution endpoints, Layer 3 retains a history, initial payload, output, and output-agreement witness.

`Canonical.layer4` chooses:

- **boundary:** the retained history and initial payload;
- **remainder:** the output paired with its execution-agreement witness;
- **certificate:** Layer 3's existing output certificate.

Compaction removes the output-and-agreement package from the view. Recovery reruns the executor and supplies its reflexive agreement. `compact-retained` and `recover-request` compute by reflexivity for the canonical constructor.

The general Layer 4 interface proves history, input, and output recovery. The original source program is covered only when it is part of the chosen source record; this instance operates on Layer 3's retained execution record, not on an inverse of the earlier syntax compiler.

## Controls and concrete integration

The existing circle-cover machine supplies two retained executions: an empty history and a two-turn history, both beginning at true and producing true.

The formal controls prove:

- their scores coincide;
- their histories and canonical Layer 4 views remain distinct;
- no decoder from the score recovers every retained execution;
- no certified reduction whose compaction is that score function can exist.

An extra completion certificate is then attached to the two-turn execution. The checked two-stage reduction first omits this extra certificate, then omits the output/agreement package. The resulting view still retains the two-turn history and its initial payload. Recovery reconstructs the complete wrapped record up to a path.

Two negative modules attempt to:

1. certify an arbitrary Boolean remainder as contractible;
2. identify the compacted empty and two-turn histories because their scores agree.

Both are rejected with the expected false/true mismatch.

## Verification and scope

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module TypedGeneratorPresentation -ReceiptStem typed-generator-presentation -NegativeModules PresentationBadCompletion,PresentationBadHistory
```

Fresh safe Cubical compilation and both expected rejections passed. Execution reference: `structured_command_execution:e_25120_1791072773994760000_259`.

- Formal receipt: `results/typed-generator-presentation-formal-audit.json`.
- Source-bound checker: `checkers/check_typed_generator_presentation.py`.
- SCC model: `nima-typed-generator-presentation`.

The interface is universe-parameterized and permits higher-valued payloads. It implements certified reversible presentation changes with a concrete Layer 3 policy. [All-dimensional preservation and relative coherence](typed-generator-coherence.md) now supplies a uniform certificate for every finite dimension and every admitted stack. The [active-view engine](active-view-engine.md) implements registered Boolean replay policies with clearing, exact undo, dependency retention and byte/replay accounting. General certificate discovery, arbitrary-payload runtime support and a verified runtime/codec remain open. A many-to-one score is still a readout, not a reversible substitute for its source history.
