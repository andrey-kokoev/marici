# A route swap would force the primitive v_alg covector

## Question

Once an integral comparison identifies site exchange with swapping the two anchored route generators, what freedom remains in the rank-one complementary readout?

## Claim boundary

This is a conditional uniqueness theorem. The required integral action on the fixed pencil remains unconstructed, as recorded in `erratum_site_exchange_does_not_yet_identify_v_alg_inside_one_split_fiber_pencil.md`.

## Equivariance equation

Let

\[
E=\mathbb Z\langle\beta_{12},\beta_{13}\rangle
\]

and suppose the transported site exchange acts by

\[
S(\beta_{12})=\beta_{13},
\qquad
S(\beta_{13})=\beta_{12}.
\]

Let the complementary readout be

\[
q=(a,b):E\longrightarrow\mathbb Z\langle v_{\rm alg}\rangle.
\]

Since \(v_{\rm alg}\) is exchange-odd, equivariance requires

\[
qS=-q.
\]

This gives

\[
(b,a)=(-a,-b),
\]

hence

\[
b=-a.
\]

Therefore every equivariant readout has the form

\[
q=a(1,-1).
\]

Its image is primitive exactly when \(|a|=1\). Under the primitive-image condition, the only possibilities are

\[
q=\pm(1,-1).
\]

The sign is the remaining orientation convention.

## Forced route kernel

For either primitive orientation,

\[
K_{\rm route}
=
\mathbb Z\langle\beta_{12}+\beta_{13}\rangle.
\]

Thus site-exchange equivariance would force the physical quotient to retain the route difference and kill the route sum.

There is an integral subtlety. The exchange-odd eigenvector

\[
\beta_{12}-\beta_{13}
\]

maps to \(\pm2v_{\rm alg}\), not to a primitive unit. Primitivity of the quotient comes from either individual route generator mapping to \(\pm1\), while their difference records twice that unit. One must not divide the odd eigenvector by two unless its divisibility is separately established in the ambient lattice.

## Role in the information flow

Conditional on the missing fixed-pencil action, the four-vertex flow is forced to take the antisymmetric coequalizer

\[
\mathbb Z\langle\beta_{12},\beta_{13}\rangle
\big/
\mathbb Z\langle\beta_{12}+\beta_{13}\rangle
\longrightarrow
\mathbb Z\langle v_{\rm alg}\rangle.
\]

The symmetric route combination belongs to the physically null kernel; the antisymmetric route class survives, with orientation fixed by one period calculation.

## Disposition

The remaining freedom is not an arbitrary pair \((a,b)\) once route-swap equivariance is proved. It collapses to one sign. The exact next acceptance test is therefore: construct the integral fixed-pencil swap, verify that it exchanges \(\beta_{12},\beta_{13}\), and compute one route period to be a unit.

Verification:

- `research/voevodsky/checkers/check_conditional_route_swap_v_alg_covector.py`
- `research/voevodsky/results/conditional_route_swap_v_alg_covector.json`
