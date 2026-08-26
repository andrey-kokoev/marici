# The metaplectic lift counts Fourier aliases but does not confine zeros

## Status

Exact two-label no-go theorem. The lifted Fourier minor carries a coherent
crossing grade, but the grade is universal bookkeeping: for every pair of
distinct arithmetic labels, motion in spectral height crosses infinitely many
aliasing walls. The lift remembers the orientation changes; it does not forbid
them and therefore supplies no RH-selective law by itself.

## Arithmetic specialization

Take two labels

\[
1\leq n<m
\]

with logarithmic positions

\[
q_1=\log n,
\qquad
q_2=\log m.
\]

For two spectral frequencies \(\xi_1<\xi_2\), the centered oriented Fourier
minor is

\[
\widetilde\Delta
=
2\sin\left(
\frac{(\xi_2-\xi_1)\log(m/n)}{2}
\right).
\]

It vanishes exactly when

\[
(\xi_2-\xi_1)\log(m/n)=2\pi k,
\qquad
k\in\mathbb Z.
\]

Hence the positive-frequency aliasing walls are

\[
\xi_2-\xi_1
=
\frac{2\pi k}{\log(m/n)},
\qquad
k=1,2,3,\ldots.
\]

Every distinct label pair therefore produces an infinite arithmetic aliasing
lattice along spectral height.

## Canonical crossing grade

Away from the walls, set

\[
u
=
\frac{(\xi_2-\xi_1)\log(m/n)}{2\pi}
\]

and define

\[
k(u)=\lfloor u\rfloor.
\]

Then

\[
\operatorname{sgn}\widetilde\Delta
=
(-1)^{k(u)}
\]

for nonintegral \(u>0\). The lifted datum

\[
\left(
|\widetilde\Delta|,
k(u)
\right)
\]

recovers the oriented minor exactly. Crossing one wall increments the grade by
one and reverses the sign.

This is a valid metaplectic bookkeeping law. It is also universal: it follows
from the Fourier kernel before any prime weights, endpoint current, gamma
factor, or theta completion enters.

## Why coherence is not confinement

On any path avoiding the aliasing walls, the phase has a continuous lift. On a
path crossing walls transversely, the integer grade records the crossings. If
two homotopic paths meet the same walls with the same signed intersection
number, their lifted endpoints agree.

Thus path coherence can be exact while the oriented minor changes sign
infinitely often. Coherence answers which sheet the minor occupies after a
crossing. It does not prevent the crossing.

A coherent phase lift does not imply zero exclusion. This is false already for
one labelled Fourier rectangle.

## Spectral-density consequence

The wall spacing for the label pair \((n,m)\) is

\[
\delta\xi_{n,m}
=
\frac{2\pi}{\log(m/n)}.
\]

For adjacent labels,

\[
\log\left(1+\frac1n\right)\sim\frac1n,
\]

so the walls are sparse:

\[
\delta\xi_{n,n+1}\sim2\pi n.
\]

For widely separated labels the walls become dense:

\[
\delta\xi_{n,m}\to0
\]

as \(m/n\to\infty\). Completion therefore superposes aliasing lattices at
arbitrarily fine spectral scales.

Any completed orientation law must control this accumulating family, not only
choose a branch for each finite minor.

## Relation to the Tate currents

The primitive and prime-square currents could still be required to
renormalize an accumulated lifted phase. But such a renormalization would only
produce a finite relative grade unless a further source law connects that
grade to the ordered endpoint/source transmission divisor.

The trace-class tail can make a relative determinant converge. Convergence of
the lifted phase does not imply that the flagged cross-transfer is nonzero.

Therefore the proposed interpretation has two separately typed tasks:

1. phase accounting: construct a cutoff-compatible relative Maslov grade;
2. divisor confinement: prove that a flagged transmission zero would violate
   an independent source law.

The first cannot stand in for the second.

## Finite falsifier

Fix any \(n<m\) and choose

\[
\xi_2-\xi_1
=
\frac{2\pi}{\log(m/n)}.
\]

Then the center phase is well defined, the reciprocal Gram square is
nonnegative, and the metaplectic crossing grade is well defined on either side,
but

\[
\widetilde\Delta=0.
\]

This single two-label source-local matrix disproves every claim that phase
lifting or lift coherence alone makes the Fourier comparison strictly
oriented.

## Decisive conclusion

The metaplectic lift is real structure, but it is an odometer, not a barrier.
It counts Fourier aliasing crossings that are unavoidable for every distinct
arithmetic label pair. Any RH-bearing advance must derive an additional law
showing why the completed flagged transmission divisor cannot vanish despite
those local crossings. Without that bridge, the phase-lift lane adds provenance
and anomaly accounting but no zero confinement.
