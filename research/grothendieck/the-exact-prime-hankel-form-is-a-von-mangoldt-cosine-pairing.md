# The exact prime Hankel form is a von Mangoldt cosine pairing

## Question

What structure is lost when the prime contribution on a polynomial direction is bounded coefficientwise by `4^m`?

## Claim boundary

The exact quadratic form is a Gaussian-weighted cosine pairing with the von Mangoldt distribution. For the near-null polynomial `(1-y)^m`, the polynomial coefficients recombine before the prime sum into one nonnegative frequency envelope. Any improvement over the coefficientwise bound must use oscillation in `cos(u log n)` or a source identity coupling it to the gamma sector. No such cancellation estimate is proved here.

## Fourier identity

For `s>0` and `a>0`,

\[
s^{-1/2}e^{-a^2/(4s)}
=\frac1{\sqrt\pi}
\int_{-\infty}^{\infty}e^{-su^2}e^{iau}\,du.
\]

The prime heat kernel is

\[
K_P(s)=-\frac1{2\sqrt{\pi s}}
\sum_{n\ge2}\Lambda(n)n^{-1/2}
 e^{-(\log n)^2/(4s)}.
\]

Let `p(y)=sum_(j=0)^(N-1)c_j y^j`, and define its prime difference quadratic form by

\[
Q_P(t,h;p)=
\sum_{i,j}\overline{c_i}c_j
\bigl[K_P(t+(i+j)h)-K_P(t+(i+j+1)h)\bigr].
\]

Substitution of the Fourier identity and recombination of the polynomial give

\[
Q_P(t,h;p)
=-\frac1{2\pi}
\sum_{n\ge2}\Lambda(n)n^{-1/2}
\int_{-\infty}^{\infty}
 e^{-tu^2}(1-e^{-hu^2})
 |p(e^{-hu^2})|^2
 \cos(u\log n)\,du.
\]

The expression is real. For fixed `t,h`, Gaussian decay justifies the interchange after retaining the original log-Gaussian formulation; the cosine form is its Fourier reassembly, not a new conditional ordering of the prime series.

## Near-null polynomial

For

\[
p_m(y)=(1-y)^m,
\]

Vandermonde convolution gives the exact full-kernel identity

\[
Q_H(t,h;p_m)=\Delta_h^{2m+1}H(t),
\]

with the directed finite-difference convention fixed by the positive first difference `H(t)-H(t+h)`. Thus the intrinsic prime term is the same high finite difference of each log-Gaussian atom, equivalently its cube-integral derivative representation. The coefficient explosion disappears inside the integral:

\[
Q_P(t,h;p_m)
=-\frac1{2\pi}
\sum_{n\ge2}\Lambda(n)n^{-1/2}
\int_{-\infty}^{\infty}
 e^{-tu^2}(1-e^{-hu^2})^{2m+1}
 \cos(u\log n)\,du.
\]

Thus `4^m` is not intrinsic to the exact integrand. It arose from taking the coefficient `l1` norm before recombination.

For `h=kappa*t`, set `v=t*u^2`. The nonoscillatory envelope is

\[
e^{-v}(1-e^{-\kappa v})^{2m+1},
\]

whose maximum lies where

\[
e^{-\kappa v}\asymp m^{-1},
\qquad
|u|\asymp
\sqrt{\frac{\log m}{\kappa t}}.
\]

The near-null direction therefore probes the prime cosine distribution at increasing Fourier frequency rather than amplifying every coefficient with the same sign.

## Relation to the Euler source

Formally the prime cosine sum is the real boundary value of

\[
-\frac{\zeta'}{\zeta}\left(\frac12+iu\right),
\]

where the Dirichlet series is not absolutely convergent. The displayed Gaussian pairing is well defined through the original prime heat sum, but replacing it by a pointwise critical-line Dirichlet series would be invalid. Any contour argument must retain a domain with `Re s>1` and move it with explicit pole residues; otherwise it silently reintroduces the zero-side statement.

## Strongest falsification attempt

Absolute-value estimation of the prime sum discards the cosine phases and returns the previous exponential rank cost. Pointwise estimates for `zeta'/zeta` on the critical line encounter zeros and cannot provide an unconditional uniform bound. The remaining admissible possibilities are a smoothed prime-number-theorem estimate matched to this envelope or cancellation after coupling to the gamma term in the complete Weil form.

## Disposition

The next quantitative target is a source-side estimate for the Gaussian von Mangoldt cosine pairing at frequency scale `sqrt(log m/(kappa t))`, proved from `Re s>1` or an explicit PNT remainder and carrying all contour residues. Do not use the critical-line Dirichlet series pointwise.