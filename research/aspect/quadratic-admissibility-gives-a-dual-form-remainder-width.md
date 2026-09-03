# Quadratic admissibility gives a dual-form remainder width

## Question

If source constraints bound admissible q_G12 lift displacements by a positive quadratic form rather than a polytope, what is the exact omitted-route width?

## Scalar route

Let the admissible set be the ellipsoid

\[
\mathcal A_0=
\{w: w^*Hw\le1\},
\qquad
H>0,
\]

and let an omitted scalar route be the functional \(r\). Weighted Cauchy–Schwarz gives

\[
|rw|^2
\le
(rH^{-1}r^*)(w^*Hw).
\]

The bound is attained along \(H^{-1}r^*\), so

\[
\omega_r(\mathcal A_0)^2
=
rH^{-1}r^*.
\]

Thus the intrinsic route width is the dual norm determined by the source admissibility form.

## Vector route

For a vector-valued omitted route \(R\),

\[
\omega_R(\mathcal A_0)^2
=
\lambda_{\max}
\left(
H^{-1/2}R^*RH^{-1/2}
\right).
\]

Equivalently, it is the largest generalized eigenvalue in

\[
R^*R\,w=\lambda Hw.
\]

This is the same normalized-return problem on the torsor subspace, now with a source-derived denominator.

## Exact model

Take

\[
H=\operatorname{diag}(4,9),
\qquad
r=(1,1).
\]

Then

\[
\omega_r^2
=
\frac14+rac19
=
\frac{13}{36}.
\]

Testing only the two coordinate axes gives squared width \(1/4\), which misses the maximizing mixed lift. A torsor-basis diagonal audit is therefore insufficient for quantitative width even when it was sufficient for exact radical membership under positivity.

## Degenerate boundary

If \(H\) is only semidefinite, finite width requires every null direction of \(H\) to lie in \(\ker R\). Otherwise the admissible cylinder is unbounded along a route-visible direction and the width is infinite. On the quotient by that common nullspace, the formula uses the reduced inverse.

## Prime-uniform gate

A prime-dependent family requires a uniform upper bound on the largest generalized eigenvalue. Pointwise positivity of \(H_p\) is insufficient if its smallest eigenvalue approaches zero in a route-visible direction.

## Verification

`research/aspect/checkers/check_ellipsoid_remainder_width.py` verifies the exact dual formula, saturation direction, and failure of axis-only testing with rational arithmetic.

## Disposition

The source owner may replace polytope enumeration by one positive admissibility form \(H_p\) and an omitted-route map \(R_p\). The executable target is a prime-uniform generalized-eigenvalue bound on the rank-seven torsor subspace.
