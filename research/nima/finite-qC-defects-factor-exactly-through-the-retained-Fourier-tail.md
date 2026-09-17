# Finite q-C defects factor through the retained Fourier tail

A finite Pontryagin scout uses the group

$$
(\mathbb Z/2)^3
$$

with four visible and four tail coordinates. The visible-from-tail Fourier block is

$$
A=
\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}.
$$

This block is invertible.

On four source labels, define a nonlinear phase chart and its bilinear multiplicativity defect. The resulting defect operator has sixteen columns:

$$
M_2:A_{\mathrm{src}}\otimes A_{\mathrm{src}}
\to V_{\mathrm{vis}}.
$$

All sixteen columns are nonzero. Exact Gaussian-rational elimination constructs

$$
h_2=A^{-1}M_2
$$

and verifies

$$
Ah_2=M_2
$$

column by column.

Thus the retained tail supplies the degree-one q-C component on this finite packet. The multiplicativity defect is realized as a tail boundary rather than as a formal external cell.

The completion problem asks for a compatible cutoff family

$$
h_{2,X}
$$

satisfying

$$
A_Xh_{2,X}=M_{2,X}
$$

with uniform graph bounds and refinement compatibility. Finite invertibility alone does not control the norms of

$$
A_X^{-1}M_{2,X}
$$

as the cutoff moves.

The checker `check_qC_finite_defect_tail_factorization.py` performs the exact finite factorization without floating-point arithmetic.
