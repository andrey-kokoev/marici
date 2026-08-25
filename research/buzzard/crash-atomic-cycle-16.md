# Crash-atomic response persistence — cycle 16

## Increment

`DurableExecution Result` stores the durable nonce-consumed bit and optional
response. `CrashConsistent` requires the two facts to agree: consumption is
persisted exactly when a response exists.

The atomic persistence outcome has only two recovery states:

- before commit: unused nonce and no response;
- after commit: consumed nonce and the committed response.

Every atomic recovery is proved crash-consistent. The nonce-only and
response-only split writes are both proved inconsistent. Under the invariant,
durable consumption is equivalent to existence of a replayable response.

## Disposition

**Generalized the crash-split countermodel into a persistence invariant.** The
formalization specifies atomic durability but does not implement it through a
write-ahead log, database transaction, replicated log, or storage barrier.

## Missing inputs

1. Refinement from a concrete persistence protocol to the two atomic outcomes.
2. Torn writes, checksums, flush ordering, and storage failure models.
3. Epoch and authority-root persistence in the same transaction.
4. Replication and recovery quorum semantics.
5. Cache garbage collection and safe request-ID reuse.

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
