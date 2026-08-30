# Theta route resolution localizes RH to antipodal phase exclusion

## Status

Exact two-route reduction and no-go theorem. Once the two conjugate source
routes are retained, a scalar transform zero is not disappearance of either
route. It is intersection of their packet with the kernel of the forgetful
aggregation map.

Positive route norms, equal amplitudes, conjugation symmetry, and route exchange
do not exclude that kernel. The missing RH-bearing law is an independently
source-derived exclusion of antipodal relative phase in each open half-plane.

## The route-packet sequence

Let the resolved comparison packet be

\[
r(s)=(r_+(s),r_-(s))\in\mathbb C^2.
\]

The scalar readout is the forgetful aggregation

\[
\Sigma(u,v)=u+v.
\]

There is an exact sequence

\[
0
\longrightarrow
\{(u,-u):u\in\mathbb C\}
\longrightarrow
\mathbb C^2
\overset{\Sigma}{\longrightarrow}
\mathbb C
\longrightarrow0.
\]

Therefore

\[
\Sigma(r(s_0))=0
\]

means that the nonzero route packet may lie on the anti-diagonal. It does not
mean either route has vanished.

This is the same structural phenomenon seen in the occurrence-resolved
endpoint packet with coefficients \((-1,+1)\): both routes exist, while the
coarse unweighted aggregation cancels.

## Reciprocal conjugacy is insufficient

On a reciprocal or real slice, suppose sewing gives

\[
r_-(s)=\overline{r_+(s)}.
\]

Writing

\[
r_+(s)=A(s)e^{i\theta(s)},
\]

gives

\[
\Sigma(r(s))=2A(s)\cos\theta(s).
\]

Equal amplitude and conjugacy are already built into this formula. Yet the
scalar still vanishes whenever

\[
\theta(s)=\frac\pi2\pmod\pi.
\]

Equivalently, the relative route phase satisfies

\[
\frac{r_+(s)}{r_-(s)}=-1.
\]

Thus modular swapping determines the packet involution but does not orient its
projection.

## Positive energy is phase-blind

The faithful packet energy

\[
\lVert r(s)\rVert^2
=|r_+(s)|^2+|r_-(s)|^2
\]

is strictly positive for every nonzero anti-diagonal packet. The same is true
of the Clark Bargmann number energy. Such energies establish route survival and
completion control, but cannot prevent destructive scalar interference.

This explains why adding a generic positive number operator does not answer
the quartic hostile source: the state remains present while its two complex
saddle contributions become antipodal.

## Minimal missing law

Assume neither resolved route vanishes in an open half-plane. Then define the
projective phase coordinate

\[
\rho(s)=\frac{r_+(s)}{r_-(s)}.
\]

The exact remaining condition is

\[
\rho(s)\neq-1
\]

throughout that half-plane.

This condition cannot be adopted as an axiom: after scalar projection it is
exactly zero-freeness. A valid advance must derive a stronger source operation
whose consequence is antipodal exclusion. Possible forms include:

- an invariant open semicircle for the relative phase;
- a monotone phase current with endpoint values that never reach \(\pi\);
- a positive-real transfer law for a source-defined Cayley transform of
  \(\rho\);
- a contraction of the resolved projective orbit that fixes the seam boundary
  but excludes the antipode in the interior.

Each proposal must be defined before the scalar sum and must fail on the
quartic hostile family.

## Source phase current

Where a resolved route is nonzero, its local phase velocity is

\[
\theta'(s)=\operatorname{Im}\frac{r_+'(s)}{r_+(s)}.
\]

This division is local to a nonvanishing resolved route, not division by the
completed scalar transform. It is therefore a legitimate diagnostic once the
route itself has been source-constructed.

The desired theorem would integrate a source-derived bound on this current
from an authorized endpoint or seam normalization. Merely computing the phase
from the final scalar divisor would be circular.

## Finite falsifier

For any proposed phase law, retain a finite pair of labelled route amplitudes
and compute

\[
\Delta=r_++r_-.
\]

A nonzero packet with \(\Delta=0\) kills the law immediately. For a transport
law, the sharper falsifier is a finite transport square whose projective action
sends an admitted packet to the antipode \(\rho=-1\) while preserving all
claimed norms and reciprocal typing.

The quartic conjugate-saddle packet is the mandatory analytic hostile: it has
positive local source data and beyond-all-orders route amplitudes, yet its
relative phase repeatedly reaches the antipode.

## Categorical interpretation

The resolved packet category carries more information than its scalar
quotient. The forgetful functor \(\Sigma\) is not conservative: it maps a
nonzero anti-diagonal object to zero.

Consequently the remaining RH problem is not to prove that the resolved object
is positive or nonzero. It is to derive, from theta/Tate source constructors, a
subobject of admissible route packets that is disjoint from the anti-diagonal
away from the seam.
