# The gamma heat integral has an erfc series with certifiable tail

## Question

Can the remaining gamma quadrature uncertainty in the rank-two determinant be replaced by an explicit series and analytic remainder?

## Exact series

The gamma heat term uses

\[
I_\Gamma(t)=
\int_0^\infty
\frac{e^{-r}-e^{-r/4-r^2/(16t)}}{1-e^{-r}}\,dr.
\]

Expanding the denominator geometrically and integrating termwise gives

\[
I_\Gamma(t)
=
\sum_{m=0}^\infty
\left[
\frac1{m+1}
-2\sqrt{\pi t}\,
 e^{4t(m+1/4)^2}
 \operatorname{erfc}\!\bigl(2\sqrt t(m+1/4)\bigr)
\right].
\]

The full gamma kernel is

\[
K_\Gamma(t)
=
\frac{-\gamma_E-\log\pi+I_\Gamma(t)}{4\sqrt{\pi t}}.
\]

This removes improper quadrature and the removable cancellation at `r=0`.

## Tail expansion

Put `a=m+1/4`. The standard alternating asymptotic for scaled complementary error function gives

\[
2\sqrt{\pi t}\,e^{4ta^2}\operatorname{erfc}(2a\sqrt t)
=
\frac1a\left[
1-\frac1{8ta^2}
+\frac3{64t^2a^4}
-\frac{15}{512t^3a^6}+\cdots
\right].
\]

Hence each summand is

\[
\frac1{m+1}-\frac1{m+1/4}
+\frac1{8t(m+1/4)^3}
-\frac3{64t^2(m+1/4)^5}+\cdots.
\]

After a finite cutoff `M`, sums of the displayed powers are Hurwitz-zeta tails. Truncating the alternating erfc expansion at a term valid for

\[
2\sqrt t(M+1/4)>0
\]

with decreasing successive terms gives explicit upper and lower bounds from consecutive truncations.

## Direct integral tail alternative

For a split point `R>0`, the original integral tail also satisfies

\[
\left|\int_R^\infty
\frac{e^{-r}-e^{-r/4-r^2/(16t)}}{1-e^{-r}}dr\right|
\le
\frac{e^{-R}+2\sqrt{\pi t}e^{t/4}
\operatorname{erfc}((R+2t)/(4\sqrt t))}
{1-e^{-R}}.
\]

Thus either interval quadrature on a compact interval plus this tail, or the erfc series plus Hurwitz-zeta remainder, yields a certified enclosure.

## Rank-two use

Enclose `K_Gamma` at the four arguments `t,t+h,t+2h,t+3h`. Form the three differences with outward rounding and combine them with the already bounded prime differences in

\[
D_2=(g_0+p_0)(g_2+p_2)-(g_1+p_1)^2.
\]

This keeps gamma evaluation, finite prime rounding, and prime tail as separate residuals.

## Boundary

Termwise integration and the erfc asymptotic remainder must be justified uniformly on the chosen positive `t` interval. The displayed formulas provide the enclosure architecture but are not yet an executed interval certificate.

## Disposition

Replace unrestricted numerical gamma quadrature in the `D_2` checker by one of these two bounded representations. The erfc-series route is preferable when an interval implementation of scaled `erfc` and Hurwitz zeta is available.