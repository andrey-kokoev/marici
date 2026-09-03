# Quarter shifted first correction explains the monotonicity flip

## Problem

The scaled cross-ratio profiles reverse convergence direction between shifts one and two.

## Bold conjecture

For fixed shift \(a\), the expansion

\[
n^2\Theta_{n,a}=T_a+\frac{B_a}{n}+O(n^{-2})
\]

has \(B_a>0\) for \(a=0,1\) and \(B_a<0\) for \(a=2,\ldots,6\).

## Named rivals

The rivals are a fit-induced sign change, sign instability under nested windows, and monotonicity controlled by higher corrections rather than \(B_a\).

## Risky consequences

Cubic inverse-degree fits on three nested windows must retain the same sign at each shift and place the sign boundary between one and two.

## Strongest falsification attempt

Exact recurrence data through degree thirty-two were fitted on windows beginning at degrees ten, fourteen, and eighteen. Every fit gives positive \(B_a\) at shifts zero and one and negative \(B_a\) at shifts two through six. The signs are stable across all nested windows, and the fitted limits remain positive and shift-dependent. All five gates passed.

## Disposition

Retain the first-correction sign profile as the finite explanation of the monotonicity split. The normalized coefficients \(B_a/T_a\) suggest the risky affine rival

\[
\frac{B_a}{T_a}=\frac{29-19a}{24},
\]

which predicts the observed sign boundary. The next leaf is `quarter-shifted-first-correction-affine-law`, testing this formula against every shift and nested window.

## Claim boundary

Regression does not prove the expansion or the affine formula. Higher-order contamination grows with shift, so only the stable sign pattern is retained here.
