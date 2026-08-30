# Retry identity and at-most-once execution — cycle 13

## Increment

`RequestLedger` stores consumed request IDs. `admitRequest` atomically classifies
a delivery as either a fresh execution, inserting its ID, or a replay of an
already consumed ID.

Proved:

- every first delivery to an empty ledger executes;
- the second delivery of the same ID is a replay;
- the replay does not grow or otherwise change the consumed-ID ledger;
- two distinct IDs may both execute;
- therefore relabeling a retry with a fresh ID defeats duplicate suppression.

`IdentifiedRequest` carries separate source authority for its identity. The
ledger proves at-most-once execution per admitted ID; it does not derive that
two messages denote the same request.

## Disposition

**Specialized single consumption to request-indexed at-most-once execution.**
Delivery replay and capability execution are now separate dispositions. This
does not yet provide exactly-once response delivery or durable crash recovery.

## Missing inputs

1. A source-derived equality rule for request IDs across transport boundaries.
2. Cached result values if replay must return the original response.
3. Durable ledger persistence and crash-atomic insertion.
4. Garbage collection, epoch scoping, and safe ID reuse.
5. Binding between request admission and `attemptLease` in one transaction.

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
