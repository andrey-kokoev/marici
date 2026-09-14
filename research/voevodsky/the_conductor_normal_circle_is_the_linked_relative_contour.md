# The conductor normal circle is the linked relative contour

## Question

Is there a source-derived mathematical contour whose image under each wall-labelled lift has the linked winding required for the integral normal residue?

## Claim boundary

This constructs a contour in the complexified conductor parameter space and computes its winding pairing. It is not a physical detector path or laboratory control protocol.

## Normal circle

Fix \((x,y)\) with \(xy\ne0\) and away from additional conductor discriminant zeros. Since

\[
\Delta_i(0)=4x^2y^2\ne0,
\]

each oriented square root \(Y_i(E)\) is analytic on a sufficiently small disk around \(E=0\).

For sufficiently small \(\rho>0\), define the positively oriented conductor-normal circle

\[
\gamma_\rho:\quad E=\rho e^{i\theta},
\qquad 0\leq\theta\leq2\pi.
\]

This is the canonical positive generator of the first homology of the punctured normal disk, after choosing the complex orientation.

## Image under the wall lifts

For either wall-labelled map \(\Phi_i\),

\[
B=X_1-Y=E,
\qquad
C=X_2+Y=E,
\qquad
E_{\rm rel}=X_1+X_2=2E.
\]

Therefore

\[
\frac{1}{2\pi i}\oint_{\gamma_\rho}d\log B
=
\frac{1}{2\pi i}\oint_{\gamma_\rho}d\log C
=
\frac{1}{2\pi i}\oint_{\gamma_\rho}d\log E_{\rm rel}
=1.
\]

The complementary factors

\[
A=2Y_i(E)+E,
\qquad
D=-2Y_i(E)+E
\]

stay nonzero for sufficiently small \(\rho\), so their winding numbers are zero. The full winding vector is

\[
(w_A,w_B,w_C,w_D,w_E)=(0,1,1,0,1).
\]

Pairing this vector with the five residue matrices yields

\[
R_B+R_C+R_E=R_{\rm eq}.
\]

Thus the required linked residue is induced by an explicit integral cycle/form pairing, not by assigning three independent loops.

## Orientation

Reversing the complex orientation negates every winding number and sends the residue to \(-R_{\rm eq}\). At quarter twist the resulting monodromy is the inverse of the positive-orientation monodromy. Since that monodromy is involutive, both orientations give the same operator, although the signed residue and Stokes pairing remain different.

## Scope of authority

The complex orientation and punctured-disk generator authorize this contour mathematically. They do not establish that a physical experiment varies total energy around a complex loop, or that detector records implement analytic continuation. Physical readout authority therefore remains absent.

## Disposition

A canonical mathematical contour on each wall-labelled conductor cover is constructed, and its winding pairing gives exactly the linked equal-order residue. The unresolved gate is physical realization of this analytic continuation and the fractional quarter-twist local system.
