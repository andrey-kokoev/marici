# Completion availability is not negative evidence

Completion readout is typed as `Option CompletionStatus`, separating:

- `none`: the evidence is unavailable;
- `some incomplete`: available negative completion evidence;
- `some unknown`: available evidence whose completion status is unresolved.

The total recovery policy retries only `incomplete`, suppresses retry only for
`completed`, and defers for `unknown`. The theorem `unknown_status_forces_deferral`
shows that no terminal action is sound under this policy for unresolved status.

The hostile implementation `defaultUnavailableToIncomplete` silently converts
absence into negative evidence. It requests retry even in a world where the
effect already completed, violating the existing exactly-once recovery
criterion.

The module also imports Strominger's finite-observation vocabulary and restates
its independent theorem that an unavailable port differs from an available
zero-valued port. The shared abstraction is only the availability shape; port
values and completion evidence remain sector-specific types.

Missing convention-fixed inputs:

- which failures produce unavailable versus available-unknown evidence;
- whether and when unknown status may become resolved;
- timeout authority for abandoning deferred recovery;
- whether incomplete evidence is monotone or may later be superseded.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/CompletionAvailability.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8725 jobs).` The site build was not run.
