# Positive-frequency completion reduces certification to cutoff 250

## Question

Must a certification calculation integrate the corrected multiplier over the entire frequency line?

## Claim boundary

No. For \(|u|\geq100\), the corrected combined multiplier is nonnegative. Directed Arb subdivision now certifies this on \(100\leq|u|\leq10000\) with minimum lower margin \(0.8935\); the Binet bound covers the exterior region. Therefore the contribution omitted beyond a cutoff \(U\geq100\) is a nonnegative quadratic form. It suffices to certify positivity of the truncated form at one such cutoff. The stable \(U=250\) scout supplies a quantitative target, not a certificate.

## Monotone completion

Write

\[
q=q_U+r_U,
\]

where \(q_U\) contains the endpoint term and the multiplier integral over \([-U,U]\). For \(U\geq100\), the safe-cutoff theorem gives

\[
r_U(f)
=
\int_{|u|>U}
 m(u)|\widehat f(u)|^2du
\geq0.
\]

Consequently,

\[
q_U\geq0
\quad\Longrightarrow\quad
q\geq0.
\]

No numerical approximation to the infinite positive-frequency tail is required.

## Cutoff-250 target

At \(U=250\), the concentration threshold gap is

\[
\min\left(
\lambda_{25}-\frac1{130},
\frac1{130}-\lambda_{26}
\right)
\approx0.002364999.
\]

The tightest-tolerance refined Schur margin is

\[
\mu_{250}
\approx0.0044690003.
\]

Reserve a certified lower margin of \(0.001\). The combined admissible error in the Schur lower bound is then

\[
0.0034690003.
\]

The fixed-cutoff spatial-refinement change was approximately

\[
4.04\times10^{-6},
\]

but this is empirical and cannot be charged against the certificate budget without an analytic enclosure.

## Range residual

At tolerance \(10^{-12}\), the reported range residual is

\[
r\approx4.97\times10^{-8}.
\]

The former assertion \(C\geq1/40\) was too strong and is superseded. The certified concentration trace gives

\[
C\geq\alpha Q,
\qquad
\alpha=0.00486945765658\ldots,
\]

so the valid inverse factor is \(\alpha^{-1}=205.361678964\ldots\). The final directed residual calculation uses this larger factor and still passes all 25 \(LDL^*\) pivots.

## Certification obligations

A valid promotion at \(U=250\) must prove all of the following within the total budget \(0.003469\):

1. the concentration projection has rank \(25\) and remains separated by the displayed threshold gap;
2. the multiplier and endpoint matrix entries enclose the continuum form;
3. the generalized tail block is nonnegative and range-compatible;
4. the Schur eigenvalue enclosure has lower endpoint at least \(0.001\);
5. all spatial and frequency quadrature errors are included once.

The frequency region outside \([-250,250]\) requires only the already proved nonnegativity argument, not numerical integration.

## Disposition

The infinite-frequency requirement is removed. Certification is reduced to a bounded rank-\(25\), cutoff-\(250\) interval problem with an explicit error budget. No available interval backend or analytic Nyström remainder currently supplies those enclosures, so continuum positivity remains open.

## Verification

- `research/voevodsky/checkers/check_cutoff_250_certificate_budget.py`
- `research/voevodsky/results/cutoff_250_certificate_budget.json`
