# Higher-coherence topology iteration 23: real-oriented blow-up retains crossing direction, but reciprocity permits opposite-chamber pairs

## Candidate topology

Replace each resonant divisor by its sphere of real normal directions. In one
real normal coordinate `r`, the origin is replaced by two boundary faces

\[
0^-\quad\text{and}\quad0^+.
\]

A section approaching the divisor now retains its chamber and crossing
orientation. Phase jumps are encoded by clutching maps rather than erased by
continuity through zero.

This is the natural refinement of the Maslov topology from iteration 22.

## Fourier-minor chambers

For the Fourier Plücker coordinate

\[
\Delta_F=-2i e^{-im}\sin(\theta/2),
\]

the blow-up separates the signs of `sin(theta/2)` at every resonant hypersurface
`theta=2 pi k`. The alternating crossing sign is retained as boundary data.

An affine spectral-flow coordinate can make the total current continuous. If
the regular current jumps by `-2A` and the index coordinate jumps by `+A`, then

\[
\widehat\nu=\nu+2I
\]

is clutching-invariant. This is a genuine use of an added higher system to
absorb local discontinuity.

## Why chamber resolution does not give avoidance

The blow-up replaces an intersection by boundary data; it does not remove the
intersection. A path may reach the exceptional face, acquire its oriented
index, and leave through the opposite chamber. To prove noncollision one still
needs that the physical section remains in the interior of one chamber.

That is a transversality or barrier theorem, not a consequence of the blow-up
topology.

## Critical-seam blow-up

For the Haar multiplier, use normal coordinate

\[
a=\operatorname{Re}z.
\]

The oriented blow-up separates the chambers `a>0` and `a<0`, with the critical
line as the exceptional face. Reciprocity sends

\[
a\longmapsto-a
\]

and exchanges the two chambers.

An off-seam reciprocal zero pair occupies one point in each chamber and is
perfectly compatible with the blown-up symmetry. The topology records the pair
more faithfully but does not exclude it.

## Completion issue

A sequence can stay in one open chamber while approaching the exceptional
face. Conversely, finite sections can alternate chambers with no convergent
unblown representative but a well-defined stratified limit. To derive
confinement from chamber data one needs a uniform distance from every forbidden
exceptional face, or a source rule forcing all Xi points onto the exceptional
face itself.

The first is stronger than RH off the divisor; the second is RH.

## Higher-cone interpretation

Repeated cones can supply affine index coordinates that make every crossing
current globally well typed. They convert discontinuous representatives into a
continuous stratified object. Their success concerns bookkeeping of crossings,
not their absence.

A positive compression annihilating the affine holonomy would be additional
input and remains unproved.

## Verdict for topology 23

Real-oriented blow-up/chamber topology successfully retains approach direction,
Maslov signs, and affine clutching through repeated higher systems. It does not
prevent reciprocal off-seam chamber pairs or force the Haar normal coordinate
to vanish.

The next nonredundant topology to test is a barrier/viability topology—e.g. a
cone field or Nagumo invariant-region condition—asking whether the source flow
can be proved tangent to the critical exceptional face and unable to enter
either open chamber.