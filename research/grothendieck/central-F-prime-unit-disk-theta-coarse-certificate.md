# A coarse theta-moment certificate closes the unit-disk `F'` gate

Write

\[
 Y(t)=\Xi(1/2+\sqrt t)=\sum_{n\ge0}b_nt^n,
 \qquad b_n>0.
\]

For every integer `n>=1`, `n/9^n<=1/9`; for `n>=2`,
`n(n-1)/9^n<=2/81`. Hence

\[
 Y'(1)\le Y(9)/9,
 \qquad Y''(1)\le2Y(9)/81.
\]

The farther real value has the elementary bound

\[
 Y(9)=\Xi(7/2)<3/4.
\]

Indeed,

\[
 \Xi(7/2)=\frac{35}{8}\pi^{-7/4}\Gamma(7/4)\zeta(7/2).
\]

Log-convexity between `Gamma(1)=Gamma(2)=1` gives `Gamma(7/4)<=1`.
The integral test, separating the `n=2` term, gives
`zeta(7/2)<6/5`. Finally `pi>31/10` implies `pi^(7/4)>7`
(raise both sides to the fourth power), so `pi^(-7/4)<1/7`.
Multiplication gives the claimed strict upper bound `3/4`.

Thus the endpoint quantities of the theta-moment reduction obey

\[
 A=Y'(1)<1/12,
 \qquad B=Y''(1)<1/54.
\]

The independent directed Rouché certificate gives
`m=2Xi(1/2)-Xi(3/2)>0.1189`. Directed substitution into

\[
 |F'|\le4A/m+5\{B/m+(A/m)^2\}
\]

therefore yields

\[
 \boxed{\sup_{|t|\le1}|F'(t)|<6.038308<20.}
\]

Together with the already certified zero-free unit disk, this closes both
premises of the outer-disk Cauchy reduction. It bounds the degree-five tail on
`|t|<=1/4` by `6.038308/768<0.007863`, well inside the certified allowance
`0.0298826`. Consequently `|F'|>1/16` on that quarter disk, and the one-circle
Cauchy gate proves pointwise reciprocal-slope concavity on the first positive-
width central cell `[10^-8,3*10^-8]`.

This is a local continuum theorem for the source-derived operator. It neither
establishes all cells nor proves RH.

## Durable verification

- Checker: `checkers/F_prime_unit_disk_theta_coarse_certificate.py`
- Result: `results/F-prime-unit-disk-theta-coarse-certificate.json`
