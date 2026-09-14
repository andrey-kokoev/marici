# Mellin--Plancherel normalization makes the Hardy spectral-flow coefficient exactly Connes's two-log-Lambda counterterm

## Mellin convention

Use the logarithmic Fourier/Mellin transform

\[
\widehat g(s)
=
\int_\mathbb R
 g(t)e^{-ist}dt
\]

with inverse

\[
g(t)
=
\frac1{2\pi}
\int_\mathbb R
\widehat g(s)e^{ist}ds.
\]

Then Plancherel is

\[
\boxed{
\|g\|_2^2
=
\frac1{2\pi}
\int_\mathbb R
|\widehat g(s)|^2ds.
}
\]

On one angular fiber, write

\[
m_{g,\chi}(s)
=
\widehat g_\chi(s).
\]

Summing angular characters gives

\[
\boxed{
\frac1{2\pi}
\sum_\chi
\int_\mathbb R
|m_{g,\chi}(s)|^2ds
=
\|g\|_2^2
=h(1)
}
\]

for `h=g*g*`.

## Relative Hardy coefficient

For the cutoff phase

\[
\sigma_L(s)
=e^{-2iLs},
\]

the relative projection formula contributes

\[
\frac1{2\pi i}
\partial_s
\log\sigma_L(s)
=
-
\frac L\pi.
\]

Pairing with the observer density gives

\[
\begin{aligned}
a_L(g)
&=
-
\frac L\pi
\sum_\chi
\int
|m_{g,\chi}(s)|^2ds\\
&=
-
\frac L\pi
(2\pi)
\|g\|_2^2\\
&=
-
2Lh(1).
\end{aligned}
\]

Since

\[
L=
\log\Lambda,
\]

we obtain

\[
\boxed{
a_L(g)
=-
2\log\Lambdah(1).
}
\]

The opposite orientation `e^(2iLs)` gives the positive sign.

## Match with Connes's normalization

Connes's semilocal trace formula is

\[
\operatorname{Tr}
(P_\Lambda Q_\Lambda U_S(h))
=
2h(1)\log\Lambda
+
W_S(h)
+
o(1).
\]

Thus the magnitude of the universal Hardy spectral-flow term is exactly

\[
\boxed{
2h(1)\log\Lambda.
}
\]

There is no unresolved scalar factor once the Mellin Plancherel measure `ds/(2pi)` is retained.

The sign determines which Hardy/cutoff polarity corresponds to Connes's orientation.

## Oriented identification

Choose the orientation whose cutoff phase is

\[
\sigma_L^{Connes}(s)
=e^{2iLs}
\]

if the relative projection is written as

\[
\Pi_{\sigma_L}-
\Pi.
\]

Then

\[
\frac1{2\pi i}
\partial_s
\log e^{2iLs}
=
\frac L\pi,
\]

and therefore

\[
\boxed{
\operatorname{Tr}_{rel}^{bulk}
=
2Lh(1).
}
\]

If the earlier recentering convention produces `e^(-2iLs)`, then either reverse the projection difference or assign it to the opposite polarity. Both conventions describe the same oriented pair.

## Centered Tate projection trace

Let

\[
\sigma_{L,\chi}^{Connes}(s)
=e^{2iLs}
\gamma_\chi(s).
\]

Then

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}_{rel}
\left(
M_{|m_{g,\chi}|^2}
(\Pi_{\sigma_{L,\chi}^{Connes}}-
\Pi)
\right)\\
&\quad-
\frac L\pi
\int
|m_{g,\chi}(s)|^2ds\\
&=
\frac1{2\pi i}
\int
|m_{g,\chi}(s)|^2
\partial_s
\log\gamma_\chi(s)ds\\
&\qquad+
e_{end,\chi}(g).
\end{aligned}
}
\]

After angular summation, the subtracted term is exactly

\[
2\log\Lambdah(1).
\]

## Spectral connection term

Define

\[
V_\chi(s)
=
\frac1{2i}
\partial_s
\log\gamma_\chi(s).
\]

Then

\[
\frac1{2\pi i}
\partial_s
\log\gamma_\chi
=
\frac1\pi
V_\chi.
\]

Therefore the centered finite coefficient is

\[
\boxed{
\frac1\pi
\sum_\chi
\int
|m_{g,\chi}(s)|^2
V_\chi(s)ds
+
E_{end}(g).
}
\]

If the spectral pairing `B_S` uses measure `ds/pi` rather than `ds`, this factor is absorbed into its definition. The same measure must be used on edge `C_13`.

## Completed normalization square

The normalization comparison is now

\[
\boxed{
\begin{matrix}
\text{cutoff phase }e^{2iLs}
&\longmapsto&
2\log\Lambdah(1)\\
\downarrow&&\downarrow\\
\text{Tate phase }\gamma_\chi
&\longmapsto&
\dfrac1{2\pi i}
\int|m|^2d\log\gamma_\chi.
\end{matrix}
}
\]

The upper row is universal Plancherel volume. The lower row is the local spectral connection. Endpoint winding completes the square.

## What remains

The coefficient and orientation are now fixed. The remaining regulator theorem must show that Connes's finite product-cutoff trace and the relative Hardy projection trace differ by a term tending to zero after both subtract this same

\[
2\log\Lambdah(1).
\]

This is no longer a normalization problem. It is trace-norm/relative-trace convergence of the concrete regulators.

## Consequence for earlier claims

The earlier suggestion that the sewing term should be `o(log Lambda)` before centering was incorrect. The relative Hardy pair carries a nonzero linear spectral-flow term. After centering by the exact common coefficient, the target remainder is finite.

Likewise, the two cutoff polarities carry opposite signed spectral-flow terms. Their positive feature completion must retain both before applying the signed relative-trace readout.

## Disposition

Mellin Plancherel fixes the coefficient exactly:

\[
\boxed{
\frac L\pi
\sum_\chi
\int|m_{g,\chi}|^2ds
=
2Lh(1)
=
2\log\Lambdah(1).
}
\]

Thus Connes's volume subtraction is precisely the Hardy projection-pair spectral-flow subtraction in the matching orientation. The sole remaining signed `C_34` gate is centered regulator convergence, with no scalar ambiguity.
