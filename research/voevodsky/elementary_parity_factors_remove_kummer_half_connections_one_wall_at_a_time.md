# Elementary parity factors remove Kummer half-connections one wall at a time

## Question

Is the factorization \(J=J_1J_2\) compatible with the audited Gauss–Manin connection, or is it only an arithmetic Smith decomposition?

## Claim boundary

This factors the recorded conductor-frame connection conjugation exactly. It does not identify either elementary factor with the published relative intersection matrix or construct a contour pairing.

## Primitive and enhanced connections

In the primitive conductor frame, the audited connection is

\[
A_{\rm prim}=
\begin{pmatrix}
a_1&0&a_1/2\\
0&a_2&a_2/2\\
0&0&0
\end{pmatrix},
\]

where

\[
a_i=-\frac12d\log\Delta_i.
\]

The enhanced frame has diagonal connection

\[
A_{\rm exc}=\operatorname{diag}(a_1,a_2,0).
\]

The full intertwiner obeys

\[
A_{\rm exc}J=JA_{\rm prim}.
\]

## Wallwise conjugations

Using the commuting factors

\[
J_1=
\begin{pmatrix}2&0&1\\0&1&0\\0&0&1\end{pmatrix},
\qquad
J_2=
\begin{pmatrix}1&0&0\\0&2&1\\0&0&1\end{pmatrix},
\]

conjugation by \(J_2\) gives

\[
A_{(2)}=J_2A_{\rm prim}J_2^{-1}
=
\begin{pmatrix}
a_1&0&a_1/2\\
0&a_2&0\\
0&0&0
\end{pmatrix}.
\]

Thus \(J_2\) removes exactly the wall-two half-connection while leaving the wall-one term unchanged. Applying \(J_1\) then gives

\[
J_1A_{(2)}J_1^{-1}=A_{\rm exc}.
\]

In the opposite order,

\[
A_{(1)}=J_1A_{\rm prim}J_1^{-1}
=
\begin{pmatrix}
a_1&0&0\\
0&a_2&a_2/2\\
0&0&0
\end{pmatrix},
\]

and \(J_2A_{(1)}J_2^{-1}=A_{\rm exc}\).

## Consequence

Each determinant-two factor has a separate geometric role in the recorded connection:

- \(J_1\) clears the half-extension attached to \(\Delta_1\);
- \(J_2\) clears the half-extension attached to \(\Delta_2\).

The factors commute, and site exchange swaps both the factors and the two Kummer forms. Therefore the two-copy interpretation is connection-compatible, not merely an equality of Smith invariants.

## Relation to the relative source

The mined relative matrix also has a half-integral inverse and its connection is obtained by an intersection-matrix gauge transformation. This now motivates a sharper conjecture: each \(J_i\) should arise from one wall-relative intersection comparison that removes one half-extension term.

The source still does not provide the required basis map, support identification, or integral normalization. Connection-shape agreement cannot construct those arrows.

## Disposition

The two elementary parity steps exactly factor both the conductor lattice map and its Gauss–Manin diagonalization. The remaining geometric gate is to realize each step as a labelled integral relative intersection pairing.
