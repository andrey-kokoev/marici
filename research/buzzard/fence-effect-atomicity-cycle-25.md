# Cycle 25 — fence/effect crash atomicity

## Increment

`FencedEffectState` couples the resource's ordered fence register with a finite
count of protected effects. `attemptFencedEffect` is the positive atomic
specification: a fresh token advances the register and increments the effect
count in one transition; replay is rejected without another increment.

## Positive examples from two sectors

- Temporal authority: accepted token state persists and rejects replay.
- Distributed execution: the protected side effect occurs exactly once under
  an atomic fence/effect transition.

## Hostile countermodels

- `fenceOnlyCrash`: token `4` is durable but the effect is missing. Retry is
  rejected, so the requested effect is permanently lost.
- `effectOnlyCrash`: the effect occurred but the register remains at `3`.
  Retry with token `4` succeeds and raises the effect count to two.

Ordered comparison alone therefore proves neither durable completion nor
exactly-once execution.

## Abstraction disposition

Specialized. This reuses the earlier crash-atomic response distinction without
claiming that every resource supports transactions with its fence register.

## Missing convention-fixed inputs

- A concrete transaction or recovery protocol spanning fence state and effect.
- Whether the protected effect is rollbackable, idempotent, or compensatable.
- Which durable observation constitutes completion after a crash.
- Recovery authority for resolving an in-doubt transition.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8716 jobs).` The Marici site build was not run.
