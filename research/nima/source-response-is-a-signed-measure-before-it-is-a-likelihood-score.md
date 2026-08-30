# Source response is a signed measure before it is a likelihood score

## Claim boundary

For an amplitude affine in a source parameter, symmetric event-weight differences recover the exact derivative of the unnormalized event measure. A likelihood-ratio score is a later representation that requires domination by the central measure. It can fail at support zeros even though the underlying event-measure family remains regular and neighboring support enters at second order.

This is a source-level and finite-event theorem. It does not supply shower, detector, exposure, covariance, or publication authority.

## Affine amplitude

Let the event amplitude at phase-space point \(x\) be

\[
\mathcal A_\theta(x)=a(x)+\theta b(x).
\]

The unnormalized event weight is

\[
w_\theta(x)=|\mathcal A_\theta(x)|^2.
\]

It is quadratic in \(\theta\), and its derivative is

\[
\partial_\theta w_\theta(x)
=2\operatorname{Re}\!\left(\overline{\mathcal A_\theta(x)}b(x)\right).
\]

For every nonzero step \(h\), the symmetric difference is exact:

\[
\frac{w_{\theta+h}(x)-w_{\theta-h}(x)}{2h}
=\partial_\theta w_\theta(x).
\]

No small-step limit is needed because the weight is quadratic.

## Measure derivative

Let \(\mu_\theta\) be the unnormalized event measure

\[
d\mu_\theta(x)=w_\theta(x)\,d\Phi(x),
\]

where \(d\Phi\) is the declared phase-space carrier. Its source derivative is the signed measure

\[
d\dot\mu_\theta(x)=\partial_\theta w_\theta(x)\,d\Phi(x).
\]

This object remains defined without dividing by the central weight.

## Likelihood score and its domain

The pointwise likelihood score is

\[
s_\theta(x)=\partial_\theta\log w_\theta(x)
=\frac{\partial_\theta w_\theta(x)}{w_\theta(x)}.
\]

It exists only where \(w_\theta(x)>0\). Writing

\[
d\dot\mu_\theta=s_\theta\,d\mu_\theta
\]

therefore requires the derivative measure to be absolutely continuous with respect to the central measure.

The score representation is not the source response itself. It is one Radon–Nikodym coordinate for that response on an admitted domination domain.

## Smallest support falsifier

Take the real amplitude

\[
\mathcal A_\theta=1-\theta.
\]

At \(\theta=1\),

\[
w_1=0,
\qquad
w_{1+h}=h^2,
\qquad
w_{1-h}=h^2.
\]

The first derivative is zero there, while every nonzero neighboring weight is positive. Ratios to the central weight are undefined despite the event-weight family being perfectly regular.

More generally, a support point can enter at second order. A first-order score at the zero-weight center cannot describe that source response.

This falsifies any compiler that treats central reweight ratios as universally equivalent to the local source family. At the support zero, the first derivative vanishes and the nontrivial information is second-order.

## Support-safe dominating experiment

Choose a positive proposal measure \(\nu\) that dominates every admitted source measure in a declared neighborhood. One finite construction is the symmetric mixture

\[
\nu=\mu_{\theta-h}+\mu_\theta+\mu_{\theta+h}.
\]

Then the three weights have densities \(r_-,r_0,r_+\) with respect to \(\nu\), and the derivative density is

\[
\dot r_\theta=\frac{r_+-r_-}{2h}.
\]

For affine amplitudes this represents the exact signed-measure derivative on the union of the three supports. It never divides by \(r_0\).

The proposal construction must itself be source-authorized. A fitted support cover chosen after inspecting failures would not carry response authority.

## Normalization and null outcomes

Normalizing selected events introduces a quotient by the total rate. It removes the common-rate direction unless exposure or completed-trial information is retained as an independent port.

Accordingly, a complete response instrument must distinguish:

1. the unnormalized signed-measure derivative;
2. the selected-event shape score;
3. the total-rate response;
4. the null or unselected outcome;
5. the calibrated exposure reference.

Deleting the last three can turn a rank-two source response into a rank-one shape readout even when both source derivatives remain nonzero.

## Constructor gate

A reweight-based source-response constructor must declare:

- the amplitude parameter map;
- the common phase-space carrier;
- a source-authorized dominating proposal;
- support coverage across the admitted neighborhood;
- whether it returns an unnormalized derivative or a normalized score;
- rate, exposure, and null-outcome ports;
- detector and nuisance transport;
- the smallest support-zero falsifier.

The durable distinction is:

> Differentiability of the source measure does not imply existence of a likelihood-ratio score in the central measure. Support authority precedes score authority.
