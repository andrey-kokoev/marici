# A degree-twenty-six directed jet extends complex Pick positivity to radius twenty-one

## Higher-order interval correction

The centered Xi checker now computes to order 57 and emits the coefficients of \(4F'\) through degree 26.

The Euler-tail injection was also corrected to use the configured truncation depth `P.DEPTH` rather than the formerly hard-coded value 300. With depth 600 and 180-digit interval arithmetic, the high-order coefficient enclosures remain narrow enough for evaluation on disks of radius above twenty.

Updated checker:

`research/grothendieck/checkers/central_xi_log_even_series_interval.py`

## Radius-28 Cauchy data

The existing positive-source estimate gives

\[
|C(t)|
>
0.108914490838235047403030229879
\qquad
(|t|\le28)
\]

and

\[
|F'(t)|
<
20.974176494145319145271773178
\qquad
(|t|=28).
\]

## Radius-21 target

The degree-26 directed polynomial satisfies

\[
\operatorname{Re}F'_{26}(t)
>
0.08532959362030325549105999028
\qquad
(|t|\le21).
\]

Cauchy's estimate bounds the degree-27-and-higher tail by

\[
0.03551395344990115856648913307.
\]

Therefore

\[
\boxed{
\operatorname{Re}F'(t)
>
0.04981564017040209692457085721
\qquad
(|t|\le21).
}
\]

Vertical integration yields

\[
\boxed{
|t|\le21,
\quad
\operatorname{Im}t>0
\Longrightarrow
\operatorname{Im}F(t)>0.
}
\]

## Durable verification

Checker:

`research/grothendieck/checkers/degree_twenty_six_Fprime_cauchy_radius_twenty_one_certificate.py`

Result:

`research/grothendieck/results/degree-twenty-six-Fprime-cauchy-radius-twenty-one-certificate.json`

The checker uses directed decimal rounding and no zero locations.

## Present limit

At radius 22, the same radius-28 Cauchy model becomes negative because the geometric remainder rises to approximately \(0.1455\), while the polynomial margin remains approximately \(0.08494\).

Further progress requires either:

1. another increase in jet degree;
2. a better source lower bound on a circle near radius 28;
3. a stronger anchor than the current radius-81 estimate.

## Scope

This remains a bounded-disk complex Pick theorem, not a global proof or RH.

## Disposition

The certified complex Pick disk is now

\[
\boxed{|t|\le21.}
\]

with derivative margin exceeding \(0.0498\).
