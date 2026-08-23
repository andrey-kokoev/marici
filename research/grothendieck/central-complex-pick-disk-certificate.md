# A genuine complex Pick disk closes around the central boundary

The completed theta source now certifies the Pick inequality on a
two-dimensional region:

\[
 \boxed{|t|\le1,\quad \operatorname{Im}t>0
 \quad\Longrightarrow\quad \operatorname{Im}F(t)>0.}    \tag{1}
\]

This uses no zero locations.

## Denominator-aware theta argument

Write

\[
 F'(t)=g_0+\sum_{n\ge1}g_nt^n.
\]

The directed central Xi jet gives

\[
 g_0=F'(0)>0.09245714506096115284.
\]

Put `C(t)=Y(t)/Y(0)`, `p=C'/C`, and `q=C''/C-p^2`. Then

\[
 F'(t)=4p(t)+(4t-1)q(t).
\]

The normalized completed-theta coefficient certificate reconstructs
`C` through degree six and bounds all remaining positive coefficients using
`C(9)`. On the unit disk it proves

\[
 |C(t)|>0.97664462949,
\]

and, retaining the common denominator,

\[
 |F'(t)-F'(0)|<0.004865634015.
\]

Consequently

\[
 \operatorname{Re}F'(t)
 >0.087591511046.                                     \tag{2}
\]

For `t=x+iy` in the upper half-disk, the vertical segment from `x` to `t`
stays inside the disk. Since `F` is real on the real segment,

\[
 \operatorname{Im}F(x+iy)
 =\int_0^y\operatorname{Re}F'(x+iv)\,dv
 >0.087591511046\,y>0.                                 \tag{3}
\]

## Meaning

This upgrades the previous real-axis finite-rank certificates to one open
complex region where the full scalar Pick sign holds. In the angular picture,
every quarter-centered arc portion lying in this `t` disk has strictly
decreasing Xi modulus.

Earlier Cauchy estimates reached radii `0.015`, `1/4`, `0.39`, and `0.74`.
They lost the common denominator in the logarithmic derivative. Preserving
that denominator closes the entire source-certified unit disk and gives a
larger margin.

A bounded disk is still only local evidence; global Pick positivity and RH
remain open.

## Durable verification

- Checker: `checkers/central_complex_pick_disk_certificate.py`
- Result: `results/central-complex-pick-disk-certificate.json`
- Inputs: `results/central-xi-log-even-series-interval.json` and
  `results/F-prime-unit-disk-theta-sharp-certificate.json`
- Analyticity input: `results/xi-centered-unit-disk-Rouche-certificate.json`
