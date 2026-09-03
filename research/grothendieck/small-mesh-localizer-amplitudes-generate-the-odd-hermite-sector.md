# Small-mesh localizer amplitudes generate the odd Hermite sector

## Question

Is the explicit Gaussian-polynomial source image too restricted to confront the full nonlocal Weil obstruction?

## Scaled polynomial family

For integer `k>=0`, choose

\[
p_{h,k}(y)=h^{-k}(1-y)^k.
\]

The canonical localizer amplitude is

\[
G_{t,h,k}(u)
=e^{-tu^2/2}q_h(u)p_{h,k}(e^{-hu^2}),
\]

where

\[
q_h(u)=u\left(\frac{1-e^{-hu^2}}{u^2}\right)^{1/2}.
\]

As `h` tends to zero,

\[
\frac{q_h(u)}{\sqrt h}\longrightarrow u,
\qquad
h^{-1}(1-e^{-hu^2})\longrightarrow u^2.
\]

Therefore

\[
h^{-1/2}G_{t,h,k}(u)
\longrightarrow
u_{t,k}(u)=e^{-tu^2/2}u^{2k+1}.
\]

## Schwartz convergence

After differentiating any fixed number of times, the Taylor remainders are polynomial in `u` times `h` and a Gaussian with slightly weakened positive exponent. Multiplication by any Schwartz weight remains uniformly dominated for sufficiently small `h`. Hence the convergence holds in every real-line Schwartz seminorm.

The functions `u^(2k+1)e^(-tu^2/2)` span the odd polynomial--Gaussian sector. After a fixed dilation in `u`, triangular change of basis identifies this span with the odd Hermite functions. The Hermite expansion theorem therefore makes their finite span dense in the odd real-line Schwartz space.

## Consequence

The union of sampled localizer amplitudes over shrinking mesh is not a small finite-feature family. Its real-line Schwartz closure contains the entire odd Hermite sector. This agrees with the no-finite-recurrence result: a surviving source factor must be infinite-dimensional.

It also blocks an explanation that relies on the tests being too smooth or too sparse to see prime singularities. Their closure has arbitrary odd Schwartz resolution on the real spectral axis.

## Topology boundary

Real-line Schwartz density is not automatically a form-core theorem for the completed Weil form. Endpoint evaluation at complex arguments and other analytic continuation terms need a stronger graph topology. Convergence in Schwartz seminorms on the real axis does not control those evaluations.

Thus the result proves source-image richness but does not promote positivity from the sampled family to every classical Weil test.

## Relation to RH detection

Independent generic-mesh pole rigidity already shows the sampled family detects off-line zeros without requiring a full form-core theorem. Oddness does not erase nontrivial zero parameters because those spectral points are nonzero. A direct equivalence with the complete odd Weil criterion still requires the analytic test-space normalization.

## Disposition

Treat the sampled source image as an infinite-dimensional odd Gaussian core candidate, not a narrow loophole. The next functional-analytic gate is continuity of endpoint, gamma, and prime terms in one analytic Hermite graph topology.