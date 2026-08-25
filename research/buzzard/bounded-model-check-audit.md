# Bounded finite model-check evidence in Lean

Owner: `marici.Buzzard`

Strength: finite-cutoff theorem and hostile larger-domain countermodel.

Source fixtures:

- `research/buzzard/marici_formal/MariciFormal/SmallScheduleModelCheck.lean`
- `research/buzzard/marici_formal/MariciFormal/AuditRecord.lean`
- Strominger's bounded two-site distributed linear-consumption schedule model.

## Formal increment

`CheckedDomain X` contains an explicit finite list and a no-duplicates proof.
`CheckedDomain.Covers` is the additional proposition that every `X` occurs in
that list. `FiniteModelCheck X` records a predicate and proof for each listed
input. Its conversion to `BoundedClaim X` preserves exactly that membership
boundary.

`FiniteModelCheck.universal_of_coverage` proves the only admitted promotion:
listed checks become universal over `X` when an explicit coverage witness for
`X` is supplied.

For the six read-before-write schedules:

- `legalSplitDomain_covers` proves exhaustive coverage of
  `LegalSplitSchedule`;
- `splitClassificationCheck` verifies that exactly the serialized schedules
  `AABB` and `BBAA` are safe;
- `checked_split_classification_is_universal_on_declared_type` promotes this
  classification only over the declared six-constructor type;
- `splitScheduleAudit` embeds the check in `SourceRelativeAuditRecord`, with
  distinct producer/verifier values, result `(2,4)`, and bound `6`.

## Hostile enlargement

`ExtendedSchedule` adds `retryAfterCrash` to the six legal schedules.
`extendedSplitDomain` contains embeddings of every old schedule but does not
contain the new constructor. Lean proves:

- every old schedule is covered;
- the enlarged type is not covered;
- the lifted bounded check is not universal on the enlarged type.

Thus exhaustive checking is relative to a typed schedule grammar. Transporting
all old cases cannot manufacture coverage of new crash, retry, communication,
or recovery behavior.

## Assumptions and missing interfaces

The generic definitions require only types, lists, membership, and
propositions. The fixture uses the already frozen Boolean two-site machine and
its six legal schedules. No probability, fairness, liveness, physical timing,
or unbounded concurrency assumption is present.

Promotion to a richer protocol requires independently supplied:

1. the larger schedule grammar;
2. an exhaustive enumerator or other coverage theorem for that grammar;
3. semantics for each newly admitted action and failure mode;
4. a fidelity theorem relating the finite machine to the claimed source;
5. bounds on sites, retries, crashes, messages, and recovery epochs;
6. producer and verifier authority for the enlarged claim.

The numeric audit bound is evidence metadata, not coverage or authority.

## Verification

Run from `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/BoundedModelCheckAudit.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

Results on 2026-08-25:

- targeted file: exit code `0`, no diagnostics;
- project: `Build completed successfully (8732 jobs)`;
- no site build was run.

Changed owned files:

- `research/buzzard/marici_formal/MariciFormal/BoundedModelCheckAudit.lean`
- `research/buzzard/marici_formal/MariciFormal.lean`
- `research/buzzard/bounded-model-check-audit.md`

No Git command was used. Nothing was committed or pushed.
