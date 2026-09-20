# Higher-coherence topology iteration 16: operator-system CP lifts make positivity coherent, but two-sided passivity is the confinement condition

## Candidate topology

Replace vector transport by its quadratic lift on an operator system. For a
source arrow `A`, define

\[
\mathcal E_A(X)=A^*XA.
\]

This map is completely positive, and composition is strict:

\[
\mathcal E_A\circ\mathcal E_B
=\mathcal E_{BA}.
\]

Thus repeated primitive transports automatically generate coherent positive
higher operations on every matrix level. This is a genuine topology/category
in which positivity and higher composition coexist.

## Prime transport

On the one-dimensional local valuation line, prime transport is

\[
A_{p,z}=p^{-z}I.
\]

Its CP lift is

\[
\mathcal E_{p,z}(X)
=p^{-2\operatorname{Re}z}X.
\]

This is completely positive for every `z`. Complete positivity alone therefore
places no restriction on the spectral real part.

## Passivity

A CP map is subunital precisely when

\[
\mathcal E_{p,z}(I)
=p^{-2\operatorname{Re}z}I\le I,
\]

which is equivalent to

\[
\operatorname{Re}z\ge0.
\]

The reciprocal branch has transport `p^z` and CP lift

\[
\mathcal E_{p,z}^{\rm recip}(X)
=p^{2\operatorname{Re}z}X.
\]

Its subunitality is equivalent to

\[
\operatorname{Re}z\le0.
\]

Consequently simultaneous passivity of both reciprocal CP channels gives

\[
\boxed{\operatorname{Re}z=0.}
\]

Equivalently, both maps are unital/lossless only on the critical seam.

## Interpretation of the Haar residual

The defect operator of the forward branch is

\[
I-\mathcal E_{p,z}(I)
=
(1-p^{-2\operatorname{Re}z})I.
\]

Pairing with the retained state gives exactly

\[
(1-p^{-2\operatorname{Re}z})E_p(b_z).
\]

Thus the relative-Haar residual is the failure of the forward CP channel to be
unital. The reciprocal residual is the opposite branch's failure.

## Does higher CP coherence prove passivity?

No. The Adams square lift proves that the maps are CP and compose coherently.
It does not prove they are subunital. A scalar amplification `X maps to cX` is
CP for every `c>1`.

A Stinespring dilation exists for a contraction only after subunitality is
known. Using its defect column to prove subunitality is circular. Moreover, a
valid Stinespring square does not automatically supply all edges of a proposed
higher simplex.

## Potential reformulation

The terminal theorem can be stated cleanly in operator-system language:

> At an Xi zero, the source-derived forward and reciprocal prime channels are
> simultaneously passive on the same nonzero retained state.

This is equivalent to confinement but may expose new tools: Schwarz
inequalities, complete order embeddings, or a source Markov property. Any such
tool must establish subunitality independently of the Xi-zero conclusion.

## Verdict for topology 16

Operator-system/CP topology successfully makes every quadratic higher
coherence positive and compositionally strict. It does not constrain the
prime modulus. The missing energy-cycle law becomes simultaneous passivity of
two reciprocal CP maps, which is exactly the critical-line condition.

The next nonredundant topology to test is a probabilistic/Markov or dilation
boundary topology, asking whether source normalization forces both reciprocal
channels to be trace-preserving rather than merely completely positive.