# Quarter D positive-real programme

## Question

Can the D-condensation family be proved uniformly Hurwitz stable through a positive-real certificate rather than finite source-size enumeration?

## Problem

Retained exact checkers exhibit positive Gram diagonals for bounded Cayley pairs, but no recurrence yet proves those diagonals positive at arbitrary condensation depth.

## Bold conjecture

**The D condensation identity induces a positive recurrence for every diagonal coefficient of the Cayley Gram polynomial, yielding a uniform positive-real certificate.**

## Named rivals

1. Positivity is bounded and eventually fails.
2. The Gram diagonals stay positive but no coefficientwise recurrence exists; a nondiagonal KYP certificate is required.
3. Positive-realness holds only after source-specific cancellations not preserved by condensation.

## Risky consequences

A valid recurrence must reproduce every retained exact Gram coefficient, preserve strict positivity without finite-depth assumptions, handle the unit-feedthrough degree drop, and imply the endpoint Hurwitz minors used by the network construction.

## Strongest falsification attempt and exact residual

Retained checker `checkers/rh_quarter_D_positive_real_diagonal_gram.py` independently reconstructs 21 exact diagonal Gram certificates. Retained counterexample `checkers/rh_TP2_signed_autocorrelation_counterexample.py` rejects generic log-concavity plus TP2 as sufficient. Retained shell-majorization checkers reject local and directional shell matching in 1,026 of 1,092 profiles. The exact residual is the absent all-depth recurrence or KYP factorization for the Gram diagonals.

## Disposition

The bounded positive-real claim survives independently executable retained evidence. Uniform positivity remains open. Continue only with a source-derived Gram recurrence or nondiagonal KYP factorization; do not revive deleted recursive-DPC outputs or further shell-order variants.

## Claim boundary

This programme packet relies only on retained post-correction checkers. It does not reinstate deleted artifacts, validate superseded graph events, or prove an all-order Hall inequality.
