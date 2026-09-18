# Many-many wall/jump-preserving refinements

A source-basis refinement

$$
R=\begin{pmatrix}a&b\\c&d\end{pmatrix}
$$

preserves the wall/jump splitting exactly when `H R H` is diagonal. This is equivalent to

$$
 a=d,
\qquad
 b=c.
$$

Thus the source-basis form is

$$
R=aI+bB,
\qquad
B=\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

and the wall/jump eigenvalues are `a+b` and `a-b`. Since

$$
T_\theta=SH,
\qquad S=\operatorname{diag}(-2,1),
$$

this same refinement remains diagonal after corrected wall transport:

$$
T_\theta R T_\theta^{-1}
=\operatorname{diag}(a+b,a-b).
$$

Status: exact criterion for preserving the corrected wall/jump decomposition derived.
