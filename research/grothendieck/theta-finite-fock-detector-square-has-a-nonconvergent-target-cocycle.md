# Theta finite Fock detector square has a nonconvergent target cocycle

## Distinguished finite lines

For a finite prime set (S) and (s=sigma+it) with (sigma>1/2), let

\[
 \omega_{p,s}
 =\sqrt{1-p^{-2\sigma}}
 \sum_{k\ge0}p^{-ks}e_{p,k}
\]

be the normalized local Fock state, and put

\[
 \Omega_{S,s}=\bigotimes_{p\in S}\omega_{p,s}.
\]

Let (L_{S,s}) be its one-dimensional span. For (S\subset T), the
source-authorized inclusion is

\[
 i_{S,T}(v)=v\otimes
 \bigotimes_{p\in T\setminus S}\omega_{p,s}.
\]

## Detector cocycle

The local Euler detector has amplitude

\[
 a_p(s)
 ={\sqrt{1-p^{-2\sigma}}\over1-p^{-s}},
\]

which is nonzero at every finite prime. The finite detector satisfies

\[
 d_{S,s}(\Omega_{S,s})=A_S(s),
 \qquad
 A_S(s)=\prod_{p\in S}a_p(s).
\]

Define the target bonding map (j_{S,T}) to be multiplication by

\[
 u_{S,T}(s)=\prod_{p\in T\setminus S}a_p(s).
\]

Then the exact finite square is

\[
 d_{T,s}i_{S,T}=j_{S,T}d_{S,s},
\]

and the target multipliers obey

\[
 u_{S,U}=u_{T,U}u_{S,T}.
\]

Every finite detector on the distinguished line is injective because every
(a_p(s)) is nonzero.

## Why strict exactness does not yet pass to completion

The cocycle (u_{S,T}) does not define an ordinary convergent target
transport in the critical half-strip. Its logarithm contains the prime term

\[
 \log|a_p(s)|
 =\operatorname{Re}(p^{-s})+O(p^{-2\sigma}).
\]

Absolute convergence therefore begins only at (sigma>1). In
(1/2<\sigma\le1), the distinguished state completes, but its finite Euler
detector cocycle does not supply a canonical continuous target limit.

Thus the desired comparison

\[
 \ker d_s
 \stackrel{?}{=}
 \overline{\varinjlim_S\ker d_{S,s}}
\]

is not false at this stage; it is not yet typed because (d_s) has not been
obtained as the continuous limit of the finite target squares.

## Tautological trivialization

At finite support one can choose a target frame multiplied by
(A_S(s)^{-1}). In that frame every distinguished detector equals one. This
forces the squares to commute with identity target maps, but it divides by the
very scalar section whose zeros the completed theory must explain.

Such a trivialization cannot be used in the RH argument. It erases rather
than controls the possible completed divisor.

## Required relative square

The next admissible construction must replace the raw scalar target by a
boundary-bearing relative target (Y_{S,s}) with bonding maps that:

1. retain the primitive, square, seam, and archimedean currents;
2. converge in a source-defined topology for (1/2<\sigma\le1);
3. reproduce the finite Euler detector after scalar compression;
4. never divide by the completed scalar section; and
5. make the completed kernel comparison a meaningful strict-exactness
   statement.

The finite falsifier is a normalized distinguished-line sequence whose full
relative target tends to zero while its source state remains nonzero. A
vanishing scalar compression alone is not that falsifier.

## Scope

This packet constructs the exact finite bonding square and proves why its raw
scalar target does not complete where RH lives. It neither constructs the
relative target nor proves or disproves strict exactness after that target is
defined.
