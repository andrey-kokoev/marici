# Determinantal profiles commute with coefficient base change

Owner: `marici.Buzzard`

Source locator: the specialization step in
`research/buzzard/fitting-rank-strata.md`, audited against the typed profile in
`research/buzzard/two-by-two-determinantal-profile.md`.

## Formal increment

For a ring homomorphism `f : R →+* S`, Lean proves:

- mapping the entry ideal of any rectangular matrix equals the entry ideal of
  its coefficientwise mapped matrix;
- mapping the determinant ideal of a two-by-two matrix equals the determinant
  ideal of its mapped matrix;
- consequently both fields of `TwoByTwoDeterminantalProfile` commute with
  coefficient base change.

The API retains an important distinction. Rectangular matrices use the
pointwise `Matrix.map`, while square matrices may use the bundled
`RingHom.mapMatrix` because only the latter carries matrix multiplication and
determinant compatibility.

Lean also identifies the existing `specializeMatrix point` operation with
mapping coefficients by `MvPolynomial.eval point`. At the origin, the mapped
entry ideals of `diag(u,v)` and `diag(1,u*v)` remain unequal. Thus the hostile
lower-minor distinction survives the typed specialization.

## Assumptions and boundary

The general entry-ideal theorem needs only commutative rings and no finiteness
assumption on matrix indices. The determinant and profile theorems are bounded
to `Fin 2`. The hostile fixture uses rational coefficients.

This proves algebraic base-change compatibility. It does not assert flatness,
faithful flatness, preservation of module kernels, a completion universal
property, or source authority for a specialization point.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/DeterminantalProfileBaseChange.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build, Git command, commit, or push is part of this increment.
