# Fixed wall/Wronskian endpoint Gram is critical, not strict

The source-fixed endpoint columns are

$$
w_\theta=\binom{1/2}{1/2},
\qquad
j_\theta=\binom{1/4}{-1/4}.
$$

With endpoint metric `2I`, their Gram matrix is

$$
\begin{pmatrix}
w_\theta^*(2I)w_\theta&w_\theta^*(2I)j_\theta\\
j_\theta^*(2I)w_\theta&j_\theta^*(2I)j_\theta
\end{pmatrix}
=
\begin{pmatrix}1&0\\0&1/4\end{pmatrix}.
$$

Equivalently, for

$$
Q=\begin{pmatrix}1/2&1/4\\1/2&-1/4\end{pmatrix},
$$

one has

$$
Q^*(2I)Q=\operatorname{diag}(1,1/4).
$$

Thus the even wall direction saturates the unit threshold. The local endpoint packet is nonnegative and full rank, but it has no strict contraction margin by itself. The odd Wronskian direction has quarter energy and remains strictly below the threshold.

The completion graph metric must supply strictness in the saturated even direction through its bulk/history contribution. The derivative estimate `||partial G_C^-1/2|| approximately 0.625` controls the odd incidence but does not lower the endpoint even eigenvalue. A complete normalized loading Gram must include the wall-to-history map `M_Phi` and prove that the enlarged denominator dominates the saturated endpoint column.

Status: local `2x2` endpoint Gram computed exactly; pure endpoint strictness fails only in the even wall direction, localizing the next estimate to the wall-to-history bulk coupling.
