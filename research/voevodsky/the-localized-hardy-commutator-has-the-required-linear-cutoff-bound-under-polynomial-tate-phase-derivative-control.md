# The localized Hardy commutator has the required linear cutoff bound under polynomial Tate-phase derivative control

## Model operator

Let `Pi` be the Hardy projection on `L2(R)`. For a bounded symbol `sigma`, the commutator

\[
[\Pi,M_\sigma]
\]

has, up to the Fourier convention, singular-integral kernel

\[
K_\sigma(s,t)
=
c
\frac{
\sigma(s)-\sigma(t)
}{s-t}.
\]

Let `m` be an observer localization multiplier. Then

\[
[\Pi,M_\sigma]M_m
\]

has kernel

\[
K_{\sigma,m}(s,t)
=
c
\frac{
\sigma(s)-\sigma(t)
}{s-t}
m(t).
\]

Therefore

\[
\boxed{
\|[\Pi,M_\sigma]M_m\|_{HS}^2
=
|c|^2
\int_\mathbb R
|m(t)|^2
\left[
\int_\mathbb R
\frac{
|\sigma(s)-\sigma(t)|^2
}{|s-t|^2}ds
\right]dt.
}
\]

This is an exact Hilbert--Schmidt criterion for the localized commutator.

## Tate-scattering symbol

Take

\[
\sigma_{L,\chi}(s)
=
e^{2iLs}
\gamma_\chi(s),
\]

where

\[
|\gamma_\chi(s)|=1.
\]

Use

\[
\begin{aligned}
|\sigma(s)-\sigma(t)|
&\le
|e^{2iLs}-e^{2iLt}|\\
&\quad+
|\gamma_\chi(s)-\gamma_\chi(t)|.
\end{aligned}
\]

Thus the squared difference is bounded by twice the square of each term.

## Exact oscillatory contribution

For fixed `t`, set `r=s-t`. Then

\[
|e^{2iLs}-e^{2iLt}|^2
=
4\sin^2(Lr).
\]

The standard integral gives

\[
\int_\mathbb R
\frac{
4\sin^2(Lr)
}{r^2}dr
=
C_0L
\]

for an explicit convention-independent positive constant `C_0` up to Fourier normalization.

Hence the cutoff phase contributes exactly

\[
\boxed{
C_0L\|m\|_2^2.
}
\]

This proves that the radial transition growth is linear in `L=log Lambda`, not quadratic.

## Gamma-phase contribution

Assume the unimodular Tate phase satisfies

\[
\boxed{
|\gamma_\chi'(s)|
\le
C
(1+|s|+|\chi|)^d.
}
\]

For `|s-t|<=1`, the mean-value theorem gives

\[
|\gamma_\chi(s)-\gamma_\chi(t)|
\le
C
|s-t|
(2+|t|+|\chi|)^d.
\]

For `|s-t|>1`, unimodularity gives

\[
|\gamma_\chi(s)-\gamma_\chi(t)|
\le2.
\]

Splitting the inner integral at radius one yields

\[
\boxed{
\int_\mathbb R
\frac{
|\gamma_\chi(s)-\gamma_\chi(t)|^2
}{|s-t|^2}ds
\le
C_d
(2+|t|+|\chi|)^{2d}.
}
\]

The far region contributes a constant; the near region contributes the polynomial derivative bound.

## Localized estimate

Combining the oscillatory and gamma contributions gives

\[
\boxed{
\begin{aligned}
\|[\Pi,M_{\sigma_{L,\chi}}]M_m\|_{HS}^2
&\le
C
L\|m\|_2^2\\
&\quad+
C_d
\int_\mathbb R
|m(t)|^2
(2+|t|+|\chi|)^{2d}dt.
\end{aligned}
}
\]

If observer multipliers satisfy, for every `N`,

\[
|m_{g,\chi}(t)|
\le
C_{g,N}
(1+|t|+|\chi|)^{-N},
\]

then choosing `N` sufficiently large gives

\[
\boxed{
\|[\Pi,M_{\sigma_{L,\chi}}]
M_{m_{g,\chi}}\|_{HS}^2
\le
C_{g,N}
(1+L)
(1+|\chi|)^{-N'}
}
\]

for any prescribed `N'`, after increasing `N`.

This is stronger than the previously requested polynomial growth bound: observer localization can make the characterwise contribution rapidly decreasing.

## Sum over angular characters

If the discrete angular dual has polynomial counting growth, choose `N'` larger than that growth dimension. Then

\[
\boxed{
\sum_\chi
\|[\Pi,M_{\sigma_{L,\chi}}]
M_{m_{g,\chi}}\|_{HS}^2
\le
C_g
(1+L).
}
\]

Thus the observer-weighted angular transition is traceable and has the required logarithmic cutoff growth in this localized Hardy-commutator model.

## Archimedean gamma estimates

For the real gamma factor, the logarithmic derivative is a combination of digamma functions. Stirling's estimate gives logarithmic rather than fixed polynomial growth:

\[
|\partial_s\log\gamma_\chi(s)|
\le
C
\log(2+|s|+|\chi|).
\]

This is dominated by `(2+|s|+|chi|)^epsilon` for every positive `epsilon`, so the displayed polynomial hypothesis holds with arbitrarily small positive loss.

Higher derivatives improve at infinity.

## Finite-place gamma estimates

For a finite place, the unitary gamma factor is a conductor monomial times a rational function of `p^(-is)`. On the real `s` axis away from source-excluded poles, its derivative is bounded by a polynomial in conductor exponent and angular-character length.

Rapid decay of the smooth observer coefficients dominates this polynomial growth.

## Off-diagonal Hardy block

The Hankel block

\[
H_\sigma
=(I-\Pi)M_\sigma\Pi
\]

is one corner of the commutator. Therefore, whenever the observer multiplier is placed after the same source projection,

\[
\boxed{
\|H_\sigma M_m\|_{HS}
\le
\|[\Pi,M_\sigma]M_m\|_{HS}
}
\]

provided the projection/multiplier ordering matches.

This supplies the desired characterwise estimate for that ordering.

## Operator-order caveat

The actual semilocal transition contains a specific sequence of:

- Hardy projection;
- Tate scattering multiplier and reflection;
- observer Mellin multiplier;
- second physical regulator.

A multiplier `M_m` does not commute with a Hardy projection. Therefore one must derive the exact characterwise factorization before replacing the transition by

\[
H_\sigma M_m.
\]

Different placements create additional commutators

\[
[\Pi,M_m],
\]

which are also Hilbert--Schmidt for smooth `m` and satisfy analogous estimates, but must be included explicitly.

Thus the analytic inequality is proved for the localized commutator model; matching it to the exact semilocal operator ordering remains a typing step.

## Additional observer commutator

The same kernel argument gives

\[
\|[\Pi,M_m]\|_{HS}^2
=c
\int|u||\widehat m(u)|^2du.
\]

For smooth rapidly decreasing `m`, this is finite and rapidly decreasing in `chi`. Hence reordering `M_m` across one Hardy projection produces a controlled lower-order correction, not a new logarithmic divergence.

## Disposition

Under polynomial Tate-phase derivative control, the observer-localized Hardy commutator satisfies

\[
\boxed{
\sum_\chi
\|[\Pi,M_{e^{2iLs}\gamma_\chi}]
M_{m_{g,\chi}}\|_{HS}^2
=O_g(1+L).
}
\]

The linear `L` term is computed exactly from the exponential cutoff phase. The remaining semilocal step is to write the precise characterwise operator ordering and account for the controlled commutators created when moving the observer multiplier to the displayed position.
