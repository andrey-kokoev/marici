# Quarter no-log pivot remainder is not verified

## Problem

Unconditional transport of \(-7/2\) requires the normalized pivot remainder to contain no \((\log n)/n\) term.

## Bold conjecture

After subtracting the candidate pivot limit,

\[
\log A_n(\kappa)-\log A(\kappa)
=rac{b(\kappa)}n+O(n^{-2}),
\]

with zero logarithmic coefficient.

## Named rivals

The rivals are a genuine logarithmic remainder, contamination from finite-window error in the unproved limit \(A\), and instability caused by collinearity of \((\log n)/n\) and \(1/n\).

## Risky consequences

Direct fits through degree twenty-eight must place the logarithmic coefficient within \(0.03\) of zero at every tested ratio.

## Strongest falsification attempt

The fitted coefficients are \(0.04379,0.02901,-0.00205,-0.01357\). They change sign and remain below \(0.05\), but the first value fails the preregistered \(0.03\) gate. Thus the data neither establish zero nor resolve whether the residual comes from the remainder or from the fitted crossover limit.

## Disposition

Do not promote unconditional transport of \(-7/2\). Stop this branch at the first missing object: an independently proved pivot limit \(A(\kappa)\) with an error smaller than \((\log n)/n\). Its acceptance test is the same four-ratio coefficient gate after replacing fitted limits by the theorem. Reallocate to the independent executable leaf `quarter-pivot-curvature-two-proof`.

## Claim boundary

The failed zero gate is not evidence for a nonzero logarithmic term because the limit subtracted from the data is itself conjectural and finitely extrapolated.
