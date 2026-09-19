# The missing first-Adams Green coordinate is exactly the sigma-z control channel

## Pauli decomposition

The unique required target Gram is

\[
G_\theta^{\rm req}
=
\begin{pmatrix}
a+4b+4u&a-4b-4iv\\
a-4b+4iv&a+4b-4u
\end{pmatrix}.
\]

Using

\[
\sigma_x=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\quad
\sigma_y=
\begin{pmatrix}0&-i\\i&0\end{pmatrix},
\quad
\sigma_z=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]

it decomposes exactly as

\[
\boxed{
G_\theta^{\rm req}
=(a+4b)I
+(a-4b)\sigma_x
+4v\sigma_y
+4u\sigma_z.
}
\]

Thus the four real Stieltjes coordinates map bijectively to the four Hermitian
matrix channels.

## Meaning of the channels

- `I`: common-mode energy;
- `sigma_x`: symmetric cross-channel coupling;
- `sigma_y`: reciprocal orientation;
- `sigma_z`: forward/backward energy imbalance.

The ordinary two-ray four-grade Hilbert Gram

\[
\begin{pmatrix}D&C\\C&D\end{pmatrix}
=DI+C\sigma_x
\]

contains only the `I` and `sigma_x` channels. It has neither reciprocal
orientation nor directed energy imbalance.

The strict Stieltjes cross-pairing `u>0` requires

\[
4u\sigma_z.
\]

Therefore the first missing completed-Green coordinate is exactly the
`sigma_z` control channel.

## Control realization

In a dynamic extension with auxiliary state `h`, let the two directed ports
couple by columns `k_+` and `k_-` to an auxiliary storage operator `A`. A Schur
reduction contributes

\[
-K^*A^{-1}K,
\qquad
K=(k_+,k_-).
\]

Its diagonal polarization is

\[
-\langle k_+,A^{-1}k_+\rangle
+\langle k_-,A^{-1}k_-\rangle.
\]

To produce the required target, the completed wall/tail controller must satisfy

\[
\langle k_-,A^{-1}k_-\rangle
-
\langle k_+,A^{-1}k_+\rangle
=8u,
\]

with sign adjusted if the Green extension uses the opposite Schur convention.

## Homotopy interpretation

The `sigma_z` component is antisymmetric under exchange of the two phase rows.
It is therefore the finite matrix coordinate naturally carried by the
forward/backward homotopy direction of the prism. The `sigma_y` component
records reciprocal orientation within that plane.

This connects the control and homotopy pictures: the higher compensator must
supply the missing `sigma_z` storage imbalance while preserving the
`sigma_y` star orientation.

## Next finite test

For any proposed complete Green block, compute its Schur-reduced Pauli
coordinates. Reject it unless they equal

\[
(a+4b,\ a-4b,\ 4v,\ 4u)
\]

in the ordered basis `(I,sigma_x,sigma_y,sigma_z)` before Xi-zero evaluation.