# Native rule applications are not yet seed traversal events

## Source inspected

- `agda/NativeTableRules.agda`: `comparison-package`, `identity-comparison`, `inverse-comparison`, `compose-comparisons`, `Arity`, `input`, `output`.
- `agda/NativeTableResolution.agda`: `Full`, `declaration`, `Ports`, `premise`, `kernel-table`.
- Existing finite execution adapter: `checkers/check_seed_typed_execution.py`.

## What native constructors actually specify

A comparison package consumes an equivalence and its marked-point witness. Inverse constructs the inverse comparison while retaining its parent; composition constructs the composite and retains both comparisons. These definitions do not allocate runtime event IDs or emit one of the six seed labels.

A closed native derivation exposes either an admitted literal or a rule application together with its premise family. The table retains the declaration and premise ports. This is dependency/provenance data, not by itself an ordered physical execution trace.

In particular, E and P rules have arity Lift I for arbitrary I : Type. Their signatures do not provide a finite enumeration or a temporal order. Even for Boolean comparison ports, an order one could choose in code is not a source-derived execution schedule. Mapping every derivation into a finite chronological seed word therefore needs additional restrictions and data.

## Why automatic event counting would be unsound

- A `compare-kind` rule supplies a comparison witness; it does not say whether a comparison attempt was executed now or merely described.
- An `identity-kind` package cannot distinguish a cost-free identity description from an executed zero-update attempt, which the proposed resource policy still charges.
- `compose-kind` constructs a retained composite. Charging it as a third traversal, beyond its two constituent histories, would be a new resource rule.
- Reusing a retained derivation as a premise does not specify whether it is being referenced or re-executed. Fresh execution occurrence IDs resolve that only after an execution policy chooses the interpretation.
- Arbitrary premise families need not support finite serial enumeration. A dependent family of witnesses must not silently become a list of traversal events.

## Minimal adapter contract

An executable source-selected fragment needs the following independently justified data:

1. A binding from admitted native packages/comparisons to the seed's actual vertex and primitive-edge roles; this is stronger than matching labels.
2. A classification of rule applications into representation operations and actual attempts. A zero-update attempt remains distinguishable from an unexecuted identity.
3. A finite execution schedule or other specified concurrency semantics for the chosen derivation fragment, respecting dependencies and explicit reuse/replay policy.
4. An emission witness for each scheduled attempt: primitive seed label, matching endpoints, fresh occurrence identity and a window back to the native application instance. If an attempt is not a seed-edge traversal, its event type must be declared rather than forced into the six-arrow alphabet.
5. A physical reader and cost calibration, independently bound to the source profile. Event count alone does not supply energy or proper time.

The finite seed path model already supplies endpoint validation, fresh occurrences, composition and optional triangle spectral windows once a word is explicitly requested. It does not supply items 1--3 or 5, nor a native proof of item 4.

## Follow-up: an existing ordered route fragment

`native-triangle-route-to-seed-binding-audit.md` locates and freshly checks `ThreeRecordTriangleRegression.agda` and its `NativeNormalizationRouteCompiler`. That compiler DOES execute and compile explicitly supplied finite coherent routes. The arbitrary-arity observation above applies to the generic resolver, not to a claim that no native ordered executor exists. The concrete instance compares AB-BC with AC, with supplied Boolean flip laws; it is not yet bound to the original directed AB-BC-CA seed. Reuse that executor once the binding is supplied rather than creating another scheduler.

## Synthesis and stopping boundary

The useful separation is now explicit:

    native derivation / dependency record
        -- missing source execution policy --> execution occurrences
        -- existing finite path composition --> retained typed history
        -- missing calibrated reader --> physical rung4 observation.

Static seed spectrum and retained presentation conversion remain available alongside this chain. They do not choose its execution policy.

No emission policy was added to owner code. This is a source inspection result, not a newly compiled Agda theorem or proof that no such policy exists anywhere in the repository. Further construction should start from an actual supplied seed/native application binding and scheduling rule, rather than another prototype that declares all comparisons to be traversals.
