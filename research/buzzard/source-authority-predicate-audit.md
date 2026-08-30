# Optional source-authority predicate audit

An audit of all `sourceAuthority`, `RepairAuthorized`, `ResolutionAuthorized`,
and `MayRecover` occurrences found one exact duplication:

```text
∃ witness, optionalAuthority = some witness
```

This predicate is now named `SourceAuthorized` in the shared temporal-authority
foundation. Both `RepairAuthorized` and `ResolutionAuthorized` delegate to it.
The positive `some` and hostile `none` theorems are proved once.

The audit deliberately did not merge:

- `MayRecover`, which is a Boolean live permission rather than an optional
  source-authority witness;
- `ShardGrant`, `NamespaceGrant`, and `BoundedMultiplicityAuthority`, whose
  mandatory `SourceAuthority` fields make absence unrepresentable;
- completion evidence, which remains evidence rather than authority.

Disposition: generalized narrowly. The new predicate reduces exact duplication
while preserving every existing producer/verifier, evidence/authority, and
mandatory/optional distinction.

Verification commands from `research/buzzard/marici_formal`:

```text
lake build MariciFormal.TemporalAuthority
lake env lean MariciFormal/CompensatingRecovery.lean
lake build
```

Result: all commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8730 jobs).` The foundational edit triggered a
full downstream rebuild, which completed without diagnostics. The site build
was not run.
