# Geometric panels give a self-contained negligible Gauss remainder

## Question

Can the geometric frequency panels support an analytic Gauss--Legendre remainder smaller than the \(10^{-5}\) Arb entry radius?

## Claim boundary

Yes by an enormous margin. A self-contained Chebyshev approximation argument supplies the Gauss error estimate, and elementary recurrence plus Binet bounds supply a deliberately coarse integrand envelope. This closes frequency quadrature but not concentration-projector enclosure.

## Analytic domains

Use Bernstein parameter

\[
\rho=2
\]

on every affine panel with positive edges

\[
0,1,2,4,8,16,32,64,128,250
\]

and their reflections.

For the central panel \([0,1]\), the ellipse has imaginary semiaxis \(3/8\), strictly below the nearest digamma pole at imaginary frequency \(1/2\). For every panel \([a,2a]\) with \(a\geq1\), its leftmost real coordinate is \(7a/8>0\); hence the ellipse does not meet the imaginary-axis digamma poles. The final panel \([128,250]\) has the same separation property.

## Conservative integrand envelope

Across these ellipses the maximum imaginary frequency height is \(45.75\). For unit \(L^2(-L,L)\) vectors, Cauchy--Schwarz gives

\[
|\widehat f(u)\widehat g(-u)|
\leq
\frac{L}{\pi}e^{2L|\operatorname{Im}u|}
<10^{15}.
\]

Also,

\[
|\cos(u\log2)|<10^{15}.
\]

For digamma, every ellipse stays at least \(1/16\) away from a pole after the change of variable \(z=1/4+iu/2\). Shifting by the recurrence

\[
\psi(z)=\psi(z+24)-\sum_{k=0}^{23}\frac1{z+k}
\]

puts the argument \(w=z+24\) in \(\operatorname{Re}w\geq11/8\), with \(|w|<160\). Binet's representation and

\[
|t^2+w^2|
=|t+iw||t-iw|
\geq(\operatorname{Re}w)^2
\]

give

\[
|\psi(w)|
\leq
|\log w|+\frac1{2|w|}
+
\frac1{12(\operatorname{Re}w)^2}
<11.
\]

Bounding each of the twenty-four recurrence reciprocals by \(16\) yields \(|\psi(z)|<395<10^6\).

Thus the full bilinear integrand is bounded by

\[
M=10^{32}.
\]

The slack absorbs normalization constants and is sufficient without optimizing any factor.

## Self-contained Gauss remainder

For a function analytic on the Bernstein ellipse, Cauchy's estimate gives Chebyshev coefficients

\[
|a_k|\leq2M\rho^{-k}.
\]

Its degree-\((2n-1)\) truncation therefore has uniform error at most

\[
\frac{2M\rho^{-2n}}{1-\rho^{-1}}.
\]

Both integration on \([-1,1]\) and the positive \(n\)-node Gauss rule have norm \(2\), and Gauss is exact through degree \(2n-1\). Their difference is consequently bounded by four times the displayed approximation error. After affine scaling, the half-lengths of all reflected panels sum to \(250\). With \(n=160\), \(\rho=2\), and \(M=10^{32}\), the summed entrywise frequency-quadrature remainder is bounded by

\[
1.873\times10^{-61}.
\]

This is negligible compared with the Arb radius \(10^{-5}\).

## Numerical cross-check

The composite Schur scout gives maximum entry changes

\[
1.76\times10^{-7}
\]

from \(160\) to \(220\) nodes per half-panel and

\[
2.12\times10^{-7}
\]

from \(220\) to \(280\). Their nonmonotone order indicates a numerical floor around \(10^{-7}\), not resolved quadrature decay. All least Schur values remain near \(0.004470\).

## Disposition

Frequency quadrature is bounded without an external Gauss theorem: exactness, positivity of Gauss weights, and Chebyshev truncation suffice. The remaining continuum-to-matrix arrow is concentration-projector enclosure and propagation of that enclosure through the generalized Schur construction. No positivity promotion or RH implication is asserted.

## Verification

- `research/voevodsky/checkers/check_bernstein_gauss_budget.py`
- `research/voevodsky/checkers/scout_composite_frequency_schur.py`
- `research/voevodsky/results/bernstein_gauss_budget.json`
