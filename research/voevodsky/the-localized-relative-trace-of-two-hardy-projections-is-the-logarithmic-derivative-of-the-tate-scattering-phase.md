# The localized relative trace of two Hardy projections is the logarithmic derivative of the Tate scattering phase

## Pair of Hardy projections

Let `Pi` be a Hardy projection on `L2(R)` and let

\[
\gamma(s)
=
e^{i\vartheta(s)}
\]

be a sufficiently regular unimodular scattering symbol. Define

\[
\boxed{
\Pi_\gamma
=M_\gamma\PiM_\gamma^*.
}
\]

Neither `Pi_gamma` nor `Pi` has finite trace. Their difference is interpreted through a localized relative trace.

Let

\[
f(s)
=|m(s)|^2
\]

be a smooth rapidly decreasing observer density.

## Relative projection-trace formula

For an admitted symbol class in which the localized projection difference is traceable, the one-dimensional projection-pair/spectral-shift formula is

\[
\boxed{
\operatorname{Tr}_{rel}
\left(
M_f(\Pi_\gamma-\Pi)
\right)
=
\frac{1}{2\pi i}
\int_\mathbb R
f(s)
\gamma(s)^{-1}
\gamma'(s)ds.
}
\]

Since `gamma=e^(i vartheta)`, this is

\[
\boxed{
\operatorname{Tr}_{rel}
\left(
M_f(\Pi_\gamma-\Pi)
\right)
=
\frac1{2\pi}
\int_\mathbb R
f(s)\vartheta'(s)ds.
}
\]

The overall sign changes if the opposite Hardy projection or scattering orientation is selected.

## Calibration by a linear phase

Take

\[
\gamma_a(s)
=e^{ias}.
\]

In the Fourier-dual variable, multiplication by `e^(ias)` translates the Hardy half-line by `a`. Thus

\[
\Pi_{\gamma_a}-\Pi
\]

is the signed projection onto an interval of length `|a|`.

Its trace density is

\[
\frac{a}{2\pi}.
\]

The formula gives

\[
\frac{1}{2\pi i}
\gamma_a^{-1}
\gamma_a'
=
\frac{a}{2\pi},
\]

so the normalization agrees.

## Kernel derivation of the infinitesimal formula

Let

\[
\gamma_\varepsilon(s)
=e^{i\varepsilon\vartheta(s)}.
\]

Then

\[
\left.
\frac d{d\varepsilon}
\Pi_{\gamma_\varepsilon}
\right|_{\varepsilon=0}
=
i[M_\vartheta,\Pi].
\]

The diagonal of the commutator kernel vanishes pointwise, but its localized relative trace has the Hardy boundary anomaly

\[
\operatorname{Tr}_{rel}
\left(
M_fi[M_\vartheta,\Pi]
\right)
=
\frac1{2\pi}
\int f(s)\vartheta'(s)ds.
\]

Integrating this infinitesimal identity along the path `epsilon in [0,1]` yields the projection-pair formula, provided the relative trace class is stable along the path. Integer winding/spectral-flow terms must be retained if the phase does not admit one global logarithm.

## Tate scattering phase

For angular character `chi`, take

\[
\gamma
=
\gamma_\chi
\]

to be the unitary Tate gamma factor on the critical line. Define

\[
\boxed{
V_\chi(s)
=
\frac1{2i}
\partial_s
\log\gamma_\chi(s).
}
\]

Then

\[
\frac{1}{2\pi i}
\gamma_\chi^{-1}
\gamma_\chi'
=
\frac1\pi
V_\chi(s).
\]

Therefore

\[
\boxed{
\operatorname{Tr}_{rel}
\left(
M_{|m_{g,\chi}|^2}
(\Pi_{\gamma_\chi}-\Pi)
\right)
=
\frac1\pi
\left\langle
m_{g,\chi},
V_\chim_{g,\chi}
\right\rangle.
}
\]

