# The quarter-disk gate tolerates a large omitted tail

Write `ell'(t)=sum a_n t^n` and `F'(t)=sum g_n t^n`, where

\[
 g_n=(n+1)(4a_n-a_{n+1}).
\]

The directed centered jet supplies `a_0,...,a_5`, hence `g_0,...,g_4`.
On `|t|<=1/4`, the triangle inequality gives

\[
 \left|\sum_{n=0}^4g_nt^n\right|
 \ge \inf g_0-\sum_{n=1}^4\sup|g_n|4^{-n}
 >0.0923826193.
\]

The desired disk gate asks only for `|F'|>=1/16=0.0625`. Therefore the entire
unknown tail may have supremum approximately `0.0298826193` and the gate still
closes. The known polynomial's radial variation is only about `7.48e-5`.

The next task is to bound `sup_|t|<=1/4 |sum_(n>=5) g_n t^n|` below this
allowance using a Cauchy/radius estimate for the centered Xi-log series. That
tail bound is not yet proved, so neither the disk gate nor continuum concavity
is established; RH remains open.

## Durable verification

- Checker: `checkers/central_F_prime_disk_polynomial_budget.py`
- Result: `results/central-F-prime-disk-polynomial-budget.json`
