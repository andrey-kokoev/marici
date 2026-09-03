# The Weil Gaussian threshold runs backward against the heat maximum principle

## Exact reparameterization

The spectral Gaussian

\[
G_t(y)=e^{-ty^2}
\]

satisfies

\[
\partial_tG_t
=-\frac{1}{4t^2}\partial_y^2G_t-rac{1}{2t}G_t.
\]

For the completed translated Weil kernel, define

\[
\tau=\frac1{4t},
\qquad
U(\tau,\xi)=\sqrt t\,\Theta(t,\xi).
\]

Then

\[
\partial_\tau U=\partial_\xi^2U.
\]

Thus increasing `tau` is forward heat smoothing, while increasing `t` moves backward in heat parameter and sharpens the Gaussian probe.

## Consequence for broad smoothing

The established broad positivity regime is small `t`, equivalently large `tau`. The heat maximum principle propagates positivity toward larger `tau`, hence toward still smaller `t`. It gives no propagation from the broad regime toward the narrow probes reached as `t` increases.

At a first contact reached by increasing `t`,

\[
\Theta=0,
\qquad
\partial_\xi\Theta=0,
\qquad
\partial_\xi^2\Theta\ge0.
\]

The exact equation gives

\[
\partial_t\Theta
=-\frac{1}{4t^2}\partial_\xi^2\Theta\le0
\]

at that contact. This sign is compatible with crossing from positive to negative. The parabolic maximum principle therefore does not exclude the first double contact; it predicts its admissible orientation.

## Required new input

A contact-exclusion proof must spend arithmetic information absent from the heat equation, such as a lower bound coupling the endpoint and gamma channels against the oscillatory von Mangoldt term at the contact equations. Semigroup positivity and broad initial positivity alone are insufficient because the desired direction is backward heat flow.

## Disposition

Reject any argument that propagates small-`t` positivity to all `t` by the forward heat maximum principle. Retain broad positivity as existence of a finite threshold and use the contact equations as the frontier. The next source inequality must control curvature or prime-character amplitude at a putative contact.
