# Exact two-label theta curvature certificate

Author: `marici.Grothendieck`

## Target

Let `x=pi e^{2u}` and write

\[
 \Phi=\phi_1(1+r_2+T_3),
 \qquad
 r_2=4\frac{8x-3}{2x-3}e^{-3x}.
\]

For `V_1=-log phi_1`, the primitive curvature derivative is

\[
 V_1'''=8x-\frac{48x(2x+3)}{(2x-3)^3}.
\]

It changes sign once, at `x=x_*`, where

\[
 (2x_*-3)^3=6(2x_*+3),
 \qquad \pi<x_*<\frac72.
\]

The purpose of this packet is to prove that the exact two-label potential

\[
 V_{\{1,2\}}=V_1-\log(1+r_2)
\]

has positive fourth derivative throughout this primitive transition.

## Logistic channel decomposition

Put

\[
 \ell=\log r_2,
 \qquad p=\frac{r_2}{1+r_2},
 \qquad q=p(1-p),
 \qquad d=1-2p,
\]

and define positive channel magnitudes

\[
 A=-D\ell,\quad B=-D^2\ell,\quad C=-D^3\ell,\quad E=D^4\ell,
 \qquad D=2x\frac d{dx}.
\]

On `pi<=x<=x_*`, all four are positive and

\[
 DA=B,\qquad DB=C,\qquad DC=-E,\qquad Dp=-qA.
\]

The exact logistic identity is

\[
\begin{aligned}
 D^4\log(1+r_2)={}&pE+4qAC+3qB^2\\
 &+qA^2\bigl[(1-6p+6p^2)A^2-6dB\bigr].
\end{aligned}
\]

The cubic term `-6dqA^2B` is the unique internal repair channel. It must be
retained with the quartic consumer.

## Seam-majorant monotonicity

The paired bracket is bounded above by

\[
 K=A^2-6dB>0.
\]

Define

\[
 \mathcal U=pE+4qAC+3qB^2+qA^2K.
\]

The differential chain gives

\[
 D(pE)<0,\qquad D(qAC)<0,\qquad D(qB^2)<0,
 \qquad D(qA^2K)<0.
\]

Hence

\[
 D^4\log(1+r_2)\le\mathcal U(x)\le\mathcal U(\pi).
\]

The primitive reserve is

\[
 V_1''''=16x+
 \frac{96x(4x^2+24x+9)}{(2x-3)^4},
\]

which decreases on the strip and satisfies

\[
 V_1''''(x)\ge V_1''''(7/2)=\frac{1939}{8}.
\]

## Exact rational endpoint

Using

\[
 \frac{333}{106}<\pi<\frac{355}{113}
\]

and a positive Taylor lower bound for `e^{3pi}` gives

\[
 p(\pi)<\frac{109}{50000}.
\]

Rational substitution into the channel formulas gives

\[
 \mathcal U(\pi)
 <\frac{29432252144493483}{125000000000000}.
\]

Therefore

\[
 \boxed{
 \frac{1939}{8}-\mathcal U(\pi)
 >\frac{864622855506517}{125000000000000}>0.
 }
\]

It follows that

\[
 \boxed{V_{\{1,2\}}''''(u)>0\qquad(0\le u\le u_*).}
\]

## Scope

This theorem concerns exactly the primitive and `n=2` theta labels. It does
not discard the modular tail and does not itself prove the completed-source
statement. Tail absorption is proved separately in
`theta-modular-tail-envelope.md`.
