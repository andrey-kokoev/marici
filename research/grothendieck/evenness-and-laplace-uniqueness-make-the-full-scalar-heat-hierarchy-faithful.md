# Evenness and Laplace uniqueness make the full scalar heat hierarchy faithful

## Distinguish order zero from all orders

Pointwise positivity of the scalar slice

\[
\Theta(t,0)=\langle\rho,e^{-tu^2}\rangle
\]

is not faithful. Complete monotonicity for every order and every `t>0` is different.

Let `pi(u)=u^2` and let

\[
\eta=\pi_*\rho
\]

be the pushforward of the completed even spectral distribution to the nonnegative squared coordinate. Then

\[
\Theta(t,0)=\langle\eta,e^{-t\lambda}\rangle.
\]

## Bernstein and source identification

If `Theta(t,0)` is completely monotone, Bernstein's theorem gives a positive measure `mu` on the nonnegative line with the same Laplace transform:

\[
\Theta(t,0)=\int_0^\infty e^{-t\lambda}\,d\mu(\lambda).
\]

The Laplace transform is injective on distributions supported on the nonnegative line under the tempered growth present here. Therefore

\[
\eta=\mu
\]

as distributions. The positive Bernstein measure is not a fitted substitute; uniqueness identifies it with the source pushforward.

## Lift through the squared coordinate

Because `rho` is even, it is determined by `eta`. For any nonnegative compactly supported smooth test `phi`, replace it by its even part

\[
\phi_{\rm ev}(u)=\frac{\phi(u)+\phi(-u)}2\ge0.
\]

Every smooth even test has the form

\[
\phi_{\rm ev}(u)=\psi(u^2)
\]

for a smooth compactly supported function `psi` on the nonnegative half-line, with `psi>=0`. Hence

\[
\langle\rho,\phi\rangle
=
\langle\rho,\phi_{\rm ev}\rangle
=
\langle\eta,\psi\rangle
=
\langle\mu,\psi\rangle
\ge0.
\]

Thus `rho` is positive.

## Consequence

The complete scalar Laguerre hierarchy

\[
(-1)^k\partial_t^k\Theta(t,0)\ge0
\qquad(k\ge0,t>0)
\]

is already Weil-faithful when combined with source evenness and Laplace uniqueness. It implies every all-character Gram matrix. The earlier nonfaithfulness applies only to order-zero positivity or finitely many derivatives.

## Disposition

There are now two equivalent minimal contracts:

1. prove complete monotonicity of the explicit scalar endpoint--gamma--prime heat kernel for every order;
2. choose one Gaussian width and prove positive definiteness of its imaginary-character difference kernel.

Neither is weaker than RH. The scalar route trades spatial Gram rank for an infinite derivative hierarchy; the difference-kernel route trades derivative order for all finite matrix ranks.
