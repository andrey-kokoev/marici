# Primitive theta flux is a moving-wall third difference

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact reduction with one remaining sign theorem

## Fixed carrier and moving wall

For the primitive endpoint family, write

\[
c=e^{2a},
\qquad
v=u+a.
\]

Up to a positive factor independent of the moment order, every member is a
translation of the same carrier

\[
F(v)=e^{5v/2}\left(2e^{2v}-3\right)e^{-e^{2v}}.
\]

Its moments are therefore

\[
M_k(a)=\int_a^\infty(v-a)^kF(v)\,dv.
\]

For every $k\ge1$, differentiation under the integral gives the exact
moving-wall recursion

\[
M_k'(a)=-kM_{k-1}(a).
\]

No theta sum, incomplete-gamma differentiation, or numerical approximation
remains in this identity.  Changing the apparent source parameter is exactly
translation of the observation wall through one fixed carrier.

## Flux derivative

Define

\[
\Omega(a)=
\log\frac{M_8M_4}{M_6^2}
-\log\frac{M_{10}M_6}{M_8^2}.
\]

The wall recursion gives

\[
\Omega'(a)=
-4\frac{M_3}{M_4}
+18\frac{M_5}{M_6}
-24\frac{M_7}{M_8}
+10\frac{M_9}{M_{10}}.
\]

Put

\[
h_k(a)=k\frac{M_{k-1}(a)}{M_k(a)}.
\]

Then

\[
\Omega'(a)
=-h_4+3h_6-3h_8+h_{10}.
\]

Thus monotonicity of the primitive cubic flux is exactly one step-two third
finite difference of source-derived wall-response rates.

Integration by parts supplies their score meaning.  If

\[
\sigma(v)=\frac{F'(v)}{F(v)},
\]

and $Q_{k,a}$ is the probability law proportional to
$(v-a)^kF(v)\,dv$, then

\[
h_k(a)=-\mathbb E_{Q_{k,a}}\sigma.
\]

The remaining sign is therefore a third-order transport statement for one
decreasing carrier score under successive residual-power biases.

## Boundary regimes

At $c\downarrow3/2$, the carrier vanishes linearly at the wall.  At
$c\to\infty$, the residual law approaches an exponential law.  In that
limit

\[
\Omega(a)\longrightarrow
\log\frac{784}{675}>0,
\]

while $\Omega'(a)\to0$.  A diagnostic sweep finds both
$\Omega(a)>0$ and $\Omega'(a)>0$ from $c=1.500001$ through $c=200$.

## Continuous exponent exposes the required order

Extend the wall response continuously by

\[
h(q,a)=-\mathbb E_{Q_{q,a}}\sigma,
\]

where $Q_{q,a}$ has density proportional to
$(v-a)^qF(v)\,dv$, and put

\[
H=\log(v-a).
\]

Standard differentiation of this exponential family gives

\[
\frac{\partial^3}{\partial q^3}h(q,a)
=-\operatorname{cum}_{Q_{q,a}}(\sigma,H,H,H).
\]

The step-two finite-difference identity is

\[
\Omega'(a)
=\int_{[0,2]^3}
\frac{\partial^3}{\partial q^3}
h(4+s_1+s_2+s_3,a)
\,ds_1ds_2ds_3.
\]

Hence the desired monotonicity follows from the source-local mixed-cumulant
orientation

\[
\operatorname{cum}_{Q_{q,a}}(\sigma,H,H,H)<0
\qquad
4\le q\le10.
\]

The pointwise condition is sufficient rather than necessary; the exact
requirement is negativity after the cubic B-spline average above.  This
identifies the natural proof order: a four-copy oriented transport, not a
two-copy covariance or three-copy skewness argument.

## Far-wall coefficient is exactly positive

Set $r=y/(2c)$ and expand the fixed carrier relative to the moving wall.  Its
log-density ratio is

\[
\log\frac{F(a+r)}{F(a)}
=-y+\frac{A_1(y)}c+\frac{A_2(y)}{c^2}
+\frac{A_3(y)}{c^3}+O(c^{-4}),
\]

where

\[
A_1=\frac94y-\frac12y^2,
\qquad
A_2=\frac32y-\frac16y^3,
\]

and

\[
A_3=\frac94y-\frac34y^2-\frac1{24}y^4.
\]

Integrating the exponential expansion against the gamma carrier
$y^ke^{-y}\,dy$ gives rational asymptotic coefficients for every $M_k$ and
$h_k$.  Under the cubic combination

\[
-h_4+3h_6-3h_8+h_{10},
\]

the first two ratio coefficients cancel exactly.  The next combined
coefficient is $32$, and the leading factor $2c$ yields

\[
\Omega'(a)=\frac{64}{c^2}+O(c^{-3}).
\]

Therefore the flux is increasing for all sufficiently remote walls.  The
first nonzero response appears only after three lower asymptotic layers
cancel, matching the order-four cumulant diagnosis above.  An explicit
uniform remainder bound is still needed to turn “sufficiently remote” into a
numerical analytic threshold.

## Explanation and obstacle

The flux is no longer an unexplained four-moment coincidence.  It is the
response of moment curvature to moving a hard observation wall through a
fixed superexponential carrier.

The singular remaining theorem is

\[
-h_4(a)+3h_6(a)-3h_8(a)+h_{10}(a)>0
\qquad
a>\frac12\log(3/2).
\]

Ordinary monotonicity of $h_k$, log-concavity of the carrier, and increasing
hazard do not determine a third finite difference.  The proof must use a
stronger property of this explicit carrier—an order-four signed cumulant or
equivalently a four-copy oriented representation of its residual-power
transport.

This is the real analytic obstacle.  Solving it proves monotonicity of the
whole primitive endpoint family; falsifying it returns the first endpoint at
which the proposed stiffness explanation fails.

## Reproduction

Run

```powershell
python research/grothendieck/checkers/theta_primitive_endpoint_flux.py
python research/grothendieck/checkers/theta_primitive_far_wall_asymptotic.py
```

The sweep is reconnaissance.  It is not substituted for the uniform sign
theorem.
