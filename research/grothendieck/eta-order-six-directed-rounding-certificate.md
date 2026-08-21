# Certified eta input jet for the order-two corner

The directed-rounding eta evaluator has been extended through derivative
order six. It retains the 9,999-term prefix, uses the separately proved
15-transform Euler tail at `N=10000`, and outwardly enlarges every derivative
by `2e-52`. Correctly rounded 80-digit decimal logarithms and directed
arithmetic enclose all finite operations.

All seven eta-derivative intervals have width below `5e-52`. This is ample for
the earlier `10^-12` localizer robustness scale and supplies every regular
Dirichlet input needed to derive `A_0,...,A_5`.

The remaining step is deliberately algebraic: construct the Laurent-free
completed logarithmic derivative as a truncated interval series, substitute
`x-1/4=e+e^2`, invert that substitution, and read off the six moments. This
generic route prevents sign or Faà di Bruno mistakes in hand formulas.

## Scope

This certifies the eta jet through order six, not yet the order-two moment
matrices and not RH.

## Durable verification

- Checker: `checkers/eta_order_six_decimal_interval.py`
- Result: `results/eta-order-six-decimal-interval.json`
