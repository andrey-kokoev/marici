# The canonical Jacobi grid suppresses the first shift

## Question

Does the canonical monic degree indexing support a nonzero coefficient \(a_1\) in

\[
a_n=A n^4\left(1+\frac{a_1}{n}+O(n^{-2})\right)?
\]

A 500-digit Gram--Schmidt grid through degree sixteen fits \(a_n/n^4\) on degrees six through thirteen and tests degrees fourteen through sixteen. Successive inverse-degree models give

\[
a_1=-4.12\times10^{-2},
\quad -3.69\times10^{-3},
\quad -4.98\times10^{-6},
\]

at orders one, two, and three. Their holdout errors fall from \(6.11\times10^{-2}\) to \(1.42\times10^{-3}\) and then \(8.67\times10^{-7}\). The higher-order fit therefore strongly supports \(a_1=0\), with leading constant \(A\approx189.0727\).

## Disposition

Resolve the finite diagnostic in favor of vanishing canonical first shift. Combined with the conditional branch calculation, this restores six as the candidate leading defect-correction coefficient.

The next leaf is `jacobi-first-shift-analytic-zero`: derive \(a_1=0\) from the fixed-start Freud/string equations or another valid large-degree theorem.

## Claim boundary

Regression does not prove exact vanishing. The leading constant and higher coefficients remain finite-grid estimates, and the defect argument still requires selection of the \(p=-1\) branch.
