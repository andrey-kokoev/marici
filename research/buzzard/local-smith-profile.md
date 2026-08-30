# Determinant order does not classify local failure

Owner: `marici.Buzzard`

Source locator: `Divisor order does not classify the failure module` and
`Determinantal ideals recover the Smith profile` in
`research/strominger/distinction-preserving-completion.md`.

## Formal increment

Lean represents the ordered local Smith exponents of a two-direction fixture
as a pair of natural numbers. Their sum is the determinant order, while the
number of positive exponents is the seam corank.

The profiles `(0,2)` and `(1,1)` both have determinant order two. The first has
corank one and represents one depth-two alias; the second has corank two and
represents two depth-one aliases. Lean proves the profiles and failure types
are distinct despite equal aggregate order.

The first two determinantal-ideal valuations are modeled as the minimum
exponent and the total exponent. Lean proves generally for ordered profiles
that successive differences recover the original Smith pair. The fixtures
give valuations `(0,2)` and `(1,2)`, which recover `(0,2)` and `(1,1)`.

## Type-system consequence

Determinant order is an aggregate and is not a complete failure invariant.
The shared interface must retain the local Smith profile, or equivalently the
successive determinantal-ideal valuations, to distinguish one deep lost
direction from several shallow ones.

This increment specializes the divisor-multiplicity theorem by exposing the
internal partition that aggregate order erases.

## Boundary and missing interfaces

- the actual analytic observability matrix over a local discrete valuation ring;
- cokernel modules and their finite-length proof;
- minor-ideal valuation for arbitrary matrix size;
- invariance under regular invertible row and column transformations;
- the source interpretation of each Smith generator.

## Verification

From `research/buzzard/marici_formal/`:

```powershell
& "$env:USERPROFILE/.elan/bin/lake.exe" env lean MariciFormal/LocalSmithProfile.lean
& "$env:USERPROFILE/.elan/bin/lake.exe" build
```

No Marici site build or Git operation is part of this increment.
