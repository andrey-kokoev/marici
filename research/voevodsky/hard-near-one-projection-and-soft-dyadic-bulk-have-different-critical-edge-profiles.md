# Hard near-one projection and soft dyadic bulk have different critical edge profiles

## Finite dyadic residual

For a positive contraction `B`, the first `n` dyadic defect levels satisfy

\[
\sum_{j=0}^{n-1}
B^{2^j}
(I-B^{2^j})
=
B-B^{2^n}.
\]

Set

\[
m=2^n.
\]

Then the soft dyadic bulk has weight

\[
b_m^{soft}(\lambda)
=\lambda^m
\]

and the soft residual has weight

\[
\boxed{
r_m^{soft}(\lambda)
=\lambda-\lambda^m.
}
\]

## Hard residual

Choose a threshold

\[
\delta_m
=
\frac a m
\]

with fixed `a>0`. The hard near-one bulk projection is

\[
E_m^{hard}
=1_{[1-a/m,1]}(B).
\]

The corresponding positive residual weight is

\[
\boxed{
r_{m,a}^{hard}(\lambda)
=
\lambda1_{\{m(1-\lambda)>a\}}.
}
\]

The strict or non-strict endpoint convention is immaterial unless the spectral measure has an atom exactly at the threshold.

## Critical edge coordinate

Introduce

\[
\boxed{
x
=m(1-\lambda).
}
\]

For fixed `x>=0`,

\[
\lambda
=1-
\frac xm
\]

and

\[
\lambda^m
=
\left(
1-
\frac xm
\right)^m
\longrightarrow
e^{-x}.
\]

Therefore the soft residual profile converges to

\[
\boxed{
r^{soft}(x)
=1-e^{-x},
}
\]

whereas the hard residual profile converges to

\[
\boxed{
r_a^{hard}(x)
=1_{\{x>a\}}.
}
\]

## Difference profile

Their critical-scale difference is

\[
\boxed{
D_a(x)
=1-e^{-x}
-
1_{\{x>a\}}.
}
\]

Explicitly,

\[
D_a(x)
=
\begin{cases}
1-e^{-x},&0\le x\le a,\\
-e^{-x},&x>a.
\end{cases}
\]

This function is not zero. It has positive mass below the hard threshold and negative mass above it.

Thus matching the nominal scales

\[
\delta_m
\asymp
m^{-1}
\]

does not make the two residual filters pointwise asymptotic.

## Observer-weighted edge measure

For observer pair `g,h`, let

\[
\mu_{\Lambda,g,h}(E)
=
\operatorname{Tr}
\left(
A_h^*
E_{B_\Lambda}(E)
A_g
\right).
\]

Along a joint path `m=m(Lambda)`, push this measure forward by

\[
x=m(1-\lambda)
\]

and denote the resulting measure by

\[
\nu_{\Lambda,g,h}^{(m)}.
\]

Then the difference between soft and hard residual Gram forms is exactly

\[
\boxed{
\begin{aligned}
&K_{\Lambda,m}^{soft}(g,h)
-
K_{\Lambda,m,a}^{hard}(g,h)\\
&\quad=
\int
\left[
\lambda-\lambda^m
-
\lambda1_{\{m(1-\lambda)>a\}}
\right]
d\mu_{\Lambda,g,h}(\lambda).
\end{aligned}
}
\]

At critical scaling the bracket tends to `D_a(x)`.

## Limit criterion

Suppose the pushed-forward measures converge weakly on the edge region:

\[
\nu_{\Lambda,g,h}^{(m)}
\Longrightarrow
\nu_{g,h}.
\]

Under uniform integrability sufficient to pass the bounded edge profile to the limit,

\[
\boxed{
K_{\Lambda,m}^{soft}(g,h)
-
K_{\Lambda,m,a}^{hard}(g,h)
\longrightarrow
\int_0^\infty
D_a(x)d\nu_{g,h}(x).
}
\]

Consequently hard and soft bulk removal are asymptotically equivalent exactly when

\[
\boxed{
\int_0^\infty
D_a(x)d\nu_{g,h}(x)
=0
}
\]

for every observer pair in the source domain.

This is an additional moment identity, not a consequence of `delta approximately 1/m`.

## Threshold calibration

For one positive diagonal observer measure, the equation

\[
\int D_ad\nu_{g,g}
=0
\]

may determine a threshold `a=a_g`. But a physical bulk projection must use one threshold independent of the observer.

A universal `a` requires

\[
\boxed{
\int D_ad\nu_{g,h}=0
\quad
\text{for all }g,h.
}
\]

This can occur if, for example, the edge measures factor as

\[
\nu_{g,h}
=G(g,h)\rho
\]

with one universal scalar profile `rho` and `a` is calibrated against `rho`. Without such factorization, observer-dependent thresholds are unavoidable and do not define one spectral projection of `B_Lambda`.

## Exact meet endpoint

For fixed cutoff and `m->infinity`,

\[
\lambda^m
\to
1_{\{1\}}(\lambda).
\]

Then both a hard threshold tending all the way to zero and the soft filter approach the exact meet atom. But this terminal fixed-cutoff regime is different from the critical joint edge regime where `x=m(1-lambda)` remains finite.

## Canonical status of the soft tower

The soft dyadic tower is canonical once `B` is given:

\[
B
=
B^m
+
(B-B^m).
\]

It also carries exact isometric transition maps between depths. No threshold convention is required.

The hard projection is orthogonal but introduces the extra scalar parameter `a` and a discontinuous filter. It is canonical only after the edge law selects `a`.

Therefore the positive filtered/pro-simplicial construction should retain the soft dyadic bulk as primary. A hard orthogonal bulk projection is a derived object, not prior data.

## Consequence for absolute-Gram convergence

Suppose the soft residual converges to the absolute Tate form:

\[
K_{\Lambda,m}^{soft}
\to
q_{|A_S|}.
\]

Then the hard residual converges instead to

\[
\boxed{
q_{|A_S|}
-
\left[
(g,h)
\mapsto
\int D_ad\nu_{g,h}
\right].
}
\]

Thus replacing the soft tower by a hard projection can alter the finite positive boundary form even though both use the same nominal gap scale.

## Bounds away from the edge

For `x=m(1-lambda)`, elementary estimates give

\[
\lambda^m
\le
e^{-x}
\]

for `0<=lambda<=1`. Hence:

- above the threshold, the soft bulk tail decays exponentially in `x`;
- below the threshold, the soft residual behaves as `1-e^(-x)` and is of order `x` near zero.

Therefore differences outside a bounded critical `x` interval can be controlled. All nontrivial regulator dependence is concentrated in the transition-band edge measure.

## Revised acceptance test

A source-derived near-one theorem must provide:

1. a joint scale `m(Lambda)`;
2. polarized weak convergence of `nu_(Lambda,g,h)^(m)`;
3. uniform integrability outside compact `x` intervals;
4. angular-character summability;
5. either retention of the soft profile or a universal hard-threshold moment identity.

Without item 5, “orthogonal hard bulk removal” and “dyadic bulk removal” define different positive fillers.

## Disposition

At critical near-one scaling,

\[
\boxed{
\text{soft residual profile}
=1-e^{-x},
\qquad
\text{hard residual profile}
=1_{\{x>a\}}.
}
\]

Their difference generally survives the cutoff limit. The soft dyadic tower is canonical; a hard bulk projection requires additional edge-law calibration and must not be assumed equivalent merely because `delta_Lambda approximately 2^(-n(Lambda))`.
