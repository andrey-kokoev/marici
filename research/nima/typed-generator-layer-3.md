# Layer 3: dependent payload transport over retained histories

## Checked interface

Formal source: `agda/TypedGeneratorTransport.agda`.

Active SCC obligations: attachment transport, forward realization, and route/coherencer compatibility.

`Layer3 L K` depends on the fixed Layer 1 term L and Layer 2 representation K. Its supplied fields are a payload family over states and a typed movement function for each original relation witness. Payload types can vary with the state and can contain higher paths.

`Stack3` retains all three layers. `layers-recovered` recovers the original Layer 1 and Layer 2 pair by reflexivity.

## General execution

The executor walks the explicit retained history. Each edge moves the current payload into the next state's payload type. The empty history returns the input.

| Obligation | Checked declaration |
|---|---|
| Sequential execution of joined histories | `Layer3.walk-join` |
| Composition through any Layer 2 representation | `Layer3.execute-compose` |
| Identity and single-edge execution | `Layer3.execute-identity`, `Layer3.execute-single` |
| Retained history and initial payload | `Layer3.history-recovered`, `Layer3.input-recovered` |
| Output-and-execution-agreement certificate | `Layer3.output-certificate` |
| Higher certificate | `Layer3.higher-certificate` |

The movement operation is supplied data for a general relation. No composition of the original relation is assumed by this executor.

## Agreement with composite-path transport

For path witnesses, `PathTransport` defines movement by dependent transport in the supplied payload family. Layer 2's path fold interprets the history as a single composite path.

`PathTransport.agreement` gives a path from transport along that composite to the result of stepwise execution. It applies to every retained history and initial payload, through any admitted Layer 2 representation.

`agreement-natural` compares the two routes formed by this agreement and any path between histories with fixed endpoints. In particular, it applies to the unit and associativity paths supplied by Layer 2.

`semantic-certificate` proves contractibility of the output paired with agreement to composite-path transport. Its chosen center is the history executor's result. The proof works for arbitrary payload types, including higher-valued fibers. It does not assume that individual fixed-endpoint comparison types are propositions.

## Circle-cover machine integration

`MachineBridge.history` compiles the previous machine's route syntax into retained path histories. A turn contributes the actual nontrivial circle-index loop. Consecutive routes join their histories.

`compile` translates every closed machine term into its initial Boolean and a retained history. `compiler-agreement` proves that executing the compiled history agrees with the existing independent machine evaluator. `step-preserved` proves semantic preservation for every existing machine reduction step.

The benchmark uses the supplied circle double cover and its Boolean fiber. Its Layer 1 instance has an identity generator; the nontrivial loop histories are supplied route inputs rather than iterations of that identity generator.

Compilation flattens route syntax. `retain-compilation` stores the original program with its translation and agreement proof. `program-recovered` recovers that source exactly.

## Controls

- One turn at unchanged base endpoints flips true to false.
- Two turns recover either Boolean value while retaining a nonempty history.
- `no-endpoint-only-action` excludes implementing all histories from endpoints alone.
- `no-output-history-decoder` excludes recovery of all these histories from the final Boolean.
- `no-action-history-decoder` excludes recovery even from the entire Boolean action.
- `no-total-payloads` reuses the cover's obstruction to a global section. Transport operates on a supplied initial payload.

The two negative modules separately attempt endpoint-only value recovery and erasure of a two-turn history. Both fail with the expected false/true mismatch.

## Verification and scope

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module TypedGeneratorTransport -ReceiptStem typed-generator-transport -NegativeModules TransportLayerBadEndpoint,TransportLayerBadHistory
```

Fresh safe Cubical compilation and both rejections passed. Execution reference: `structured_command_execution:e_25120_1791067324982031600_248`.

- Receipt: `results/typed-generator-transport-formal-audit.json`.
- Source-bound checker: `checkers/check_typed_generator_transport.py`.
- SCC model: `nima-typed-generator-transport`.

The general transport and agreement theorems are universe-parameterized. The operational integration covers the existing closed circle-cover machine. It proves evaluator agreement and stepwise semantic preservation, rather than a bijection of source syntax or execution traces. Integration with the separate Bool/Nat choose machine and an explicit all-dimensional simplicial transport interface remain open.

[Layer 4](typed-generator-layer-4.md) now supplies certified presentation changes over these retained execution records. Its canonical view retains history and input while omitting the recomputable output-and-agreement package.
