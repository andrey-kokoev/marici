# Bounded multiplicity traces

`BudgetState` records remaining uses and successful uses. `attemptBudget`
consumes one unit exactly when one remains, and `runBudgetTrace` executes an
arbitrary finite number of attempts.

The general conservation theorem proves:

```text
final remaining + final successes = initial remaining + initial successes
```

Consequently a fresh capability can never produce more successes than its
declared bound.

Executable histories distinguish the resource types:

- bound one followed by three attempts yields one success;
- bound two followed by three attempts yields two successes.

Thus `BoundedMultiplicity 2` is not a repair preserving single-use semantics;
it is an explicitly different authority type. A Boolean “available” projection
maps both initial states to `true`, demonstrating that availability erases the
resource distinction.

Missing convention-fixed inputs:

- whether budget is global or partitioned across loci;
- atomic persistence of decrement and protected side effect;
- replenishment authority, if replenishment is permitted;
- treatment of failed or compensated executions in budget accounting.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/BoundedMultiplicity.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8724 jobs).` The site build was not run.
