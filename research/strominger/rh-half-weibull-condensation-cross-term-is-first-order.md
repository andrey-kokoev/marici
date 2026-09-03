# The half-Weibull condensation cross term is first order

## Question

Can the negative cross-minor term in the staircase condensation recurrence be discarded at leading asymptotic order?

Define its fraction of the positive first term by

\[
\theta_n(a,b)=
\frac{ab\,S_{n-1}(a+1,b+1)^2}
{(a+n-1)(b+n-1)S_{n-1}(a,b)S_{n-1}(a+2,b+2)}.
\]

For the source parameters \((a,b)=(1,3/2)\), exact rational determinants give \(0<\theta_n<1\) and monotone decay. However,

\[
n\theta_n=0.3388,
0.3314,
0.3250,
0.3193,
0.3143
\]

for \(n=10,\ldots,14\). Moreover,

\[
n\left(n\theta_n-\frac14\right)
\approx0.89,\ldots,0.90,
\]

so the finite grid supports

\[
\theta_n=rac1{4n}+O(n^{-2}).
\]

Consequently

\[
\log(1-	heta_n)
=-\frac1{4n}+O(n^{-2}),
\]

which contributes at the same order needed to determine logarithmic free-energy coefficients.

## Disposition

Reject dominant balance that discards the cross minor. The next leaf is `half-weibull-cross-ratio-quarter`: prove \(n\theta_n\to1/4\) and its remainder, then retain this term in the condensation asymptotic.

## Claim boundary

The limit \(1/4\) is a finite-grid candidate. Positivity proves only \(0<\theta_n<1\), not its rate.
