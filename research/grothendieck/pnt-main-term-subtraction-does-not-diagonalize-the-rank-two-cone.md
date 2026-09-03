# PNT main-term subtraction does not diagonalize the rank-two cone

## Question

Does splitting the prime measure into its continuum PNT density and arithmetic fluctuation produce separately positive rank-two blocks?

## Source split

The continuum prime model is

\[
P_{\rm cont}(t)
=-\frac12e^{t/4}\bigl(1+\operatorname{erf}(\sqrt t/2)\bigr).
\]

Write the remainder source as

\[
\Gamma+P
=(\Gamma+P_{\rm cont})+(P-P_{\rm cont}).
\]

The first term combines the archimedean kernel with mean prime density; the second is the arithmetic fluctuation around the PNT main term.

## Rank-two scan

At `(t,h)=(0.001,0.001)`, the archimedean-plus-continuum determinant is positive, approximately `0.200625`, and dominates. The fluctuation determinant is about `8.47e-7`, but their cross term is negative, approximately `-0.00210`.

At `(0.01,0.005)`,

\[
D_2^{\Gamma+P_{\rm cont}}\approx1.216\times10^{-6},
\]

while

\[
D_2^{P-P_{\rm cont}}\approx-1.170\times10^{-5}.
\]

The positive total `1.353e-4` is supplied by a cross term of approximately `1.458e-4`.

At `(0.05,0.01)`, both diagonal pieces are negative:

\[
D_2^{\Gamma+P_{\rm cont}}\approx-6.317\times10^{-6},
\qquad
D_2^{P-P_{\rm cont}}\approx-7.064\times10^{-6}.
\]

Their cross term is approximately `1.3457e-5`, leaving the small positive total `7.553e-8`.

## Consequence

Subtracting the PNT main density explains endpoint-scale cancellation but does not diagonalize the Hankel cone. In the larger-heat sample, neither the mean-completed archimedean block nor the prime fluctuation block is rank-two positive. Their coupling remains essential.

Thus a proof based on

\[
R=R_{\Gamma+P_{\rm cont}}\oplus R_{P-P_{\rm cont}}
\]

is ruled out by the same first nonlinear gate as the raw gamma/prime split.

## Relation to large-heat asymptotics

This matches the prior saddle analysis: the PNT main term cancels exponential endpoint growth only to algebraic scale. The much smaller completed heat scale resides in correlated gamma and arithmetic fluctuations. The determinant cone detects that correlation already at rank two.

## Boundary

The scan is uncertified. The continuum formula is exact, the prime cutoff tail is negligible on these boxes, and gamma finite evaluation remains the certification residual.

## Disposition

Retain PNT subtraction for asymptotic bookkeeping, not as a positive Gram decomposition. Any viable source factor must couple the archimedean completion and prime fluctuation beyond their mean-density split.