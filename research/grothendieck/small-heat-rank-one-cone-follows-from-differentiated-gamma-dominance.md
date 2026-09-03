# Small-heat rank-one cone follows from differentiated gamma dominance

## Question

Can prior broad-smoothing estimates prove any universal part of the endpoint-free cone without assuming RH?

## Claim boundary

Yes: there exists `t0>0` such that the completed arithmetic heat kernel `H(t)` is strictly decreasing on `(0,t0)`. Hence

\[
H(t)-H(t+h)>0
\]

whenever `t>0` and `t+h<t0`. This proves only the small-heat rank-one region, not rank two or the all-rank cone.

## Gamma derivative

Write

\[
K_\Gamma(t)=\frac{A(t)}{4\sqrt{\pi t}},
\]

where

\[
A(t)=-\gamma_E-\log\pi+
\int_0^\infty
\frac{e^{-r}-e^{-r/4-r^2/(16t)}}{1-e^{-r}}\,dr.
\]

The prior broad-smoothing proof gives

\[
A(t)\ge \frac12\log(1/t)-C
\]

for sufficiently small `t`. Differentiating under the integral is justified by the same `(0,t)`, `(t,1)`, `(1,infinity)` split used for gamma-kernel holomorphy, and gives

\[
A'(t)=
-\int_0^\infty
\frac{r^2}{16t^2}
\frac{e^{-r/4-r^2/(16t)}}{1-e^{-r}}\,dr<0.
\]

Therefore

\[
K_\Gamma'(t)
=\frac1{4\sqrt\pi}
\left(t^{-1/2}A'(t)-\frac12t^{-3/2}A(t)\right)
\le -\frac{t^{-3/2}}{16\sqrt\pi}
\bigl(\log(1/t)-2C\bigr).
\]

Thus the gamma derivative is negative with logarithmically growing margin relative to `t^{-3/2}`.

## Endpoint and prime derivatives

The endpoint derivative is

\[
K_E'(t)=\frac14e^{t/4}=O(1).
\]

For the prime term, differentiating each log-Gaussian summand gives a polynomial factor in `t^{-1}` multiplying

\[
\exp\!\left(-\frac{(\log n)^2}{4t}\right).
\]

Since the first displacement is `log 2`, the same logarithmic-integral comparison as in the broad-smoothing packet yields constants `C1,C2,c>0` with

\[
|K_P'(t)|
\le C_1t^{-C_2}e^{-c/t}
\]

for sufficiently small `t`. Termwise differentiation is dominated by this bound.

Consequently the negative gamma derivative eventually dominates both the bounded endpoint derivative and the exponentially suppressed prime derivative:

\[
H'(t)=K_E'(t)+K_\Gamma'(t)+K_P'(t)<0
\]

on some interval `(0,t0)`.

## Strongest falsification attempt

The argument does not extend to arbitrary `t`: the prime derivative is no longer exponentially suppressed, and the gamma logarithmic margin is a small-heat effect. It also says nothing about the rank-two determinant, where cross-time products appear. Thus it cannot be promoted to an RH proof or an all-rank factorization.

## Disposition

Record the small-heat rank-one region as an unconditional theorem. The first remaining scalar region is `t+h>=t0`; the first nonlinear obstruction remains rank two even inside the small-heat range.