# Version-consistent epoch snapshots — cycle 19

## Increment

`SnapshotRead` records opening and closing versions plus the sampled epoch
vector. `VersionStable` requires equal versions. `SnapshotCertificate` then
ties the stable version and sampled vector to one `VersionedEpochState`.

The Cycle 18 torn read opens at version 2 and closes at version 4, so it is
rejected. A stable version-6 read of the required `(4,9)` vector has an
executable certificate and is proved to match every required epoch.

A second hostile fixture shows that equal versions alone are insufficient if
the sample is not bound to the versioned state: a fabricated stable-version
read can still carry the wrong epoch vector.

## Disposition

**Specialized the atomic-snapshot requirement into a proof-relevant version
certificate.** This is an interface, not a seqlock, MVCC, or transaction
implementation.

## Missing inputs

1. A protocol proving that version equality excludes intervening writes.
2. Version monotonicity, wraparound, and ABA protection.
3. Memory barriers and read ordering.
4. Crash persistence of version and epoch vector.
5. Refinement from a concrete snapshot algorithm.

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
