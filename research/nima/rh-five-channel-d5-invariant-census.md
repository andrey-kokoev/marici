# Five-Channel RH D5 Invariant Census

## Question

Does the five-channel RH packet admit the same smallest dihedral representation
completion that produced the Flavor (D_5) window, and what is the first mixed
invariant missed by its quadratic analysis?

## Frozen five-channel packet

Use the two reciprocal tail channels, two directed seam traces, and the
coherence line:

\[
(P,Q,M_+,M_-,L).
\]

Reciprocal reflection acts by

\[
(P,Q,M_+,M_-,L)
\mapsto
(Q,P,M_-,M_+,L).
\]

Its permutation cycle type is

\[
(12)(34)(5).
\]

This is exactly the restriction of the five-vertex permutation representation
of (D_5) to a reflection.

The provisional (D_5) decomposition is

\[
\mathbf5=\mathbf1\oplus V_1\oplus V_2.
\]

Here (V_1) and (V_2) are the two inequivalent faithful real doublets of
rotation weights one and two. This is a representation hypothesis only. No
source-derived order-five rotation has yet been constructed.

## Complex doublet coordinates

Write the two doublets as complex coordinates (z_1,z_2). A generating
rotation acts with weights one and two, while reflection acts by conjugation:

\[
z_1\mapsto\zeta z_1,
\qquad
z_2\mapsto\zeta^2z_2,
\qquad
\zeta^5=1,
\]

and

\[
z_1\mapsto\overline{z_1},
\qquad
z_2\mapsto\overline{z_2}.
\]

The singlet (L) is fixed.

## Exact invariant dimensions

The exact dimensions of the real invariant spaces from degrees zero through
six are

\[
1,1,3,5,10,16,26.
\]

At degree two, the complete basis is

\[
L^2,
\qquad
|z_1|^2,
\qquad
|z_2|^2.
\]

There is no mixed quadratic invariant between (V_1) and (V_2).

At mixed bidegree ((2,2)), the invariant space is one-dimensional:

\[
|z_1|^2|z_2|^2.
\]

This reproduces the exact quadratic complementarity that made the Flavor
(D_5) result surprising.

## The first omitted constructors

At degree three, two mixed invariants survive:

\[
C_{112}=\operatorname{Re}(z_1^2\overline{z_2}),
\qquad
C_{122}=\operatorname{Re}(z_1z_2^2).
\]

The second exists because its rotation weight is five. The first exists because
the weight of (z_1^2) matches the weight of (z_2).

Write

\[
z_1=a+ib,
\qquad
z_2=c+id.
\]

Then

\[
C_{112}=(a^2-b^2)c+2abd,
\]

and

\[
C_{122}=a(c^2-d^2)-2bcd.
\]

These are the exact analogues of the Flavor cubic that escaped the quartic
window.

## Scalar-zero hostile

If the first even channel vanishes, then (a=0). The cubics reduce to

\[
C_{112}=-b^2c,
\qquad
C_{122}=-2bcd.
\]

They need not vanish. The exact witness

\[
(a,b,c,d)=(0,1,1,1)
\]

gives

\[
(C_{112},C_{122})=(-1,-2).
\]

Therefore one scalar zero does not annihilate the complete (D_5)-allowed
mixed constructor grammar.

If both even channels vanish, then (a=c=0), and both mixed cubics vanish.
This supports the earlier conclusion that the scalar zero must be related to a
second seam-value condition before the hidden odd channels can be constrained.
It does not supply that relation.

## Categorical typing obstruction

The known reflection acts correctly on the five channels, but an order-five
rotation would mix two tail states, two directed seam states, and one
arrow-level coherence channel. Such a map is not an ordinary state-space
automorphism.

A genuine (D_5) completion must therefore act on a category of presentations
or factorization roles. It must not coerce the determinant line into a state
port merely to realize a five-cycle.

The source gate is a constructor (R) with

\[
R^5=1
\]

and

\[
\rho R\rho=R^{-1},
\]

whose domain and codomain typing is defined at every step.

## Disposition

The Flavor procedure transfers exactly and produces the same result shape:

- the five-channel reflection representation admits a canonical abstract
  (D_5) extension;
- the two doublets have complementary quadratic channels;
- mixed bidegree ((2,2)) is purely radial;
- two mixed cubic constructors survive;
- a single scalar zero does not kill those cubics;
- the order-five source operation remains unconstructed.

Thus (D_5) is a strong representation candidate but not yet an RH symmetry.
The next admissible step is to seek the source genesis of the order-five
rotation and, independently, identify whether either mixed cubic occurs in the
actual doubled theta/Tate boundary grammar.

The smallest falsifiers are:

1. no typed order-five constructor exists;
2. the source representation does not match the provisional five-channel
   decomposition;
3. an actual mixed cubic leaves a nonzero residual at a scalar zero;
4. the proposed rotation maps a state channel into arrow-level coherence
   without an authorized categorical lift.
