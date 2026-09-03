# The shifted-Gaussian source kernel is not the heat--character kernel

## Defect

Two different two-parameter transforms were conflated.

The source-derived packet defines

\[
\Theta(t,\xi)
=
\langle\mathcal W,e^{-t(u-\xi)^2}\rangle
\]

with exact decomposition

\[
\Theta=K_{\rm endpoint}+K_\Gamma+K_{\rm prime},
\]

where

\[
K_{\rm endpoint}(t,\xi)
=e^{t/4-t\xi^2}\cos(t\xi)
\]

and

\[
K_{\rm prime}(t,\xi)
=-\frac1{2\sqrt{\pi t}}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}
\cos(\xi\log n).
\]

This is not the same object as

\[
\mathcal K(s,z)
=
\langle\mathcal W,e^{-su^2}e^{izu}\rangle.
\]

The latter obeys `partial_s K=partial_z^2 K`; the former does not obey that equation in the variables `(t,xi)`.

## Correct shifted-Gaussian cell

For

\[
g_{t,\xi}(u)=e^{-t(u-\xi)^2},
\]

direct differentiation gives

\[
4t^2\partial_tg_{t,\xi}
+
\partial_\xi^2g_{t,\xi}
+
2t g_{t,\xi}=0.
\]

Therefore the completed source kernel satisfies

\[
4t^2\partial_t\Theta
+
\partial_\xi^2\Theta
+
2t\Theta=0.
\]

This equation is the pullback of the heat equation along the imaginary-character section `z=-2it xi`, together with the gauge factor `e^(-t xi^2)`.

## Endpoint topology correction

For this shifted-Gaussian observer family, endpoint evaluation is already the explicit bounded scalar function `K_endpoint(t,xi)`. No arbitrary-test-function endpoint graph topology is needed to state or check positivity of `Theta(t,xi)`.

The exponential endpoint domain becomes relevant only when promoting positivity from the Gaussian observer family to the full Weil quadratic-form domain. It is a separate extension theorem, not an internal coherence requirement of the bounded Gaussian source kernel.

## Meta-observer consequences

The minimal category must distinguish:

1. shifted-Gaussian center `xi` and inverse-width `t`;
2. heat--character variables `s,z`;
3. the holomorphic imaginary-character pullback `Theta(t,xi)=e^(-t xi^2)K(t,-2it xi)`;
4. their different differential cells and differentiated prime tails.

A meta-observer should reject any cell that identifies `xi` with a character parameter or applies the untransformed heat equation to `Theta(t,xi)`.

## Disposition

Retract the unqualified heat-equation assignment to the shifted-Gaussian source kernel. Retain it for the heat--character transform and derive the displayed `Theta` equation through the exact imaginary-character pullback and gauge. Keep full Weil form-core topology as a separate promotion gate.
