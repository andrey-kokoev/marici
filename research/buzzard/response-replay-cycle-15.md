# Cached response replay — cycle 15

## Increment

`ResponseState Result` stores the lease state and a request-indexed optional
response. `attemptWithResponse` performs one specification transition:

- a cached ID returns `replayed result` without executing;
- a fresh authorized ID executes, consumes the lease, and atomically stores
  `produce id`;
- a rejected request stores nothing.

The finite fixture proves request 7 first returns and caches 107, then a retry
returns exactly the cached 107. Revocation rejection creates no cache entry.

The hostile crash-split record has persisted consumption but no persisted
response. It is at-most-once safe but not replay-complete, proving that
at-most-once execution alone is weaker than exactly-once observable replay.

## Disposition

**Specialized replay from disposition-only to result-preserving replay.** The
state transition is atomic by specification. It is not a durability theorem.

## Missing inputs

1. Crash-atomic persistence of nonce, request identity, and response together.
2. Response serialization and content-address integrity.
3. Failure semantics when response computation itself is partial.
4. Garbage collection and safe ID/cache expiry.
5. Concrete storage or transaction refinement.

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
