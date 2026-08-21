# The order-three corner crosses the first prefix threshold

The `4x4` Hausdorff corner requires `A_6,A_7` and eta derivatives through
order eight. At the previous logarithmic threshold `log N>9`, no transform
depth through 100 makes all required derivative-sign polynomials positive.
This is the first genuine scaling change in the finite certification program.

Raising the prefix to `N=100000`, so `11<log N<12`, restores the theorem with
only eight Euler transforms. Exact rational evaluation proves

\[
 P_{m,j}(11)>0\quad(m=8,9;\ 0\le j\le8).
\]

Consequently

\[
 |R_j|\le\frac{8!P_{8,j}(12)}{2^8 100000^9}<4\,10^{-36}
\]

for every required eta derivative. The cost increase is therefore a tenfold
finite prefix, not a loss of rigorous acceleration. This predicts an
approximately linear transcendental-evaluation cost for the next corner.

## Scope

This certifies the order-eight tail architecture only. It does not yet compute
`A_6,A_7` or the `4x4` determinants.

## Durable verification

- Checker: `checkers/eta_order_eight_tail_bound.py`
- Result: `results/eta-order-eight-tail-bound.json`
