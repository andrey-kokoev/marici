# The degree-ten log-Xi jet shows that the radius-nine loss is entirely in the tail majorant

The directed centered Xi checker has been extended from order 13 to order 25. It now produces the normalized boundary/Pick derivative coefficients through degree ten.

Because

\[
\frac{G(\sqrt t)}{t^{3/2}}
=
4F'(t),
\]

the resulting coefficients divided by four are the Taylor coefficients of \(F'\).

The first terms are

\[
4F'(t)
=
0.3698285802438446113\ldots
-
0.0011906765685798377\ldots t
+
0.00000692830508740975\ldots t^2
-
\cdots.
\]

The directed coefficients continue through degree ten and decay rapidly, with alternating signs in the computed range.

## Radius-nine polynomial margin

A deliberately crude triangle bound on the degree-ten polynomial gives

\[
\operatorname{Re}F'_{10}(t)
\ge
0.08962963564359785474306408850
\qquad
(|t|\le9).
\]

Thus the computed polynomial is nowhere close to losing positivity at radius nine.

By contrast, the older degree-six source quotient majorant gives a lower bound near

\[
-0.00122
\]

at radius nine. The discrepancy proves that the failure of that certificate is caused by its coarse aggregate tail/denominator estimate, not by the known Taylor polynomial.

## Updated checker

`research/grothendieck/checkers/central_xi_log_even_series_interval.py`

now records:

1. twelve directed coefficients of the centered logarithmic derivative \(L(t)\);
2. eleven directed coefficients of \(4F'(t)\), through degree ten;
3. the central normalized-margin interval using the full degree-ten polynomial.

The result remains

`research/grothendieck/results/central-xi-log-even-series-interval.json`.

## Remaining radius-nine obligation

To certify the full disk \(|t|\le9\), it is enough to prove

\[
\left|
F'(t)-F'_{10}(t)
\right|
<
0.0896296
\qquad
(|t|\le9).
\]

This is an extremely loose target relative to the observed coefficient decay.

However, analyticity known only up to the same radius does not by itself provide a boundary Cauchy estimate. One needs either:

1. a zero-free source disk of radius strictly larger than nine;
2. a direct positive-coefficient remainder estimate for the logarithmic quotient;
3. a correlation-preserving Taylor model for \(C,C',C''\) on the radius-nine disk.

## Direct-annulus experiment

A direct polar Arb evaluation of the completed zeta product was also attempted on

\[
8.9\le|t|\le9.
\]

It suffers severe dependency inflation and is not competitive with the centered source series. Its negative or zero-containing boxes are indeterminate, not counterexamples.

## Disposition

The radius-nine obstruction has been localized to one technical estimate:

\[
\boxed{
\text{bound the degree-11-and-higher logarithmic tail by }0.0896296.
}
\]

No hostile interior behavior appears in the directed degree-ten jet.
