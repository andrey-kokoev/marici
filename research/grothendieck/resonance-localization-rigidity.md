# Resonance failure is rigid under coefficient localization

## Rigidity theorem

Let `w:X->X` be a map of a finite set and let `R[X]` be its basis
linearization over a nonzero commutative ring `R`. If `w` is not bijective,
then the linearized map is not invertible over `R` or over any nonzero
localization of `R`.

Indeed, a nonbijective self-map of a finite set has two inputs with the same
image and at least one missing image. Its matrix has repeated columns and a
zero row. These defects persist under every nonzero base change.

Applied to a bad power--Mackey fiber word, this shows that resonance failure
is combinatorial. Unlike the scalar norm `|ker(phi)|`, it cannot be repaired
by coefficient localization.

## A4 hostile control

For `A4->C3` at index three, the order-three action `A` on `V4` satisfies

`I+A+A^2=0`.

The twisted norm sends all four kernel elements to zero. Its basis
linearization has rank one over fields of characteristics `2,3,5,7`, even
though the norm degree four is a unit at prime three.

## Scope

This rules out localization as an algebraic repair of resonance. It says
nothing about constructing the still-missing physical chain transfer.
