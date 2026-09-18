# Explicit boundary cross blocks for the conservative generator

Use the decomposition

$$
\widetilde H=\mathbb Cu\oplus M\oplus\mathbb C_{\rm end},
\qquad M=u^\perp,
$$

and write the self-adjoint bilateral generator as

$$
D=
\begin{pmatrix}d&r^*\\r&D_M\end{pmatrix},
$$

where `d` is real and `D_M` is self-adjoint on the induced domain. Put

$$
s=\|b\|^{-1},
\qquad
J_{\rm col}=
\begin{pmatrix}0&0&s\\0&I_M&0\\s&0&0\end{pmatrix}.
$$

For arbitrary real scalars `x_0,y_0`, define

$$
\widetilde A=
\begin{pmatrix}
d&r^*&x_0\\
r&D_M&s r\\
y_0&s^{-1}r^*&d
\end{pmatrix}.
$$

Its history compression is exactly `D`. Direct multiplication gives

$$
J_{\rm col}\widetilde A
=
\begin{pmatrix}
sy_0&r^*&sd\\
r&D_M&sr\\
sd&sr^*&sx_0
\end{pmatrix},
$$

which is self-adjoint. Hence

$$
\widetilde A^*J_{\rm col}=J_{\rm col}\widetilde A.
$$

Therefore the conservative Green equation uniquely fixes the off-diagonal vector blocks up to the two real scalar boundary parameters `x_0,y_0`. The fixed vectors are the coupling `r` between the forcing direction `u` and its orthogonal history complement.

The two scalar freedoms must be fixed by the source boundary convention, reciprocity, or transfer normalization. Choosing them arbitrarily proves existence of a conservative extension but not source authority or preservation of the Xi transfer.

Status: explicit boundary-enlarged conservative generator constructed with unchanged history compression; source selection of the two scalar boundary parameters and transfer comparison remain open.
