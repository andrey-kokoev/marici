# Phase-I Carrier obstructions: Lean packet

## Source boundary

This increment formalizes the exact algebraic cores of Grothendieck's
`phase-i-connected-sewing-unit-obstruction.md`,
`phase-i-face-coproduct-idempotence.md`, and the algebraic consequence in
`phase-i-monoidal-additive-completion.md`. It preserves the distinction
between a coefficient-line generator and a Carrier-object unit.

## Formal objects and coefficient types

Connected sewing arities are natural numbers with law `n + m - 2`; all
subtraction theorems state the lower bounds needed for natural subtraction.
The stable family means even arity at least four. The coproduct obstruction is
stated over an arbitrary additive commutative monoid and an arbitrary
additive commutative group.

## Theorems and hostiles

- `connectedSew_profiles` checks the published arity profiles.
- `boundaryExcess_additive` proves additivity of `arity - 2`.
- `connectedSew_unit_arity_eq_two` proves that any Carrier unit must have
  arity two.
- `fourPoint_coefficientUnit_is_not_carrierUnit` proves the persistent
  four-point residual `2`.
- `no_connectedSew_unit_in_stableEvenFamily` proves that the admitted stable
  even family has no connected-sewing unit.
- `additiveHom_eq_zero_of_idempotent` proves that every additive map from a
  globally idempotent coproduct monoid to a group is zero.
- `idempotent_element_maps_to_zero` gives the pointwise cancellation law.
- `natGeneratedMap` and
  `additiveMap_from_nat_determined_by_generator` give the universal additive
  map out of finite generator multiplicities.
- `intGeneratedMap` and
  `additiveMap_from_int_determined_by_generator` give the corresponding free
  signed additive map after group completion.

## Missing interfaces

The octagon support excess `130` still depends on the enumerated face model
and its exact join computation. A source-authorized finite disjoint-coproduct
completion needs actual objects, injections, morphisms, and the universal
mapping property. Adjoining a two-point interface Carrier likewise requires
source authorization and coherence. Neither repair follows from the
coefficient-line unit. The `ℕ` and `ℤ` theorems are conditional algebraic
consequences only: they do not prove that the Carrier supplies the required
multiplicity-sensitive geometric operation.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/PhaseICarrierObstructions.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
