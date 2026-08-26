# Theta full tail-seam shift is an exact source isometry

## Moving-cut source decomposition

Let \(f\in L^2(0,\infty)\). For \(q\ge0\), define the translated tail

\[
 g_q(t)=f(t+q),
 \qquad t\ge0,
\]

and the reflected seam history

\[
 h_q(t)=\mathbf 1_{[0,q]}(t)f(q-t).
\]

These are the complete source components on opposite sides of the moving
cut. The seam component retains the entire crossed history rather than a
finite collection of moments or antiderivatives.

## Exact norm identity

A change of variables gives

\[
 \|g_q\|_2^2
 =\int_q^\infty|f(v)|^2\,dv,
\]

and

\[
 \|h_q\|_2^2
 =\int_0^q|f(v)|^2\,dv.
\]

Therefore

\[
 \|g_q\|_2^2+\|h_q\|_2^2=\|f\|_2^2
\]

for every \(q\ge0\).

The map

\[
 U_qf=(g_q,h_q)
\]

is an isometry from the source space into the full tail--seam state space.

## Boundary flux

Whenever point evaluation is meaningful in the chosen rigging,

\[
 {d\over dq}\|g_q\|_2^2=-|f(q)|^2,
\]

while

\[
 {d\over dq}\|h_q\|_2^2=|f(q)|^2.
\]

The moving boundary transfers energy without loss:

\[
 {d\over dq}
 \left(\|g_q\|_2^2+\|h_q\|_2^2\right)=0.
\]

This is the infinite-dimensional conservation law whose finite
antiderivative shadows fail to close in packet 199.

## Quarter-turn extension

Tensor the source with the Clark quadrature port from packet 200. Because
the quarter-turn acts only on the two-dimensional sheet factor and \(U_q\)
acts only on the tail--seam factor, they commute:

\[
 (J\otimes I)(I\otimes U_q)
 =(I\otimes U_q)(J\otimes I).
\]

Thus the full source transport simultaneously retains:

- the two cofactor quadratures;
- the complete crossed seam history; and
- the exact source norm.

No finite-rank seam repair has these three properties.

## What spectral transport changes

The centered Mellin flow multiplies the two sheet directions by reciprocal
hyperbolic factors. It is unitary only when the centered real part vanishes.
The identity above therefore supplies the fixed source reference norm against
which that spectral distortion and all boundary currents must be measured.

It does not imply that the spectrally transported endpoint flux vanishes.
That remains the RH-bearing boundary theorem.

## Falsifier

The source-isometry claim fails if either moving-cut component is omitted,
if the seam reflection has a non-unit Jacobian, or if the two norm
derivatives do not cancel as distributions in the selected rigging.

## Scope

This proves exact source-level no-escape for the full tail--seam shift and its
compatibility with the Clark quarter-turn port. It does not include Mellin
hyperbolic weighting, arithmetic determinant aggregation, or endpoint
nonvanishing.
