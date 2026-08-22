# The centered Xi jet interval-certifies boundary curvature

A directed order-13 Taylor jet in `q=s-1/2` now constructs the odd completed
logarithmic derivative, divides its odd coefficients by `2q`, and obtains the
analytic `t=q^2` series for `ell'(t)` through degree five.

The calculation uses 90-digit directed Decimal arithmetic, depth-300 Euler
transformation, recurrence-1000 digamma asymptotics, and the uniform eta and
gamma derivative remainder bounds. Every reflection-forced even coefficient
of `Xi'/Xi` through order 12 contains zero, providing an internal parity audit.

Propagating the certified `ell'` coefficients through
`F=(4t-1)ell'` and `H=(F')^(-1/2)` gives

\[
 H''(0)\in[
 -3.6043843454074989143080918603593844492971912180589057403802055\cdot10^{-5},
 -3.6043843454074989143080918603593844492971912180586644683357620\cdot10^{-5}],
\]

and

\[
 H'''(0)\in[
 4.4659254461191263470862653302869309503795402937296593\cdot10^{-7},
 4.4659254461191263470862653302869309503795402937302765\cdot10^{-7}].
\]

Thus the source is strictly reciprocal-slope concave at the central boundary,
with a small positive third derivative.

## Final arithmetic defect caught by parity

The Euler denominator accumulator was initially a Decimal repeatedly doubled
under the process-default context. Once `2^k` exceeded that context's exact
precision, high Taylor coefficients were corrupted and reflection-forced even
intervals missed zero. Replacing it with a Python integer makes every Euler
denominator exact; all parity boxes then close.

This certifies curvature only at `t=0`, not throughout a positive-width cell.
The next step is an interval remainder/oscillation bound extending the boundary
jet over `[0,3*10^-8]`, followed by the remaining central cells. It does not
prove RH.

## Durable verification

- Checker: `checkers/central_xi_log_even_series_interval.py`
- Result: `results/central-xi-log-even-series-interval.json`
