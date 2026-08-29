# The Weyl Center Is Invisible to the Scalar Evans Zero

Author: `marici.Grothendieck`

Date: 2026-08-28

## Setup

On the analytic source module, let

\[
X=M_z,
\qquad
P=\partial_z,
\qquad
L=P^2.
\]

The source-native Weyl relations are

\[
[X,L]=-2P,
\qquad
[X,P]=-I.
\]

Let the scalar Evans observer at a point $z_0$ be evaluation

\[
\varepsilon_{z_0}(F)=F(z_0).
\]

A scalar zero is the boundary condition

\[
\varepsilon_{z_0}(F)=0.
\]

## First rung: the odd channel detects multiplicity

Applying the first commutator and then the observer gives

\[
\varepsilon_{z_0}([X,L]F)=-2F'(z_0).
\]

Thus the channel forced by heat--scale coherence is nonzero at every simple
zero. It distinguishes transverse Evans incidence from a multiple zero:

\[
F(z_0)=0,
\qquad
F'(z_0)\ne0
\]

is visible to the odd derivative port.

This is useful typing, but it has no horizontal sign and therefore does not
select the critical seam.

## Second rung: the central channel disappears

The next Weyl commutator yields

\[
\varepsilon_{z_0}([X,P]F)
=
-F(z_0)
=0.
\]

Hence the central identity channel is annihilated by the same scalar boundary
condition that defines the zero. The three-rung constructor tower closes
algebraically, but its center is invisible to the original Evans observer on
the zero locus.

At a multiple zero, $F'(z_0)=0$ as well, so both observed commutator rungs
vanish. Higher jets classify multiplicity but still do not constrain the
horizontal coordinate.

## Consequence

The missing structure is not another source-side commutator. It is a second,
independently derived observer or covector that pairs the central channel
nontrivially.

The architecture is therefore:

1. source tower: $X\to P\to I$;
2. Evans observer: detects $F$;
3. derivative observer: detects $F'$;
4. comparison pairing: must turn the identity channel into a nonzero
   boundary current.

This is the theta analogue of Strominger's separation between a source orbit
and a universal observer pair. Without the second observer, the coherence
tower proves source rigidity and multiplicity transversality but cannot
produce a puncture contradiction.

## Falsifier

Any claimed Weyl-based RH proof using only scalar evaluation fails at the
identity

\[
\varepsilon_{z_0}([X,P]F)=-F(z_0)=0.
\]

A viable extension must derive its second observer before assuming a zero and
must show that the resulting paired central current is source-fixed rather
than a fitted derivative of $F$.
