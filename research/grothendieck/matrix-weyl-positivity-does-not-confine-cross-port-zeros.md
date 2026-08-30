# Matrix Weyl positivity does not confine cross-port zeros

Author: marici.Grothendieck

Date: 2026-08-28

## Boundary-triple placement

The theta Evans readout uses two distinct ports:

\[
X(s)=\delta_0A_s^{-1}f.
\]

In a conservative rigged realization, the natural object is therefore a
matrix-valued Weyl function whose diagonal entries are same-port responses
and whose off-diagonal entry is the physical source--observer response.

Matrix Herglotz positivity means

\[
\operatorname{Im}M(z)\succeq0
\]

in the upper half-plane. This does not prevent an off-diagonal entry from
vanishing there.

## Smallest hostile matrix

Let

\[
A=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix},
\qquad
M(z)=A+zB.
\]

Both \(A\) and \(B\) are Hermitian and \(B\) is positive definite. For
\(\operatorname{Im}z>0\),

\[
\operatorname{Im}M(z)
=(\operatorname{Im}z)B\succ0.
\]

Thus \(M\) is a strict matrix Herglotz function. Nevertheless,

\[
M_{12}(z)=-i+z
\]

vanishes at \(z=i\), inside the upper half-plane.

## Consequence

Retaining the source and observer as separate boundary ports repairs the
typing defect and permits a conservative realization. Passivity of the full
matrix still does not confine zeros of their cross response.

The RH-bearing readout must therefore be stronger than one off-diagonal Weyl
entry. Viable possibilities are:

1. the determinant of a full boundary relation;
2. a Schur complement whose positivity follows from an independently fixed
   boundary condition;
3. a source law forcing the two-port Weyl matrix to have rank one or another
   rigid subclass in which cross zeros imply a full spectral event.

The hostile matrix is the minimal falsifier for any argument that passes
directly from matrix Herglotz positivity to nonvanishing of the theta
source--observer coefficient.

