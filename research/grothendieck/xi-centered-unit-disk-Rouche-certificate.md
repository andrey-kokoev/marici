# The centered unit disk is zero-free without using zero locations

The positive theta-kernel Rouché reduction requires only

\[
 \Xi(3/2)<2\Xi(1/2).
\]

This comparison now has a deliberately coarse directed certificate.

For `zeta(1/2)`, forty positive Euler-transform terms with directed square
roots give

\[
 |\zeta(1/2)|>1.46035.
\]

Elementary integral bounds give `Gamma(1/4)>3.4`, while `pi^(-1/4)>0.7`.
Consequently

\[
 \Xi(1/2)>0.434455.
\]

For the other endpoint, log-convexity of Gamma on `[1,2]` gives
`Gamma(3/4)<=4/3`; the integral test gives `zeta(3/2)<3`; and `pi>3` gives
`pi^(-3/4)<1/2`. Hence

\[
 \Xi(3/2)<\frac34.
\]

The certified comparison margin is

\[
 2\Xi(1/2)-\Xi(3/2)>0.1189109.
\]

Theta positivity and Rouché's theorem therefore prove

\[
 \boxed{\Xi(s)\ne0\quad\text{whenever }|s-1/2|\le1.}
\]

No Riemann-zero location enters the proof. This closes the analyticity half of
the unit-disk `F'` gate. It does not yet prove `|F'|<=20`, first-cell continuum
concavity, or RH.

## Durable verification

- Checker: `checkers/xi_centered_unit_disk_rouche_certificate.py`
- Result: `results/xi-centered-unit-disk-rouche-certificate.json`
