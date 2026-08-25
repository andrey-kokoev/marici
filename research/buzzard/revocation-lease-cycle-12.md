# Revocation-linearized execution leases — cycle 12

## Increment

`ExecutionLease` carries the authority epoch validated at check time, an
expiry time, and one authority kind. `LeaseState` carries the current live
epoch and the single-use nonce state.

`LeaseExecutable` requires simultaneously:

1. unchanged epoch;
2. execution before expiry;
3. an unused nonce;
4. exact authority-kind equality.

`attemptLease` performs this check and nonce consumption as one mathematical
transition. `attemptLease_success_iff` proves that success is equivalent to all
four conditions.

Finite fixtures prove a fresh live scoped lease succeeds, while nonce replay,
epoch revocation between validation and use, expiry, and authority-kind
widening each fail. The cached epoch equality at validation does not override
a later live-epoch change.

## Disposition

**Integrated temporal validity, kind preservation, and linear consumption in
one atomic specification.** This closes the abstract time-of-check/time-of-use
gap. It does not prove that a concrete implementation reads the epoch and
consumes the nonce atomically.

## Missing inputs

1. Refinement from an implementation transaction/CAS to `attemptLease`.
2. Multiple required authority roots and an atomic vector of epoch snapshots.
3. Clock semantics for lease expiry across loci.
4. Crash persistence and recovery of nonce/epoch state.
5. Operation and target scopes beyond the authority-kind field.

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
