# Harmonic carrier control metric: WP1002

## Question

Can the WP1001 candidate actuator acquire a source-defined reset and positive
control cost without importing a norm directly on the desired ((q,k))
response?

## Carrier action

Give the two singlet backgrounds independent strictly convex source potentials

\[
V_{\rm ctrl}=
\frac{M_A^2}{2}\phi_A^2-j_A\phi_A
+\frac{M_s^2}{2}\phi_s^2-j_s\phi_s,
\qquad M_A^2,M_s^2>0.
\]

The labelled source currents (j_A,j_s) are the admitted inputs. Their unique
stationary carrier values are

\[
\epsilon_A=\phi_A=\frac{j_A}{M_A^2},
\qquad
\epsilon_s=\phi_s=\frac{j_s}{M_s^2}.
\]

Setting both currents to zero defines a unique reset attribute
((\phi_A,\phi_s)=(0,0)). This is an algebraic preparation/reset statement;
no physical relaxation time is assumed.

The positive carrier displacement cost relative to reset is

\[
C(\epsilon)=\frac12\epsilon^T G_\epsilon\epsilon,
\qquad
G_\epsilon=\operatorname{diag}(M_A^2,M_s^2).
\]

It is derived from the carrier action rather than chosen in coefficient
coordinates.

## Induced coefficient metric

Let (J_\epsilon) be WP1001's response from carrier displacements to
(z=(\log q,\log k)). When both port couplings are nonzero, the unique
small-signal carrier command for a coefficient displacement is
(epsilon=J_\epsilon^{-1}\delta z). Therefore

\[
C=\frac12\delta z^T G_z\delta z,
\qquad
G_z=J_\epsilon^{-T}G_\epsilon J_\epsilon^{-1}.
\]

At the unit reference packet
(a=c=\kappa_A=\kappa_s=M_A^2=M_s^2=1),

\[
J_\epsilon=\begin{pmatrix}-1&0\\-6&-1\end{pmatrix},
\qquad
G_z=\begin{pmatrix}37&-6\\-6&1\end{pmatrix},
\qquad
\det G_z=1.
\]

The off-diagonal term is forced by the fact that the adjoint-mass port changes
both (q) and (k). It would be lost by assigning an observer-side Euclidean
metric to the coefficient plane.

## Support corridor

The leading mediator masses remain positive only on

\[
a_0+\kappa_A\epsilon_A>0,
\qquad
c_0+\kappa_s\epsilon_s>0.
\]

Any finite robust-control claim must remain inside a preregistered subset of
this corridor and inside the controlled-elimination domain. The quadratic cost
does not authorize crossing a mass-zero boundary.

## Classification

The completed candidate supplies a source-derived positive pairing, reset
attribute, and local rank-two actuator metric. Its current-off minimum selects
the carrier reference, not a preferred numerical flavor point: the baseline
masses (a_0,c_0) remain free source parameters. Thus it is an actuator and
carrier rigidifier, not a flavor selector.

## Physical-instrument boundary

The source currents, carrier curvatures, and displacement readouts still lack
laboratory calibration. Finite widths, mixing, backreaction on the carrier
potentials, reset fidelity, uncertainty, detector response, and accessible
range are unmeasured. Hence (G_z) is source-defined within the candidate
model but not yet an experimentally calibrated physical metric.

## Smallest exact falsifier

At the unit packet, replacing (G_z) by the identity is falsified by the exact
pullback matrix above. Deleting either port makes (J_\epsilon) singular and
the two-dimensional induced metric undefined.

## Claim boundary

WP1002 proves the exact static carrier minimizer and quadratic pullback metric
for the candidate extension. It does not prove a dynamical reset rate,
experimental control, global stability of the coupled source, or selection of
(a_0,c_0).

## Disposition

Promote the candidate from an unpriced actuator schema to a source-priced
local control model. Withhold physical-instrument and numerical-selector
authority pending calibration and coupled-completion tests.

