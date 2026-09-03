# Quarter monotonicity reduces to a Neville-pivot curvature bound

## Question

What quantitative inequality beyond strict total positivity is exactly equivalent to degree monotonicity of the shifted cross ratios?

## Claim boundary

The reduction is exact at every degree and shift. The curvature inequality itself has only been verified on a finite grid.

## Disposition

Let

\[
P_{n,a}=\frac{D_{n,a}}{D_{n-1,a}}>0
\]

be the leading Gaussian–Neville pivot. Then

\[
\frac{\Theta_{n+1,a}}{\Theta_{n,a}}
=
\frac{P_{n,a+1}^2}{P_{n,a}P_{n,a+2}}
\bigg/\frac{q_a(n)}{q_a(n-1)}.
\]

Thus strict degree monotonicity is equivalent to

\[
\frac{P_{n,a+1}^2}{P_{n,a}P_{n,a+2}}
<\frac{q_a(n)}{q_a(n-1)}.
\]

All 377 exact cases satisfy the identity and bound. Total positivity supplies positive pivots but not this upper bound. The next leaf is `quarter-pivot-curvature-gap-newton`, clearing denominators and testing whether the resulting gap polynomial has an all-shift Newton positivity certificate at bounded degrees.
