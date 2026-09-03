# Second quarter Jacobi coefficients are positive for all shifts

## Question

Does the monomial-coefficient certificate extend to \(\alpha_2\) and \(\beta_2\)?

## Claim boundary

The result covers Jacobi order two for every real source shift \(a\geq0\). It does not establish an arbitrary-order formula or induction.

## Disposition

Corrected exact Hankel determinant formulas give rational expressions for

\[
\alpha_2,
\quad 1-\alpha_2,
\quad \beta_2.
\]

Every numerator and denominator coefficient is strictly positive. Therefore

\[
0<\alpha_2(a)<1,
\qquad \beta_2(a)>0
\]

for all \(a\geq0\). An initially mis-indexed bordered determinant produced a false failed certificate; correcting its second and third minors restored agreement with the exact Jacobi construction and passed all gates. Direct expressions already reach degrees 1104 and 524, so blind order enlargement is stopped. The next leaf is `quarter-jacobi-positive-polynomial-induction`, seeking a structural recurrence that preserves coefficientwise positivity.
