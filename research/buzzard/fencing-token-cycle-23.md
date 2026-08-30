# Cycle 23 — execution-target fencing

## Increment

`ExpiryOnlyExecutable` models a target that validates only lease time.
`FencedExecutable` additionally requires the capability epoch to equal the
execution target's current monotone epoch.

After `revokeEpoch`, the old lease is still unexpired but fails the fence.
Successful fenced execution therefore supplies an equality witness tying the
presented capability to the target's live epoch. Identity transport cannot
refresh that witness.

## Two-sector evidence

- Temporal authority: advancing the live epoch revokes earlier grants.
- Distributed execution: the resource must validate the epoch at the point of
  side effect; issuer-side revocation state alone cannot stop a stale holder.

## Hostile countermodel

`expiry_check_alone_does_not_enforce_epoch_revocation` exhibits an unexpired
stale lease accepted by the weak check and rejected by the fenced check.

## Abstraction disposition

Specialized: this does not add a universal revocation mechanism. It isolates
the smallest missing interface—an execution target must expose authoritative,
monotone epoch validation.

## Missing convention-fixed inputs

- Which component owns and durably increments the fencing epoch.
- Whether epoch comparison is equality or an ordered-token policy.
- The crash-atomic relationship between epoch advancement and side effects.
- Wraparound bounds if the concrete token type is finite.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8716 jobs).` The Marici site build was not run.
