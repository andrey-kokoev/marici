# Finite unitary-orbit growth: Lean packet

## Source boundary

This increment formalizes the norm-theoretic proposition in Grothendieck's
`li-finite-unitary-orbit-no-go.md`. It does not assert Li positivity or import
an unboundedness theorem for the Li coefficients.

## Formal objects and coefficient types

The ambient coefficient object is an arbitrary seminormed additive
commutative group. `NormPreserving operator` states exactly the property used
from unitarity. Iteration is by natural numbers. No linearity, scalar field,
inner product, completeness, or finite dimension is needed for the bound.

## Theorems and hostile

- `norm_iterate_eq` proves norm preservation for every iterate.
- `orbitCoboundary_norm_le_two` proves
  `‖x - U^[n] x‖ ≤ 2 ‖x‖`.
- `orbitCoboundary_norm_sq_le_four` proves the squared bound
  `‖x - U^[n] x‖^2 ≤ 4 ‖x‖^2`.
- `no_unbounded_finiteOrbitCoboundary` rules out unbounded coboundary norms
  for a fixed finite-norm source vector.
- `orbitCoboundary_bound_sharp` uses negation on the real line to attain both
  constants exactly.

## Missing interfaces

Applying the no-go to a named Li sequence requires an independently proved
unbounded-growth statement and a typed equality between that sequence and
the proposed orbit norm. Infinite or renormalized measures, distributional
vectors, varying domains, and non-unitary positive forms are different
resource types and are not rejected by this theorem.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteUnitaryOrbitNoGo.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
