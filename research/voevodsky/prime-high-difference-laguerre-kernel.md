# Prime high-difference Laguerre kernel

## Question

What exact function controls the prime contribution to the near-null observer

\[
p_m(y)=(1-y)^m?
\]

## Claim boundary

Every high difference of a prime log-Gaussian atom has an exact generalized-Laguerre integral. This retains all binomial cancellation and identifies the oscillatory region that a rank-uniform estimate must control. It does not give a global sign or uniform bound.

## Prime atom

Apart from its positive arithmetic weight and the completed negative prefactor, one prime atom is

\[
f_a(u)
=
u^{-1/2}e^{-a/u},
\qquad
a=\frac{(\log n)^2}{4}.
\]

For any integer \(q\geq0\), direct differentiation gives

\[
f_a^{(q)}(u)
=
(-1)^q q!\,
u^{-q-1/2}e^{-a/u}
L_q^{-1/2}\left(\frac au\right),
\]

where \(L_q^{-1/2}\) is a generalized Laguerre polynomial.

## High finite difference

The cube-integral identity gives

\[
\Delta_h^qf_a(t)
=
(-1)^q
\int_{[0,h]^q}
f_a^{(q)}(t+u_1+\cdots+u_q)
\,du_1\cdots du_q.
\]

The two signs cancel, so

\[
\begin{aligned}
\Delta_h^qf_a(t)
={}&q!
\int_{[0,h]^q}
U^{-q-1/2}e^{-a/U}\\
&\qquad\times
L_q^{-1/2}\left(\frac aU\right)
\,du_1\cdots du_q,
\end{aligned}
\]

with

\[
U=t+u_1+
\cdots+u_q.
\]

For the near-null degree \(m\), use \(q=2m+1\).

## Prime quadratic form

The exact prime contribution is therefore

\[
Q_{\mathrm{prime}}(p_m)
=
-
\frac1{2\sqrt\pi}
\sum_{n\geq2}
\Lambda(n)n^{-1/2}
\Delta_h^{2m+1}f_{a_n}(t).
\]

This expression has no coefficientwise \(4^m\) factor.

## Sign geometry

The leading coefficient of \(L_q^{-1/2}(z)\) is

\[
\frac{(-1)^q}{q!}.
\]

For odd \(q\), the Laguerre factor is negative at sufficiently large \(z\). In that region the atom's high difference is negative, and the completed negative prime prefactor makes its contribution positive.

The Laguerre polynomial has positive roots and changes sign. Hence prime atoms for which

\[
\frac{a_n}{U}
\]

falls in an oscillatory Laguerre interval can contribute with either sign. There is no global sign theorem from the leading coefficient alone.

## Quantitative coherence target

A rank-uniform theorem must control the weighted Laguerre sum relative to the leading gamma energy:

\[
\frac{
\left|
\sum_{n\geq2}
\Lambda(n)n^{-1/2}
\Delta_h^{2m+1}f_{a_n}(t)
\right|
}{
\Delta_h^{2m+1}K_{\Gamma,\mathrm{leading}}(t)
}.
\]

The parameters couple through

\[
q=2m+1,

y=rac{a_n}{U}.
\]

The discriminating asymptotic regimes are therefore determined by the location of \(a_n/U\) relative to the Laguerre turning region, rather than by coefficient norm alone.

## Disposition

The prime rank problem has been reduced to a weighted generalized-Laguerre turning-point estimate. The next step is to divide the prime sum into regions below, within, and above the Laguerre turning range and compare each region with the gamma alpha-family energy. Any uniform claim must include the coupled regime \(m\asymp1/t\).

## Verification

- `research/voevodsky/checkers/check_prime_high_difference_laguerre_kernel.py`
- `research/voevodsky/results/prime_high_difference_laguerre_kernel.json`
