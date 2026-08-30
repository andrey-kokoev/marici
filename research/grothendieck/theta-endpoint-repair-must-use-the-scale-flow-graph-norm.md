# Theta endpoint repair must use the scale-flow graph norm

## Scope correction to packet 162

Packet 162 proposed that the Clark square `|partial_z G|^2` might become a
logarithmic-derivative weight for the coefficient-synthesis multiplier.  The
abstract weighted trace criterion stated there is correct, but its application
to the theta tail was not derived and conflates two Fourier variables.

The actual tail feature is

\[
 G(q,z)=e^{-q/2}\int_0^\infty
 \phi(q+r)e^{izr}\,dr.
\]

Therefore

\[
 \boxed{
 \partial_zG(q,z)
 =i e^{-q/2}\int_0^\infty
 r\phi(q+r)e^{izr}\,dr.}
\]

It inserts the relative tail coordinate `r=v-q`.  It does not, without an
additional intertwining theorem, act as multiplication by
`Phihat'/Phihat` on the coefficient packet used in the full-synthesis Gram
calculation.  No endpoint repair follows from packet 162 as written.

## Source-native endpoint topology

The endpoint belongs to the `q`-scale differential system, so its native
topology is the graph topology of that system.  For any tail state
`G` in `H1(0,infinity)` with `G(infinity)=0`,

\[
 |G(0)|^2
 =-\int_0^\infty\partial_q|G(q)|^2\,dq
 \le2\lVert G\rVert_2\lVert\partial_qG\rVert_2
 \le\lVert G\rVert_2^2+\lVert\partial_qG\rVert_2^2.
\]

Hence

\[
 \boxed{G\mapsto G(0)\text{ is continuous in the scale-flow graph norm}.}
\]

This is not an appended scalar norm: it is the canonical trace theorem for
the already source-derived operator

\[
 (\partial_q+s)G+f=0.
\]

## Exact relation to the native Clark bulk

The flow gives

\[
 f=-\partial_qG-sG,
 \qquad
 G+f=-\partial_qG+(1-s)G.
\]

Thus the positive square already present in the two-sheet bulk,

\[
 |G+f|^2,
\]

is the graph energy of the first-order operator

\[
 -\partial_q+(1-s).
\]

The endpoint question is therefore reduced to a genuine first-order estimate:
does the complete doubled energy control the `H1` graph norm on each open
sector, after all seam and boundary channels are included?

## Remaining coercive gate, now typed

One must prove on the admissible two-ended domain, locally uniformly in each
open sector,

\[
 \lVert G\rVert_{H^1}^2
 \le C_K\left(
 \lVert-\partial_qG+(1-s)G\rVert_2^2
 +\text{declared seam/boundary energy}
 \right).
\]

This estimate may fail at the seam or through a boundary null mode.  Its
smallest falsifier is a normalized sequence whose native doubled energy tends
to zero while `|G(0)|` stays nonzero.

## Disposition

Packet 162 remains only an abstract conditional weighted-`L2` lemma.  It is
not evidence that the Clark `z`-derivative repairs the theta endpoint.  The
source-native candidate repair is the `q`-flow graph norm and its boundary
trace theorem.
