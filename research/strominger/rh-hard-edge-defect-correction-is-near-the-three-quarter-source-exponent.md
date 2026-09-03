# The hard-edge defect correction is near the three-quarter source exponent

## Question

Which inverse-power correction best describes

\[
2-n^2\varepsilon_n?
\]

Training on degrees six through thirteen and holding out fourteen through sixteen gives a free fitted exponent

\[
\delta=0.785.
\]

Among fixed candidates, \(3/4=1-\beta\) predicts best, with holdout error \(0.0148\), compared with \(0.0325\) for \(2/3\), \(0.0691\) for \(1/2\), and \(0.0363\) for \(1\). The free exponent has error \(0.00743\).

## Disposition

The finite grid favors

\[
n^2\varepsilon_n
=2-c_Xn^{-\delta}+o(n^{-\delta}),
\qquad
\delta\approx0.785,
\]

with the source exponent \(1-\beta=3/4\) as the leading analytic candidate. Do not identify them without a remainder theorem.

The next leaf is `hard-edge-three-quarter-source`: derive or reject the \(n^{-(1-\beta)}\) correction from the Weibull Jacobi coefficient asymptotics.

## Claim boundary

Finite holdout selection neither proves the limit two nor fixes the correction exponent.
