# The theta-tail Evans readout is a native symplectic determinant

Author: marici.Grothendieck

Date: 2026-08-28

## Source-derived phase plane

Let

\[
G_s(q)=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv.
\]

Then

\[
G_s'=-sG_s-f.
\]

Retain the forcing amplitude as an independent constant channel \(c\). The
homogeneous rank-two system is

\[
\frac d{dq}
\begin{pmatrix}G\\c\end{pmatrix}
=
\begin{pmatrix}
-s&-f(q)\\
0&0
\end{pmatrix}
\begin{pmatrix}G\\c\end{pmatrix}.
\]

This is the native value--source boundary plane. No auxiliary phase or
post-hoc operator has been introduced.

## Exact Evans determinant

The solution selected by the terminal condition at infinity and normalized
by \(c=1\) has endpoint vector

\[
y_s(0)=
\begin{pmatrix}
X(s)\\1
\end{pmatrix},
\qquad
X(s)=\int_0^\infty f(v)e^{sv}\,dv.
\]

The boundary condition \(G(0)=0\) is the line spanned by

\[
e_c=
\begin{pmatrix}0\\1\end{pmatrix}.
\]

Therefore

\[
\det(e_c,y_s(0))=-X(s).
\]

A transform zero is exactly loss of transversality between the transported
source line and the endpoint-condition line.

## Native symplectic structure

The original coefficient matrix has trace \(-s\), so its oriented area is
conformally transported. Apply the canonical half-trace gauge

\[
z(q)=e^{sq/2}y(q).
\]

The gauged flow is

\[
z'=
\begin{pmatrix}
-s/2&-f(q)\\
0&s/2
\end{pmatrix}z.
\]

Its matrix has trace zero. In dimension two this is precisely the symplectic
Lie algebra for the standard Green matrix

\[
J=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

Thus the quarter-turn and oriented determinant are source-native. The bridge
proposed in entry 4120 is real.

## What remains

Complex symplectic transport alone does not confine intersections. Generic
real seeds, including hostile finite-atom sources, have the same rank-two
Evans and symplectic structure while admitting off-seam zeros.

The remaining RH theorem is now sharply separated:

1. double this phase plane through the reciprocal theta sector;
2. derive the Real or Hermitian form selected by modular sewing;
3. prove that in each open half-plane the transported source line cannot meet
   the endpoint line;
4. show that this exclusion fails only on the fixed reciprocal seam.

The zero-to-boundary-rank-loss bridge is established. The missing force is a
theta-specific restriction on the allowable symplectic path.

