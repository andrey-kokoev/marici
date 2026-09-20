# The chart-zero rigged crossing of the Clark primitive has an explicit shell packet

## Setup

Fix a shell `[a,b]`, a seam `c`, and a regular first leg `f`. Write

\[
K_{1,c}(y)=-\frac12|y-c|+\delta_c(y).
\]

The regular pair-to-border formulas extend distributionally in the second leg.
It is enough to compute the chart-zero packet; the other three charts follow
by the declared Fourier covariance.

## Delta leg

For `t>=0`,

\[
\rho_{f,\delta_c}^{[a,b]}(t)
=\int_a^b f(x)\delta(x+t-c)\,dx
=f(c-t)\mathbf1_{[c-b,c-a]}(t),
\]

with endpoint half-values interpreted in the fixed wall convention.

The endpoint distribution is

\[
e_{f,\delta_c}^{[a,b]}(t)
=\frac12\left[
 f(b)\delta(t-(c-b))-f(a)\delta(t-(c-a))
\right].
\]

Rather than multiply boundary distributions, define the Wronskian coordinate
by the exact Stokes relation

\[
w_{f,\delta_c}=2(e_{f,\delta_c}-\partial_t\rho_{f,\delta_c}).
\]

Its Laplace coordinates are therefore

\[
R_{f,\delta_c}(z)
=\int_{[c-b,c-a]\cap[0,\infty)}
 e^{-zt}f(c-t)\,dt,
\]

\[
E_{f,\delta_c}(z)
=\frac12\left[
f(b)e^{-z(c-b)}\mathbf1_{c\ge b}
-f(a)e^{-z(c-a)}\mathbf1_{c\ge a}
\right],
\]

and

\[
W_{f,\delta_c}(z)
=2\bigl(E_{f,\delta_c}(z)-zR_{f,\delta_c}(z)
+\rho_{f,\delta_c}(0)\bigr).
\]

## Absolute-value leg

Set

\[
\rho_{f,K_c}^{[a,b]}(t)
=\int_a^b f(x)|x+t-c|\,dx,
\]

\[
e_{f,K_c}^{[a,b]}(t)
=\frac12\left[
f(b)|b+t-c|-f(a)|a+t-c|\right].
\]

These are locally absolutely continuous with polynomial growth and have
Laplace transforms on the stable chart. Again define

\[
w_{f,K_c}=2(e_{f,K_c}-\partial_t\rho_{f,K_c}),
\]

which agrees with the direct distributional Wronskian because
`partial_y |y-c|=sgn(y-c)`.

## Primitive packet

By linearity,

\[
(\rho_0,E,W,R)_{f,K_{1,c}}
=(\rho_0,E,W,R)_{f,\delta_c}
-\frac12(\rho_0,E,W,R)_{f,K_c}.
\]

Every component is now an explicit integral or endpoint value of the regular
first leg. No unspecified partial-transpose kernel remains in chart zero.

The combined return is

\[
\mathcal J_{RL}(f,K_{1,c};z)
=R_{f,K_{1,c}}(z)+2E_{f,K_{1,c}}(z).
\]

## Prime-shell simplification

If the seam lies strictly to the left of a positive shell, `c<a`, then the
delta correlation and endpoint packets vanish for `t>=0`. If the seam is the
right shell endpoint, `c=b`, then

\[
R_{f,\delta_b}(z)=\int_0^{b-a}e^{-zt}f(b-t)\,dt,
\]

\[
E_{f,\delta_b}(z)=\frac12f(b)
-\frac12f(a)e^{-z(b-a)}.
\]

Thus the moving endpoint delta contributes a genuine shell history rather
than only a point evaluation.

## Next exact comparison

Insert `f=u_-` or `u_+` and the source-prescribed shell seam `c`. The
transverse difference of the two resulting packets is then an explicit
functional of the two stable histories. Its dependence on

\[
u_-(0;z)-u_+(0;z)=\tau(z)
\]

can now be tested directly, without invoking canonical Stokes cancellation.