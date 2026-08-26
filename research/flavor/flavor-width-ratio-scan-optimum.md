# Width-ratio scan optimum (WP376)

## Dimensionless design family

Remove WP375's equal mass-width restriction by defining

\[
r=\frac{\Omega}{L}>0,
\qquad
h=\frac dL>0.
\]

After removing only positive overall dimensional factors, WP374's determinant
magnitude is

\[
D(h;r)=
\frac{8rh^3P(h,r)}
{(1+r^2)^2((1+h)^2+r^2)^2((1+2h)^2+r^2)^2},
\]

where

\[
P=3+12h+6r^2+15h^2+12r^2h+6h^3+3r^4+7r^2h^2.
\]

For every fixed \(r>0\), \(D\) is positive and tends to zero as \(h\) tends
to either positive boundary.

## Global uniqueness

Apart from a positive factor, the derivative has sign opposite to

\[
\begin{aligned}
Q_r(h)={}&48h^7+(84r^2+180)h^6+(216r^2+216)h^5\\
&+(25r^4+98r^2+9)h^4\\
&-(54r^4+252r^2+198)h^3\\
&-(20r^6+220r^4+380r^2+180)h^2\\
&-(66r^6+198r^4+198r^2+66)h\\
&-(9r^8+36r^6+54r^4+36r^2+9).
\end{aligned}
\]

For every \(r>0\), the descending coefficient sequence has four positive
terms followed by four negative terms: exactly one sign change. Also
\(Q_r(0)<0\), while its leading coefficient is positive. Descartes' rule and
continuity therefore prove exactly one positive stationary point. Since
\(D\) vanishes at both boundaries, that point is the unique global maximum.

The source-scaled prescription is

\[
d_\star=Lh_\star(\Omega/L),
\]

where \(h_\star(r)\) is the unique positive root of \(Q_r\). At \(r=1\), the
polynomial reduces to four times WP375's exact polynomial. Illustrative
locators are approximately 1.07451, 1.27037, and 1.84275 for width ratios
\(1/2\), 1, and 2 respectively.

## Disposition

The unique finite optimum persists for every positive width ratio, but its
value is not universal. It is transported by independently measured source
pole data. Covariance, scan cost, and background support remain frozen as in
WP375; changing them requires a new design functional.

This is a source-calibrated instrument-design law, not a flavor selector. Its
smallest falsifier is any admitted positive width ratio for which \(Q_r\) has
more than one positive root; the exact sign theorem excludes that within the
declared model.

Run `uv run --with sympy python
research/flavor/checkers/wp376_width_ratio_scan_optimum.py` to regenerate the
exact result.
