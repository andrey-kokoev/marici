# The fourth-order barrier region has a rational candidate boundary

## Question

What fourth-order coefficient values are supported by the truncated Weibull grid, and what barrier region would they imply?

Cubic inverse-degree extrapolation of degrees eight through sixteen gives

\[
r_3=-20.3683,
\qquad
e_4=12.9009,
\qquad
r_3+e_4=-7.4674.
\]

These support the rational candidates

\[
r_3=-\frac{163}{8},
\qquad
e_4=\frac{103}{8},
\qquad
r_3+e_4=-\frac{15}{2}.
\]

If these exact values hold, the fourth-order corrected-barrier slack is

\[
-8-r_3+2\kappa-2\kappa^2-2c-e_4
=-\frac12+2\kappa-2\kappa^2-2c.
\]

Its positive region is therefore

\[
c<-rac14+\kappa-\kappa^2.
\]

The finite profile \((\kappa,c)=(0.31,-1)\) lies well inside this region; its predicted fourth-order slack is \(1.9278\), near the observed \(1.85\).

## Disposition

Resolve the finite fourth-order candidate and barrier geometry. The next leaf is `weibull-rational-fourth-coefficients`: derive \(r_3=-163/8\) and \(e_4=103/8\) from the Jacobi asymptotic rather than regression.

## Claim boundary

The rational values are inferred from a short extrapolation and are not proved. The open-region inequality also needs a signed \(O(n^{-5})\) remainder for eventual barrier propagation.
