# The order-four corner has a half-million-term finite prefix

The `5x5` corner requires moments through `A_9` and eta derivatives through
order ten. Exact derivative-sign search moves the threshold to `log N>13`.
Choosing `N=500000`, with `13<log N<14`, and ten Euler transforms proves

\[
 P_{m,j}(13)>0\quad(m=10,11;\ 0\le j\le10)
\]

and bounds every required tail below `6e-50`.

The architecture continues, but direct prefix cost has grown from ten
thousand terms at order two to one hundred thousand at order three and half a
million at order four. Future corners should cache a certified logarithm table
or replace repeated prefixes with a reusable rigorous quadrature certificate.

## Scope

This certifies the order-ten tail only, not the eta jet, `5x5` localizers, or
next Ritz estimate.

## Durable verification

- Checker: `checkers/eta_order_ten_tail_bound.py`
- Result: `results/eta-order-ten-tail-bound.json`
