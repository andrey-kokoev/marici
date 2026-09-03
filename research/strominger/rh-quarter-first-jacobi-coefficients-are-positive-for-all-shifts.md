# First quarter Jacobi coefficients are positive for all shifts

## Question

Can finite numerical Jacobi positivity be promoted to an exact statement uniform in the source shift?

## Claim boundary

The result covers \(\alpha_0\), \(\alpha_1\), and \(\beta_1\). It does not provide a formula or induction for arbitrary Jacobi order.

## Disposition

Exact polynomial arithmetic derives the five rational functions

\[
\alpha_0,
\quad 1-\alpha_0,
\quad \beta_1,
\quad \alpha_1,
\quad 1-\alpha_1.
\]

After a common positive sign normalization, every numerator and denominator has strictly positive monomial coefficients in \(a\). Therefore, for every real \(a\geq0\),

\[
0<\alpha_0(a),\alpha_1(a)<1,
\qquad \beta_1(a)>0.
\]

This is an all-shift low-order theorem, stronger than grid testing. The next leaf is `quarter-cross-ratio-second-jacobi-coefficient-pattern`, testing whether the same coefficientwise certificate extends to \(\alpha_2\) and \(\beta_2\).
