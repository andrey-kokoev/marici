# Tate reflection coherence is invisible on the physical line

Date: 2026-08-23

The physical derived pullback of the six-point connector has

\[
H_1\cong\mathbb Z,\qquad H_i=0\quad(i\ne1),
\]

with primitive generator (z=(1,0,1,0,0)) and road augmentation (+1).
Its loaded reflection character is even because the road-orientation and
polarity signs multiply to (+1).

The source and literal reflection maps are connected by the unique loaded
conductor homotopy.  Chain-homotopic maps induce the same map on homology.
Therefore both reflections act on the physical line by

\[
\boxed{[z]\longmapsto[z].}
\]

The six mixed conductor cells do not add a second physical direction:

\[
\operatorname{rank}H_1^{\rm phys}=1
\quad\text{before and after the comparison}.
\]

Their role is coherence, not state multiplicity.  They make two
presentations induce the same physical operation while disappearing under
ordinary support-forgetting.  By rigid Cut induction, this equality is
transported through every even arity in the cellular fs/Kato sector.

This identifies the categorical physical readout but not a numerical
amplitude, period, or CHY integral.

Evidence:

- `research/nima/checkers/check_tate_reflection_on_physical_line.py`
- Entries 435--436, 542, and 544.
