# The Euler--theta incidence is uniformly too small to exhaust the window area

## Cancellation in the sampled derivative

Recall

\[
\kappa_p
=2L\sum_{k\ge1}p^{-k/2}\Phi'(kL),
\qquad L=\log p,
\]

and

\[
\Phi'(u)
=-e^{u/2}\sum_{n\ge1}x_n(u)Q(x_n(u))e^{-x_n(u)},
\]

where

\[
x_n(u)=\pi n^2e^{2u},
\qquad
Q(x)=8x^2-30x+15.
\]

At the sampled point \(u=kL\), the half-density factors cancel exactly:

\[
p^{-k/2}e^{kL/2}=1.
\]

Consequently

\[
|\kappa_p|
=2L\sum_{k,n\ge1}x_{n,k}Q(x_{n,k})e^{-x_{n,k}},
\qquad
x_{n,k}=\pi n^2p^{2k}.
\]

All summands are positive because \(x_{n,k}\ge4\pi\).

## Uniform first-term bound

For \(x\ge4\pi\),

\[
0<Q(x)<8x^2,
\]

so

\[
|\kappa_p|
<16L\sum_{k,n\ge1}x_{n,k}^3e^{-x_{n,k}}.
\]

For fixed \(k,n\), the function

\[
L\longmapsto Lx(L)^3e^{-x(L)},
\qquad
x(L)=\pi n^2e^{2kL},
\]

has logarithmic derivative

\[
\frac1L+6k-2kx(L)<0
\qquad(L\ge\log2),
\]

because \(x(L)\ge4\pi>12\).  Hence every summand, including the outer factor
\(L\), is maximal at \(p=2\).  It is therefore enough to bound

\[
16(\log2)\sum_{k,n\ge1}
(\pi n^24^k)^3e^{-\pi n^24^k}.
\]

For \((n,k)=(1,1)\), using \(3<\pi<4\), monotonicity of \(x^3e^{-x}\) for
\(x>3\), and \(e^{12}>160000\),

\[
(4\pi)^3e^{-4\pi}
<12^3e^{-12}
<\frac{1728}{160000}<0.0108.
\]

Every other pair has \(n^24^k\ge16\), hence \(x_{n,k}>48\).  Bounding the
sparse tail by the full integer tail (with a harmless polynomial multiplicity
majorant) gives

\[
\sum_{(n,k)\ne(1,1)}x_{n,k}^3e^{-x_{n,k}}<0.001.
\]

For completeness, this last coarse estimate follows from

\[
\sum_{j\ge48}j^4e^{-j}
\le
\frac{48^4e^{-48}}
{1-e^{-1}(49/48)^4}
<0.001.
\]

Since \(16\log2<12\),

\[
\boxed{|\kappa_p|<0.142}
\]

for every prime.  The constants are intentionally coarse; the actual maximum
is approximately \(0.05476\) at \(p=2\).

## Comparison with the uniform resolved area

The ordinary-window theorem gives

\[
\Delta_p^{\mathrm{res}}>d_*,
\qquad
d_*
=4(\log2)^2-\frac{12\log2}{\pi\sqrt2}+\frac2{\pi^2}
>0.25.
\]

On the other hand,

\[
\frac{\kappa_p^2}{4}
<\frac{0.142^2}{4}
<0.006.
\]

Therefore

\[
\boxed{
\Delta_p^{\mathrm{res}}-\frac{\kappa_p^2}{4}>0.244
}
\]

for every prime.

## Status

This closes the scalar positivity inequality for the oriented local
first-Adams two-by-two block, **conditional on** the typed assembly that puts
the resolved positive form and transported Stokes/Wronskian linking form on
the same carrier.  The scalar estimate does not construct that comparison
map.

It also does not repair the dense nonclosed range of the isolated comparison
in the declared Köthe topology, nor prove common-domain continuity or radical
descent for the full pushout.  Those are now earlier gates than local scalar
positivity.  No RH conclusion is authorized.
