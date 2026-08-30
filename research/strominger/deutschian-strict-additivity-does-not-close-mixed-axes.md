# Strict additivity does not close mixed axes

## Deutschian conjecture

The strongest interpretation of the strict seven-slot result is:

> In a strictly additive source sector, once every directed residual is a
> genuine differential and ordinary composition is associative, no additional
> coherence constructor is required.

This conjecture predicts that independently valid differential directions
automatically assemble into a multi-directional complex.

## Minimal falsifier

Work over \(\mathbb F_7^2\) and take

\[
d_h=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad
d_v=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix}.
\]

Each direction is individually strict:

\[
d_h^2=0,
\qquad
d_v^2=0.
\]

Composition is ordinary associative matrix multiplication.  Nevertheless the
graded mixed curvature is

\[
K_{hv}=d_hd_v+d_vd_h=I.
\]

Thus the total odd differential fails:

\[
(d_h+d_v)^2=I.
\]

The obstruction is invariant under simultaneous change of basis because the
identity matrix remains the identity under conjugation.  It is not a chart
artifact.

## Falsification verdict

Strict additivity closes parenthesization along one direction.  It does not
force graded interchange between independent directions.  The broad
termination conjecture is false.

The missing constructors are the pairwise mixed curvatures

\[
K_{ij}=d_id_j-(-1)^{|d_i||d_j|}d_jd_i,
\]

with their required source values.  For two odd differentials this is the
anticommutator.

## Three-axis Boolean packet

For three independent directions, source closure has one obligation for every
nonempty subset of axes:

- three singleton obligations for the individual directions;
- three pair obligations for graded interchange;
- one triple obligation for cube coherence.

The count is

\[
\binom31+\binom32+\binom33=3+3+1=7.
\]

Equivalently, it is the number of nonempty vertices of the Boolean subset
lattice:

\[
2^3-1=7.
\]

This is a principled seven-slot architecture.  It is numerically equal to
`2(2+1)+1`, but its typing is different.  The slots are indexed by nonempty
axis subsets, not by two copies of a three-slot residual packet.

For \(r\) independent axes, the corresponding raw closure inventory is

\[
\sum_{j=1}^{r}\binom rj=2^r-1.
\]

Whether every listed obligation is independent depends on source identities.
Ordinary associativity can discharge some triple relations, while graded
Jacobi, Koszul, or Bianchi identities may discharge others.  The Boolean count
is the preregistered inventory, not a claim that every slot carries a nonzero
class.

## Revised Deutschian conjecture

> Strict additivity terminates sequential associator regress, but independent
> axes generate a Boolean family of mixed interchange obligations.  The source
> must construct or trivialize each obligation; no axiswise theorem implies
> the mixed cells.

This predicts the RH three-axis coherence cube directly from source,
composition, and reciprocity, without deriving its seven slots from the
arithmetic prime seven.
