# Cohomology representative anomaly: Lean packet

## Source boundary

This increment formalizes the quotient-independence core of Grothendieck's
`cohomology-representative-anomaly-class.md`. It does not invent the graded
complexes, defect operator, or physical boundary matrices needed for the full
chain-level statement.

## Formal objects and coefficient types

Parameters, target cochains, and source classes are arbitrary additive
commutative groups. A boundary and pullback are additive homomorphisms.
`CohomologousBy` records a change by an image of the boundary.
`representativeAnomaly alpha` is the pullback of that boundary.

## Theorems and hostile

- `representativeIndependent_iff_anomaly_zero` proves that the pullback is
  independent of representatives exactly when every anomaly vanishes.
- `exact_target_maps_to_zero_of_representativeIndependent` isolates the
  necessary exact-to-zero law.
- `nonzero_representativeAnomaly_hostile` uses identity maps on `ℤ`: `0`
  and `1` are declared cohomologous through the identity boundary, but the
  exact representative maps to `1`, so descent fails.

## Missing interfaces

The full theorem needs graded source and target complexes, square-zero
differentials, a graded map `S`, its degreewise defect `Omega`, the defect
Bianchi identity, cocycle subobjects, coboundary quotients, and the formula
relating `S* d` to `d S* + alpha Omega`. Cocycles mapping to cocycles is an
independent condition and is not implied by representative independence.
Five-site physical use remains gated by frozen relative boundary matrices.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/RepresentativeAnomaly.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
