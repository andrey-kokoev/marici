# The normalized theta jet sharpens the unit-disk source bound

Let

\[
 C(t)=\frac{Y(t)}{Y(0)}=\sum_{n\ge0}c_nt^n,
 \qquad \ell'(t)=\frac{Y'(t)}{Y(t)}=\sum_{n\ge0}a_nt^n.
\]

The exact recurrence

\[
 (n+1)c_{n+1}=\sum_{k=0}^n a_kc_{n-k}
\]

turns the directed central logarithmic jet into intervals for
`c_0,...,c_6`. Every interval is strictly positive, as required by the theta
representation.

The elementary source bounds `Y(9)<3/4` and
`Y(0)=Xi(1/2)>0.4344554663` give

\[
 C(9)<1.726316\ldots.
\]

Because all `c_n` are positive, the tails beginning at degree seven satisfy

\[
\begin{aligned}
 \sum_{n\ge7}c_n&\le C(9)9^{-7},\\
 \sum_{n\ge7}nc_n&\le7C(9)9^{-7},\\
 \sum_{n\ge7}n(n-1)c_n&\le42C(9)9^{-7}.
\end{aligned}
\]

Combining the reconstructed coefficients and these tails bounds `C(1)`,
`C'(1)`, and `C''(1)`. Positivity then controls their suprema on the unit
disk, while Rouché gives `|C(t)|>=2-C(1)`. Directed substitution into

\[
 |F'|\le4|\ell'|+5|\ell''|
\]

proves

\[
 \boxed{\sup_{|t|\le1}|F'(t)|<0.103.}
\]

There is a stronger consequence. Put `p=C'/C` and
`q=C''/C-p^2`, so `F'=4p+(4t-1)q`. Keeping this common denominator instead
of applying Cauchy directly to `F'` gives directed bounds for
`|p-p(0)|`, `|q-q(0)|`, and hence

\[
 \boxed{\operatorname{Re}F'(t)>0.087
 \qquad(|t|\le1).}
\]

Thus the normalized theta source maps the entire unit disk through `F'` into
the open right half-plane.

This replaces the earlier elementary bound `6.038308` by more than a factor
of 58 without evaluating any zeros or introducing a new special-function
engine. Its immediate use is a substantially larger complex Pick disk.

## Durable verification

- Checker: `checkers/F_prime_unit_disk_theta_sharp_certificate.py`
- Result: `results/F-prime-unit-disk-theta-sharp-certificate.json`
