# Uniform equalizer control does not yet control scalar pairing zeros

## The typing gap

The combined law

\[
x\longmapsto(D_+(z)x,D_-(z)x,Jx)
\]

has a cutoff-independent inverse margin away from the seam in the labelled
model.  It excludes nonzero states that satisfy both sector equations in one
common frame.

A zero of the completed scalar need not have that type.  It may instead be a
vanishing pairing between two distinct nonzero sector states:

\[
\sigma(z)=\langle u_-(z),u_+(z)\rangle=0.
\]

This does not imply \(u_+(z)=u_-(z)\), and it does not produce a nonzero vector
in the common-frame equalizer.

## Exact finite hostile

Let

\[
u_+=\binom10,
\qquad
u_-=\binom01.
\]

Both vectors are nonzero, their scalar pairing vanishes, and their equality
equalizer contains only zero.  The quarter-turn comparison

\[
R=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]

satisfies \(u_-=Ru_+\).  Therefore an invertible, norm-preserving,
orientation-bearing sector comparison can coexist with a scalar zero and no
common state.

The hostile preserves exactly the distinction that earlier holonomy arguments
missed: canonical transport of a line or vector does not imply nonzero overlap
with the original line or vector.

## Consequence for the conditional theorem

The uniform equalizer estimate is mathematically valid but does not yet imply
RH.  A separate source-derived bridge must prove that every zero of the theta
section yields one of the following:

1. a nonzero state in the native common-frame equalizer;
2. a nonzero cohomology class in a complex controlled by the same estimate;
3. a unit boundary-loop eigenstate whose graph is identified with that
   equalizer by an authorized comparison cell.

Without such a bridge, the estimate controls the wrong kernel.

## DPC verdict

The current route has established a candidate off-seam acyclicity law for
common labelled states.  It has not established the zero-to-state constructor.
The next theorem cannot be another estimate.  It must be a typed incidence from
the divisor or scalar-zero fiber into the controlled state object.

The required diagram is

\[
\ker\sigma(z)
\longrightarrow
\operatorname{Eq}(D_+(z),D_-(z))
\]

or a correctly derived cohomological replacement.  The arrow must be built
from theta/Tate source operations before zero locations are inspected.

The finite falsifier for any proposed bridge is a pair of nonzero transported
sector states with zero scalar pairing but trivial equalizer.  The two-vector
quarter-turn model is the smallest such witness.

## Relation to hostile symmetric multipliers

This typing gap explains why hostile symmetric multipliers are not yet rejected
by the equalizer theorem.  They can change the scalar divisor while leaving an
independently defined common-state law untouched.  A valid zero-to-state bridge
must fail for those hostile sources for a source-local reason, or the route
remains circular.

## Verification

`check_rh_pairing_zero_not_equalizer.py` verifies the quarter-turn hostile,
zero pairing, invertible norm-preserving transport, and trivial equality
equalizer exactly over the rationals.

