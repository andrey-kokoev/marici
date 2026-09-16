# A radius-twenty-six Cauchy circle doubles the certified complex Pick disk to radius sixteen

The positive normalized Xi coefficients and the elementary radius-81 anchor give

\[
C(26)
<
1.80637131903370127783979460200.
\]

Therefore

\[
|C(t)|
>
0.19362868096629872216020539800
\qquad
(|t|\le26),
\]

so the source is certified zero-free on this larger disk without using zero locations.

Directed bounds for \(C,C',C''\) imply

\[
|F'(t)|
<
6.204111287522618546218522930
\qquad
(|t|=26).
\]

On the target disk \(|t|\le16\), the directed degree-ten Taylor polynomial satisfies

\[
\operatorname{Re}F'_{10}(t)
>
0.08720286379192184433509027095.
\]

The radius-26 Cauchy bound gives the degree-eleven-and-higher remainder estimate

\[
|F'(t)-F'_{10}(t)|
<
0.07731538252961785312789395668.
\]

Consequently

\[
\boxed{
\operatorname{Re}F'(t)
>
0.00988748126230399120719631428
\qquad
(|t|\le16).
}
\]

Vertical integration from the real axis yields

\[
\boxed{
|t|\le16,
\quad
\operatorname{Im}t>0
\Longrightarrow
\operatorname{Im}F(t)>0.
}
\]

## Durable verification

Checker:

`research/grothendieck/checkers/degree_ten_Fprime_cauchy_radius_sixteen_certificate.py`

Result:

`research/grothendieck/results/degree-ten-Fprime-cauchy-radius-sixteen-certificate.json`

The calculation uses directed decimal rounding, positive source coefficients, and no zero locations.

## Optimization observation

For the degree-ten model, radius 26 is close to the useful Cauchy-scale optimum. Smaller circles increase the factor \((16/R)^{11}\); larger circles make the source lower bound \(2-C(R)\) deteriorate rapidly.

At target radius 17 the present bound becomes negative. Extending farther therefore requires a higher-degree directed jet or a stronger outer source anchor.

## Scope

This is genuine complex Pick positivity on a bounded disk. It does not establish the global upper-half-plane property or RH.

## Disposition

The certified complex Pick region has advanced from radius nine to

\[
\boxed{|t|\le16.}
\]

The next efficient step is to extend the centered log-Xi jet beyond degree ten, which exponentially suppresses the radius-26 Cauchy remainder.
