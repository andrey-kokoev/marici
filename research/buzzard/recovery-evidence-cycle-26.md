# Cycle 26 — in-doubt recovery evidence

## Increment

`RecoveryCorrect happened retry` says to retry exactly when the protected effect
did not already happen. The reusable impossibility theorem proves that no one
Boolean decision is correct in both worlds.

`deterministic_recovery_cannot_guarantee_exactly_once` then makes the epistemic
premise explicit: if both crash worlds expose the same durable observation, a
deterministic recovery policy necessarily returns the same decision and fails
in at least one world.

## Positive examples from two sectors

- Distributed execution: an authoritative `CompletionWitness` selects retry or
  no-retry correctly.
- Typed authority: `AuthorizedRecovery` keeps completion evidence separate from
  source authorization to perform recovery.

## Hostile countermodels

- Identical durable observations cannot distinguish effect-missing from
  effect-completed worlds.
- Correct completion evidence with `sourceAuthorized = false` still does not
  confer recovery authority.
- Recovery authority without completion evidence cannot choose safely across
  both possible worlds.

## Abstraction disposition

Generalized narrowly across crash recovery and typed authority. The model does
not assert that a completion witness exists, is truthful, or can be reconstructed
from a fence record.

## Missing convention-fixed inputs

- Which side-effect owner may issue a completion witness.
- Authentication and freshness of that witness.
- Whether an absent witness means incomplete or merely unavailable.
- Authorized resolution for permanently ambiguous executions.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8716 jobs).` The Marici site build was not run.
