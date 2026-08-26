# Positive translate labels and a complete moment tower do not constrain the divisor

## Bounded question

Do positive translated source labels, an augmentation readout, and the complete
logarithmic moment tower supply any zero-confinement force before modular
sewing?

## Positive translate-labelled hostile packet

Fix

\[
0<\varepsilon<1,
\qquad
0<q<\frac1{\sqrt2},
\]

and define

\[
g_{\varepsilon,q}(x)
=
e^{-x^2}
+\frac{\varepsilon}{2}e^{-(x-q)^2}
+\frac{\varepsilon}{2}e^{-(x+q)^2}.
\]

This is a positive finite packet of three translated Gaussian labels. It may
also be written as

\[
g_{\varepsilon,q}(x)
=
e^{-x^2}
\left[1+\varepsilon e^{-q^2}\cosh(2qx)\right].
\]

## Uniform strict log-concavity

After removing the common Gaussian, the remaining logarithm is the log-sum-exp
of three affine functions whose slopes are (0,2q,-2q). The second derivative
of a log-sum-exp is the variance of its slopes. Since a variable supported in
an interval of length (4q) has variance at most (4q^2),

\[
(\log g_{\varepsilon,q})''(x)
\le
-2+4q^2<0.
\]

Thus the hostile packet is uniformly strictly log-concave as well as positive,
even, smooth, and Schwartz.

## Exact transform and off-axis zeros

For

\[
F_{\varepsilon,q}(z)
=
\int_{\mathbb R}g_{\varepsilon,q}(x)e^{izx}\,dx,
\]

translation of the Gaussian gives

\[
F_{\varepsilon,q}(z)
=
\sqrt\pi e^{-z^2/4}
\left[1+\varepsilon\cos(qz)\right].
\]

Its zeros are

\[
z_{n,\pm}
=
\frac{(2n+1)\pi}{q}
\pm
\frac{i}{q}\operatorname{arcosh}(1/\varepsilon),
\qquad n\in\mathbb Z.
\]

They form explicit conjugation and reflection packets away from the real axis.

## Complete labelled observation still has no divisor force

Let (e_r) denote the label at translation coordinate (r\in\{-q,0,q\}).
On their span define

\[
\epsilon(e_r)=1,
\qquad
Le_r=re_r,
\qquad
\mu_k(v)=\epsilon L^kv.
\]

The three moments (mu_0,\mu_1,\mu_2) recover every coefficient of this
packet because their evaluation matrix is the Vandermonde matrix on
(-q,0,q). Hence the full moment tower is jointly faithful here.

Translation by (t) sends (e_r) to (e_{r+t}). For the generating
function

\[
M_v(z)=\sum_r c_r e^{rz},
\]

this transport acts by

\[
M_{T_tv}(z)=e^{tz}M_v(z).
\]

The multiplier is an entire unit, so translation transports the divisor but
cannot orient or remove it.

Therefore all of the following coexist with explicit off-axis zeros:

1. positive source coefficients;
2. positive translated carrier atoms;
3. augmentation as the scalar readout;
4. a complete finite logarithmic moment tower;
5. triangular translation laws for those moments;
6. divisor-preserving unit transport;
7. uniform strict log-concavity of the aggregated carrier.

## Consequence

Algebraic label recovery answers which packet produced the scalar. It does not
answer where the scalar may vanish. Prime transport and every finite
logarithmic moment are therefore observational or functorial data, not an
orientation law.

The only theta operation absent from this finite translation algebra is the
completed primal--dual Poisson correspondence. Its scalar functional equation
still merely transports the divisor. Any remaining RH force must therefore
occur before aggregation, through a primal--dual labelled coupling or boundary
mismatch current that the hostile packet cannot realize.

This also locates the scale of the missing effect. The finite moment tower is
complete on every finite packet, while the earlier boundaryless theorem killed
every algebraic separation jet. A surviving discriminator must be an
infinite-label completion incidence, not one more finite moment.

## Next falsifier

Construct the completed primal--dual correspondence directly on labelled
theta packets and apply the same construction to this hostile three-label
packet. If the hostile packet admits the correspondence with the same typed
boundary current, then labelled Poisson sewing still supplies no
zero-confinement force and this route closes.
