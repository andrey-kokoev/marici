# One real theta inequality proves the centered unit disk is zero-free

Use the positive Riemann theta kernel in the normalization

\[
 \Xi\left(\frac12+q\right)=
 \int_0^\infty\Phi(u)\cosh(qu)\,du,
 \qquad \Phi(u)>0.
\]

For every complex `q` with `|q|<=1`, the power series of cosh and positivity
give

\[
 |\cosh(qu)-1|\le\cosh(u)-1.
\]

Consequently

\[
 \left|\Xi(1/2+q)-\Xi(1/2)\right|
 \le\Xi(3/2)-\Xi(1/2).
\]

If

\[
 \boxed{\Xi(3/2)<2\Xi(1/2),}
\]

then the variation is strictly smaller than the nonzero constant
`Xi(1/2)`. Rouché's theorem proves that `Xi(1/2+q)` has the same number of
zeros as that constant on `|q|<1`: none.

A zero-free eta/gamma evaluation gives approximately

\[
 \Xi(1/2)=0.4971208,\qquad \Xi(3/2)=0.5087310\ldots,
\]

with a Rouché margin near `0.4855`, so the inequality is extraordinarily loose.
The next step is a directed interval evaluation at these two real arguments;
no complex interval covering is needed for analyticity.

This reduction and its implication are exact, but the displayed numerical
comparison is not yet interval-certified. It uses no zero locations and does
not prove the separate bound `|F'|<=20`, continuum concavity, or RH.

The comparison is now certified by coarse directed eta and elementary gamma
bounds, with margin greater than `0.1189`. See
`xi-centered-unit-disk-Rouche-certificate.md`.

## Durable verification

- Checker: `checkers/xi_centered_unit_disk_rouche.py`
- Result: `results/xi-centered-unit-disk-rouche.json`
