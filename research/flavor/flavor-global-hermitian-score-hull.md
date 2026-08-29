# Global Hermitian score hull: WP1009

## Question

Is the WP1008 strict local maximum the global maximum of the positive
commutator score on the complete normalized Hermitian-pair quotient?

## Exact quotient reduction

Simultaneous unitary conjugation diagonalizes a generic Hermitian X. Central
parts, diagonal components of Y in that basis, and non-maximal triangle phases
can only dilute the positive normalized score. Normalize both Frobenius norms,
choose an ordered Weyl chamber, and write

\[
X_z=\operatorname{diag}(-1,z,1-z),\qquad -1\le z\le\frac12.
\]

Let A,B,C be its three normalized squared eigenvalue gaps:

\[
A=\frac{(z+1)^2}{2(z^2-z+1)},\quad
B=\frac{(2z-1)^2}{2(z^2-z+1)},\quad
C=\frac{(z-2)^2}{2(z^2-z+1)}.
\]

For the normalized squared edge magnitudes u,v,w,

\[
u,v,w\ge0,\qquad u+v+w=\frac12.
\]

At the determinant-maximizing triangle phase the complete score becomes

\[
F(z,u,v)=2(Au+Bv+Cw)
+4\frac{44376}{275}ABCuvw.
\]

These are quotient coordinates, not time variables or causal operations.

## Boundary exhaustion

Throughout the Weyl chamber, C is the largest squared gap and

\[
2-C=\frac{3z^2}{2(z^2-z+1)}\ge0.
\]

On an edge of the magnitude simplex, uvw vanishes and

\[
F\le\max(A,B,C)=C\le2.
\]

At either Weyl endpoint one squared gap vanishes, so the same bound holds.
The WP1007 witness has score

\[
F_\star=\frac{2417}{946}>2,
\]

and therefore no boundary point can dominate it.

## Interior KKT exhaustion

Clear the positive denominators in the three equations

\[
\partial_uF=\partial_vF=\partial_zF=0
\]

and eliminate u and v. The final exact elimination polynomial is

\[
z(z-1)(z^2-z+1)^2p_{12}(z),
\]

where

\[
\begin{aligned}
p_{12}(z)={}&37009z^{12}-222054z^{11}+377805z^{10}
+146470z^9-513261z^8-1268370z^7\\
&+2921811z^6-1268370z^5-513261z^4
+146470z^3+377805z^2-222054z+37009.
\end{aligned}
\]

An exact real-root count gives zero real roots for p12. The factor
z²-z+1 is also strictly positive. Only z=0 lies in the chosen chamber.
At z=0 the interior equations have exactly two solutions:

\[
(u,v)=\left(\frac{11}{516},\frac{11}{516}\right),
\qquad
(u,v)=\left(\frac{25}{172},\frac{25}{172}\right).
\]

Their scores are respectively

\[
\frac{37523}{19350}
<2
<\frac{2417}{946}.
\]

Thus the second point, with w=9/43, is the unique global maximizer in the
ordered chamber. Other labelings are simultaneous-permutation
representatives of the same quotient orbit.

## Classification

The positive algebraic score has a unique global maximizing Hermitian orbit
modulo the declared full simultaneous weak-basis group and scales. This is a
global mathematical selector for the coefficient-pair quotient.

It is not yet a source-generated flavor selector: the coefficient ratio was
chosen to expose the orbit, and no calibrated physical instrument implements
the score. No map from this coefficient orbit to a selected viable physical16
flavor point has been established.

## Smallest exact falsifier

A real root of p12, an additional z=0 interior solution, or any boundary score
above 2 would invalidate the exhaustion. The checker deliberately tests the
lower stationary point against the witness so that confusing stationarity
with global selection fails.

## Claim boundary

The theorem is global only for normalized Hermitian coefficient pairs under
the displayed positive score. It does not select measured flavor data, confer
source authority on R/Q, or establish an executable preparation or readout.

## Disposition

Close the global upper-hull gate positively. The sharp remaining frontier is
physical rather than algebraic: derive the ratio from an admitted source
action, map the selected coefficient orbit into the viable physical16 domain,
and type a calibrated instrument.

