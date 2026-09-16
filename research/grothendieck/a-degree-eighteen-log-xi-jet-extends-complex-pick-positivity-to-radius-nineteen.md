# A degree-eighteen log-Xi jet extends complex Pick positivity to radius nineteen

## Higher directed jet

The centered Xi checker now works to series order 41. It produces:

1. twenty directed coefficients of
   \[
   L(t)=\frac d{dt}\log\Xi(\sqrt t);
   \]
2. nineteen directed coefficients, through degree eighteen, of
   \[
   4F'(t)=\frac{G(\sqrt t)}{t^{3/2}}.
   \]

The checker is

`research/grothendieck/checkers/central_xi_log_even_series_interval.py`.

## Radius-28 source circle

Positive normalized Xi coefficients and the radius-81 anchor give

\[
C(28)
<
1.89108550916176495259696977013.
\]

Therefore

\[
|C(t)|
>
0.10891449083823504740303022987
\qquad
(|t|\le28).
\]

Directed bounds for \(C,C',C''\) imply

\[
|F'(t)|
<
20.97417649414531914527177318
\qquad
(|t|=28).
\]

## Radius-19 target disk

The degree-eighteen directed polynomial satisfies

\[
\operatorname{Re}F'_{18}(t)
>
0.08609385182813923956881854449
\qquad
(|t|\le19).
\]

The radius-28 Cauchy estimate bounds all terms of degree nineteen and higher by

\[
0.04120180693061574486692103793.
\]

Hence

\[
\boxed{
\operatorname{Re}F'(t)
>
0.04489204489752349470189750656
\qquad
(|t|\le19).
}
\]

Vertical integration gives the genuine Pick inequality

\[
\boxed{
|t|\le19,
\quad
\operatorname{Im}t>0
\Longrightarrow
\operatorname{Im}F(t)>0.
}
\]

## Durable verification

Checker:

`research/grothendieck/checkers/degree_eighteen_Fprime_cauchy_radius_nineteen_certificate.py`

Result:

`research/grothendieck/results/degree-eighteen-Fprime-cauchy-radius-nineteen-certificate.json`

The calculation uses directed decimal rounding and no zero locations.

## Current limit

The source lower bound on the radius-28 circle is only about \(0.109\), so the bound for \(|F'|\) there is deliberately coarse. The degree-eighteen decay nevertheless leaves substantial target margin at radius nineteen.

Extending materially beyond radius nineteen requires either:

1. an even higher directed jet;
2. a better source lower bound than \(2-C(R)\);
3. a stronger outer anchor reducing the unknown positive coefficient tail.

## Scope

This remains a bounded-disk theorem and does not prove global Pick positivity or RH.

## Disposition

The certified complex Pick disk is now

\[
\boxed{|t|\le19.}
\]

with quantitative derivative margin exceeding \(0.04489\).
