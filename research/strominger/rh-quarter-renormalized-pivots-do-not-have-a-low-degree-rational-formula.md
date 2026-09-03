# Quarter renormalized pivots do not have a low-degree rational formula

## Question

Can the product

\[
\prod_{j\geq1}\rho_j
\]

be evaluated by recognizing each \(\rho_j\) as a low-degree rational function of \(j\)?

Exact determinant arithmetic supplies \(\rho_j\) through \(j=13\). For each equal numerator and denominator degree from one through five, the unique rational interpolant was fitted on the first \(2d+1\) values and tested on every remaining value. Every holdout test failed exactly.

Thus no single rational function

\[
\rho_j=rac{P_d(j)}{Q_d(j)},
\qquad d\leq5,
\]

matches the exact sequence. In particular, the target \(208/1575\) is not explained by a low-degree termwise telescoping product of linear factors.

## Disposition

Reject the low-degree rational-interpolation route. The next leaf is `quarter-renormalized-product-barnes-asymptotic`: derive the product amplitude from a global determinant or Barnes-type constant instead of termwise pivot recognition.

## Claim boundary

The test excludes only equal-degree rational functions up to degree five. It does not exclude higher-degree, non-rational, recurrence-defined, or block-periodic formulas.