The factor `1/pi` is convention-dependent and must be reconciled with the source Mellin normalization.

## Separation from cutoff translation

The complete Tate--cutoff symbol is

\[
\sigma_{L,\chi}(s)
=e^{-2iLs}\gamma_\chi(s).
\]

Factor it as

\[
M_{\sigma_{L,\chi}}
=M_{e^{-2iLs}}
M_{\gamma_\chi}.
\]

The exponential translates the Hardy boundary and produces the universal volume/spectral-flow term. The gamma factor changes the translated projection by a relative pair whose localized trace is the logarithmic-derivative integral above.

Thus the asymptotic coefficients separate:

\[
\boxed{
\text{cutoff exponential}
\longmapsto
\text{bulk }2Lh(1),
}
\]

\[
\boxed{
\text{Tate phase}
\longmapsto
\langle m,V_\chi m\rangle.
}
\]

This is the precise spectral-shift version of the proposed strong-Szego/Widom expansion.

## Angular summation

The local gamma derivatives grow at most polynomially/logarithmically in `chi` and `s`, while `m_(g,chi)` decays rapidly for smooth observers. Hence

\[
\sum_\chi
\left|
\left\langle
m_{g,\chi},
V_\chi m_{g,\chi}
\right\rangle
\right|
<\infty.
\]

Subject to the exact Plancherel measure and multiplicity convention, summing yields

\[
\boxed{
\sum_\chi
\operatorname{Tr}_{rel}
\left(
M_{|m_{g,\chi}|^2}
(\Pi_{\gamma_\chi}-\Pi)
\right)
=
\frac1\pi
\langle
\widehat g,
V_{loc,S}\widehat g
\rangle.
}
\]

## Endpoint and winding terms

If `gamma_chi` has nonzero winding or only a meromorphic logarithm, the relative projection pair carries an integer index/spectral-flow term. In the completed explicit formula these terms correspond to boundary/pole data and cannot be discarded.

Thus the full identity is

\[
\boxed{
\operatorname{Tr}_{rel}
(M_f(\Pi_\gamma-\Pi))
=
\frac{1}{2\pi i}
\int fd\log\gamma
+
\operatorname{Index}_{end}(f,\gamma),
}
\]

with the endpoint functional determined by the chosen logarithm and Hardy polarization.

## Relation to `C_34`

The spectral edge represents the local Weil current as

\[
V_{loc,S}
=
\frac1{2i}
\partial_s
\log J_{loc,S}.
\]

The cutoff edge produces a relative pair of Hardy/prolate projections. The formula above identifies the finite relative trace of that projection pair with the same logarithmic derivative.

Therefore, at the characterwise relative-trace level,

\[
\boxed{
C_{34}:
\text{Tate scattering connection}
\longleftrightarrow
\text{Hardy projection spectral shift}
}
\]

is explicit.

## Remaining comparison with the exact product cutoff

The projection-pair formula concerns the localized relative trace after separating the exponential cutoff translation from the Tate phase. To finish the original sewing problem one must prove that the exact finite `(Lambda,R,N)` product-cutoff expression converges to this relative trace, with:

- the same normalization;
- the same endpoint index;
- rapidly summable angular remainders;
- compatibility with the opposite cutoff orientation.

That is a regulator-comparison theorem, not a missing phase calculation.

## Disposition

The finite Tate-phase contribution is determined by the standard relative Hardy projection formula:

\[
\boxed{
\operatorname{Tr}_{rel}
\left(
M_f(M_\gamma\Pi M_\gamma^*-\Pi)
\right)
=
\frac1{2\pi i}
\int f(s)
\partial_s\log\gamma(s)ds
+
\text{endpoint index}.
}
\]

Hence the finite spectral-shift coefficient is exactly the dual--canonical connection `V_chi`. The remaining gate is to identify this relative projection trace with the limit of Connes's exact regulated product-cutoff sewing expression.
