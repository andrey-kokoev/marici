# The diagonal truncation grid prefers an integer inverse-degree expansion

## Question

Does a fixed inverse-degree correction predict unseen coefficients better than a free fractional exponent?

Using degrees four through ten for training and eleven through twelve as holdout, compare

\[
s_n=C+d/n,
\qquad
s_n=C+d/n+e/n^2,
\qquad
s_n=C+d n^{-\delta},
\]

where \(s_n=n^3(b_n^{(X)}/b_n-1)\).

The holdout root-mean-square errors are respectively

\[
4.66\times10^{-4},
\qquad1.64\times10^{-5},
\qquad7.74\times10^{-5}.
\]

The integer two-correction model outperforms the free single-exponent model despite not fitting \(\delta\).

## Disposition

Select the integer inverse-degree expansion as the finite diagnostic model. Do not select its fitted constants as asymptotic coefficients. The next leaf is `inverse-degree-expansion-source`: derive or falsify such an expansion from the incomplete-gamma moment structure rather than regression.

## Claim boundary

The holdout has only two degrees. Predictive superiority on this grid is not proof of an asymptotic expansion or a uniform remainder.
