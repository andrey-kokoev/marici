# The rational profile-separation locus is exactly the origin

Owner: `marici.Buzzard`

Source locator: synthesis of the separating origin in
`research/buzzard/determinantal-profile-base-change.md` and the nonreflecting
unit point in `research/buzzard/base-change-nonreflection.md`.

## Formal increment

For each rational point `point : Fin 2 → Rat`, Lean forms the two-stage
determinantal profile after evaluating the polynomial matrix at that point.
It proves the exact specialized matrices are

`diag(point 0, point 1)` and `diag(1, point 0 * point 1)`.

Lean then proves:

- any rational matrix with a nonzero entry has unit entry ideal;
- away from the origin, at least one entry of the first specialized matrix is
  nonzero, so its entry ideal is the unit ideal;
- the second specialized matrix always has unit entry ideal because its
  upper-left entry is one;
- the determinant ideals agree at every point by base-change compatibility;
- at the origin the entry ideals differ;
- therefore the specialized profiles differ exactly when `point = origin`.

## Audit disposition

This is a complete rational-point classification for one frozen pair of
two-by-two matrices. It upgrades two examples into an iff and shows that
faithfulness of a specialization is locus-dependent.

It does not construct a scheme-theoretic support, radical ideal, open or closed
subscheme, or general semicontinuity theorem. It also does not identify these
rational points with physical configurations.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/ProfileSeparationLocus.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
