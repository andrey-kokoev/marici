# Cycle 22 — bounded collision audit

## Increment

`CollisionFreeOn audited digest` records injectivity only on an explicit audited
domain. `CollisionFree digest` remains full mathematical injectivity.

The finite digest `threeToBoolDigest : Fin 3 → Bool` distinguishes the audited
pair `{0, 1}` but collides on `1` and `2`. Thus a successful bounded collision
audit cannot be promoted to universal collision freedom.

## Cross-sector reading

- Distributed authority: a content-bound epoch snapshot may rely on an exact
  injective identifier, or on a separately typed cryptographic assumption.
- Source-relative audit: tested inputs and bounds remain part of the claim and
  cannot silently become an unrestricted ontology.

## Hostile countermodel

`bounded_collision_audit_does_not_imply_collision_free` supplies a concrete
three-input/two-digest countermodel.

## Missing interface

A faithful statement of computational collision resistance still needs a
security parameter, an adversary class, a probability distribution, and a
negligibility notion. None is inferred from bounded testing, and no real hash
is asserted mathematically injective.

## Verification

Run from `research/buzzard/marici_formal`:

```text
lake env lean MariciFormal/TemporalAuthority.lean
lake build
```

Result: both commands passed under Lean `v4.33.1`; the project reported
`Build completed successfully (8716 jobs).` The Marici site build was not run.
