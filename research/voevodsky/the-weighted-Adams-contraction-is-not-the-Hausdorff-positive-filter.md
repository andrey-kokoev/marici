# The weighted Adams contraction is not the Hausdorff positive filter

Prior research constructs the weighted Adams map

\[
S_re_{p,k}=e_{p,rk}
\]

with a strict positive scalar cocycle

\[
\rho_r(p,k)=\frac1r p^{-(r-1)k/2}.
\]

This makes the analytic Adams transport a contraction in operator norm. It does not make it a positive operator.

A weighted grade-raising shift has finite model

\[
A=
\begin{pmatrix}0&0\\\rho&0\end{pmatrix},
\qquad0<\rho<1.
\]

Then

\[
A^*A\leq I,
\]

so \(A\) is contractive, but

\[
A\neq A^*
\]

and its quadratic form takes negative values. It is not an order-positive self-adjoint contraction.

The Hausdorff binary filter instead requires

\[
0\leq Y_h\leq I,
\qquad
Y_h=e^{-hL}
\]

on one fixed carrier, for every additive real heat step \(h\).

The source types also differ:

- Adams uses multiplicative integer grade reindexing \(k\mapsto rk\);
- its range is the proper closed divisible-grade subspace;
- Hausdorff transport varies continuously in an additive heat parameter;
- \(e^{-hL}\) is self-adjoint and positive.

Therefore the existing Adams semigroup cannot be identified directly with the RH-bearing Hausdorff filter. The phrase “positive cocycle contraction” refers to positive scalar weights and norm contraction, not positivity in the operator order.

A surviving route would have to construct a self-adjoint operator from Adams and its adjoint, then prove its source moments equal \(H(t+nh)\). Obvious symmetrizations such as \((A+A^*)/2\) are not positive in general and do not inherit the Adams semigroup law.

## Verification

```text
python research/voevodsky/checkers/check_Adams_contraction_is_not_Hausdorff_positive_filter.py
```

Artifacts:

- `research/voevodsky/checkers/check_Adams_contraction_is_not_Hausdorff_positive_filter.py`
- `research/voevodsky/results/Adams_contraction_not_Hausdorff_positive_filter.json`
