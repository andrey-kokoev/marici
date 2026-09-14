# In the regular half-line model the two-cutoff sewing localizes to one boundary integral and vanishes by oscillation

## Model

Work on `L2(R)` in a logarithmic translation coordinate. Let

\[
P_L=1_{(-\infty,L]},
\qquad
A_{L,M}=P_M-P_L=1_{(L,M]},
\]

with `M>L`. Let `Q_T` be a translation-invariant orthogonal projection with convolution kernel `q_T`, and let `A_g` be convolution by `g`.

Set

\[
H_g=A_gA_g^*,
\]

whose convolution kernel is

\[
h=g*g^*.
\]

The regulated sewing trace is

\[
\boxed{
\mathcal E_{L,M,T}(g)
=
\operatorname{Tr}
\left(
P_LQ_TA_{L,M}H_g
\right).
}
\]

This cross-boundary product can be trace class because `A_(L,M)` has finite width. The individual half-line leg `Q_TP_LA_g` is generally not Hilbert--Schmidt in this Haar-translation model, so the expression must not be introduced as an ordinary Hilbert--Schmidt inner product.

## Trace-kernel formula

Since `Q_T` is a projection,

\[
\begin{aligned}
\mathcal E_{L,M,T}(g)
&=
\operatorname{Tr}
\left(
A_g^*P_LQ_TA_{L,M}A_g
\right)\\
&=
\operatorname{Tr}
\left(
P_LQ_TA_{L,M}H_g
\right).
\end{aligned}
\]

The diagonal kernel gives

\[
\boxed{
\mathcal E_{L,M,T}(g)
=
\int_{x\le L}
\int_{L<y\le M}
q_T(x-y)h(y-x)dydx.
}
\]

This formula is absolutely meaningful when `h` has compact support and `q_T` is locally bounded with the usual projection-kernel estimates.

## Boundary-overlap weight

Set

\[
u=x-y.
\]

For fixed `u`, the conditions

\[
x\le L,
\qquad
L<x-u\le M
\]

have no solutions unless `u<0`. For `u<0`, their `x`-measure is

\[
\boxed{
m_{M-L}(u)
=
\min(-u,M-L).
}
\]

Therefore

\[
\boxed{
\mathcal E_{L,M,T}(g)
=
\int_{u<0}
\min(-u,M-L)
q_T(u)h(-u)du.
}
\]

The expression is independent of the boundary location `L`; only the annular width `M-L` remains.

## Stabilization of the outer cutoff

Assume

\[
\operatorname{supp}h
\subset[-R_h,R_h].
\]

If

\[
M-L
\ge R_h,
\]

then on the support of the integrand

\[
\min(-u,M-L)
=-u.
\]

Hence

\[
\boxed{
\mathcal E_{L,M,T}(g)
=
\int_{u<0}
(-u)q_T(u)h(-u)du
}
\]

for every sufficiently wide annulus.

Thus the second cutoff is needed for typing, but its value disappears exactly after it exceeds the observer propagation radius.

## Sinc Fourier cutoff

For the standard real Fourier cutoff,

\[
q_T(u)
=
\frac{
\sin(Tu)
}{
\pi u
}.
\]

The factor `-u` cancels the kernel singularity:

\[
\boxed{
\mathcal E_{L,M,T}(g)
=-
\frac1\pi
\int_{u<0}
\sin(Tu)h(-u)du.
}
\]

If `h` is smooth and compactly supported, the Riemann--Lebesgue lemma gives

\[
\boxed{
\mathcal E_{L,M,T}(g)
\longrightarrow0
\qquad(T\to\infty).
}
\]

Repeated integration by parts gives rapid decay when the extension of `h(-u)1_(u<0)` has vanishing boundary jets at zero. Without those jet conditions, the decay rate is controlled by the boundary value `h(0)`.

## Boundary value asymptotic

For smooth `h`, integration by parts on the negative half-line gives, under the displayed convention,

\[
\int_{-\infty}^0
\sin(Tu)h(-u)du
=
-
\frac{h(0)}{T}
+O_h(T^{-2})

\]

when the support boundary terms vanish. Hence

\[
\boxed{
\mathcal E_{L,M,T}(g)
=
\frac{h(0)}{\pi T}
+O_h(T^{-2}).
}
\]

The precise sign depends on the Fourier and inner-product conventions; vanishing is convention-independent.

## Interpretation

In this regular translation model:

1. the finite annular regulator makes the combined cross-boundary trace meaningful, without making the infinite half-line leg Hilbert--Schmidt;
2. the outside regulator stabilizes once wider than observer propagation;
3. sewing is supported at the shared physical boundary;
4. Fourier oscillation kills the sewing as bandwidth tends to infinity.

Therefore the positive triple compression and product cutoff have the same finite part in this elementary model.

## Why this does not settle the semilocal case

After the Radon--Nikodym transform of `L2(X_S)`, the physical cutoff is a logarithmic half-line, but the transported additive Fourier projection is not known to be translation-invariant in that logarithmic coordinate.

Its kernel also couples:

- the norm-one compact directions;
- finite-place valuation shells;
- the `S`-unit quotient orbits.

Thus one cannot substitute a scalar sinc kernel `q_T(x-y)` in the semilocal trace.

The model identifies the exact semilocal statement to seek: after orbit decomposition and boundary recentering, the Fourier kernel should have enough oscillation/Schwartz decay that the weighted boundary integral tends to a controlled limit.

## Semilocal target

For each `S`-unit orbit `q`, seek a recentered boundary kernel `q_(Lambda,S,q)(u;omega,omega')` such that the regulated sewing term has the form

\[
\mathcal E_{\Lambda,R,S}(g)
=
\sum_q
\int_{u<0}
(-u)
q_{\Lambda,S,q}
(u;\omega,\omega')
H_{g,q}
(-u;\omega',\omega)
d\nu,
\]

once `log R-log Lambda` exceeds the radial propagation of the observer.

The required estimate is a summable bound in `q` and angular variables, followed by convergence of the oscillatory radial integral.

## Consequence for scale correlation

For compactly supported radial propagation, any correlated scale satisfying

\[
\log R-
\log\Lambda
\longrightarrow\infty
\]

is sufficient to remove the outer cutoff from the stabilized sewing formula. The power law

\[
R=\Lambda^\rho,
\qquad
\rho>1,
\]

is convenient but not canonical.

This weakens the earlier suggestion that one special ratio, such as `rho=2`, should be geometrically preferred.

## Disposition

The observer-weighted two-cutoff sewing problem is solved in the regular half-line/sinc model:

\[
\boxed{
\mathcal E_{L,M,T}(g)
=
-
\frac1\pi
\int_{u<0}
\sin(Tu)h(-u)du
\longrightarrow0.
}
\]

The remaining semilocal gate is to derive the analogous recentered boundary-kernel formula from Connes's quotient Fourier transform and prove geometric summability over `O_S*`.
