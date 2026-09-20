# Higher-coherence topology iteration 24: scalar Nagumo barriers are vacuous, but projective Schubert viability is a genuine candidate

## Candidate topology

Treat spectral/cutoff evolution as a flow on a state-observer Grassmannian.
The safe region is the Evans Schubert big cell where the distinguished
observation is nonzero. A cone field or Nagumo condition could make this region
forward invariant under every source attachment.

## Failure of the scalar barrier

Let the scalar observation be `y=u^*x` and use the nonnegative barrier

\[
b(x)=|y|^2.
\]

Along any differentiable trajectory,

\[
\dot b=2\operatorname{Re}(\overline y\dot y).
\]

At `y=0`, this derivative vanishes for every `dot y`. Thus the ordinary
first-order Nagumo test is vacuous: a trajectory may cross the zero-output
locus while `b` has quadratic contact.

A neighborhood estimate

\[
|\dot y|\le C|y|
\]

would prevent crossing, but it is a bound on `dot y/y`; deriving it after
scalar projection assumes the desired zero exclusion unless state-level kernel
invariance supplies `C` independently.

## Projective graph flow

Split the source state by the fixed observer into visible and hidden sectors.
For generator

\[
A=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix},
\]

the graph coordinate satisfies a Riccati-type equation. A source-defined
projective domain can avoid the Schubert divisor if its boundary cone field is
inward-pointing and the hidden-to-visible shear `beta` is controlled.

The two-state matrix

\[
A=\begin{pmatrix}0&1\\0&0\end{pmatrix}
\]

shows why ambient positivity is insufficient: a hidden state immediately
enters the visible coordinate.

## Higher-cone role

Repeated cones may enlarge the graph state so that endpoint, seam, primitive,
square, and archimedean residuals become additional Riccati coordinates. If
the combined generator preserves one source-selected projective cone, all
higher residuals are absorbed without allowing the Evans line to reach the
Schubert divisor.

This is a genuine possible mechanism, not merely a quotient topology.

## Available finite barrier clue

Prior source work derives a first-contact necessary condition. At zero
character, normalized curvature

\[
y=\frac{2\sqrt{\pi t}\,A_2}{M_2}
\]

must satisfy

\[
-1\le y\le0.
\]

Contacts with `A_2>0` or
`A_2<-M_2/(2 sqrt(pi t))` are excluded. Only the interval

\[
-\frac{M_2}{2\sqrt{\pi t}}\le A_2\le0
\]

survives the quadratic barrier test. This is concrete but not a complete
invariant-region theorem.

## Acceptance test

A viable projective topology must:

1. derive `alpha,beta,gamma,delta` before examining zeros;
2. define one invariant domain containing the source-normalized state;
3. prove its closure avoids the Schubert divisor in each open half-plane;
4. retain a cutoff-uniform distance or a strict cone condition;
5. survive every higher-cone attachment and restricted-product completion;
6. reject signed-prime and polynomial-shear hostile flows.

## Verdict for topology 24

Scalar barrier topology fails because its first derivative vanishes on the zero
locus. Projective Schubert-cell viability remains a serious noncircular
candidate: it could make the entire higher-coherence tower preserve an open
safe chamber. The required block generator and invariant cone are not yet
constructed.

The next nonredundant topology to test is a graph-transform/dominated-splitting
or cone-hyperbolic topology, which may provide a quantitative invariant region
and cutoff-uniform distance from the Schubert divisor.