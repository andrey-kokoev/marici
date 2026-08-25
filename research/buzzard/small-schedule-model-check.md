# Exhaustive split read/write schedule check

`SplitMachineState` explicitly records shared memory, each site's cached read,
and both success bits. `LegalSplitSchedule` enumerates the six interleavings of
two read/write pairs that preserve each site's read-before-write program order.

Executable classification proves:

- serialized `AABB` and `BBAA` schedules preserve exactly one success;
- the four schedules where both reads precede their relevant writes produce
  `(true,true)`;
- exactly two of the six legal schedules are safe and four violate single use.

The `ABAB` execution reduces to the earlier `lostUpdateTrace`, connecting the
enumeration to the theorem-level hostile fixture.

This bounded check is regression evidence only. It does not prove correctness
for arbitrary site counts, weak-memory executions, compiler reorderings, or
unbounded histories.

Missing convention-fixed inputs:

- concrete memory-order semantics;
- whether reads/writes may fail or be retried;
- scheduler constraints beyond per-site program order;
- extension from two sites to a parameterized finite site type.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/SmallScheduleModelCheck.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8729 jobs).` The site build was not run.
