# Version ABA hostile audit — cycle 20

## Increment

The hostile trace opens at version 6 with the required epoch vector, changes at
version 7, then closes after reusing version 6. Endpoint versions agree even
though the epoch vector changed in between.

`FreshTransition` requires every state-changing transition to allocate a
strictly larger version. Two fresh transitions imply a strictly increasing
endpoint version, so endpoint stability and an intervening two-step change are
incompatible. The ABA fixture is proved to violate this discipline.

## Disposition

**Rejected version equality without non-reuse/monotonicity.** A stable endpoint
number plus state binding is not evidence that no intervening update occurred
when versions may wrap or be reused.

## Missing inputs

1. Bounded-counter wraparound policy and epoch extension.
2. Proof that every concrete state mutation increments the version.
3. Crash persistence and rollback behavior of the counter.
4. Distributed allocation of globally ordered versions.
5. Whether monotonicity or a unique content hash is the source contract.

## Verification

From `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Results:

- targeted file: passed with no diagnostics;
- project: `Build completed successfully (8716 jobs).`

Lean/mathlib version: `v4.33.1`. The Marici site build was not run.
