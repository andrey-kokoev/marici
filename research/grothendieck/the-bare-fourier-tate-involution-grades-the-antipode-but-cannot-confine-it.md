# The bare Fourier–Tate involution grades the antipode but cannot confine it

## Completed two-chart state

Assemble the one-sided Mellin charts into

\[
V(z)=
\begin{pmatrix}
K(z)\\
K(-z)
\end{pmatrix}.
\]

Reciprocal sewing exchanges the two charts. On this completed state its
internal action is the constant matrix

\[
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The symmetric and antisymmetric channels diagonalize it:

\[
F=\frac{K(z)+K(-z)}2,
\qquad
G=\frac{K(z)-K(-z)}2,
\]

with

\[
S(F,G)=(F,-G).
\]

Thus Fourier–Tate sewing supplies an exact parity grading.

## Scalar zeros are authorized antisymmetric states

At a completed scalar zero,

\[
F(z)=0,
\qquad
V(z)=G(z)
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]

This is simply the negative eigenspace of \(S\). The reciprocal involution
does not reject it. More importantly, \(S\) is independent of \(z\), so it
cannot distinguish the seam from either open half-plane.

The bare sewing law therefore grades the antipodal state but supplies no
incidence-location theorem.

## Constant invariant metrics add no sector information

Any constant Hermitian control form commuting with \(S\) is diagonal in the
\((F,G)\) basis. It can assign different fixed weights to the symmetric and
antisymmetric sectors, but those weights do not depend on
\(\operatorname{Re}z\).

Consequently, no constant Fourier-invariant metric can turn the real
current-amplitude power

\[
-\operatorname{Re}(z)|G(z)|^2
\]

into a conservation law that vanishes only on the seam. Choosing a
\(z\)-dependent sign by hand would import the desired half-plane distinction
rather than derive it.

## What the control tower must contain

The control tower needs more than the reciprocal involution. It must contain
a transport law whose metric, connection, or boundary form changes
covariantly with \(z\), while reducing to unitary Fourier–Tate sewing on the
seam.

The required extra datum is therefore differential rather than merely
equivariant:

- the involution supplies the two grades;
- the connection supplies motion between spectral fibers;
- a Green identity relates that motion to the endpoint current;
- the boundary condition decides whether an antisymmetric state is admissible
  at a given spectral point.

This is why the control tower cannot be collapsed into the value tower's
Fourier parity cell. The grading is static; RH needs a location-sensitive
transport constraint.

## Scope

The result does not show that no Fourier-derived control exists. It shows that
the bare order-two sewing action and every constant invariant metric are
insufficient. A successful construction must retain the source-derived
connection, analytic domain, or boundary current that is lost when Fourier
transport is reduced to its sheet permutation.

## Operator stimulus

The operator asked whether the coherence comparison itself needs another
tower. Here it does. Fourier coherence produces a valid comparison cell, but
that cell is only a grading. Its own transport and boundary compatibility form
the next rung required to distinguish where the antisymmetric state may occur.
