# The ordinary window determinant has a uniform elementary lower bound

## Remainder form of the closed Gram

For \(x\ge0\), write

\[
R(x)=\frac{x}{2}+\varepsilon(x),
\]

where

\[
\varepsilon(x)
=-\frac{x}{2}\operatorname{erfc}\!\left(\sqrt{\frac\pi2}x\right)
+\frac{e^{-\pi x^2/2}}{\pi\sqrt2}.
\]

The Gaussian Mills bound

\[
\operatorname{erfc}(z)<\frac{e^{-z^2}}{z\sqrt\pi}
\qquad(z>0)
\]

shows \(\varepsilon(x)>0\).  Direct differentiation gives

\[
\varepsilon'(x)=-\frac12
\operatorname{erfc}\!\left(\sqrt{\frac\pi2}x\right)<0.
\]

Hence

\[
0<\varepsilon(x)<\varepsilon(0)=e_0,
\qquad
e_0=\frac1{\pi\sqrt2}.
\]

## Determinant bound

Using the closed ordinary window Gram,

\[
\begin{aligned}
A(L)&=2L+2(\varepsilon(2L)-e_0),\\
D(L)&=4L+2(\varepsilon(4L)-e_0),\\
C(L)&=2L+2(\varepsilon(3L)-\varepsilon(L)).
\end{aligned}
\]

Monotonicity of \(\varepsilon\) gives

\[
A(L)>2L-2e_0,
\qquad
D(L)>4L-2e_0,
\qquad
0<C(L)<2L.
\]

Therefore

\[
\boxed{
D_0(L)>4L^2-12e_0L+4e_0^2.
}
\]

The quadratic on the right is increasing for \(L>3e_0/2\).  Since
\(\log2>3e_0/2\), every prime label satisfies

\[
D_0(\log p)
>
4(\log2)^2-\frac{12\log2}{\pi\sqrt2}+\frac2{\pi^2}.
\]

The right side is positive (for example, the elementary bounds
\(0.69<\log2<0.70\), \(3.14<\pi<22/7\), and
\(1.41<\sqrt2<1.42\) already certify a positive rational lower bound).
Thus the ordinary two-window area has a prime-uniform positive lower bound.

## Resolved consequence

Positive-Gram domination then gives

\[
\Delta_p^{\mathrm{res}}
\ge(1+M_\Phi^2)^2D_0(\log p)
\ge D_0(\log p)
> d_*,
\]

where

\[
d_*
:=4(\log2)^2-\frac{12\log2}{\pi\sqrt2}+\frac2{\pi^2}>0.
\]

Numerically \(d_*\approx0.252\), while the exact determinant at \(p=2\) is
approximately \(0.420126\).  The numerical value is not needed for the
symbolic lower bound.

## What this closes and what it does not

This removes the possibility that the resolved determinant degenerates along
large primes. The subsequent theta-series estimate proves uniformly that

\[
\frac{\kappa_p^2}{4}<0.006<d_*,
\]

so the conditional scalar oriented margin is now closed. See
`the-euler-theta-incidence-is-uniformly-too-small-to-exhaust-the-window-area.md`.

Typed assembly remains prior logically: without a common carrier, the
resolved determinant and oriented coefficient cannot yet be added. The Köthe
closed-range, common-domain, and radical-descent gates also remain open. No RH
conclusion is authorized.
