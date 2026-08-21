# Extremal Jacobi nodes give directional first-ordinate estimates

Assume the complete moments come from a positive measure `mu` on `[0,4]`.
Multiplication by `u` compresses to nested polynomial spaces, so

\[
 u_{\max}^{(n)}=\max_{\deg p\le n}\frac{\int u|p|^2d\mu}{\int|p|^2d\mu}
 \le u_{\max}^{(n+1)}\le\sup\operatorname{supp}\mu.
\]

If the top support point is present, polynomial density gives convergence to
it. Since `gamma(u)=sqrt(u^(-1)-1/4)` decreases,

\[
 \widehat\gamma_1^{(n)}\ge\widehat\gamma_1^{(n+1)}\ge\gamma_1.
\]

The source-derived sizes one through four give approximately

\[
 24.9452,\quad14.6084,\quad14.1520,\quad14.1351,
\]

strictly decreasing as predicted, without zero input. This turns the blind
match into a falsifiable convergence law for every newly certified corner.

## Scope

Finite principal-compression monotonicity is unconditional. Identifying the
limit with a Riemann ordinate requires the full positive-measure/RH
interpretation. Displayed eigenvalues are numerical, not interval-certified.

## Durable verification

- Checker: `checkers/quarter_point_extremal_ritz_convergence.py`
- Result: `results/quarter-point-extremal-ritz-convergence.json`
