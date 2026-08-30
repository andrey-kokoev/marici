# Atomic identified lease transaction — cycle 14

## Increment

`IdentifiedLeaseState` combines the live epoch/nonce state with the consumed
request-ID ledger. `attemptIdentifiedLease` is one specification transition:

1. a previously consumed ID is returned as `replayed` without execution;
2. a fresh ID attempts the temporally and kind-scoped lease;
3. only successful lease execution consumes both the nonce and request ID;
4. a failed lease is `rejected` without inserting its request ID.

Finite fixtures prove the first authorized request executes and consumes both
resources, its same-ID retry replays, a fresh second ID cannot reuse the
consumed lease, and a request rejected after epoch revocation does not poison
the identity ledger.

## Disposition

**Integrated request identity and temporal single consumption in one atomic
specification.** It distinguishes `executed`, `replayed`, and `rejected`.
This is not yet a database or hardware transaction implementation theorem.

## Missing inputs

1. Cached response values for replay, rather than disposition alone.
2. Concrete crash-atomic persistence of nonce and request ledger together.
3. A refinement from an implementation transaction to this transition.
4. Epoch-scoped ID reuse and garbage collection.
5. Multiple capability/lease objects and request-to-target binding.

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
