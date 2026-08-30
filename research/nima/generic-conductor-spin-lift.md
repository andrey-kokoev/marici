# Generic Conductor Spin Lift

The common conductor of the two alternating scaffold strata imposes

\[
(p_i+p_{i+1})^2
=\langle i,i+1\rangle[i,i+1]=0
\qquad(i\bmod 6).
\]

Label each adjacent edge by whether its angle or square bracket vanishes.  If
two consecutive edges have the same label, three successive momenta share one
spinor and a next-nearest invariant vanishes.  Excluding those deeper strata,
the labels must alternate around the cycle.  There are exactly two words:

\[
(\angle,\square,\angle,\square,\angle,\square),
\qquad
(\square,\angle,\square,\angle,\square,\angle).
\]

The checker gives an explicit momentum-conserving six-momentum point with all
adjacent invariants zero and every next-nearest invariant nonzero, proving that
this generic stratum is nonempty.

On these two components,

\[
\boxed{\text{one-step scaffold rotation}=\text{physical parity}}
\]

as permutations of the normalized lift: both exchange the two alternating
words.  This does **not** restore the rejected global identification of the two
operations.  They remain independent on the full source.  Their actions agree
only after restriction to the generic common conductor.

Consequently the mixed line

\[
Q_{\rm scaffold}\otimes Q_{\rm spin}
\]

is invariant under the source-defined diagonal action on this stratum.  This
is the first legitimate place where the product character can descend.  The
remaining section-level test is whether the helicity-evaluated conductor has a
nonzero component in this diagonal-invariant line and whether its soft image
is the BMS orientation line.

Certificate:
`research/nima/checkers/check_generic_conductor_spin_lift.py`
