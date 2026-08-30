# Certified eta input jet for the order-three corner

The eta evaluator now encloses derivatives through order eight. It makes one
pass over the 99,999-term prefix and reuses each correctly rounded logarithm
for all nine powers. Eight Euler transforms at `N=100000` close the tail, with
the separately proved `4e-36` bound added outwardly.

Every derivative interval has width below `9e-36`. The larger width than the
order-six certificate is intentional and dominated by the conservative tail
box; it remains vastly narrower than any observed moment scale. No zero
locations or tabulated Stieltjes constants enter.

The full regular analytic input for `A_6,A_7` is therefore certified. The next
step is to parameterize the generic completed-series engine at degree seven
and evaluate the three `4x4` localizer determinants.

## Scope

This certifies the eta jet, not yet the order-three determinants and not RH.

## Durable verification

- Checker: `checkers/eta_order_eight_decimal_interval.py`
- Result: `results/eta-order-eight-decimal-interval.json`
