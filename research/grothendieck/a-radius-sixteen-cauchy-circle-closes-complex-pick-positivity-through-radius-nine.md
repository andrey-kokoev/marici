# A radius-sixteen Cauchy circle closes complex Pick positivity through radius nine

## Source extension

Write the normalized even source as

\[
C(t)=\frac{\Xi(\sqrt t)}{\Xi(0)}
=1+\sum_{n\ge1}c_nt^n,
\qquad c_n>0.
\]

The elementary anchor at radius 81 gives

\[
C(81)<12.229144780268399.
\]

Using the first seven directed coefficients and assigning all remaining positive mass to the worst admissible degree gives

\[
C(16)
<
1.44081362427279793341468521985.
\]

Consequently, on \(|t|=16\),

\[
|C(t)|
\ge
2-C(16)
>
0.55918637572720206658531478015.
\]

Thus the normalized source is zero-free on the full disk \(|t|\le16\), without using zero locations.

## Cauchy bound for the Pick derivative

Since

\[
F(t)=(4t-1)\frac{C'(t)}{C(t)},
\]

we have

\[
F'(t)
=
4\frac{C'}C
+
(4t-1)
\left[
\frac{C''}C
-
\left(\frac{C'}C\right)^2
\right].
\]

Directed positive-coefficient bounds for \(C,C',C''\), together with the source lower bound above, give

\[
|F'(t)|
<
0.53523919271548687513600508852
\qquad
(|t|=16).
\]

## Degree-ten Taylor model

The directed log-Xi jet gives

\[
\operatorname{Re}F'_{10}(t)
\ge
0.08962963564359785474306408851
\qquad
(|t|\le9).
\]

Cauchy's estimate on the radius-sixteen circle bounds the omitted degree-eleven-and-higher tail by

\[
0.00218231603758895707948926893.
\]

Therefore

\[
\boxed{
\operatorname{Re}F'(t)
>
0.08744731960600889766357481958
\qquad
(|t|\le9).
}
\]

## Complex Pick consequence

The source is analytic and nonzero on this disk. Since \(F\) is real on the real axis, vertical integration yields

\[
\operatorname{Im}F(x+iy)
=
\int_0^y
\operatorname{Re}F'(x+iv)
\,dv.
\]

Hence

\[
\boxed{
|t|\le9,
\quad
\operatorname{Im}t>0
\Longrightarrow
\operatorname{Im}F(t)>0.0874473196\,\operatorname{Im}t>0.
}
\]

This closes the previously unresolved annulus \(8.9<|t|\le9\).

## Durable verification

Checker:

`research/grothendieck/checkers/degree_ten_Fprime_cauchy_radius_nine_certificate.py`

Result:

`research/grothendieck/results/degree-ten-Fprime-cauchy-radius-nine-certificate.json`

The calculation uses directed decimal rounding and no zero locations.

## Scope

This proves genuine complex-interior Pick positivity on \(|t|\le9\), not merely boundary monotonicity. It remains a bounded-disk theorem and does not prove the global Pick property or RH.

## Disposition

The central complex gate is closed through the complete certified source disk:

\[
\boxed{
\operatorname{Im}F(t)>0
\quad
(|t|\le9,\ \operatorname{Im}t>0).
}
\]

Moreover, the same source estimate establishes analyticity through \(|t|\le16\). The next target is to extend the Pick derivative certificate beyond radius nine using a higher-degree jet or a second Cauchy scale.
