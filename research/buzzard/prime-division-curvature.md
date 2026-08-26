# Prime multiplication/division curvature: Lean packet

## Source boundary

This increment formalizes the finite arithmetic core of Grothendieck's
`prime-multiplication-division-curvature-is-positive-exclusion.md` and
`the-vacuum-obstructs-zero-state-exclusion-annihilation.md`.

## Formal objects and assumptions

Labels are natural numbers. `multiplyLabel p n` is multiplication by `p`, and
`divideLabel p n` is partial division represented by `Option Nat`. The exact
curvature predicate compares division-after-multiplication with
multiplication-after-partial-division. Positivity is represented only by its
support predicate: the residual occurs precisely when `p` does not divide the
label.

For coefficient packets, the coefficient type has only a distinguished zero.
`ExclusionAnnihilated c p` says every coefficient visible outside the
`p`-divisible sector vanishes.

## Theorems and hostile

- `divisionAfterMultiplication_eq` proves the everywhere-defined route is the
  identity when `p > 0`.
- `multiplicationAfterDivision_eq` proves the reverse route is the identity on
  divisible labels and unavailable elsewhere.
- `primeDivisionCurvature_iff_not_dvd` identifies the residual exactly with
  primitive exclusion.
- `allPrimeExclusions_jointlyFaithful` uses Euclid's theorem to show that
  simultaneous annihilation by every prime exclusion kills every positive
  integer coefficient. Label zero is explicitly excluded.
- `prime_exclusion_reads_vacuum` and `nonzero_vacuum_hostile` prove that a
  nonzero coefficient at label one prevents annihilation by every individual
  prime port.

This distinguishes positive arithmetic readout from a scalar zero condition:
joint faithfulness does not supply selector authority or remove the vacuum.

## Missing interfaces

The operator statement still needs `ℓ²` over positive integer labels, the
isometric multiplication shift and its Hilbert adjoint, projection positivity,
prime-power valuation filtration, and the Gaussian sampling identity realizing
the shift. Most importantly, no established source theorem maps a scalar theta
zero to simultaneous exclusion annihilation; the vacuum packet proves that the
raw Mellin-transported source cannot provide such a map.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/PrimeDivisionCurvature.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
