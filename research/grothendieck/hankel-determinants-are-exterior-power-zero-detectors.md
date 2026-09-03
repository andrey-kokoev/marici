# Hankel determinants are exterior-power zero detectors

## Question

Can Dodgson condensation or a determinant recurrence make the remainder Hankel cone source-positive without confronting the zero geometry?

## Atomic determinant identity

For a finite exponential moment sequence

\[
a_n=\sum_j w_jy_j^n,
\]

Cauchy--Binet gives the rank-`r` Hankel determinant

\[
\det(a_{i+j})_{0\le i,j<r}
=
\sum_{j_1<\cdots<j_r}
\left(\prod_{k=1}^r w_{j_k}\right)
\prod_{p<q}(y_{j_q}-y_{j_p})^2.
\]

The square is algebraic, not an absolute-value square. It is termwise nonnegative precisely when the sampled bases and weights are positive real.

For the remainder localizer,

\[
y_\rho=e^{-h\lambda_\rho},
\qquad
w_\rho=e^{-t\lambda_\rho}(1-e^{-h\lambda_\rho}),
\]

plus the endpoint atom. On RH every summand is nonnegative. Off RH, conjugate grouping makes the full determinant real but does not turn each Vandermonde square into a modulus square.

## Infinite zero set

Gaussian decay permits finite-zero truncation followed by locally uniform convergence at each fixed rank and positive `t,h`. Thus the determinant is an exterior-power sum over zero packets. Positivity at every rank says every cyclic exterior power of the sampled zero operator has a positive Gram norm.

This identifies what a source-side determinant proof must achieve: the endpoint--gamma--prime formula must reorganize the exterior-power sum into genuinely positive source factors. Merely applying a universal determinant recurrence does not supply those factors.

## Dodgson limitation

Dodgson condensation states a relation among adjacent minors. Its denominators and neighboring factors are themselves Hankel minors. An induction therefore needs positive initial data plus a source sign for the condensation numerator. Without such a sign, condensation restates the target cone.

Likewise, Jacobi pivots are ratios of consecutive Hankel determinants. A positive J-fraction is equivalent to positivity of these exterior-power sums; it is useful only if its coefficients have independent endpoint--gamma--prime formulas with provable signs.

## First nontrivial source target

The rank-two determinant is

\[
D_2=a_0a_2-a_1^2
=
\sum_{j<k}w_jw_k(y_j-y_k)^2.
\]

A credible induction must first produce a source-positive identity for this quantity, with rigorous prime tails. Entrywise monotonicity `a_n>=0` does not control it.

## Falsifier

Any proposed Gram, Jacobi, or Dodgson construction that imports positivity of a neighboring Hankel minor, replaces `(y_j-y_k)^2` by `|y_j-y_k|^2`, or assumes real recurrence coefficients has already assumed the spectral reality it is meant to prove.

## Disposition

Use `D_2` as the first arithmetic gate. Search prior low-rank heat inequalities for an endpoint--gamma--prime identity proving `a_0a_2-a_1^2>=0`; do not promote formal condensation alone as an induction.