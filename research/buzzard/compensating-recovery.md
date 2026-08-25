# Compensating recovery is not rollback

`CompensationState` records historical protected effects and compensating
actions separately. `OutstandingEffects` is their truncated difference.

A completed-and-compensated history and a rollback history both have zero
outstanding effects, but the states differ: compensation retains one effect and
one compensation. It also fails `UncompensatedExactlyOnce`, which requires one
effect and no compensation.

Controlled compensation succeeds only while an uncompensated effect remains.
A hostile naive implementation can compensate twice, yielding one effect and
two compensations.

Recovery resolutions are separately typed as retry, abandon, compensate, and
manual adjudication. Every resolution requires explicit source authority. Retry,
abandon, and compensate have different state semantics; abandon and manual
adjudication demonstrate that equal state projections do not make authority
kinds interchangeable.

Missing convention-fixed inputs:

- the domain-specific meaning of a compensating action;
- whether compensation is partial, fallible, or itself retryable;
- authorization for compensation and manual adjudication;
- accounting semantics when effects are not invertible.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/CompensatingRecovery.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8730 jobs).` The site build was not run.
