# Crash and restart traces

`CrashTraceEvent` makes persistence boundaries explicit over the fenced-effect
state machine:

- `atomicAttempt` persists fence advancement and effect together;
- `persistFenceOnly` models the advance-only crash split;
- `persistEffectOnly` models the effect-only crash split;
- `restart` reloads durable state without changing it.

All three histories use the same retry policy after restart:

```text
atomic attempt / split persistence -> restart -> atomic retry
```

Their final effect counts are respectively `1`, `0`, and `2`. Thus retry logic
and restart transport do not compensate for a missing crash-atomic persistence
interface.

The general restart theorem proves that restart preserves both the fence and
effect count. Delayed restart therefore cannot undo an effect or manufacture a
missing one.

Missing convention-fixed inputs:

- which fields are durable at each crash point;
- write ordering and storage acknowledgment semantics;
- recovery authority for in-doubt external effects;
- whether the external effect shares a transaction domain with the fence.

Verification commands from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/CrashRestartTrace.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8723 jobs).` The site build was not run.
