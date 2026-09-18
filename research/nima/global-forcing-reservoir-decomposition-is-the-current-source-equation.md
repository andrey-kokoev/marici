# Global forcing-reservoir decomposition is the current source equation

For two spectral heights `w,z`, the completed theta forcing reservoir is

$$
\mathcal F(w,z)
=
\langle\Phi,G_z\rangle
+
\langle G_w,\Phi\rangle.
$$

At finite arithmetic cutoff `X`, the required source identity is

$$
\mathcal F_X(w,z)
=
\mathcal F_X^{(1)}(w,z)
+
\mathcal F_X^{(2)}(w,z)
+
\mathcal F_X^{(\ge3)}(w,z)
+
\mathcal F_X^{({\rm seam})}(w,z)
+
\mathcal F_X^{(\infty)}(w,z).
$$

The five right-hand terms are respectively the primitive, square, connected, seam, and archimedean currents on their already constructed common logarithmic/determinant-line carrier.

Define the residual

$$
\mathcal Q_X(w,z)
=
\mathcal F_X(w,z)
-
\sum_{r\in\{1,2,\ge3,{\rm seam},\infty\}}
\mathcal F_X^{(r)}(w,z).
$$

The global conservative colligation exists only if

$$
\mathcal Q_X(w,z)=0
$$

as a typed two-height kernel before scalar trace and before Xi specialization.

Because the common logarithmic operator

$$
H_X=\sum_{p\le X}\sum_{k\ge1}\frac1kQ_p^k
$$

already separates the first, second, and connected grades, the arithmetic part can be tested coefficientwise in `(p,k)`. The remaining comparisons are:

1. grade `1` against the primitive endpoint current;
2. grade `2` against the square current;
3. grades `k>=3` against the `det_3` connected logarithm;
4. the finite endpoint remainder against the seam current;
5. the smooth completion remainder against the Tate/gamma current.

No repository source located in the current search proves this complete two-height decomposition. One scalar explicit-formula equality or determinant product is insufficient because it does not determine mixed-height Gram entries.

Status: exact global source equation fixed; coefficientwise two-height current decomposition remains open.
