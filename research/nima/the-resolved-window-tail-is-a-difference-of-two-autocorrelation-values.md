# The resolved window tail is a difference of two autocorrelation values

## Further exact reduction

The integrated-tail factorization supplies the missing relation in the previous
cosine-transform packet.  On the rapid zero-mode-reduced full-line core,

\[
B=H_KD,
\qquad
K(r)=\int_r^\infty\Phi(s)\,ds,
\]

where the one-sided kernel is extended by zero to the opposite half-line.
Therefore, with

\[
\widehat f(\xi)=\int_{\mathbb R}f(q)e^{-2\pi iq\xi}\,dq,
\]

the resolved-tail symbol is

\[
b_\Phi(\xi)=2\pi i\xi\,\widehat K_+(\xi)
\]

(up to the harmless causal/anticausal conjugation convention).  Hence

\[
|b_\Phi(\xi)|^2
=4\pi^2\xi^2|\widehat K_+(\xi)|^2.
\]

This cancels the apparent \(\xi^{-2}\) factor in the previously derived
window formula.

Let

\[
\rho=-H',
\qquad
F:=K_+*\rho.
\]

Because

\[
\widehat W_t(\xi)
=-\frac{\sin(2\pi t\xi)}{\pi\xi}\widehat\rho(\xi),
\]

we obtain directly

\[
\widehat{BW_t}(\xi)
=-2i\sin(2\pi t\xi)\widehat K_+(\xi)\widehat\rho(\xi).
\]

Thus, for \(L=\log p\),

\[
\boxed{
 g_p=4\int_{\mathbb R}
 |\widehat F(\xi)|^2
 \sin(2\pi L\xi)\sin(4\pi L\xi)\,d\xi.
 }
\]

## Autocorrelation form

Define the real autocorrelation

\[
C_F(a)
:=\langle F,T_aF\rangle
=\int_{\mathbb R}|\widehat F(\xi)|^2
  \cos(2\pi a\xi)\,d\xi.
\]

The imaginary Fourier contribution vanishes because
\(|\widehat F|^2\) is even.  Applying

\[
2\sin x\sin2x=\cos x-\cos3x
\]

gives the exact physical-space identity

\[
\boxed{
 g_p=2\bigl(C_F(L)-C_F(3L)\bigr).
 }
\]

Equivalently,

\[
g_p
=2\int_{\mathbb R}
F(q)\bigl(F(q+L)-F(q+3L)\bigr)\,dq,
\]

with the translation sign immaterial because autocorrelation is even.

## What this changes

The joint density sought in the previous packet is not an independent unknown:

\[
\frac{|b_\Phi(\xi)|^2|\widehat\rho(\xi)|^2}{\xi^2}
=4\pi^2|\widehat{K_+*\rho}(\xi)|^2.
\]

Therefore the positive resolved two-window block no longer requires a new
spectral-factor identification.  It requires only two values of the
autocorrelation of the explicit source-derived function \(F=K_+*\rho\).

This also makes graph-domain finiteness transparent: if
\(K_+\in L^1\) and \(\rho\in L^2\), then \(F\in L^2\), and

\[
|g_p|\le4\|F\|_2^2
\le4\|K_+\|_1^2\|\rho\|_2^2.
\]

The bound is prime-independent.

## Sign and large-prime behavior

No universal sign follows from positive definiteness of \(C_F\): a positive
definite function need not be monotone on the positive half-line.  The exact
sign question is

\[
C_F(L)\mathrel{?}C_F(3L).
\]

However, if the declared regularity indeed gives \(F\in L^2\), then
translations converge weakly to zero and

\[
C_F(a)\to0\qquad(|a|\to\infty).
\]

Consequently

\[
g_p\to0\qquad(p\to\infty).
\]

So this mixed tail entry cannot itself provide a prime-uniform positive lower
bound.  Uniform coercivity, if true, must come from the full resolved diagonal
wall-plus-base terms, not from \(g_p\).

## Remaining local calculation

The earliest exact scalar calculation is now

\[
C_{K_+*\rho}(\log p)-C_{K_+*\rho}(3\log p).
\]

A closed theta-series value or a monotonicity theorem for this particular
autocorrelation would finish the real mixed-tail entry.  It remains separate
from arithmetic calibration of the oriented Stokes block and from completed
radical descent.  No RH conclusion is authorized.
