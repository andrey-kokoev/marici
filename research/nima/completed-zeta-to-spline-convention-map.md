# Completed-zeta to spline convention map

## Question

Does the checker’s executable tuple follow from the declared completed-zeta factorization under an explicit transform convention?

## Declared hypothesis and transform

Assume

\[
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

For the even log-coordinate function `f`, use the spectral test

\[
h(t)=\int_{-\infty}^{\infty}f(2x)e^{itx}\,dx
=\frac12\widehat f(t/2)
\]

up to the single Fourier normalization fixed by inversion. Equivalently, choose the normalization so that pairing `1/(b+it/2)` against the spectral test yields

\[
\int_0^\infty f(x)e^{-bx}\,dx.
\]

This equation, rather than an untyped Fourier symbol, fixes the map used below.

## Component derivation

The logarithmic derivative is

\[
\frac{\xi'}{\xi}(s)=\frac1s+\frac1{s-1}-\frac12\log\pi
+\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s).
\]

On `s=1/2+it`, the gamma argument is `1/4+it/2`. The digamma expansion

\[
\psi(z)=-\gamma+\sum_{n\ge0}\left(\frac1{n+1}-\frac1{n+z}\right)
\]

and the declared transform pairing give exactly

\[
-(\gamma+\log\pi)f(0)+
\sum_{n\ge0}\left(\frac{f(0)}{n+1}-
\int_0^\infty f(x)e^{-(n+1/4)x}\,dx\right).
\]

Thus the kernel shift `n+1/4` and constant in the checker come from the gamma and pi factors.

For `Re(s)>1`,

\[
-\frac{\zeta'}{\zeta}(s)=
\sum_{p^m}\frac{\log p}{p^{ms}}.
\]

Moving to the critical normalization `s=1/2+it` supplies `log(p)/sqrt(p^m)` and the phase at `log(p^m)`. Pairing reciprocal phases for an even test supplies the factor two. With the checker’s side orientation, the arithmetic term is

\[
-2\sum_{p^m}\frac{\log p}{\sqrt{p^m}}f(\log p^m).
\]

Finally, `1/s+1/(s-1)` produces the two pole evaluations. The baseline Laurent multiplier

\[
P(z)=\left(z+z^{-1}-\frac52\right)^2
\]

has double zeros at `z=2` and `z=1/2`, so those evaluations vanish for the baseline and may be absent from its specialized checker.

## Comparison

The derived component tuple is exactly

\[
(\log p^m,\;\log p/\sqrt{p^m},\;-2,\;n+1/4,\;-(\gamma+\log\pi)f(0)),
\]

plus pole evaluations that vanish only on the pole-annihilating coefficient ray. This matches the executable baseline tuple componentwise.

## Claim boundary

This is a derivation conditional on the displayed completed-zeta factorization, contour pairing, decay needed to exchange sums and integrals, and the declared transform normalization. It is not an external-source citation and does not prove the contour theorem, the zero-side identity, RH, or a radial–G4 comparison.

## Disposition

The earlier source-audit blocker is narrowed: the executable convention is internally derived from a declared completed-zeta hypothesis, but external source authority and a fully checked contour/zero-side theorem remain absent.
