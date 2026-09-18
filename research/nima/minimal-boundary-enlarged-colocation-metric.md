# Minimal boundary-enlarged colocation metric

Let `H` be the bilateral two-history space, let `b in H` be the nonzero lifted forcing vector, and enlarge to

$$
\widetilde H=H\oplus\mathbb C_{\rm end}.
$$

Normalize `u=b/||b||` and decompose

$$
H=\mathbb Cu\oplus u^\perp.
$$

Use the input and output columns

$$
B=\binom{b}{0},
\qquad
C^*=\binom{0}{1}.
$$

Define `J_col` by

$$
J_{\rm col}u=\frac1{\|b\|}e_{\rm end},
\qquad
J_{\rm col}e_{\rm end}=\frac1{\|b\|}u,
$$

and let `J_col` act as any bounded invertible self-adjoint operator on `u^perp`. Then

$$
J_{\rm col}B=C^*.
$$

Choosing the identity on `u^perp` makes `J_col` bounded, self-adjoint, and invertible. Its active two-dimensional block is

$$
\frac1{\|b\|}
\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

so it has one positive and one negative direction. This is a canonical hyperbolic colocation metric after the forcing normalization is fixed.

The construction solves the port typing and colocation problem but not generator compatibility. A conservative boundary generator `A_tilde` must still satisfy

$$
\widetilde A^*J_{\rm col}=J_{\rm col}\widetilde A.
$$

That equation determines the required history-to-boundary and boundary-to-history cross blocks; setting them to zero generally fails because the dilation generator moves `u` out of its span.

Status: minimal bounded nondegenerate boundary-enlarged colocation metric constructed; conservative generator cross blocks remain open.
