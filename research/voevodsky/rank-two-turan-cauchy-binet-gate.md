# Rank-two Turán and Cauchy--Binet gate

## Question

What is the first nontrivial arithmetic inequality in the remainder Hankel cone, and how does it detect nonreal sampled spectral bases?

## Claim boundary

The rank-two determinant and its Cauchy--Binet decomposition are exact. No endpoint--gamma--prime evaluation with certified tails is supplied.

## Rank-two determinant

For moments

\[
a_n=\sum_jw_jy_j^n,
\]

the first nontrivial Hankel minor is

\[
D_2=a_0a_2-a_1^2.
\]

Expanding gives

\[
D_2
=
\sum_{j<k}
w_jw_k(y_j-y_k)^2.
\]

The square is algebraic, not an absolute-value square.

If all \(w_j\geq0\) and all \(y_j\in\mathbb R\), every term is nonnegative. This is the rank-two shadow of the full Cauchy--Binet exterior-power factorization.

## Conjugate-pair obstruction

For an isolated conjugate pair

\[
y=u+iv,
\qquad
\bar y=u-iv,
\]

with equal positive real weight \(w\), its pair contribution is

\[
w^2(y-\bar y)^2
=-4w^2v^2.
\]

Thus conjugate grouping does not repair positivity by producing \(|y-\bar y|^2\). It produces the opposite sign.

This does not mean every off-axis zero forces \(D_2<0\). Cross terms with other bases can dominate the negative pair. The checker exhibits such compensation explicitly. Rank two is therefore a falsifier and first arithmetic gate, not an individual-zero detector.

## Sampled-function form

For remainder differences

\[
a_n
=H_R(t+nh)-H_R(t+(n+1)h),
\]

write

\[
X_k=H_R(t+kh).
\]

Then

\[
D_2(t,h)
=
(X_0-X_1)(X_2-X_3)
-(X_1-X_2)^2.
\]

Equivalently,

\[
D_2(t,h)
=
[H_R(t)-H_R(t+h)]
[H_R(t+2h)-H_R(t+3h)]
-
[H_R(t+h)-H_R(t+2h)]^2.
\]

This is a discrete Turán inequality for the first-difference sequence.

## Higher-rank pattern

For an \(r\)-by-\(r\) Hankel determinant, Cauchy--Binet gives sums over \(r\)-element subsets:

\[
\det(a_{i+j})_{0\leq i,j<r}
=
\sum_{J,\ |J|=r}
\left(\prod_{j\in J}w_j\right)
\Delta(y_J)^2.
\]

Again, \(\Delta^2\) is algebraic. It is termwise nonnegative only for appropriately signed real data. Any Dodgson, Jacobi, or continued-fraction recurrence merely repackages these determinants unless its coefficient signs are established independently from the arithmetic source.

## Certification target

The first useful computation is not another floating-point scan. It is an interval enclosure of

\[
D_2(t,h)
\]

from the exact endpoint--gamma--prime formula, with:

- a declared rational domain for \(t,h\);
- outward-rounded evaluation of the retained terms;
- explicit prime and zero truncation bounds;
- separate endpoint and gamma errors;
- a retained sign-indeterminate result when the enclosure crosses zero.

A certified negative value would refute the proposed remainder cone. A certified positive patch would establish only rank two on that parameter patch.

## Disposition

The full RH-strength gate begins with one explicit four-sample Turán determinant. Its algebraic decomposition explains both why real positive spectral data pass and why conjugate poles are dangerous. The unresolved work is arithmetic enclosure, not further matrix reformulation.

## Verification

- `research/voevodsky/rank-two-turan-cauchy-binet-gate-v1.json`
- `research/voevodsky/checkers/check_rank_two_turan_cauchy_binet_gate.py`
- `research/voevodsky/results/rank_two_turan_cauchy_binet_gate.json`
