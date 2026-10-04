# Executable active-view engine

## Question

Can the Layer 4 reduction interface support an executable view that selects eligible cached components, retains dependencies, reconstructs omitted data, and exposes its costs?

Active SCC obligations: forward realization, route/coherencer compatibility, and readout descent.

## Claim boundary

The first backend accepts ordered lists of `stay` and `turn` instructions with a Boolean input. It supports two registered cache components: the resulting Boolean and the replay trace, each with its fixed replay-rule identifier. It does not accept arbitrary type expressions or discover arbitrary contractibility proofs.

The conjecture tested here is that this restricted policy can automate clearing without merging distinct requests or trusting claimed cache correctness. Rivals are output-based history deduplication, trust in rule labels without replay, and a smaller active view whose unreported retained state or undo receipt costs more than the original representation.

## Formal model

`agda/ActiveViewMachine.agda` defines execution, traces, and four presentation modes: full, output-only, trace-only, and compact.

Each cache type pairs its value with a path from the specified computation. The model proves these dependent components contractible. Every change between fixed modes is a Layer 4 certified reduction, preserves the source request, and inherits the all-dimensional certificate. Mode is a presentation parameter, not a component silently contracted inside one undifferentiated state type.

`layer3-agreement` connects the instruction evaluator to the existing Layer 3 machine execution. Raw instruction lists are retained independently of this compilation; explicit stays are never deleted from the source. `trace-length` proves that a trace contains one more Boolean than its instruction count.

Fresh safe compilation and two intended trace/history rejection controls passed: `structured_command_execution:e_25120_1791076163117628200_266`.

## Runtime interface

Implementation: `checkers/active_view.py`, Python standard library only.

An artifact contains a retained request store and an ordered list of active views. A view references its source request and contains zero, one, or two cache components. Content addresses share only identical requests; equal outputs do not authorize sharing distinct histories.

| Command | Operation |
|---|---|
| `build` | Construct full caches from a JSON request list |
| `inspect` | Validate and report visibility, storage and replay counts |
| `plan` | Select registered components under byte-saving and recovery-step constraints |
| `apply` | Revalidate a source-bound plan and clear exactly its selected fields |
| `recover` | Materialize requested cache fields, full by default |
| `undo` | Use the saved plan to restore the exact previous cache visibility and contents |
| `demo` | Run the fixed three-request demonstration |

`recover` produces a chosen presentation. For exact reversal of a clearing operation starting from any partial presentation, retain its plan and use `undo`. The plan records the removed fields and source/target fingerprints; it is part of the undo storage cost.

The selector considers traces then outputs in view order. It keeps only removals meeting the requested byte threshold and total missing-cache replay budget. Requests shared by multiple views are charged once. This is a deterministic selection policy, not a globally optimal compression algorithm.

## Validation and dependency management

The engine checks the current formal receipt at startup and binds artifacts and plans to that receipt and the runtime source digest. Local formal/runtime source changes invalidate an open engine. Imported library and compiler inventories are checked at startup by the existing receipt verifier.

Every supplied cache is replay-checked against its retained request; the rule name alone has no evidential force. Plans are recomputed before application or accepted undo. Unknown fields, instructions, rules and schema versions; stale source/target plans; missing or altered dependencies; malformed Boolean values; duplicate JSON keys; and policy-bound violations are rejected. Operations return new objects without mutating input artifacts. There is no dependency garbage collection.

Bounds are 4,096 instructions per request, 128 stored requests, 256 views, 65,536 stored instructions in total, and 8 MiB per input JSON file. Recovery counters concern instruction replay, not total CPU work. JSON decoding, hashing, allocation, validation and source admission also have costs.

## Running it

From the repository root, these commands work in PowerShell 7. Use distinct output files; shell redirection must never target the input file.

```powershell
python research/nima/checkers/active_view.py build research/nima/examples/active-view-requests.json > research/nima/results/view-full.json
python research/nima/checkers/active_view.py plan research/nima/results/view-full.json --replay-budget 100 > research/nima/results/view-plan.json
python research/nima/checkers/active_view.py apply research/nima/results/view-full.json research/nima/results/view-plan.json > research/nima/results/view-small.json
python research/nima/checkers/active_view.py inspect research/nima/results/view-small.json
python research/nima/checkers/active_view.py undo research/nima/results/view-small.json research/nima/results/view-plan.json > research/nima/results/view-restored.json
```

The checker also leaves directly usable demonstration artifacts:

- `results/active-view-full.json`
- `results/active-view-plan.json`
- `results/active-view-compact.json`

## Tests and measured costs

`checkers/check_active_view.py` runs `test_active_view.py` and writes `results/active-view-audit.json` and `results/active-view-tests.log`.

Coverage includes every instruction list through length five and both inputs: 126 requests, each in four cache modes. An independent prefix-parity oracle checks output and trace. Tests exercise replay budgets, exact undo of partial modes, input immutability, shared dependencies, malformed artifacts, stale/forged plans, and the actual CLI pipeline.

The fixed demonstration retains three requests, including one with 256 instructions:

| Canonical JSON storage | Full | Cleared |
|---|---:|---:|
| Active views | 2,019 bytes | 271 bytes |
| Retained request store | 2,091 bytes | 2,091 bytes |
| Whole artifact | 4,242 bytes | 2,494 bytes |

The saved undo plan takes 1,033 bytes. The cleared artifact plus that plan takes 3,527 bytes. Full recovery takes 258 replay steps and restores the original canonical JSON exactly. Planning and applying each also perform 258 validation replay steps. Undo performs additional plan revalidation.

A separate hostile confirms that, for a tiny record, saving the undo plan costs more than the cache removal saves. Thus active-view reduction is not a universal storage or speed improvement. Byte counts concern canonical UTF-8 JSON, not peak heap allocation or filesystem overhead.

## Disposition and trust boundary

The restricted backend implements automatic allowlist selection, clearing, dependency retention, materialization, exact undo, and explicit cost reporting. Its formal model has universal mode-change and execution-agreement proofs. The executable Python/JSON implementation has bounded conformance and hostile-test evidence; it is not extracted from Agda or proved to refine the model.

Hashes are integrity/version guards, not authentication or proof terms. Serialized replay-rule identifiers do not stand for arbitrary Agda witnesses. General typed payload support, automatic discovery of new contraction rules, and a fully verified runtime/codec remain open. Files remain uncommitted.
