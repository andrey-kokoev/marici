# Finite Weil negativity is interpolation-exact; completion is a condition-number problem

Event 10288 isolated the negative disagreement values

\[
\widehat f(\rho)=1,
\qquad
\widehat f(\rho^\vee)=-1.
\]

For every finite divisor packet, these values can be realized exactly.

Let

\[
Z_X=\{z_1,\ldots,z_N\}
\]

be a finite set of distinct divisor evaluation points containing
\(\rho,\rho^\vee\). Finite Lagrange interpolation gives a polynomial \(P_X\)
such that

\[
P_X(\rho)=1,
\qquad
P_X(\rho^\vee)=-1,
\qquad
P_X(z)=0
\quad
(z\in Z_X\setminus\{\rho,\rho^\vee\}).
\]

To place the interpolant in a vertically decaying Mellin class, choose a
center \(s_0\) and \(R>0\), and write

\[
\Phi_X(s)
=
P_X(s)e^{(s-s_0)^2/R^2}.
\]

After absorbing the two nonzero exponential values into the interpolation
data, one obtains

\[
\Phi_X(\rho)=1,
\qquad
\Phi_X(\rho^\vee)=-1,
\qquad
\Phi_X(z)=0
\]

at every other point of \(Z_X\), while \(\Phi_X\) decays Gaussianly on
vertical lines.

Thus the finite Weil packet contains the exact negative value

\[
Q_{Z_X}(\Phi_X,\Phi_X)=-2m_\rho
\]

up to the frozen multiplicity convention. Finite positivity already excludes
every off-seam pair that lies in the tested packet.

## Completion obstruction

The finite theorem does not provide one admissible completed test. The
interpolation norm may diverge with:

- the number of constrained zeros;
- small separation between evaluation points;
- height of the target pair;
- the required vertical-decay rung;
- endpoint and archimedean side constraints.

Define the minimal interpolation cost

\[
\mathfrak C_X(\rho)
=
\inf
\left\{
\|\Phi\|_{\mathcal E}:
\Phi(\rho)=1,\ 
\Phi(\rho^\vee)=-1,\ 
\Phi|_{Z_X\setminus\{\rho,\rho^\vee\}}=0
\right\}.
\]

Completion-stable localization requires a controlled family of costs in the
declared test topology. A uniform bound is sufficient but may be stronger
than necessary; density plus tail control can also pass the negative
direction to the limit.

This is the exact analytic analogue of the earlier triangular-shear and
composite-coherence bounds: every finite normal form exists, while the
coordinate change exposing it may become singular.

## Source authority

An arbitrary entire Gaussian interpolant need not be the Mellin transform of
an authorized source packet. The source theorem must show that the chosen
Mellin/Paley–Wiener or projective exponential class:

1. separates finite reciprocal divisor packets;
2. is closed under the required interpolation multipliers;
3. maps back to the common nine-operation source domain;
4. controls prime, gamma, and endpoint evaluations;
5. has completion-stable interpolation cost.

Therefore the RH frontier has become a precise test-space theorem:

> Is the source-authorized Mellin transform class sufficiently rich and
> sufficiently well-conditioned to realize the negative swap mode of every
> hypothetical off-seam reciprocal pair?

If yes, positivity of the complete Weil form excludes all such pairs. If not,
an off-seam negative block may remain invisible because the constructor test
space cannot address it.
