# Certified eta input jet for the order-four corner

A one-pass 90-digit evaluator encloses `eta^(j)(1)` for `0<=j<=10`. It
computes 499,999 logarithms once each, generates powers iteratively, and
applies ten Euler transforms at `N=500000`. The exact tail theorem is included
as a symmetric `6e-50` enclosure.

Every derivative interval has width at most `1.2e-49`, dominated by the tail
box rather than prefix rounding. The run completes in about 43 seconds on the
current workstation and is not restart-sensitive.

All regular input for `A_8,A_9` is certified. Degree-nine series composition
and the three `5x5` determinants are next.

## Scope

This certifies the eta jet, not the order-four localizers or RH.

## Durable verification

- Checker: `checkers/eta_order_ten_decimal_interval.py`
- Result: `results/eta-order-ten-decimal-interval.json`
