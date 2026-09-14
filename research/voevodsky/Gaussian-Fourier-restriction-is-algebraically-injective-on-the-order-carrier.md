# Gaussian Fourier restriction is algebraically injective on the order carrier

## Theorem

Let \(\lambda_k\) be an unbounded sequence of logarithmic arithmetic labels satisfying

\[
\lambda_{k+1}-\lambda_k\longrightarrow0.
\]

For distinct parameter pairs \((\sigma_j,a_j)\), with \(\sigma_j>0\), the Riesz vectors obtained from

\[
F_j(\lambda)=e^{-\sigma_j\lambda^2}e^{-ia_j\lambda}
\]

are finitely linearly independent in the complexified order completion.

## Proof

Suppose

\[
\sum_jc_jr_{\sigma_j,a_j}=0.
\]

The represented functional vanishes on every finite zero-sum coefficient packet. Testing adjacent differences shows that

\[
S(\lambda_k)=
\sum_jc_jF_j(\lambda_k)
\]

is constant in \(k\). Every summand tends to zero as \(k\) tends to infinity, so this constant is zero.

Let \(\sigma_0\) be the smallest width occurring in the relation. Multiplication by \(e^{\sigma_0\lambda_k^2}\) gives

\[
P(\lambda_k)+o(1)=0,
\]

where

\[
P(x)=
\sum_{\sigma_j=\sigma_0}c_je^{-ia_jx}
\]

is a finite trigonometric polynomial. Its derivative is bounded. Since the logarithmic label gaps tend to zero, convergence of \(P(\lambda_k)\) to zero implies that \(P(x)\) tends to zero along the entire positive tail.

The long-interval mean square of a trigonometric polynomial is the sum of the squared magnitudes of its coefficients. Since \(P(x)\) tends to zero, that mean square vanishes, and every coefficient in the minimal-width layer is zero.

Repeating the argument for the remaining widths proves that all \(c_j\) vanish.

For prime or prime-power logarithmic labels, the required gap condition follows from the standard asymptotic distribution of primes.

## Kernel descent

Because the Riesz map is algebraically injective, the polarized source kernel has no finite relation ambiguity on its image. It therefore defines a unique Hermitian form on the algebraic Gaussian Riesz span by

\[
q_0
\left(
\sum_jc_jr_j,
\sum_kd_kr_k
\right)
=
\sum_{j,k}\overline{c_j}d_kK(j,k).
\]

Thus finite algebraic descent is complete.

## Remaining topological gate

Injectivity does not imply closability. A sequence of distinct finite combinations may converge to zero in the order norm while remaining Cauchy with a nonzero value in \(q_0\). Excluding precisely those sequences is the already recorded kernel closability criterion.

Accordingly, the live obstruction has moved from algebraic descent to topological compatibility between the base Gram kernel and the source Weil kernel.

## Verification

```text
python research/voevodsky/checkers/check_gaussian_restriction_algebraic_injectivity.py
```

The checker audits 2,262 prime logarithms and three mixed width/translation families. Its numerical ranks are diagnostic; the theorem is supplied by the analytic argument above.

Artifacts:

- `research/voevodsky/checkers/check_gaussian_restriction_algebraic_injectivity.py`
- `research/voevodsky/results/gaussian_restriction_algebraic_injectivity.json`
