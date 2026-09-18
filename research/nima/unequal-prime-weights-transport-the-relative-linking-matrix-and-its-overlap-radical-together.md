# Unequal prime weights transport the relative linking matrix and its overlap radical together

Let

$$
\Omega_0=
\begin{pmatrix}
0&1&-1\\
-1&0&1\\
1&-1&0
\end{pmatrix},
\qquad
\Omega_0r=0,
\qquad r=(1,1,1)^T.
$$

Suppose typed prime pushforward acts on the three faces by an invertible diagonal incidence

$$
P_p=\operatorname{diag}(a_p,b_p,c_p),
$$

where the entries carry primitive, square, and constant-wall weights. Then the pushed-forward linking form is

$$
\Omega_p
=P_p\Omega_0P_p^T
=
\begin{pmatrix}
0&a_pb_p&-a_pc_p\\
-a_pb_p&0&b_pc_p\\
a_pc_p&-b_pc_p&0
\end{pmatrix}.
$$

Its radical is not generally the unweighted vector `r`. Instead,

$$
\Omega_p r_p=0,
\qquad
r_p=P_p^{-T}r
=
\begin{pmatrix}a_p^{-1}\\b_p^{-1}\\c_p^{-1}\end{pmatrix}.
$$

Thus unequal Euler weights transport the overlap relation and the ordered linking matrix together. Requiring the same canonical matrix or the same relation `(1,1,1)=0` after pushforward is wrong unless

$$
a_p=b_p=c_p.
$$

Primitive and square Euler incidences are unequal, so the arithmetic target must retain the weighted overlap vector `r_p`. The wall coefficient `c_p` is not a free normalization: it is fixed by the source transport of the constant overlap face.

The correct naturality test is therefore the congruence

$$
\boxed{
\Omega_p^{\rm arith}
=P_p\,(\omega_p\Omega_0)\,P_p^T
}
$$

together with

$$
r_p=P_p^{-T}r.
$$

This is stronger than comparing one Wronskian scalar and more accurate than demanding an unchanged canonical skew matrix. It checks all three oriented face pairs and the transported radical simultaneously.

A transpose/mate error replaces `P Omega_0 P^T` by an oppositely typed expression; a missing wall transport leaves the wrong radical; pushforward after scalar codiagonalization cannot reconstruct either defect.

Status: exact weighted linking and radical transport derived; source extraction of the wall incidence `c_p` and comparison with the arithmetic three-face block remain open.
