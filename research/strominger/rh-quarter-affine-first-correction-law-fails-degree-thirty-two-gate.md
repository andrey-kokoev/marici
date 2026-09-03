# Quarter affine first-correction law fails the degree-thirty-two gate

## Problem

The sign profile suggested the exact normalized correction law

\[
\frac{B_a}{T_a}=rac{29-19a}{24}.
\]

## Bold conjecture

The formula holds for shifts zero through six.

## Named rivals

The rivals are a nearby nonaffine shift profile, finite-window leakage from higher corrections, and an affine law with different intercept or slope.

## Risky consequences

Across nested cubic-correction fits, the latest maximum absolute residual must be below \(0.005\), improve with the lower cutoff, and preserve the predicted signs.

## Strongest falsification attempt

The maximum residual decreases from \(0.03559\) on the degree-ten window to \(0.01625\) on the degree-eighteen window, and every predicted sign is correct. However, \(0.01625\) fails the declared \(0.005\) gate. The failure is largest at high shift, where higher-order contamination is also largest.

## Disposition

Do not recognize the affine formula. The finite data preserve its sign prediction and show residual improvement, so they do not yet discriminate an incorrect formula from slow convergence. The next executable leaf is `quarter-shifted-affine-law-degree-forty-eight-stress-test`, extending recurrence degree and nested cutoffs to determine whether the maximum residual crosses the fixed \(0.005\) gate.

## Claim boundary

Failure of this finite gate is not a proof that the formula is false. The already established sign profile survives independently of the exact affine candidate.
