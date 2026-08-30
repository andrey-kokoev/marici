# Directed-rounding certificate for the regular eta jet

For each `0<=j<=4`, the checker encloses the first 9,999 terms of

\[
 \eta^{(j)}(1)=(-1)^j\sum_{n\ge1}(-1)^{n-1}\frac{(\log n)^j}{n},
\]

then applies 60 Euler transforms at `N=10000`. `Decimal.ln` supplies a
correctly rounded center; adjacent 80-digit decimals enclose the exact log.
Every arithmetic operation is rounded separately downward and upward. The
independently proved `<10^-100` Euler remainder is added symmetrically.

All five derivative boxes have width below `10^-70`. They use no zero
locations and no imported Stieltjes constants. The next composition is the
interval triangular reconstruction of `gamma_0,...,gamma_3`, followed by the
completed `l_j` formulas and the existing localizer robustness calculation.

## Scope

This relies on Python Decimal's correct-rounding contract for logarithm. It
certifies the eta jet, not yet the composed determinant and not RH.

## Durable verification

- Checker: `checkers/eta_jet_decimal_interval.py`
- Result: `results/eta-jet-decimal-interval.json`
