# The first sectorwise readout-algebra composition square closes

## Physical finite model

Entry 1056 quotients the radiative-memory carrier by modes annihilated by the
sphere operator.  On three direction-labelled displacement-memory samples,
the finite constant mode is the diagonal line

\[
(x,y,z)\sim(x+c,y+c,z+c).
\]

The source-derived finite quotient constructor is centering:

\[
F(x,y,z)=(X,Y,Z)
=(x-\bar x,y-\bar x,z-\bar x),
\qquad X+Y+Z=0.
\]

Write

\[
(X,Y,Z)=(a,-a+b,-b).
\]

The second constructor is the \(D_3\)-invariant scalarization

\[
E(a,b)=(q_2,q_3)
=(a^2-ab+b^2,ab(a-b)).
\]

## Composition

Direct pullback to the original samples gives

\[
F^*q_2
=\frac12\sum_{i=1}^3(x_i-\bar x)^2,
\qquad
F^*q_3
=\prod_{i=1}^3(x_i-\bar x).
\]

The exact identity is

\[
\boxed{
(E\circ F)^*=F^*\circ E^*.
}
\]

Both functions are invariant under all six permutations of the directions
and under addition of the discarded constant mode.

## Result

This is the first closed composition square in one readout-algebra fiber:

\[
\text{directional memory samples}
\xrightarrow{\text{constant-mode quotient}}
\text{standard }D_3\text{ plane}
\xrightarrow{\text{invariant scalarization}}
\operatorname{Spec}\mathbb Q[q_2,q_3].
\]

It uses a genuine quotient resource and a genuine symmetry-invariant readout;
no cross-sector algebra map is asserted.

## Verification and boundary

The checker verifies 2,197 rational composition identities, 13,182
permutation controls, and 10,985 constant-mode translation controls.

This finite three-direction model represents only the constant sample line of
Entry 1056's full \(l\le1\) kernel.  It does not claim that three point
samples realize the complete sphere harmonic quotient or the full BMS
readout algebra.

Evidence: Ledger Entry 1056 and
`research/nima/check_radiative_memory_readout_composition.py`.
