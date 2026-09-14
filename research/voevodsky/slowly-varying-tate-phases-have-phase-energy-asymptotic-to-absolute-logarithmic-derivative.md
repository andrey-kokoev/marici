# Slowly varying Tate phases have phase energy asymptotic to the absolute logarithmic derivative

## Setup

Let

\[
\gamma(t)
=e^{i\theta(t)}
\]

with real smooth phase. Define

\[
\boxed{
\kappa_\gamma(t)
=
\frac1{4\pi^2}
\int_\mathbb R
\frac{
|e^{i\theta(t+r)}-e^{i\theta(t)}|^2
}{r^2}dr.
}
\]

Let

\[
a(t)
=|\theta'(t)|.
\]

We study points/sequences where

\[
a(t)
\to\infty.
\]

## Slowly varying inverse-slope hypothesis

Assume there is a function `R(t)->infinity` such that

\[
\boxed{
\sup_{|r|\le R(t)/a(t)}
\frac{
|\theta'(t+r)-
\theta'(t)|
}{a(t)}
\longrightarrow0,
}
\]

and

\[
\boxed{
\frac{R(t)}{a(t)}
\longrightarrow0
}
\]

when a local coordinate condition requires the window to shrink.

The first condition says the accumulated phase error is uniformly small on an expanding number of inverse-slope wavelengths. The prefactor `R(t)` is retained to justify passage over the expanding near region.

A sufficient differential condition is the existence of `R(t)->infinity` with

\[
\boxed{
R(t)
\sup_{|r|\le R(t)/a(t)}
\frac{|\theta''(t+r)|}{a(t)^2}
\longrightarrow0.
}
\]

## Rescaling

Write

\[
\epsilon(t)
=
\operatorname{sgn}\theta'(t)
\]

and set

\[
u
=a(t)r.
\]

Then

\[
\begin{aligned}
\frac{
\kappa_\gamma(t)
}{a(t)}
&=
\frac1{4\pi^2}
\int_\mathbb R
\frac{
\left|
 e^{i[\theta(t+u/a)-	heta(t)]}-1
\right|^2
}{u^2}du.
\end{aligned}
\]

For every fixed `u`, the slow-variation hypothesis gives

\[
\theta(t+u/a)-	heta(t)
=
\epsilon(t)u
+o(1).
\]

Hence the integrand converges pointwise to

\[
\frac{|e^{iu}-1|^2}{u^2},
\]

independently of the sign.

## Near region

Restrict first to

\[
|u|
\le
R(t).
\]

On every fixed compact `u` interval, dominated convergence applies using

\[
|e^{ix}-1|
\le
\min(2,|x|)
\]

and the local derivative control.

Letting the compact interval grow inside `R(t)` gives

\[
\boxed{
\frac1{4\pi^2}
\int_{|u|\le R(t)}
\frac{
|e^{i[\theta(t+u/a)-	heta(t)]}-1|^2
}{u^2}du
\longrightarrow
\frac1{4\pi^2}
\int_\mathbb R
\frac{|e^{iu}-1|^2}{u^2}du
}
\]

provided the intermediate tails are controlled by the same slow-variation majorant.

## Universal integral

The standard identity gives

\[
\int_\mathbb R
\frac{|e^{iu}-1|^2}{u^2}du
=2\pi.
\]

Therefore the universal local contribution is

\[
\boxed{
\frac1{2\pi}.
}
\]

## Far region

For `|u|>R(t)`, use the crude bound

\[
|e^{ix}-1|^2
\le4.
\]

Then

\[
\boxed{
\frac1{4\pi^2}
\int_{|u|>R(t)}
\frac{
|e^{i[\theta(t+u/a)-	heta(t)]}-1|^2
}{u^2}du
\le
\frac{2}{\pi^2R(t)}
\longrightarrow0.
}
\]

This tail estimate is independent of the global behavior of the phase.

## Asymptotic theorem

Combining near and far regions yields

\[
\boxed{
\kappa_\gamma(t)
=
\frac1{2\pi}
|\theta'(t)|
(1+o(1))
}
\]

along every high-slope regime satisfying the slowly varying inverse-slope hypothesis.

