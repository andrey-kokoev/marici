# The prime tail in the rank-two gate has an explicit erfc bound

## Question

Can the arithmetic cutoff residual in the four-sample rank-two test be separated from the gamma enclosure?

## Prime tail

Ignoring the negative global sign, the prime heat tail beyond `N` is bounded using `Lambda(n)<=log n` by

\[
T_N(t)
\le
\frac1{2\sqrt{\pi t}}
\sum_{n>N}
\frac{\log n}{\sqrt n}
\exp\!\left[-\frac{(\log n)^2}{4t}\right].
\]

For

\[
f_t(x)=\frac{\log x}{\sqrt x}
\exp\!\left[-\frac{(\log x)^2}{4t}\right]
\]

and `N` beyond its monotonicity threshold, the integral test gives

\[
T_N(t)
\le
\frac{f_t(N)+I_N(t)}{2\sqrt{\pi t}},
\]

where, putting `u_0=log N` and

\[
v_0=\frac{u_0-t}{2\sqrt t},
\]

the integral is exactly

\[
I_N(t)
=e^{t/4}\left[
 t\sqrt{\pi t}\,\operatorname{erfc}(v_0)
 +2t e^{-v_0^2}
\right].
\]

This follows from the substitution `u=log x` and completion of the square

\[
\frac u2-\frac{u^2}{4t}
=
\frac t4-\frac{(u-t)^2}{4t}.
\]

## Difference and determinant propagation

For a prime localizer difference

\[
p_n=P(s_n)-P(s_n+h),
\]

the cutoff error satisfies

\[
|\delta p_n|
\le T_N(s_n)+T_N(s_n+h).
\]

For

\[
D_2=(g_0+p_0)(g_2+p_2)-(g_1+p_1)^2,
\]

interval propagation through these three bounds gives a rigorous prime-tail contribution independently of the gamma quadrature enclosure.

## Scale at the reconnaissance parameters

For `N=200000` and every heat argument used in the previous rank-two scan, the largest argument is `0.08`. Since `log N` is about `12.2`, the controlling exponential has logarithm below `-459`. The prime cutoff error is therefore far below the displayed `10^-8` total determinant residual. It cannot explain the observed negative sector determinants or positive cross repair.

This scale statement still requires outward-rounded evaluation before being cited as a certificate.

## Remaining certification gate

The prime tail is not the difficult residual at these parameters. Certification now requires:

1. interval enclosure of the gamma integral at the four sample points;
2. outward-rounded finite prime summation;
3. interval propagation through `D2`;
4. verification that the monotonicity threshold for `f_t` lies below `N` throughout the parameter box.

## Disposition

Attach the explicit erfc tail to every future rank-two computation. Do not merge prime truncation uncertainty with gamma quadrature or floating determinant conditioning.