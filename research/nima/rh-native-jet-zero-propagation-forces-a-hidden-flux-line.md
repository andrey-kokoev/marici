# Native Jet Zero Propagation Forces a Hidden Flux Line

## Exact native transport

For a multiplicative source block \(g\), the value–flux jet transport is

\[
S_g=
\begin{pmatrix}
g&0\\
g'&g
\end{pmatrix}.
\]

Let the present scalar readout be the value projection

\[
r(M,J)=M.
\]

Then

\[
r(S_g(M,J))=gM.
\]

If \(g\neq0\), value zeros propagate exactly through every such jet.

## The simultaneous obstruction

The kernel of the value readout is the pure flux line:

\[
K=\{(0,J)\}.
\]

Native transport preserves this line:

\[
S_g(0,J)=(0,gJ).
\]

Therefore every future value probe vanishes on every state in \(K\). A nonzero
flux state is behaviorally invisible to the entire multiplicative jet monoid.
The future value probes are not jointly faithful.

This is not an accident of one multiplier. Lower-triangular first-jet transport
makes the value quotient equivariant precisely by preserving the hidden flux
subobject.

## Uniqueness of the propagating scalar covector

For a general scalar covector \(r_{a,b}(M,J)=aM+bJ\), zero propagation requires
its kernel to be invariant. Acting on the covector gives

\[
r_{a,b}S_g=(ag+bg',bg).
\]

When \(g'\neq0\), proportionality to \((a,b)\) forces \(b=0\). Thus, among
ordinary scalar covectors, the value projection is the unique zero-propagating
readout up to scale. Every readout containing flux can expose the hidden line,
but loses zero propagation.

## No-go theorem

For the native multiplicative first-jet category alone, one scalar readout
cannot simultaneously satisfy:

- propagation of every present zero;
- joint faithfulness of all future probes.

The first property selects the value quotient. That quotient permanently hides
the invariant flux subobject and therefore violates the second property.

## Consequence for RH

The previous two-gate route closes in its one-readout form. A scalar zero of the
value channel can consistently represent a nonzero pure-flux state through the
entire jet orbit. No contradiction follows.

There are three possible repairs:

1. require both value and flux to vanish at a completed zero;
2. find a source generator with genuine flux-to-value mixing;
3. derive a boundary relation that forbids nonzero pure-flux states under the
   relevant endpoint conditions.

The first repair is the four-observer hypothesis in operational form, but it
needs a source bridge from the completed scalar zero to flux zero. The second
repair deliberately breaks value-zero propagation and must replace it with a
relation-valued propagation law. The third is a boundary-condition theorem and
is closest to the doubled Green conservation route.

The immediate finite test is therefore not more iteration of Euler jets. It is
whether reciprocal sewing, the archimedean endpoint, or the full boundary
condition eliminates the invariant pure-flux line.
