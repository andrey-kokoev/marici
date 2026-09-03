# Quarter positivity is not a generic recurrence invariant

## Question

Can positivity of the determinant recurrence and the bound \(0<x_{n,a}<1\) be proved from positive recurrence boundary data alone?

## Claim boundary

The test separates the source unit boundary from arbitrary positive boundary profiles. Finite verification of the source profile is not a general positivity proof.

## Disposition

For the source unit boundary, 312 exact cases through degree twenty-five and shift twelve have positive recurrence values and cross ratios strictly between zero and one. Generic positivity is false: the positive boundary profile

\[
R_{1,a}=1,
\qquad R_{1,a+1}=100,
\qquad R_{1,a+2}=1
\]

produces the negative degree-two numerator \(-524505/16\). Therefore positivity is not a recurrence invariant of arbitrary positive data. A proof must use determinant-specific total positivity or stronger source inequalities. The next executable leaf is `quarter-determinant-total-positivity-test`, which tests minors of the source matrix rather than abstract recurrence data.