Equivalently, for the real Tate multiplier

\[
w_\gamma(t)
=
\theta'(t),
\]

\[
\boxed{
2\pi\kappa_\gamma(t)
\sim
|w_\gamma(t)|.
}
\]

## Exact linear calibration

For

\[
\theta(t)
=bt+	heta_0,
\]

the hypothesis is exact and

\[
\boxed{
\kappa_\gamma(t)
=
\frac{|b|}{2\pi}
}
\]

for every `t`, with no asymptotic error.

This covers ramified conductor phases.

## Archimedean gamma phase

For a regular archimedean Tate factor, Stirling asymptotics give schematically

\[
\theta'(t)
=c\log|t|
+O(1),
\]

\[
\theta''(t)
=
\frac c t
+O(t^{-2}).
\]

Therefore

\[
\frac{|\theta''(t)|}{|\theta'(t)|^2}
=
O
\left(
\frac1{|t|(\log|t|)^2}
\right)
\longrightarrow0.
\]

Choose, for example, an expanding `R(t)` satisfying

\[
R(t)^2
=o\left(|t|(\log|t|)^2ight).
\]

Then the strengthened slowly varying hypothesis holds, and

\[
\boxed{
\kappa_{\gamma_\infty}(t)
\sim
\frac1{2\pi}
|w_{\gamma_\infty}(t)|
}
\]

as `|t|->infinity` after endpoint poles are separated.

## Unramified finite-place phase

An unramified finite-place phase is periodic in `t` and has bounded first derivative because the Euler denominator stays away from zero on the unitary line.

It has no high-slope spectral-frequency regime for fixed residue cardinality. On this sector, the previous coarse bound

\[
|w_\gamma|
\le
C(1+\kappa_\gamma)
\]

suffices. No asymptotic equivalence is required.

## Placewise graph norm

For a finite semilocal set, use the local energy

\[
\kappa_{loc,S}
=
\sum_{v\in S}
\kappa_{\gamma_v}.
\]

On ramified and archimedean high-energy tails,

\[
\boxed{
2\pi\kappa_{loc,S}
\sim
\sum_{v\in S}
|w_v|
}
\]

placewise, while bounded unramified parts contribute only lower-order graph-norm constants.

Thus the local difference-row norm is asymptotically equivalent to the absolute local Tate connection norm without cancellation among places.

## Form-domain consequence

Let

\[
A_{loc}^{abs}
=
\bigoplus_{v\in S}
|A_v|
\]

on the place-resolved carrier. Under the tail equivalence and compact-region boundedness,

\[
\boxed{
D
\left(
(I+Kappa_{loc})^{1/2}
\right)
=
D
\left(
(I+A_{loc}^{abs})^{1/2}
\right)
}
\]

with equivalent graph norms.

This identifies the positive relative phase-energy completion with the natural place-resolved absolute Tate form domain.

## Product-phase caution

For the product phase, signed local slopes can cancel. Then

\[
|\sum_vw_v|
\]

may be much smaller than

\[
\sum_v|w_v|.
\]

The asymptotic equivalence is therefore asserted placewise and for the local direct-sum energy, not as a two-sided equivalence between `kappa_(Gamma_S)` and `|sum_v w_v|` in every cancellation regime.

## Quantitative error target

A source-level proof for exact gamma factors should bound

\[
\boxed{
\left|
2\pi
\frac{\kappa_\gamma(t)}{|w_\gamma(t)|}
-1
\right|
}
\]

by a modulus depending on

\[
\sup_{|r|\le R/|w|}
\frac{|w'(t+r)|}{|w(t)|^2}
\]

plus `O(1/R)`. Optimizing `R` gives explicit archimedean tail constants.

## Disposition

For every slowly varying high-slope local Tate phase,

\[
\boxed{
\kappa_\gamma(t)
\sim
\frac{|w_\gamma(t)|}{2\pi}.
}
\]

The identity is exact for ramified linear conductor phases and asymptotic for archimedean gamma phases by Stirling. Hence the placewise positive difference-row energy has the same graph-domain growth as the absolute local Tate connection, while retaining positivity before signed assembly.
