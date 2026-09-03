# Quarter Y-system forces the affine slope but not the intercept

## Problem

Finite fits recognized an affine normalized first correction but did not show which coefficients follow from the exact recurrence.

## Bold conjecture

The shifted condensation recurrence forces the candidate slope \(-19/24\) once the shifted amplitude has second difference \(5/12\).

## Named rivals

The rivals are a residual polynomial prefactor in the recurrence, a different coefficient balance, and determination of the full affine law including its intercept.

## Risky consequences

The exact cross ratios must satisfy a coefficient-free Y-system. Substitution of

\[
x_{n,a}=T_a n^{-2}\left(1+\frac{u_a}{n}+O(n^{-2})\right)
\]

must yield a two-shift constraint compatible with the fitted profiles.

## Strongest falsification attempt

Exact rational checks verify 50 Y-system instances. Expansion gives

\[
u_{a+2}-u_a+2=T_a-2T_{a+1}+T_{a+2}.
\]

Degree-forty-eight fits have amplitude second differences within \(0.00104\) of \(5/12\), two-step correction differences near \(-19/12\), and balance residuals below \(0.005\). All six gates passed.

## Disposition

Promote the exact Y-system and conditional coefficient balance. If the amplitude second difference is \(5/12\), the affine slope is \(-19/24\). The recurrence at this order does not fix the intercept and permits a parity mode. The next leaf is `quarter-shifted-amplitude-quadratic-law`, testing the required amplitude curvature independently.

## Claim boundary

The asymptotic expansion and amplitude curvature remain finite recognitions. The exact Y-system alone does not prove either, nor does it establish the proposed intercept \(29/24\).
