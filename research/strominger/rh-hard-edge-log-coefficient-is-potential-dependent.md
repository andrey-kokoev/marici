# The hard-edge logarithmic coefficient is potential-dependent

## Question

Can the quarter-Weibull candidate \(+\alpha^2\log n\) be imported as a universal hard-edge term?

No. The exactly solvable Laguerre benchmark has \(\beta=1\) and

\[
w_\alpha(x)=x^\alpha e^{-2x}.
\]

Its monic recurrence coefficient is

\[
(a_n^{(\alpha)})^2=\frac{n(n+\alpha)}4,
\]

so

\[
\log\frac{(a_n^{(\alpha)})^2}{(a_n^{(0)})^2}
=\log\left(1+\frac\alpha n\right)
=\frac\alpha n-rac{\alpha^2}{2n^2}+O(n^{-3}).
\]

Therefore the relative Laguerre determinant free energy contains

\[
\frac{\alpha^2}{2}\log n,
\]

not \(\alpha^2\log n\). The logarithmic hard-edge coefficient cannot be transferred from \(\beta=1\) to \(\beta=1/4\) without deriving its dependence on the potential exponent.

## Disposition

Reject a universal \(+\alpha^2\log n\) hard-edge rule. Retain \(+\alpha^2\log n\) only as the quarter-Weibull finite-data candidate.

The next leaf is `beta-dependent-hard-edge-log-coefficient`: use exact generalized-gamma determinant families at several reciprocal-integer \(\beta\) to infer and then source the coefficient \(c(\beta)\) in

\[
\log\frac{D_n^{(\alpha)}}{D_n^{(0)}}
=\frac\alpha\beta n\log n+c(\beta)\alpha^2\log n+\cdots.
\]

## Claim boundary

The Laguerre benchmark falsifies universality but does not determine \(c(1/4)\). The quarter-Weibull value remains unproved.
