# The maximal tensor-compatible arithmetic shadow retains `D4` abelianization

Author: `marici.Nima`  
Date: 2026-08-20  
Status: exact algebraic construction; physical comparison not established

## Universal quotient

The full quadrilateral source group `D4` cannot be the automorphism group of
a multiplicative unit because it is nonabelian. Every map from `D4` into the
automorphisms of a monoidal unit must factor through

\[
D_4^{\mathrm{ab}}
=D_4/[D_4,D_4]
\cong C_2\times C_2.
\]

This is not a fitted quotient. Abelianization is initial among maps from
`D4` to abelian groups, so it is the maximal source-automorphism shadow that
can survive the unit-interchange law.

## Rig groupoid

Let objects be finite sets of connected `U` components. A morphism is a
bijection of components together with a `D4_ab` label on each component.
Define

- addition by disjoint union;
- multiplication by cartesian product of component sets;
- the label on `(i,j)` as the product of the labels on `i` and `j`.

Commutativity of `D4_ab` is exactly what makes the interchange law hold.
The singleton with trivial label is the multiplicative unit, and the empty
set is additive zero. Decategorification recovers the conditional initial
semiring while retaining two independent source-parity characters.

Thus

\[
\boxed{
\text{full }D_4\text{ Carrier}
\longrightarrow
D_4^{\mathrm{ab}}\text{-labelled rig groupoid}
\longrightarrow
\pi_0\cong\mathbb N
}
\]

is the current canonical arithmetic tower.

## What is not proved

The quotient kills the order-two commutator subgroup. Its universal algebraic
status does not prove that scattering, cosmology, strings, or flavor are
insensitive to that subgroup. Promoting the rig groupoid to a shared
physical realization requires the comparison test

\[
\boxed{
\text{Does every declared sector coefficient and readout factor through }
D_4^{\mathrm{ab}}?
}
\]

If one sector detects the killed commutator, the rig groupoid is only an
arithmetic lens. If all sector comparisons factor, it becomes a serious
shared quotient and the finite-set/Burnside-Witt route reopens.

The exact checker reconstructs the commutator subgroup of `D4`, obtains the
four-element abelianization, and verifies 256 label-interchange identities.
