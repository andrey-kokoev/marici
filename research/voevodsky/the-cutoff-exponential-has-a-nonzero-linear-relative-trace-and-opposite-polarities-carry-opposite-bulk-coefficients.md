# The cutoff exponential has a nonzero linear relative trace, and opposite polarities carry opposite bulk coefficients

## Relative projection formula

For a unimodular Hardy scattering symbol `sigma`, the localized relative projection trace is

\[
\operatorname{Tr}_{rel}
\left(
M_f
(\Pi_\sigma-
\Pi)
\right)
=
\frac1{2\pi i}
\int_\mathbb R
f(s)
\partial_s
\log\sigma(s)ds
+
e_{end}(f,\sigma).
\]

Take

\[
\boxed{
\sigma_{L,\chi}(s)
=e^{-2iLs}
\gamma_\chi(s).
}
\]

Then

\[
\partial_s
\log\sigma_{L,\chi}(s)
=-2iL
+
\partial_s
\log\gamma_\chi(s).
\]

Therefore

\[
\boxed{
\begin{aligned}
\operatorname{Tr}_{rel}
\left(
M_f(\Pi_{\sigma_{L,\chi}}-
\Pi)
\right)
&=
-
\frac L\pi
\int f(s)ds\\
&\quad+
\frac1{2\pi i}
\int f(s)
\partial_s
\log\gamma_\chi(s)ds\\
&\quad+
e_{end,\chi}(f).
\end{aligned}
}
\]

The coefficient `1/pi` depends on the Fourier normalization, but the existence and sign reversal of the linear term do not.

## Observer density

For

\[
f(s)
=|m_{g,\chi}(s)|^2,
\]

the linear coefficient is

\[
\boxed{
a_\chi(g)
=-
\frac1\pi
\|m_{g,\chi}\|_2^2.
}
\]

After summing angular characters, Plancherel gives

\[
\sum_\chi
\|m_{g,\chi}\|_2^2
=
\|g\|_2^2
=h(1)
\]

with the source measure normalization. Hence

\[
\boxed{
\sum_\chi
La_\chi(g)
=-
\frac L\pi
h(1).
}
\]

After reconciling Mellin `2pi` factors, this is the same type of universal Plancherel volume term as Connes's

\[
2Lh(1).
\]

It is not a finite arithmetic correction.

## Gamma-phase finite term

Define

\[
V_\chi(s)
=
\frac1{2i}
\partial_s
\log\gamma_\chi(s).
\]

Then the non-volume part is

\[
\boxed{
\frac1\pi
\langle
m_{g,\chi},
V_\chim_{g,\chi}
\rangle
+
e_{end,\chi}(g).
}
\]

Thus the relative trace separates exactly into:

1. cutoff volume;
2. Tate/gamma connection;
3. endpoint index.

## Opposite polarity

The opposite cutoff/scattering orientation uses

\[
\sigma_{L,\chi}^{op}(s)
=e^{2iLs}
\gamma_\chi(s)^{-1}
\]

up to conjugation. Its logarithmic derivative is

\[
\partial_s
\log\sigma_{L,\chi}^{op}
=2iL
-
\partial_s
\log\gamma_\chi.
\]

Therefore its relative trace is the negative of the first orientation, modulo the conjugate endpoint convention:

\[
\boxed{
\operatorname{Tr}_{rel}^{op}
=
+
\frac L\pi
\|m_{g,\chi}\|_2^2
-
\frac1\pi
\langle m_{g,\chi},
V_\chi m_{g,\chi}\rangle
+
e_{end,\chi}^{op}.
}
\]

The two bulk coefficients cancel in the signed polarity sum and add in the positive polarity Gram completion, depending on how the two rows are sewn.

## Correction to the proposed `o(L)` route

The linear coefficient of the **relative projection trace** is generally nonzero:

\[
\boxed{
a_\chi(g)
ne0.
}
\]

Hence no argument should demand its cancellation within one orientation before identifying which quantity is being compared.

Three different objects must be distinguished:

1. Connes's product-cutoff trace;
2. the positive triple-compression trace;
3. the relative Hardy projection-pair trace.

Their linear coefficients differ by orientation and normalization. The sewing relation determines how these coefficients redistribute; it is not correct to assume the sewing is `o(L)` a priori.

## Centered relative trace

Define the centered characterwise functional

\[
\boxed{
\mathfrak R_{L,\chi}^{centered}(g)
=
\operatorname{Tr}_{rel}
\left(
M_{|m|^2}
(\Pi_{\sigma_{L,\chi}}-
\Pi)
\right)
+
\frac L\pi
\|m_{g,\chi}\|_2^2.
}
\]

Then

\[
\boxed{
\mathfrak R_{L,\chi}^{centered}(g)
=
\frac1\pi
\langle m_{g,\chi},
V_\chi m_{g,\chi}
angle
+
e_{end,\chi}(g),
}
\]

independent of `L` once the relative projection formula is admitted exactly.

This is the correct centered object to compare with the finite part of Connes's trace.

## Two-polarity bulk matrix

The two orientations naturally carry a bulk density matrix

\[
\boxed{
\begin{pmatrix}
-L/\pi&0\\
0&L/\pi
\end{pmatrix}
\|m_{g,\chi}\|_2^2
}
\]

at the signed relative-trace level. Hermitian/positive completion should not simply add these signed diagonal entries. It must return to the underlying positive Gram features before applying the signed readout.

Thus cancellation of signed volume and positivity of the doubled feature are separate operations.

## Regulator-comparison target

The exact remaining comparison is now centered on both sides:

\[
\boxed{
\begin{aligned}
&\operatorname{Tr}
(P_\Lambda Q_\Lambda U_S(h))
-
2Lh(1)\\
&\qquad\longleftrightarrow
\sum_\chi
\mathfrak R_{L,\chi}^{centered}(g),
\end{aligned}
}
\]

with all normalization and endpoint terms matched.

This comparison does not require the uncentered sewing term to be `o(L)`. It requires equality of the explicitly computed linear coefficients and convergence of the centered remainder.

## Effect on finite-packet Douglas promotion

Normalized positive Gram convergence cannot be inferred by declaring the sewing `o(L)`. One must first compute the positive triple-compression volume coefficient from its own centered Gram feature.

If that coefficient equals a positive scalar multiple of the Plancherel Gram, finite-packet Douglas promotion applies after normalization by that scalar. The scalar need not be exactly Connes's `2L` before the polarity/bulk conventions are reconciled.

## Disposition

The cutoff exponential contributes a nonzero universal relative trace:

\[
\boxed{
\frac1{2\pi i}
\partial_s
\log e^{-2iLs}
=-
\frac L\pi.
}
\]

After subtracting it, the surviving finite term is exactly the Tate connection plus endpoint index. The correct next theorem is centered regulator comparison, not an uncentered `o(log Lambda)` sewing estimate.
