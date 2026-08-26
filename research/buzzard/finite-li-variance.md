# Degree-two Li determinant as variance: Lean packet

## Source boundary

This increment formalizes the finite atomic positive-measure core of
Grothendieck's `li-degree-two-variance-theorem.md`. It does not construct the
positive measure from arithmetic data and makes no Li-positivity or RH claim.

## Formal objects and coefficient types

The coefficient type is `ℝ`. A finite family indexed by `Fin n` carries
strictly positive weights and real coordinates representing `cos θ`. The
degree-two cosine moment is defined using
`cos(2θ) = 2 cos(θ)^2 - 1`. The existing weighted Cauchy--Schwarz theorem
from `WeightedRigging.lean` supplies positivity.

## Theorems and controls

- `degreeTwoLiDeterminant_eq_twice_varianceNumerator` proves the exact
  determinant/variance identity.
- `weightedDual_self_eq_mass` identifies the dual norm of the weight vector
  with total mass.
- `degreeTwoLiDeterminant_nonneg` proves positivity for strictly positive
  finite weights.
- `degreeTwoLiDeterminant_concentrated_and_spread_controls` distinguishes a
  concentrated coordinate with determinant `0` from two opposite coordinates
  with determinant `8`.

## Missing interfaces

The general measure theorem needs finite positive Borel measures on the unit
circle, measurability and integrability of cosine, and the equality cases of
Cauchy--Schwarz modulo almost-everywhere equality. The arithmetic application
still needs a source-derived positive moment functional. Positivity may not be
assumed merely by postulating the desired measure.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteLiVariance.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
