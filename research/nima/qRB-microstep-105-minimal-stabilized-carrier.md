# qRB microstep 105: minimally stabilized positive carrier

With the source-fixed linking operator `G_link`, choose the carrier stabilization

$$
M_{\rm car}=I+\lambda G_{\rm link},
\qquad
0\le\lambda\le\|G_{\rm link}\|^{-1}
$$

when `G_link` is nonzero. Then `M_car` is positive semidefinite by the bounded self-adjoint estimate.

This creates a positive carrier metric containing the fixed source-normalized linking block. It does not change the underlying signed observation and does not assert positivity of `G_link`.

At the endpoint `lambda=||G_link||^{-1}`, coercivity may be lost; strict carrier positivity requires a strict inequality.

Status: minimal bounded stabilization constructed abstractly; source choice of `lambda` and refinement invariance remain open.
