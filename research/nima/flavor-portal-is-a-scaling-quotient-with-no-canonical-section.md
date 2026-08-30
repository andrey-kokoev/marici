# Flavor Portal Is a Scaling Quotient With No Canonical Section

## Result

The physical16 portal does not merely omit some convenient detector metadata.
It identifies a nontrivial family of distinct upstream states.

Let the upstream packet be

\[
x=(g_\phi,g_\psi,\kappa,M)
\]

with partial-width channels

\[
\Gamma_\phi=g_\phi^2,
\qquad
\Gamma_\psi=g_\psi^2,
\]

coherent arc

\[
I=g_\phi g_\psi,
\]

and portal scalar

\[
J_{16}=-\frac{\kappa I}{M^2}.
\]

For positive nonzero scalings \(a,b\), define

\[
T_{a,b}(g_\phi,g_\psi,\kappa,M)
=
\left(
ag_\phi,
bg_\psi,
\frac{\kappa}{ab},
M
\right).
\]

Then

\[
J_{16}(T_{a,b}x)=J_{16}(x),
\]

while the width packet and coherent arc generally change. Thus each portal
value is a quotient fiber carrying a nontrivial positive-scaling action.

## Two independent losses

The first exact witness preserves both the portal and coherent arc while
changing the widths:

\[
(1,1,1,1)
\longmapsto
\left(2,\frac12,1,1\right).
\]

Both states have \(J_{16}=-1\) and \(I=1\), but their width packets are
\((1,1)\) and \((4,1/4)\).

The second witness preserves the portal while changing the coherent arc:

\[
(1,1,1,1)
\longmapsto
\left(2,1,\frac12,1\right).
\]

Both portal values are \(-1\), while the arcs are \(1\) and \(2\).

These are different defects. Even a perfect portal scalar reconstructs neither
the norm channels nor the coherent comparison channel.

## Categorical obstruction

Write the portal projection as

\[
\pi:X\longrightarrow Y.
\]

The scaling transformations act inside the fibers of \(\pi\). A canonical
reverse constructor would be a section

\[
s:Y\longrightarrow X,
\qquad
\pi s=1_Y.
\]

If that section were natural under the fiber symmetry, its selected point
would have to be fixed by every transformation that acts trivially on \(Y\).
The nontrivial transformations \(T_{a,b}\) have no such fixed point on the
nonzero coupling domain. Therefore the quotient has no symmetry-equivariant
canonical section.

Choosing a representative by normalization, phase convention, fitted
visibility, or assumed background is additional structure. It is not inverse
transport from physical16.

## Required repair

The legitimate construction has the opposite direction:

1. derive a mediator grammar on an upstream source object;
2. construct \(g_\phi\), \(g_\psi\), \(\kappa\), the shared final state,
   detector visibility, phase convention, and background in one frame;
3. restrict to the source-reachable subobject cut out by those relations;
4. project that subobject to physical16.

The mediator grammar may select a transversal to the scaling fibers because
it contributes new source relations. The portal scalar alone cannot.

## Cross-sector transfer

Aspect's correlated-outage hostile adds a temporal qualification. Equal
marginal visibility does not determine multi-record reliability. Consequently,
the mediator grammar must generate the phase-monitor process or temporal
correlation law, not merely a static visibility number.

Benincasa's composite-probe kernel is the same obstruction in another carrier:
an output family can be faithful only after the actual source supplies the
missing comparison probe. Algebraic availability of that probe is
insufficient.

## Finite falsifier

Any proposed constructor-independent reverse map from \(J_{16}\) is falsified
by either pair above. If it returns one upstream packet, the other packet has
the same input scalar and a different required output.

The exact checker also evaluates a nine-state positive-scaling orbit. The
portal is constant across it while all nine width packets and six coherent
arcs occur.

## Status

This closes constructor-independent reverse descent from physical16. It does
not close the Flavor programme. The live task is now narrower: derive one
microscopic mediator grammar whose reachable subobject fixes the comparison
frame before scalar projection.
