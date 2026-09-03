# Hankel–Schur hierarchy for prime double contact

## Positive prime law

At fixed `t>0`, put

\[
c_n=\frac{\Lambda(n)}{\sqrt n}e^{-(\log n)^2/(4t)}>0,
\qquad L_n=\log n,
\]

and define ordinary moments and character moments

\[
M_k=\sum_n c_nL_n^k,
\qquad
Z_k(\xi)=\sum_n c_nL_n^ke^{i\xi L_n}.
\]

For degree `d`, let

\[
G_d=(M_{j+k})_{0\le j,k\le d},

y_d=(Z_0,\ldots,Z_d)^T.
\]

## Exact Schur inequality

In the weighted Hilbert space on prime powers, `G_d` is the Gram matrix of the functions `1,L,...,L^d`, `y_d` records their inner products with the unit-modulus character `exp(i xi L)`, and that character has squared norm `M_0`. Therefore

\[
\begin{pmatrix}
G_d&y_d\\
y_d^*&M_0
\end{pmatrix}\succeq0.
\]

Whenever `G_d` is invertible, its Schur complement gives

\[
y_d^*G_d^{-1}y_d\le M_0.
\]

The pseudoinverse form applies without invertibility. This is a nested hierarchy: increasing `d` can only shrink the admissible set of character jets.

## Contact substitution

At a completed double contact, the source equations fix

\[
\operatorname{Re}Z_0=2\sqrt{\pi t}\,A,
\qquad
\operatorname{Im}Z_1=-2\sqrt{\pi t}\,\partial_\xi A,
\]

and first-contact curvature constrains

\[
\operatorname{Re}Z_2
\ge-2\sqrt{\pi t}\,\partial_\xi^2A.
\]

The remaining real or imaginary jet components are nuisance variables. Minimizing the Schur quadratic form over them yields the strongest degree-`d` contact exclusion obtainable from the scalar prime moments `M_0,...,M_{2d}` alone. If that constrained minimum exceeds `M_0`, contact is impossible.

Degree one recovers the value–slope ellipse after nuisance minimization. Degree two incorporates curvature in one positive-semidefinite certificate instead of appending a separate covariance estimate. Higher degrees add exact character derivatives and positive moment matrices with common Gaussian prime weights.

## Faithfulness and limitation

For each finite `d`, this is a necessary condition only. It does not assume independence or equidistribution of prime phases. In the infinite-degree limit, density of polynomials in the weighted prime-power space determines whether the hierarchy becomes faithful; that density must be proved rather than inferred from moment dimensions.

## Disposition

Use the constrained Schur minimum as the next certified contact filter. It consolidates value, slope, curvature, and higher jets without redundant width derivatives. A surviving feasible jet is not evidence of contact; a lower bound above `M_0` is a rigorous exclusion certificate.
