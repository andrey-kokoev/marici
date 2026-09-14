# An inverse-slope interval bound makes the positive phase energy dominate the Tate logarithmic derivative

## Phase and energy density

Let

\[
\gamma(t)
=e^{i\theta(t)}
\]

with real `theta in C2(R)`. Define

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

The signed Tate multiplier is

\[
\boxed{
w_\gamma(t)
=\theta'(t)
=
\frac1i
\partial_t
\log\gamma(t).
}
\]

The goal is a pointwise estimate

\[
|w_\gamma(t)|
\le
C
(1+\kappa_\gamma(t)).
\]

## Derivative-regularity hypothesis

Assume

\[
\boxed{
|	heta''(u)|
\le
M
(1+|\theta'(u)|)^2
}
\]

for all real `u`, with fixed `M`.

This permits derivative growth but prevents the phase slope from changing by its full magnitude on a scale much shorter than the inverse slope.

## Small-slope case

Fix `t` and put

\[
a
=|\theta'(t)|.
\]

If

\[
a\le1,
\]

then trivially

\[
\boxed{
a
\le
1+\kappa_\gamma(t).
}
\]

Only `a>1` requires an energy estimate.

## Inverse-slope interval

Assume `a>1`. Choose

\[
\delta
=
\frac{c_M}{a}
\]

with `c_M>0` sufficiently small depending only on `M`.

A bootstrap using the differential inequality shows that on

\[
|r|
\le
\delta,
\]

one has

\[
\boxed{
\frac a2
\le
|\theta'(t+r)|
\le
2a
}
\]

and the derivative keeps the sign of `theta'(t)`.

Indeed, while `|theta'|<=2a`,

\[
|	heta''|
\le
M(1+2a)^2
\le
9Ma^2.
\]

Hence over distance `c_M/a`, the derivative changes by at most

\[
9Mc_Ma.
\]

Choosing

\[
c_M
\le
\frac1{18M}
\]

makes this at most `a/2` and closes the bootstrap.

## Phase increment

For `0<=r<=delta`, monotonicity on the interval gives

\[
\boxed{
\frac a2r
\le
|\theta(t+r)-\theta(t)|
\le
2ar.
}
\]

Further choose

\[
c_M
\le
\frac\pi8.
\]

Then

\[
|\theta(t+r)-\theta(t)|
\le
\frac\pi4
\]

on the interval.

For `|x|<=pi/2`,

\[
|e^{ix}-1|
=2|\sin(x/2)|
\ge
\frac2\pi|x|.
\]

Therefore

\[
\boxed{
|e^{i\theta(t+r)}-e^{i\theta(t)}|
\ge
\frac a\pir.
}
\]

## Energy lower bound

Restrict the phase-energy integral to `0<r<delta`:

\[
\begin{aligned}
\kappa_\gamma(t)
&\ge
\frac1{4\pi^2}
\int_0^\delta
\frac{
(a r/\pi)^2
}{r^2}dr\\
&=
\frac1{4\pi^4}
a^2\delta\\
&=
\frac{c_M}{4\pi^4}
a.
\end{aligned}
\]

Hence

\[
\boxed{
a
\le
\frac{4\pi^4}{c_M}
\kappa_\gamma(t)
}
\]

when `a>1`.

Combining small and large slopes gives

\[
\boxed{
|	heta'(t)|
\le
C_M
(1+\kappa_\gamma(t)),
}
\]

where one may take

\[
C_M
=
\max
\left(
1,
\frac{4\pi^4}{c_M}
\right),

\qquad
c_M
=
\min
\left(
\frac1{18M},
\frac\pi8
\right).
\]

The constants are deliberately coarse.

## Integrated form bound

For observer functions `m_g,m_h`, the pointwise estimate gives

\[
\begin{aligned}
\left|
\int
\overline{m_h}
m_gw_\gamma
\right|
&\le
C_M
\int
|m_h|
|m_g|
(1+\kappa_\gamma)\\
&\le
C_M
\|m_h\|_{L^2(1+\kappa)}
\|m_g\|_{L^2(1+\kappa)}.
\end{aligned}
\]

Thus

\[
\boxed{
|q_{Tate}(g,h)|
\le
C_M
\|g\|_{\mathcal D_D}
\|h\|_{\mathcal D_D}.
}
\]

The signed Tate cross form extends continuously to the positive difference-energy graph domain.

## Linear conductor phases

For a ramified nonarchimedean character,

\[
\theta_\chi(t)
=-f(\chi)\log qt
+
\theta_0.
\]

Then

\[
\theta''=0
\]

and the hypothesis holds with any `M>0`. The exact energy is

\[
\kappa_\gamma
=
\frac{
|f(\chi)\log q|
}{2\pi}.
\]

Thus conductor growth is controlled exactly by the positive relative phase energy:

\[
\boxed{
|w_\chi|
=2\pi\kappa_{\gamma_\chi}.
}
\]

This shows that the difference-energy graph norm automatically carries the conductor weight missing from the unweighted Plancherel norm.

## Archimedean Tate phases

For archimedean gamma factors, Stirling and polygamma estimates give schematically

\[
|	heta'(t)|
\lesssim
1+\log(1+|t|),
\]

\[
|	heta''(t)|
\lesssim
(1+|t|)^{-1}
\]

away from separated endpoint poles. Hence

\[
|	heta''(t)|
\le
M
(1+|\theta'(t)|)^2
\]

for some finite `M` after compact-region maximization.

Therefore the inverse-slope lemma applies to the regular archimedean phase.

Exact `M` depends on the gamma normalization and should be derived from the selected digamma/trigamma bounds.

## Unramified finite-place phases

The unramified local phase is a rational Poisson-type function of

\[
e^{it\log q}.
\]

For fixed `q`, its first and second derivatives are bounded because `q^(-1/2)<1` keeps denominators away from zero. Thus the derivative-regularity hypothesis holds with a finite place-dependent constant.

For a fixed finite set `S`, the product phase obeys a corresponding bound after combining local derivatives. Uniformity over changing place sets requires separate estimates.

## Product phases

If

\[
\theta
=
\theta_1+
\cdots+
\theta_r,
\]

then

\[
\theta'
=
\sum_j
\theta_j',
\qquad
\theta''
=
\sum_j
\theta_j''.
\]

Cancellation among the first derivatives can only make `|theta'|` smaller, where the additive `1` handles the estimate. However, a uniform global constant `M` for the product does not follow mechanically from separate bounds when large local slopes cancel.

For each fixed semilocal set and conductor sector, compact/local estimates supply a finite `M`. Uniformity under place enlargement remains filtered.

## Branch and endpoint caveat

The lemma requires a `C2` real phase. Winding jumps and meromorphic endpoint crossings must first be split into finite-rank/index channels.

The positive norm of those channels is added separately to `D_D`. Distributional delta derivatives are not inserted into `kappa_gamma` as ordinary functions.

## Stronger than Plancherel semiboundedness

The Plancherel common-edge approach required a uniform lower bound on `w_gamma`, which fails with unbounded conductor.

The difference-energy metric instead grows like `|w_gamma|` on linear conductor phases. Hence it controls both signs:

\[
\boxed{
|A_S|
\preceq
C
(I+Kappa_S)
}
\]

on each filtered semilocal phase class satisfying the derivative hypothesis.

This provides the natural weighted graph carrier for global relative minimalization.

## What remains source-dependent

To apply the theorem with one declared global constant, verify from the exact local factors:

1. a `C2` phase branch after endpoint extraction;
2. polynomial/digamma derivative bounds;
3. the differential inequality with constants controlled on conductor/place filtrations;
4. angular summability in the resulting weighted domain.

The functional-analytic implication is otherwise complete.

## Disposition

Under

\[
\boxed{
|	heta''|
\le
M
(1+|\theta'|)^2,
}
\]

the positive relative phase-energy density controls the signed Tate multiplier:

\[
\boxed{
|w_\gamma(t)|
\le
C_M
(1+\kappa_\gamma(t)).
}
\]

Hence the Tate--Weil cross form extends continuously to the canonical positive difference-row graph completion. Ramified conductor phases satisfy the estimate exactly, and regular archimedean/unramified phases satisfy it under standard derivative bounds.
