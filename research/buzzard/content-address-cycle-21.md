# Content-addressed epoch snapshots — cycle 21

## Increment

`CollisionFree digest` is an explicit injectivity witness. A
`ContentBoundSnapshot` carries sampled epochs and their digest, while
`SnapshotDigestConsistent` binds the two. Two consistent snapshots with equal
digests have equal epoch vectors only when collision freedom is supplied.

The positive exact fixture uses the epoch vector itself as its digest and is
provably collision-free. This is an exact mathematical content address, not a
claim about a finite cryptographic hash.

The hostile constant digest assigns the same address to the distinct required
and early epoch states. Lean proves both digest equality and state inequality,
so equal hashes without collision evidence cannot authorize state identity.

## Disposition

**Generalized state binding to an abstract collision-free content address.**
Finite cryptographic collision resistance is probabilistic/computational and
is not silently promoted to mathematical injectivity.

## Missing inputs

1. The actual serialization and digest algorithm.
2. Canonical encoding and domain separation.
3. Computational collision-resistance assumptions and security parameter.
4. Binding between stored digest, epoch vector, and atomic snapshot event.
5. Replay and revocation behavior under digest-algorithm migration.

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
