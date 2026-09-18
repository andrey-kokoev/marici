# The derivative-loaded prime cell has an explicit weighted linking matrix and radical

On the primitive/square source packet, the frozen orientation is

$$
S_{12}=\operatorname{diag}(-1,+1).
$$

The Euler logarithmic coefficient is

$$
a_{p,k}=\frac1k p^{-k/2},
$$

and the boundary derivative contributes `2kL`, with `L=log p`. Therefore the derivative-loaded face incidences are

$$
A_p=-2Lp^{-1/2},
\qquad
B_p=2Lp^{-1}.
$$

The retained tensor-unit wall is transported separately with coefficient one. Hence, in this declared frame,

$$
P_p=\operatorname{diag}
\left(-2Lp^{-1/2},\,2Lp^{-1},\,1\right).
$$

Applying the weighted relative-linking law gives

$$
\boxed{
\Omega_p
=\omega_p
\begin{pmatrix}
0&-4L^2p^{-3/2}&2Lp^{-1/2}\\
4L^2p^{-3/2}&0&2Lp^{-1}\\
-2Lp^{-1/2}&-2Lp^{-1}&0
\end{pmatrix}.
}
$$

Its transported overlap radical is

$$
\boxed{
r_p=
\begin{pmatrix}
-\dfrac{p^{1/2}}{2L}\\[4pt]
\dfrac{p}{2L}\\[4pt]
1
\end{pmatrix},
\qquad
\Omega_pr_p=0.
}
$$

This freezes every relative coefficient except the geometric source scalar `omega_p`. Moving the factor `2kL` from the incidence into `omega_p` is a frame change and must transform all three rows, columns, and the radical coherently; it may not be done gradewise after pairing.

The endpoint/moving-seam constructor already proves exact metric naturality for the linear source bundle, with unit wall transport and the stated Adams loading. Therefore the remaining comparison is no longer an endpoint-rank problem. It is the complete bulk-plus-external-port Green identity whose anti-diagonal boundary restriction must equal this `Omega_p` and whose scalar evaluation must cancel the forcing difference.

The finite test is now explicit:

1. compute the anti-diagonal boundary block of the source bulk Green form;
2. express it in the ordered basis `(primitive,square,wall)`;
3. verify its radical is exactly `r_p`;
4. verify its three skew entries occur in the displayed ratios;
5. identify the common factor with `omega_p` from the Stokes/Wronskian source trace.

Status: weighted prime-cell linking matrix and radical fully materialized; anti-diagonal bulk Green restriction and common source coefficient remain open.
