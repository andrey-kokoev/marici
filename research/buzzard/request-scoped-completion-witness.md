# Request-scoped completion witnesses

## Increment

`ScopedCompletionWitness` binds completion evidence to a `RequestId`.
`recoverScoped` returns a recovery decision only when that identifier matches
the identified request; otherwise it returns `none`.

## Positive examples from two established structures

- Retry identity: request IDs determine whether an execution is a replay or a
  distinct operation.
- Recovery evidence: an applicable completion witness chooses retry exactly
  when its bound operation has not completed.

## Hostile countermodel

A truthful “completed” witness for request `7`, if treated as unscoped, yields
“do not retry” for incomplete request `8`, which is incorrect. The scoped
interface rejects this cross-request replay instead.

## Abstraction disposition

Generalized narrowly. Evidence persistence is preserved, but applicability does
not transport to a different request identity.

## Missing convention-fixed inputs

- Canonical construction and equality of request identifiers.
- Binding/authentication between the identifier and completion payload.
- Namespace authority preventing independent issuers from reusing IDs.
- Retention bounds for old completion witnesses.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8716 jobs).` The Marici site build was not run.
