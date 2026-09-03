# Fixed-cutoff refinement stabilizes the positive truncated Schur form

## Problem

Does the positive range-compatible Schur value at frequency cutoff \(250\) survive independent spatial and frequency quadrature refinement?

## Bold conjecture

After the cutoff reaches \(250\), the truncated Schur form is positive and its sign is not a Nyström-resolution or pseudoinverse-threshold artifact.

## Named rivals

1. Spatial refinement changes the sign.
2. Tightening the pseudoinverse tolerance changes the sign.
3. Increasing the frequency cutoff changes the sign.
4. Numerical failure of range compatibility invalidates the generalized Schur complement.

## Risky consequences

At fixed cutoff, all reported Schur values and tail spectral ranks should agree under refinement. At larger cutoff, every tolerance should remain positive and range residuals should remain small relative to the observed margin.

## Strongest falsification attempt

At cutoff \(250\), refinement from \((n_x,n_u)=(480,1800)\) to \((560,2200)\) changed the central-tolerance least Schur value only from

\[
0.00656925696
\]

to

\[
0.00657319546.
\]

The positive tail rank remained \(44\), and the range residual remained \(8.24465\times10^{-7}\). Across relative pseudoinverse tolerances \(10^{-8},10^{-10},10^{-12}\), the refined least values were

\[
0.00898010,
\qquad
0.00657320,
\qquad
0.00446900.
\]

At cutoff \(350\), the corresponding values were

\[
0.01379213,
\qquad
0.00967181,
\qquad
0.00785498.
\]

All were positive. At the tightest tolerance, the range residual was approximately \(2.98\times10^{-7}\), more than four orders below the least Schur value.

The cutoff-\(150\), tolerance-\(10^{-12}\) negative value remains the explicit truncation counterexample and prevents promotion based on low cutoffs.

## Exact residual

The frequency tail beyond \(350\) is omitted, no quadrature error is enclosed, and the pseudoinverse nullspace is numerical rather than interval-certified. The larger central-tolerance residual at cutoff \(350\) reflects extra near-null tail modes; tightening the tolerance reduces it while preserving positivity.

## Disposition

The conjecture survives all registered tests at cutoffs \(250\) and \(350\). The positive sign is stable under fixed-cutoff refinement and three pseudoinverse tolerances. This is discovery-level evidence for positivity of the truncated first-prime Schur form, not a certificate for the continuum operator and not an RH implication.

The next discriminating test is the direct spectrum of each full discretized truncated operator. Agreement with the Schur test would eliminate pseudoinverse construction as the source of the positive sign. Continuum promotion would still require interval quadrature and tail enclosures.
