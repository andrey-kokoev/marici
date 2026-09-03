# The source heat candidate exists but its zero character is not faithful

## Correction to the remaining-object statement

The source-derived heat candidate is already materialized by the centered explicit formula. For `t>0` and real character `xi`,

\[
\Theta(t,\xi)=K_{\rm endpoint}(t,\xi)+K_\Gamma(t,\xi)+K_{\mathbb P}(t,\xi),
\]

with the endpoint, digamma, and von Mangoldt terms recorded in `explicit-two-variable-weil-heat-source-formula.md`. No zero list is needed to define this function.

What is missing is not construction of a candidate measure but proof that this source distribution is positive.

## Why the scalar heat trace is insufficient

The slice

\[
\Theta(t,0)
\]

forgets translation characters. Positivity or complete monotonicity of this scalar slice does not by itself prove that the underlying Weil distribution is positive, because a signed distribution can have positive values on one centered Gaussian family.

The faithful test retains every translate:

\[
\Theta(t,\xi)\ge0
\qquad(t>0,\ \xi\in\mathbb R).
\]

Under RH this is the Gaussian mixture over real zero ordinates. Conversely, positivity for all widths and translates recovers positivity of the Weil distribution by Gaussian approximation and hence implies RH.

Thus the angular Bernstein measure and scalar Xi heat trace are useful projections, but the two-variable translated Gaussian family is the source-faithful positivity object.

## Existing partial theorem

Sufficiently broad Gaussian smoothing is uniformly positive: there exists `t0>0` such that

\[
\Theta(t,\xi)>0
\qquad(0<t<t_0,\ \xi\in\mathbb R).
\]

If global positivity fails, its first loss occurs at a finite double contact

\[
\Theta(t_*,\xi_*)=0,
\qquad
\partial_\xi\Theta(t_*,\xi_*)=0.
\]

Therefore the source problem is already an explicit zero-contact exclusion theorem for the completed endpoint--gamma--prime kernel.

## Disposition

Replace “construct a positive heat candidate” by “prove positivity of the existing two-variable explicit-formula kernel.” Do not infer distributional positivity from the zero-character Bernstein projection. The exact remaining falsifier is a finite pair `(t,xi)` with negative completed kernel, and the exact proof target is exclusion of every finite first double contact.
