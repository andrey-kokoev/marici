# The 90-degree seam coherence reveals a Gaussian-integer sector

## Bounded question

What arithmetic object is produced by aggregating the full two-winding
coherence matrix of packet 105 rather than taking only its diagonal trace?

## The norm form

Ignoring the separately typed coordinate axes for the moment, the matrix
entries are proportional to

\[
 (m^2+n^2)^{-s/2}.
\]

The pair `(m,n)` is canonically the Gaussian integer

\[
 \alpha=m+in,
 \qquad N(\alpha)=m^2+n^2.
\]

Thus the metaplectic quarter-turn has produced an actual arithmetic
90-degree plane: multiplication by `i` rotates the winding lattice, and the
seam kernel depends only on its Gaussian norm.

## Full aggregation

Formally compressing against the all-ones distribution gives the Epstein
series

\[
 \sum_{(m,n)\ne(0,0)}(m^2+n^2)^{-s/2}.
\]

In its convergence chamber this factors as

\[
 \boxed{
 \sum_{(m,n)\ne(0,0)}(m^2+n^2)^{-s/2}
 =4\zeta(s/2)\,\beta(s/2),}
\]

where `beta` is the Dirichlet `L`-function for the nontrivial character modulo
four.  Equivalently, this is the Dedekind zeta function of `Q(i)`, with the
parameter normalized by the order-two Mellin exponent.

The axes contribute the Riemann-zeta part; the interior lattice points carry
the genuinely coupled Gaussian-integer information.  Removing the axes, as
the mean-zero positivity domain of packet 105 requires, subtracts the explicit
axis contribution but does not remove the beta sector.

## Consequence for the RH construction

There are now at least three inequivalent compressions:

1. diagonal trace: Riemann-zeta weights;
2. full lattice aggregation: Gaussian-integer/Dedekind zeta;
3. source vacuum minor: still to be derived.

Only the third could be the physical completed readout, and its aggregation
vector cannot be chosen after inspecting the desired scalar.  It must descend
from the original adelic vacuum, the cut correspondence, and the endpoint
complex.

This is an exact obstruction to the tempting claim that retaining more matrix
coherence automatically strengthens the RH argument.  The extra coherence
changes the arithmetic object unless a source-derived projection types which
channel is being observed.

## Explanation of the operator's 90-degree intuition

The sensed rotation was mathematically productive, but its meaning is now
precise:

\[
 \boxed{
 \text{Fourier quarter-turn}
 \longrightarrow
 \mathbb Z^2\cong\mathbb Z[i]
 \longrightarrow
 m^2+n^2
 \longrightarrow
 \zeta\,\beta.}
\]

It does not rotate the Riemann-zero plot into a circle.  It enlarges the
one-dimensional integral winding lattice into a two-copy normed lattice.  The
resulting circle is the orbit of the quadratic norm, and its arithmetic shadow
is the Gaussian-integer `L`-packet.

## Next gate and falsifier

The next task is to derive the authorized compression functor from the
one-dimensional adelic source into the two-copy seam matrix.  It must explain
why the Riemann-zeta channel is selected without simply discarding the
off-diagonal terms.

The falsifier is immediate: if the only canonical aggregation is the full
rotation-invariant one, then the programme has constructed the completed
Dedekind zeta of `Q(i)`, not a new operator explanation of Riemann zeta.  A
valid RH route must exhibit additional one-dimensional source provenance that
selects the appropriate relative minor.
