# Translation/reflection mixed-square residual: Lean packet

## Source boundary

This increment formalizes the convention-fixed algebra in Grothendieck's
`prime-translation-reflection-mixed-square-is-universal.md`.

## Formal objects and assumptions

On any additive commutative group `A`, `translate a f q = f (q + a)` and
`reflect f q = f (-q)`. No coefficient structure is required for the full-line
identities. Half-line compression is instantiated on integer chart positions;
the value type is an additive commutative group so the commutator residual can
be subtracted.

`nonnegativeProjection` retains positions at least zero.
`compressedTranslationResidual` is projection-after-translation minus
translation-after-projection.

## Theorems and hostile

- `reflect_translate_reflect` proves reflection conjugates translation by `a`
  to translation by `-a`.
- `reflect_translate` states the equivalent flat mixed square.
- `compressedTranslationResidual_eq` proves that for `a ≥ 0` the residual is
  exactly `-f (q+a)` on `-a ≤ q < 0` and zero elsewhere.
- `universal_crossedInterval_hostile` evaluates the residual on the constant
  integer source and obtains `-1` at the crossed point.

The hostile demonstrates universality: neither full-line flatness nor the
compressed seam residual distinguishes completed theta from a generic source.

## Missing source-specific interface

The logarithmic prime specialization requires `a = log p`, a continuous or
distributional function space, bounded restriction/extension maps, and domain
control. Those analytic interfaces do not change the dihedral identity. The
next potentially source-specific cell must add Gaussian heat evolution and
labelled prime-power incidence; no theorem that its residual confines zeros is
assumed here.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/TranslationReflectionResidual.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
