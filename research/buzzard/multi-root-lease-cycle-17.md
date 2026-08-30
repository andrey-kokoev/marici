# Multi-root epoch leases — cycle 17

## Increment

`MultiRootLease n` snapshots the epochs of every required authority root and
requires `0 < n`. `MultiRootState n` carries all current epochs and the shared
single-use nonce. Execution requires pointwise equality of every epoch, lease
freshness, an unused nonce, and exact kind equality.

The two-root fixture succeeds when both epochs match. Incrementing only the
second root rejects the entire lease even though the first root still matches.
Thus a cached or fresh proper subset of roots cannot supply multi-root live
authority. A zero-root lease is unrepresentable.

## Disposition

**Generalized a scalar revocation epoch to a finite nonempty root vector.** The
vector is checked atomically by specification; no concrete multiword snapshot
algorithm is asserted.

## Missing inputs

1. Atomic snapshot/refinement for independently updated root epochs.
2. Dynamic root-set membership and root addition/removal.
3. Root identity, jurisdiction, and source provenance.
4. Distributed clock semantics for expiry.
5. Crash persistence of the vector and nonce.

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
