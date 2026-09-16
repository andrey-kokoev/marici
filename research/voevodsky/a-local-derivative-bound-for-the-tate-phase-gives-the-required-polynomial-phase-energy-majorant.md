# A local derivative bound for the Tate phase gives the required polynomial phase-energy majorant

## Phase-energy density

For a smooth unimodular Tate phase \(\gamma_\chi:\mathbb R\to\mathbb T\), set

\[
\kappa_{\gamma_\chi}(t)
=
\frac1{4\pi^2}
\int_{\mathbb R}
\frac{|\gamma_\chi(s)-\gamma_\chi(t)|^2}{|s-t|^2}
\,ds.
\]

This is the density controlling the positive relative difference row.

## Near/far decomposition

Split the integral into \(|s-t|\le1\) and \(|s-t|>1\).

For the near part, the fundamental theorem of calculus gives

\[
|\gamma_\chi(s)-\gamma_\chi(t)|
\le
|s-t|
\sup_{|u-t|\le1}|\gamma_\chi'(u)|.
\]

Hence

\[
\int_{|s-t|\le1}
\frac{|\gamma_\chi(s)-\gamma_\chi(t)|^2}{|s-t|^2}ds
\le
2\sup_{|u-t|\le1}|\gamma_\chi'(u)|^2.
\]

For the far part, unimodularity gives

\[
|\gamma_\chi(s)-\gamma_\chi(t)|\le2,
\]

and therefore

\[
\int_{|s-t|>1}
\frac{|\gamma_\chi(s)-\gamma_\chi(t)|^2}{|s-t|^2}ds
\le
8.
\]

Thus one has the explicit pointwise estimate

\[
\boxed{
\kappa_{\gamma_\chi}(t)
\le
\frac1{2\pi^2}
\sup_{|u-t|\le1}|\gamma_\chi'(u)|^2
+
\frac2{\pi^2}.
}
\]

## Polynomial Tate bound

Assume the standard local gamma-factor estimate

\[
|\gamma_\chi'(u)|
\le
C_S(1+|u|+|\chi|)^a.
\]

For \(|u-t|\le1\),

\[
1+|u|+|\chi|
\le
2(1+|t|+|\chi|).
\]

Consequently

\[
\boxed{
\kappa_{\gamma_\chi}(t)
\le
C'_{S,a}(1+|t|+|\chi|)^{2a}.
}
\]

The required character exponent for the positive difference-row energy may therefore be taken to be

\[
\boxed{d_\kappa=2a.}
\]

No global homogeneous \(H^{1/2}\) norm of \(\gamma_\chi\) is required.

## Observer energy

Let the angular Mellin coefficients satisfy, for arbitrary \(M,K\),

\[
|m_{g,\chi}(t)|
\le
C_{g,M,K}(1+|\chi|)^{-M}(1+|t|)^{-K}.
\]

Using

\[
(1+|t|+|\chi|)^{2a}
\le
(1+|t|)^{2a}(1+|\chi|)^{2a},
\]

one obtains, whenever \(2K-2a>1\),

\[
E_g(\chi)
:=
\int\kappa_{\gamma_\chi}(t)|m_{g,\chi}(t)|^2dt
\le
C_{g,S,M,K}(1+|\chi|)^{2a-2M}.
\]

If the angular dual has shell growth dimension \(q\), then

\[
\sum_\chi E_g(\chi)<\infty
\]

provided

\[
\boxed{2M>2a+q.}
\]

Because a smooth compactly supported observer has arbitrary Schwartz order, such \(M\) and \(K\) can be chosen uniformly on bounded Schwartz packets.

## Consequence for the strong relative route

The angular direct sum

\[
\bigoplus_\chi D_{0,\chi}M_{m_{g,\chi}}
\]

is Hilbert--Schmidt and has squared norm

\[
\frac12\sum_\chi E_g(\chi)<\infty.
\]

Together with exact recentered stationarity, this closes the positive strong completion of the relative difference row, conditional only on the stated standard first-derivative gamma-factor estimate and the chosen angular counting law.

The remaining open completion problem is the localized common--difference product under the translated placement projection; it is no longer an angular phase-energy problem.
