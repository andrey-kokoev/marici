# Direct Hankel ratios resolve a finite one-over-n coefficient

## Question

Does the directly computed compact-truncation determinant ratio support the \(1/n\) term inferred from recurrence coefficients?

At \(q=12\), 260-digit monic norms reconstruct

\[
L_n=\log(D_n^{(X)}/D_n)
\]

through \(n=12\). Fits to

\[
L_n=\alpha n+\beta+\gamma/n+\delta/n^2
\]

over windows \(3\!:\!12\) through \(6\!:\!12\) give \(\gamma\) decreasing from \(0.09093\) to \(0.09013\), with fit residuals decreasing to \(1.64\times10^{-8}\). The independent second-difference proxy at \(n=11\) is \(0.08914\).

## Disposition

Complete the direct finite determinant-ratio test. The \(1/n\) coefficient is supported independently of fitting recurrence ratios, and its value is consistent with the off-diagonal \(n^{-3}\) proxy.

The next leaf is `hankel-gamma-tail-start-law`: determine how \(\gamma_X\) depends on the compact truncation start and whether that dependence permits moving-start uniformity.

## Claim boundary

Finite determinant fits do not prove the expansion. The fitted linear term depends on measure normalization; only second differences and the inverse-power coefficients are relevant to recurrence comparison.
