# Laguerre-root control makes the prime near-null form positive

## Question

What is the sign of the exact prime high difference on `p_m(y)=(1-y)^m`?

## Claim boundary

Let `k=2m+1`. The prime contribution to the near-null Rayleigh form is nonnegative whenever the complete finite-difference window lies sufficiently far below the first prime displacement scale. An explicit sufficient condition is

\[
\frac{(\log2)^2}{4(t+kh)}>4k+2.
\]

This controls one polynomial direction, not the full rank-`m+1` matrix.

## Derivatives of one log-Gaussian atom

Set

\[
\phi_c(s)=s^{-1/2}e^{-c/s},
\qquad c=\frac{(\log n)^2}{4}.
\]

The exact derivative identity is

\[
\phi_c^{(k)}(s)
=(-1)^k k!\,s^{-k-1/2}e^{-c/s}
L_k^{-1/2}(c/s),
\]

where `L_k^(-1/2)` is the generalized Laguerre polynomial. Its leading coefficient is `(-1)^k/k!`. Therefore, for odd `k`, the derivative is positive whenever `c/s` lies beyond the largest Laguerre zero.

The Laguerre three-term recurrence is represented by a symmetric Jacobi matrix. A row-sum bound on that matrix gives the coarse uniform estimate

\[
x_{\max}(L_k^{-1/2})<4k+2.
\]

No sharp zero asymptotic is needed.

## Finite-difference cube

Use the directed difference

\[
\Delta_h f(s)=f(s)-f(s+h).
\]

Repeated fundamental-theorem integration gives

\[
\Delta_h^k f(t)
=(-1)^k
\int_{[0,h]^k}
f^{(k)}(t+u_1+\cdots+u_k)
\,du_1\cdots du_k.
\]

If

\[
\frac{c}{t+kh}>4k+2,
\]

then `phi_c^(k)` is positive throughout the cube. For odd `k`, this implies

\[
\Delta_h^k\phi_c(t)<0.
\]

A prime heat atom is

\[
-\frac{\Lambda(n)n^{-1/2}}{2\sqrt\pi}\phi_c(t).
\]

Its odd directed difference is therefore positive. Since `c` is minimized at `n=2`, the single displayed condition with `(log 2)^2/4` proves nonnegativity term by term for every prime power.

## Near-null consequence

Vandermonde convolution gives

\[
Q_P(t,h;(1-y)^m)=\Delta_h^{2m+1}K_P(t).
\]

Hence

\[
Q_P(t,h;(1-y)^m)\ge0
\]

under the stated Laguerre-root condition. In this regime the prime sector helps the near-null inequality; it is not an error that must be dominated by gamma energy.

## Scale implication

The sufficient condition has the form

\[
t+(2m+1)h
<\frac{(\log2)^2}{4(8m+6)}.
\]

Writing `q=2m+1` and `c0=(log 2)^2/4`, the sufficient condition is

\[
(4q+2)(t+qh)<c_0.
\]

In particular, a coarse explicit subregion has

\[
q\le C\min\{t^{-1},h^{-1/2}\}
\]

for a sufficiently small absolute `C`. The second scale is essential: a `q`th difference samples through `t+qh`, so at fixed `h/t` the accessible sign-controlled rank is of order `h^{-1/2}`, not `t^{-1}`. This replaces the artificial `4^m` cost with a parabolic termwise-sign window.

## Strongest falsification attempt

Laguerre sign control is direction-specific. A general polynomial produces `|p(e^{-hu^2})|^2`, not one odd finite difference, and its prime cosine pairing need not decompose into positive atomwise derivatives. The condition is sufficient and coarse; failure of it does not imply a negative prime contribution.

## Disposition

The near-null family is not the source of prime-driven instability inside the stated small window. Any rank-uniform obstruction must come from other polynomial directions, from windows crossing Laguerre zeros, or from the gamma–prime coupling outside this regime.