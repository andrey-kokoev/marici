# Compact truncation is superexponentially small at the moment saddle

## Question

How does deleting \([0,X]\) from the unshifted Weibull comparator affect the data used by the moving-tail recurrence?

For \(a=1\), \(\beta=1/4\), the full moments are

\[
\mu_r=4\frac{(4r+3)!}{2^{4r+4}}.
\]

The omitted compact contribution satisfies

\[
0\leq d_r(X)
=
\int_0^X x^re^{-2x^{1/4}}dx
\leq\frac{X^{r+1}}{r+1}.
\]

Therefore

\[
0\leq\frac{d_r(X)}{\mu_r}
\leq
\frac{2^{4r+4}X^{r+1}}{4(r+1)(4r+3)!},
\]

which decays superexponentially in \(r\). Thus compact deletion is negligible relative to each high raw moment.

## Translation

After restricting to \([X,\infty)\), the coordinate change \(y=x-X\) leaves off-diagonal Jacobi coefficients unchanged and subtracts \(X\) from diagonal coefficients. This statement compares a measure with its translate; it does not compare the truncated measure to the original full measure.

## Missing promotion

Entrywise high-moment proximity does not imply recurrence-coefficient proximity. Gram--Schmidt at degree \(n\) depends on the entire Hankel block \(\mu_0,\ldots,\mu_{2n}\), including low moments whose truncation error is fixed and non-negligible. Hankel inversion can amplify perturbations when conditioning deteriorates.

## Disposition

Resolve the raw-moment comparison: compact deletion is superexponentially small at the high-moment saddle. Defer recurrence transfer to `compact-truncation-jacobi-stability`, which requires a theorem controlling Jacobi coefficients under this determinate low-moment perturbation inside an indeterminate moment problem.

## Claim boundary

This packet proves no asymptotic equality of shifted and unshifted Jacobi coefficients. It isolates why the plausible moment argument is insufficient.
