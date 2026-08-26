# Cyclic Adams–Mackey exponent spectrum: Lean packet

## Source boundary

This increment formalizes the cyclic-kernel core of Grothendieck's
`adams-mackey-kernel-exponent-gate.md`.

## Formal objects and coefficient types

A cyclic kernel of order `d` is `ZMod d`. The Adams index `n` acts by scalar
multiplication `x ↦ n*x`. No coefficient ring, Betti lift, or physical chain
map is imported into this bijectivity layer.

## Theorems and hostile

- `cyclicPowerMap_bijective_iff_coprime` proves the power map is bijective
  exactly when `Nat.Coprime n d`.
- `exponentTwo_cyclicPowerMap_bijective_iff_odd` identifies the surviving
  indices on an exponent-two cyclic branch with the odd integers.
- `evenAdams_collision_hostile` shows index two identifies the distinct labels
  zero and one in `ZMod 2` and is not bijective.

This proves the cyclic fiber criterion itself. Commutation with a coefficient
fiber sum or Betti fiber lift additionally needs those correspondence legs to
be typed and connected to fiber bijectivity.

## Missing interfaces

The general finite abelian theorem needs invariant-factor decomposition and
the relation between group exponent and simultaneous cyclic bijectivity. The
central-extension theorem needs finite-group fibers and the identity
`(gk)^n=g^n k^n`; noncentral monodromy additionally needs conjugation actions,
their image exponent, and twisted norm-word bijectivity. None supplies the
source-derived physical relative-chain pushforward.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/CyclicAdamsSpectrum.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
