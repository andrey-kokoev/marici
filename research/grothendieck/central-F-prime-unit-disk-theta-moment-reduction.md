# The unit-disk `F'` bound reduces to four real endpoint quantities

Put

\[
 Y(t)=\Xi(1/2+\sqrt t)=\sum_{n\ge0}b_nt^n,
 \qquad b_n>0,
\]

and `ell=log Y`. Theta-kernel positivity gives the positive coefficients. On
`|t|<=1`, it therefore gives

\[
 \sup |Y'|\le Y'(1)=\frac{\Xi'(3/2)}2=:A,
 \qquad
 \sup |Y''|\le Y''(1)
 =\frac{\Xi''(3/2)-\Xi'(3/2)}4=:B.
\]

The already proved Rouché comparison also gives

\[
 |Y(t)|\ge m:=2\Xi(1/2)-\Xi(3/2)>0.
\]

Consequently

\[
 |\ell'|\le A/m,
 \qquad
 |\ell''|\le B/m+(A/m)^2.
\]

Since `F=(4t-1)ell'`,

\[
 |F'|\le 4A/m+5\{B/m+(A/m)^2\}
 \quad (|t|\le1).
\]

Thus the remaining complex-disk bound is only a directed real evaluation of
`Xi(1/2)`, `Xi(3/2)`, `Xi'(3/2)`, and `Xi''(3/2)`.

Double-precision reconnaissance gives

\[
 m\approx0.48551052,
 \quad A\approx0.01173539,
 \quad B\approx0.0002519464,
\]

and hence

\[
 \sup_{|t|\le1}|F'(t)|\lesssim0.102201.
\]

This is nearly 196 times smaller than the sufficient target 20. The numerical
values are not the certificate; they show that a very coarse directed endpoint
evaluation will suffice. No zero locations are used, and RH is not proved.

## Durable verification

- Checker: `checkers/F_prime_unit_disk_theta_moment_bound.py`
- Result: `results/F-prime-unit-disk-theta-moment-bound.json`
