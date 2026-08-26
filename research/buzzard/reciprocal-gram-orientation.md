# Reciprocal Gram orientation and local overlap: Lean packet

## Source boundary

This increment formalizes the finite algebra in Grothendieck's
`reciprocal-half-form-gram-positivity-does-not-orient-the-cross-kernel.md` and
the aggregation boundary of
`the-complete-one-prime-quarter-density-overlap-is-nonvanishing.md`.

## Formal objects and coefficient types

The Gram layer uses two-dimensional real coordinate vectors represented by
four scalars. `selfEnergy2` is the diagonal square norm and `crossOverlap2` the
ordinary cross pairing. A separate complex hostile represents reciprocal
conjugacy through the bilinear square sum.

The local-overlap layer is over an arbitrary field. It starts from the
normalized geometric rational expression; derivation of that expression from
an infinite prime-power series is not assumed.

## Theorems and hostile examples

- `gramDet_lagrange_identity` identifies the two-vector Gram determinant with
  a square, and `gram_principal_data_nonnegative` proves its principal data are
  nonnegative.
- `orthogonal_positiveGram_hostile` uses `(1,1)` and `(1,-1)`: both energies
  equal two, cross overlap vanishes, and determinant equals four.
- `conjugate_reciprocal_cross_hostile` uses `(1,i)`, whose bilinear square sum
  vanishes despite both components being nonzero.
- `normalizedGeometricOverlap_ne_zero` exposes the exact local numerator and
  denominator assumptions needed for nonvanishing.
- `finite_product_overlap_ne_zero` proves finite tensor-style aggregation
  preserves nonvanishing.
- `additive_overlap_cancellation_hostile` proves direct-sum aggregation need
  not preserve it.

This specializes the shared readout vocabulary: positive diagonal energy is
not cross-orientation authority, and multiplicative versus additive aggregation
must remain distinct constructors.

## Missing interfaces

The logarithmic-derivative tower still needs complex geometric-series
summation and its phase-circle lower bound. The Euler-log tower needs the
analytic logarithm, its chosen branch, and compact phase-circle nonvanishing.
Global work needs infinite-product reserve criteria. Actual theta features add
archimedean interval amplitudes, for which no acute-cone preservation theorem
is established. Canonical square-root rigging is positive but does not fill
any of these orientation interfaces.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/ReciprocalGramOrientation.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
