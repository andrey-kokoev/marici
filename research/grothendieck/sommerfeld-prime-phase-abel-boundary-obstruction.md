# The Sommerfeld prime phase has an Abel-boundary obstruction

For `Re(s)=sigma>1`, the Euler product gives the honest source phase

\[
 \Phi_\sigma(T)=\Im\log\zeta(\sigma+iT)
 =-\sum_{p}\sum_{m\ge1}\frac{p^{-m\sigma}}m
   \sin(mT\log p).
\]

The quantization line is `sigma=1/2`, outside absolute convergence. Therefore
the phrase “primes supply the boundary phase” is not yet a construction. It
requires a canonical Abel/analytic-continuation boundary value

\[
 \Phi_{1/2}(T)=\lim_{\sigma\downarrow1/2}\Phi_\sigma(T)
\]

with specified approach, branch jumps, and behavior at zeros. Raw cutoff sums
cannot provide that authority.

A dependency-free diagnostic at generic height `T=14` shows the expected
contrast: prime-power cutoff phases are comparatively controlled in the
absolute half-plane and remain strongly cutoff-sensitive once pushed through
`sigma=1`. This is illustrative rather than a convergence proof.

## Consequence for quantization

The smooth Sommerfeld action is source-derived from the gamma factor through
Riemann--Siegel theta and Stirling asymptotics. The fluctuating correction is
not source-derived until the Euler phase crosses this Abel boundary without
using zero locations. Any proposed quantization rule that simply inserts
`arg zeta(1/2+iT)` has restated the spectral problem rather than explained it.

The next viable route is to use the already regularized explicit-formula heat
or resolvent kernel to define the phase indirectly, then prove that its
boundary value agrees with the Jacobi Weyl function and has a self-adjoint
boundary condition. This keeps the pole-cancellation cone and prime smoothing
inside the construction.

## Sharp falsifier

If two admissible source regularizations give inequivalent boundary phases
beyond integer multiples of `pi`, there is no canonical Sommerfeld condition.

## Scope

This is a no-go for the raw Euler phase, not for analytic continuation or a
regularized source phase. It proves neither self-adjointness nor RH.

## Durable verification

- Checker: `checkers/euler_prime_phase_boundary_obstruction.py`
- Result: `results/euler-prime-phase-boundary-obstruction.json`
