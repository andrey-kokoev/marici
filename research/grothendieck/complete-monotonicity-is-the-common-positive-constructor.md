# Complete monotonicity is the common positive constructor

## Question

Under the entire-kernel conformance identities, when do nonnegative heat jets and positive translate-Gram matrices become equivalent rather than merely mutually reconstructible values?

## Scalar heat source

Set

\[
H(t)=\mathcal K(t,0).
\]

The heat jets are

\[
J_k(t)=(-1)^kH^{(k)}(t).
\]

Therefore positivity of every heat jet is exactly complete monotonicity:

\[
J_k(t)\ge0
\quad\text{for every }k\ge0,
\ t>0.
\]

## Bernstein constructor

By Bernstein's theorem, complete monotonicity is equivalent to a positive measure `nu` on `[0,infinity)` such that

\[
H(t)=\int_0^\infty e^{-t\lambda}\,d\nu(\lambda).
\]

Lift `nu` symmetrically through `lambda=u^2`: split the mass at each positive `lambda` equally between `plus sqrt(lambda)` and `minus sqrt(lambda)`, with the origin fixed. Call the resulting positive symmetric measure `mu`.

Define

\[
\mathcal K_\mu(t,z)
=
\int_{\mathbb R}e^{-tu^2}e^{izu}\,d\mu(u).
\]

This kernel is positive definite in `z` for every `t>0`.

## Identification with the completed kernel

The heat equation and evenness give

\[
\partial_z^{2k}\mathcal K(t,0)=H^{(k)}(t),
\qquad
\partial_z^{2k+1}\mathcal K(t,0)=0.
\]

The same identities hold for `K_mu`. Since both are entire in `z`, equality of all Taylor coefficients yields

\[
\mathcal K(t,z)=\mathcal K_\mu(t,z).
\]

Thus every finite translate-Gram matrix of the completed source is PSD.

Conversely, if `K(t,-)` is the Gaussian smoothing of one positive symmetric measure for every width with the heat-semigroup compatibility, then

\[
J_k(t)=
\int u^{2k}e^{-tu^2}\,d\mu(u)
\ge0.
\]

## Exact equivalence

Under the established conformance hypotheses—entire even `K`, heat equation, and common source across widths—the following are equivalent:

1. all heat jets are nonnegative;
2. `H` is completely monotone;
3. one positive measure `nu` represents the squared spectral source;
4. one positive symmetric measure `mu` represents `K`;
5. every finite translate-Gram observer is PSD.

The common positive constructor is the Bernstein measure followed by the symmetric square-root lift.

## Residual interpretation

A negative heat jet is a direct failure of complete monotonicity. A negative Gram direction is the corresponding failure of positive definiteness. Meta-observer conformance ensures these are two manifestations of one source defect rather than independent inequalities.

## Boundary

Bernstein's theorem constructs a positive representing measure from the full infinite jet family. It does not prove the jet inequalities from the endpoint--gamma--prime formula. That remains the RH-strength arithmetic gate. No bounded derivative truncation can supply complete monotonicity.

## Disposition

The requested common source transformation is now explicit: complete monotonicity produces a positive squared-spectral measure, whose symmetric lift generates all heat jets, the entire character kernel, and every Gram matrix. The remaining proof target can be stated solely as complete monotonicity of the explicit source scalar `H(t)`.
