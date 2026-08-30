# Theta monotonicity is termwise except for one microscopic prime-free window

## Explicit completed kernel

With

\[
h(u)=\frac12e^{u/2}\vartheta(e^{2u}),
\qquad
\Phi=(\partial_u^2-\tfrac14)h,
\]

the nonconstant theta labels give

\[
\Phi(u)
=
\sum_{n\ge1}
e^{u/2}
e^{-x_n}
\left(4x_n^2-6x_n\right),
\qquad
x_n=\pi n^2e^{2u}.
\]

The factor \(1/2\) cancels the two labels \(\pm n\). Termwise differentiation is authorized on every compact \(u\)-interval by Gaussian domination.

Differentiating gives

\[
\Phi'(u)
=
- e^{u/2}
\sum_{n\ge1}
x_n
Q(x_n)e^{-x_n},
\]

where

\[
Q(x)=8x^2-30x+15.
\]

## Exact sign threshold

The roots of \(Q\) are

\[
r_\pm
=
\frac{15\pm\sqrt{105}}8.
\]

The larger root is

\[
r_+
=
\frac{15+\sqrt{105}}8
\approx3.1559.
\]

For every \(n\ge2\) and every \(u\ge0\),

\[
x_n\ge4\pi>r_+,
\]

so every \(n\ge2\) differentiated summand is strictly negative.

The \(n=1\) summand is also strictly negative once

\[
\pi e^{2u}>r_+.
\]

Therefore

\[
\Phi'(u)<0
\]

for all

\[
u>u_*
:=
\frac12\log\frac{r_+}{\pi}.
\]

Numerically, \(u_*\) is only about \(2.3\times10^{-3}\). All possible sign competition is confined to the microscopic interval

\[
0<u\le u_*.
\]

This removes the infinite half-line from the monotonicity problem.

## Near-seam cancellation

Put

\[
x=\pi e^{2u}.
\]

On \(\pi<xle r_+\), the first label contributes positively to \(\Phi'\), while every higher label contributes negatively. Strict monotonicity is equivalent to

\[
\sum_{n\ge2}
n^2x\,
Q(n^2x)e^{-n^2x}
>
x\,[-Q(x)]e^{-x}.
\]

At \(x=\pi\), equality holds because \(\Phi\) is even and hence

\[
\Phi'(0)=0.
\]

Thus the remaining theorem is a one-variable strict departure inequality from a source-forced equality point.

## Derivative form

Define

\[
D(x)
=
\sum_{n\ge2}
n^2x\,
Q(n^2x)e^{-n^2x}
-
x[-Q(x)]e^{-x}.
\]

Then

\[
D(\pi)=0,
\]

and it suffices to prove

\[
D'(x)>0
\qquad
(\pi<x<r_+).
\]

Every derivative is an explicit polynomial times a Gaussian. The first-label derivative has a large favorable contribution because \(-Q(x)\) collapses to zero at \(r_+\), whereas the higher-label terms vary smoothly over this tiny interval.

## Two-label dominance structure

The \(n=2\) term is the only tail term of comparable size at \(x=\pi\). Labels \(n\ge3\) are exponentially smaller:

\[
e^{-n^2x}
\le
e^{-9\pi}
\qquad(n\ge3).
\]

Accordingly the certificate can be organized as

\[
D'(x)
=
D_{1,2}'(x)+R_3'(x),
\]

where \(D_{1,2}\) is elementary and the remainder admits a geometric Gaussian bound.

A rigorous proof needs only:

1. a rational lower bound for \(D_{1,2}'\) on \([\pi,r_+]\);
2. a rational upper bound for \(|R_3'|\);
3. verification that the first exceeds the second.

No prime sum, cutoff limit, or RH-dependent datum enters.

## Source significance

If this finite inequality passes, the completed theta density is strictly decreasing on \((0,\infty)\). The previous Stieltjes argument then gives

\[
\operatorname{Re}(z,m_\Phi(z))>0
\qquad
(\operatorname{Re}z>0),
\]

so the one-sided theta transfer has no right-half-plane zeros.

This leaves completed \(\Xi\)-zeros to reciprocal boundary cancellation rather than causal propagation.

## Hostiles eliminated

Positivity and rapid decay alone allowed oscillatory shoulders. The explicit derivative formula shows that any such shoulder would have to occur within \((0,u_*]\) and would have to overcome the complete \(n\ge2\) Gaussian tail.

Termwise monotonicity was almost, but not completely, true: the first label initially has the wrong sign. Ignoring that microscopic exception would invalidate the proof precisely at the reciprocal seam.

## Next executable certificate

The next checker should use interval rational bounds for

\[
\pi<x<
\frac{15+\sqrt{105}}8
\]

and certify \(D'(x)>0\), with the \(n\ge3\) tail bounded analytically rather than numerically truncated.

That single certificate would close strict theta monotonicity and the one-sided zero-free transfer theorem.
