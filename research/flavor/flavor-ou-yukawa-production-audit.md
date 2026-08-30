# Equivariant Ornstein–Uhlenbeck production of the Gaussian Yukawa law (WP121)

Owner: `marici.Figueiredo`.

## Candidate dynamics

Promote the two complex `3 x 3` Yukawa matrices to dynamical matrix variables.
For each of their 36 real coordinates impose the isotropic Langevin equation

\[
dX_t=-\kappa X_t,dt+\sqrt{2D}\,dW_t,
\qquad \kappa,D>0.
\]

Equivalently, the joint density obeys

\[
\partial_t\rho
=D\Delta\rho+\kappa\nabla\!\cdot(X\rho).
\]

Its unique normalized stationary law is

\[
\rho_*(Y_u,Y_d)=
\left(\frac{\beta}{\pi}\right)^{18}
e^{-\beta(\|Y_u\|_F^2+\|Y_d\|_F^2)},
\qquad
\beta=\frac{\kappa}{2D}.
\]

Thus WP120's Gaussian measure is no longer an unexplained mathematical choice
*conditional on this stochastic dynamics*: its shape and scale ratio follow
from drift and diffusion.

## Exact finite-time law

For one real coordinate,

\[
\mathbb E[X_t]=e^{-\kappa t}\mathbb E[X_0],
\]

and

\[
\operatorname{Var}(X_t)
=e^{-2\kappa t}\operatorname{Var}(X_0)
+\frac{D}{\kappa}(1-e^{-2\kappa t}).
\]

The stationary variance is `D/kappa=1/(2 beta)`. The affine variance map
composes exactly under time concatenation, and the convergence rate is set by
the OU spectral gap `kappa`. Consequently a finite preparation claim can use
an explicit mixing-time budget instead of pretending stationarity is reached
instantaneously.

## Weak-basis and stacky descent

The full weak-basis action is orthogonal on the 36 real matrix coordinates.
Both drift `-kappa X` and covariance `2D I` are equivariant. Therefore the
Markov semigroup commutes with the weak-basis action and pushes to a Markov
semigroup on the quotient.

Nontrivial stabilizers at degenerate matrices are authorized gauge isotropy,
not physical ambiguity. The descent is stacky: stabilizer orbits are explicitly
quotiented, and the quotient ambiguity is zero. An anisotropic diffusion tied
to a matrix entry or texture chart fails this test.

## What has and has not been derived

Derived conditionally:

- the normalized Gaussian measure class;
- `beta=kappa/(2D)`;
- uniqueness and finite-time convergence;
- weak-basis-equivariant stochastic transport;
- the WP120 Wishart/Haar `physical16` pushforward.

Not derived:

- why Yukawa couplings are dynamical stochastic variables rather than fixed
  theory parameters;
- the microscopic bath or coarse-graining that produces white isotropic noise;
- fluctuation–dissipation data fixing `kappa/D` and the UV scale;
- compatibility of this bath with gauge, locality, unitarity, and cosmological
  history;
- the RG/matching map from the stochastic UV slice to measured quark flavor.

The OU equation is therefore a **conditional production model**, not yet an
independently validated physical source. It moves the first unexplained arrow
upstream—from “why this probability density?” to “why this dynamical substrate
and bath?”—but it does not remove it.

## Hostile controls

1. **Target thermostat:** choosing `kappa/D` from observed masses is the same
   scale fitting in dynamical language.
2. **Chart bath:** unequal coordinate diffusivities break weak-basis descent.
3. **False equilibrium:** a finite-duration process must carry its residual
   distance to stationarity.
4. **Bath deletion:** removing the noise while retaining the Gaussian measure
   is descendant leakage, not a counterfactual source restriction.
5. **RG reset:** re-Gaussianizing after nonlinear RG flow introduces a new
   thermostat and requires fresh source authority.

## Disposition

`Gaussian measure dynamically derived conditional on an unvalidated OU bath`.

The next decisive question is whether any admitted local quantum or thermal
field theory yields this matrix OU generator—or a controlled deformation of
it—without using flavor readouts to fix its drift, diffusion, or scale.
