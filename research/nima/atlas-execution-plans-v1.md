# Source-replayable atlas execution plans

A compatible certified target is no longer treated as a successful construction unless a schedule is produced and replayed. The planner retains the entire starting selection, adds only target packets, and permits exactly two transition kinds:

1. **Singleton:** add one reader through an interface active in the enlarged selection, with its source already selected.
2. **Whole-body materialization:** atomically add the native intermediate readers of all currently active PE shortcuts sharing one vacant reference neutron body.

No arbitrary multi-reader batch fallback is allowed. Every step boundary is compatible and rooted. Exit and face obligations may remain pending until the final certificate, exactly as in the existing seed generator.

## Implementation

`atlas-execution-plans.mjs` exports:

- `planExecution(model, start, target, options)`: construct a schedule for a specified certified target.
- `replayExecution(model, plan)`: independently re-derive legal operations, source audits and all recorded annotations.
- `completeAndPlan(model, start, options)`: source-complete the selected set, then schedule it. A completion whose schedule fails is returned as a scheduling failure, not a construction success.

A stable anchor in the final-active graph gives a linear constructive schedule. Otherwise bounded breadth-first search explores rooted subsets between start and target using the declared transitions. This is not a globally optimal operation-count planner: the stable-anchor fast path need not minimize batches/steps. Exhaustion means unreachable under this operation family in this fixed target interval; it does not mean the assembly is impossible. State/time limits return incomplete.

Every plan binds to a fingerprint of the mode, origin bound, native cell geometry, complete marked-reader records and compiled interfaces. Every step records:

- added and resulting selected readers;
- the actual attaching interface, or all native PN/NE replacement factors of a body batch;
- exit and contact obligations before and after;
- resolved and introduced obligations;
- disabled PE shortcuts.

Replay recomputes these values from the source auditor rather than trusting saved booleans or explanations. Atomic steps do not pretend their invalid singleton intermediates are legal.

## Verification

Fresh checks produce and replay:

| Family | Result |
|---|---|
| Exact two-reader scheduling obstruction | one legal batch adding6/51; singleton-only planning is unreachable |
| Previously blocked D2 start/target pairs | all1,803 planned and replayed, each using exactly one batch |
| Previously certified body-materialization targets | all195 planned and replayed |
| Missing-face materialization completions | all70 source-completed, scheduled and replayed |
| D3 repaired-core targets from the seed | all8 planned and replayed |
| Native D0 seed construction |2 singleton steps, no experimental batch |

Nine corruptions are rejected: wrong model, wrong body, partial batch, invented native factor, false obligation annotation, disabled batch permission, deleted step, wrong resulting selection, and duplicate added packet. Additional checks cover invalid retained sets, mode mismatch, explicit state/time stops and CLI JSON replay. These are finite source-replay tests, not a universal scheduling theorem or field-sewing proof.

## CLI

A request file names the source model and retained selection. Give a target to schedule it, or omit the target to invoke completion followed by scheduling:

```json
{
  "maxOrigin": 2,
  "mode": "experimental-terminal-PE",
  "start": [0,1,2,5,16,8,20,53],
  "target": [0,1,2,5,6,16,8,20,51,53],
  "execution": {"maxStates": 100000, "maxMilliseconds": 10000}
}
```

```sh
node research/nima/plan-tessellated-atlas.mjs --request request.json --output plan.json
node research/nima/plan-tessellated-atlas.mjs --replay plan.json
node research/nima/checkers/check_atlas_execution_plans.mjs
```

CLI exits:0 success,1 invalid input/replay failure,2 resource stop,3 non-successful completion or unreachable schedule. No source or viewer admission rule is changed.

[Two-reader example plan](results/atlas-execution-plans/two-reader-plan.json) · [Regression receipt](results/atlas-execution-plans/verification.json) · [All plans, gzip JSON](results/atlas-execution-plans/plans.json.gz)

## Boundary

Field attachment remains unbound. The next field-facing input can now be an actual construction trace with explicit incidental contacts and guard changes, rather than only a final packet set. Field transport/sewing requires its own checks and is not inferred from a successful geometric execution plan.
