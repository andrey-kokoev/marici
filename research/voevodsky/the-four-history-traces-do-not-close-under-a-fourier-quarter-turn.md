# The four history traces do not close under a Fourier quarter turn

## Question

Is the retained Volterra history port \((P,Q,M_a,J_a)\) the direct Fourier transport of the endpoint-moment four-port?

## Claim boundary

No, already at seam \(a=0\). Fourier transport of the half-line history value introduces a principal-value Hilbert functional not determined by the four retained traces. Thus the history four-port is closed under reciprocal half-turn but not under the actual quarter turn without an additional nonlocal channel.

## History traces

For causal Volterra history

$$
(Hg)(u)=\int_{-\infty}^u g(v)\,dv,
$$

the seam-zero traces are

$$
P(Hg)=0,
\qquad
Q(Hg)=\int_{\mathbb R}g,
$$

$$
M_0(Hg)=\int_{-\infty}^0g(v)\,dv,
\qquad
J_0(Hg)=g(0).
$$

The total mass and seam flux coincide with two endpoint-moment source functionals, but the half-line primitive is different from the first moment.

## Fourier image of the half-line primitive

For the convention

$$
\widehat g(y)=\int g(x)e^{-2\pi ixy}\,dx,
$$

the distribution identity

$$
\int_{-\infty}^0 e^{-2\pi ixy}\,dy
=
\frac12\delta_0(x)
-
\frac1{2\pi i}\operatorname{pv}\frac1x
$$

gives

$$
M_0(H\widehat g)
=
\int_{-\infty}^0\widehat g(y)\,dy
=
\frac12g(0)
-
\frac1{2\pi i}
\operatorname{pv}\int_{\mathbb R}\frac{g(x)}x\,dx.
$$

The new functional

$$
\mathcal H_0(g)
=
\operatorname{pv}\int\frac{g(x)}x\,dx
$$

is nonlocal and is not determined by

$$
\left(
\int g,
\int_{-\infty}^0g,
g(0),
g'(0)
\right).
$$

One may vary a Schwartz function away from the seam while keeping those four quantities fixed and change \(\mathcal H_0(g)\).

## Consequence

No four-by-four matrix \(T\) can satisfy

$$
\Gamma_{\rm hist}(H\widehat g)
=T\Gamma_{\rm hist}(Hg)
$$

for all Schwartz \(g\), where \(\Gamma_{\rm hist}=(P,Q,M_0,J_0)\). The quarter-turn image leaves the retained finite trace span.

Reflection does preserve the corresponding endpoint/seam data up to channel exchange and flux sign, explaining why the previously proved half-turn square remains valid.

## Required enlargement

A quarter-turn-stable trace presentation must retain at least the principal-value Hilbert channel \(\mathcal H_0\), and then close its full Fourier orbit before completion. Equivalently, retain the complete response function rather than only four scalar history traces.

## Disposition

The retained four history traces are not the Fourier endpoint-moment port and do not form a quarter-turn representation. This is the first precise analytic obstruction to extending the new radial-to-spectral mixed square directly to the old scalar \(V_4\). The correct fourth presentation must be Fourier-saturated by nonlocal response channels.