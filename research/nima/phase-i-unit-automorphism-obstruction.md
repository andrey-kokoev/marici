# The initial semiring does not lift to the full Carrier groupoid

Author: `marici.Nima`  
Date: 2026-08-20  
Status: exact finite no-go; compatible with the conditional `pi_0` theorem

## The distinction

The endomorphism construction canonically equips

\[
\pi_0(\operatorname{Surf}^{\sqcup}_U)
\]

with the initial-semiring multiplication. It does not follow that the same
law is the decategorification of a second monoidal product on the full
surface groupoid.

Suppose such a bifunctor existed and used `U` as its multiplicative unit.
For automorphisms `g,h` of `U`, the arrows

\[
(g,1),\qquad(1,h)
\]

commute in
`Aut(U) x Aut(U)`. Functoriality and the left/right unit constraints would
send them to `g` and `h`. They would therefore have to commute. This is the
standard Eckmann–Hilton fact that endomorphisms of a monoidal unit form a
commutative monoid.

But the smallest source object used in the arithmetic audit is a cyclic
quadrilateral with source relabelling group

\[
\operatorname{Aut}(U)\supset D_4.
\]

Its rotation `r` and reflection `s` satisfy

\[
rs\ne sr.
\]

Hence

\[
\boxed{
\text{no monoidal lift with unit }U\text{ exists on the full }D_4
\text{-resolved Carrier groupoid}.}
\]

This does not refute the semiring on `pi_0`: passing to isomorphism classes
forgets precisely the noncommuting automorphism data. It shows that the
arithmetic object is currently a canonical decategorified shadow, not yet a
full Carrier-level tensor calculus.

## Consequence for Witt and Frobenius structures

Power, Burnside, and Witt operations are sensitive to automorphisms and
cycle structure. They cannot be claimed from the `pi_0` semiring alone.
There are now two typed routes:

1. construct a higher coherent power object that retains the dihedral
   automorphisms without making `U` a strict monoidal unit; or
2. quotient to the component-permutation groupoid and prove that this
   quotient is an authorized arithmetic realization rather than silent
   occurrence forgetting.

The second route is dangerous in light of existing Marici examples where
occurrence forgetting manufactures torsion. It requires an explicit
comparison theorem.

## Exact certificate

`check_phase_i_unit_automorphism_obstruction.py` reconstructs `D4` as exact
permutations, verifies its order, exhibits the noncommuting rotation and
reflection, and records the commuting-arrow interchange law that any
putative unit tensor would violate.
