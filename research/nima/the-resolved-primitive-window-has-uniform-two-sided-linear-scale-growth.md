# The resolved primitive window has uniform two-sided linear scale growth

## Resolved norm

The selected resolved primitive form is

\[
\|W_t\|_{\mathrm{res}}^2
=
(1+M_\Phi^2)\|W_t\|_2^2
+
\|BW_t\|_2^2,
\]

where the tail operator `B` is bounded on the declared window carrier.
Therefore

\[
(1+M_\Phi^2)\|W_t\|_2^2
\le
\|W_t\|_{\mathrm{res}}^2
\le
(1+M_\Phi^2+\|B\|^2)\|W_t\|_2^2.
\]

Thus resolved and ordinary window norms are uniformly equivalent on this
source family.

## Linear scale law

The exact ordinary-window calculation gives

\[
\|W_t\|_2^2
=
2t-\frac{\sqrt2}{\pi}
+O(e^{-2\pi t^2}).
\]

In particular,

\[
\frac{\|W_t\|_2^2}{t}\longrightarrow2
\]

as `t` tends to infinity. The window is nonzero for every `t>0`, and its norm
depends continuously on `t`. Hence on the closed arithmetic range

\[
t\ge\log2
\]

the positive continuous ratio `||W_t||_2^2/t` has a positive lower bound and
a finite upper bound: use compactness on `[log 2,T]` and the asymptotic bound
on `[T,infinity)`.

Consequently there are source constants `c,C>0` such that

\[
c\,t
\le
\|W_t\|_{\mathrm{res}}^2
\le
C\,t,
\qquad t\ge\log2.
\]

## Ordered source metric

Since

\[
q_t=DW_t,
\qquad
Sq_t=-2W_t,
\]

the ordered pullback norm obeys

\[
\|q_t\|_{\mathrm{ord}}^2
=\frac14\|Sq_t\|_{\mathrm{res}}^2
=\|W_t\|_{\mathrm{res}}^2.
\]

At the arithmetic label `t=k log p`, one therefore has the uniform
source-derived estimate

\[
c\,k\log p
\le
\omega_{p,k}^2
\le
C\,k\log p.
\]

This closes the two-sided estimate left open by the primitive-weight audit.

## Remaining constructor gate

The analytic norm estimate no longer blocks the interior-profile gamma-field.
The remaining obligation is functorial: prove that ordered integration on the
source front corresponds to the weighted theta-cut synthesis

\[
q_{p,k}\longmapsto\omega_{p,k}u_{p,k}
\]

in the actual Green/Weyl carrier, with reciprocal Fourier transport and cutoff
maps intertwined. Norm equivalence alone does not define this weighted target
arrow.
