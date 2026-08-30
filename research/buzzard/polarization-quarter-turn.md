# Polarization quarter-turn packet

## Grothendieck source

This formalizes the canonical algebraic part of
`research/grothendieck/paired-polarization-quarter-rotation.md`.

## Formal objects

- `PolarizationDouble X R` is the finite coefficient--Betti double.
- `polarizationQuarterTurn (c,b)=(-b,c)` is Grothendieck's canonical `J`
  after identifying the two finite free modules by their delta bases.
- `canonicalSymplecticForm` is the standard alternating coefficient--Betti
  pairing.
- `polarizationQuarterTurn_sq` proves `J^2=-1`.
- `polarizationQuarterTurn_preserves_symplectic` proves symplecticity.
- the two polarization predicates and exchange theorems show that `J`
  exchanges the coefficient and Betti Lagrangians.

## Assumptions and coefficient type

The theorem uses a finite label type and an arbitrary commutative ring. The
delta-basis identification is already incorporated by using the same
function type for both polarizations.

## Hostile and selection gate

`polarizationQuarterTurn_ne_identity` shows that `J` is genuinely different
from the identity, while the identity trivially preserves the same
symplectic form. Thus symplectic preservation and polarization data do not
select the real path `exp(theta J)`, its endpoint at `pi/4`, or a metaplectic
lift.

The eighth phase additionally requires real extension, `sqrt(2)`, a chosen
positive path, metaplectic/half-form representation data, and a source theorem
identifying that path with the physical boundary. Those inputs are missing.
No Xi determinant, spectral realization, zero confinement, or RH follows.

## Verification boundary

Static placeholder checks are permitted. Lean elaboration is withheld under
Nima's active no-build instruction.
