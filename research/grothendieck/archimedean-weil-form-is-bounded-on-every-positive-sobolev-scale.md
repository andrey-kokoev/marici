# The archimedean Weil form is bounded on every positive Sobolev scale

## Question

Which Sobolev order completes the fixed-support Weil form without assuming positivity?

## Archimedean multiplier

On the reciprocal Mellin core, the gamma contribution has the bilinear spectral form

`Gamma(f,g)=1/(4pi) integral_R fhat(u) conjugate(ghat(u)) Re psi(1/4+iu/2) du`

plus the constant `-log(pi)` multiplier already absorbed into the same estimate.

For fixed real part `1/4`, the standard digamma estimate is

`|Re psi(1/4+iu/2)| <= C_0 + C_1 log(1+|u|)`.

This estimate follows from the recurrence/asymptotic expansion of `psi` on the right half-plane and is independent of RH.

## Sobolev domination

For every `s>0`, put `alpha=min(2s,1)`. The elementary inequality

`log(1+x) <= x^alpha/alpha`

for `x>=0` gives

`1+log(1+|u|) <= C_s (1+u^2)^s`.

Therefore weighted Cauchy--Schwarz yields

`|Gamma(f,g)| <= C_s' ||f||_(H^s) ||g||_(H^s)`.

The same statement holds for every positive Sobolev order, however small.

## Failure at order zero

The multiplier `Re psi(1/4+iu/2)` grows like `log|u|`. Multiplication by it is not bounded on unweighted `L^2`: choose Fourier-normalized functions supported in unit intervals centered at frequencies tending to infinity. Their `L^2` norms remain one while the absolute multiplier expectation diverges logarithmically.

Thus the direct multiplier argument has the sharp threshold

`s>0`,

not `s=0`.

## Completed local operator

For fixed logarithmic support `[-L,L]`:

- the endpoint term is `L^2` bounded by compact exponential weights;
- the prime-power term is a finite sum and is `L^2` bounded by convolution Cauchy--Schwarz;
- the archimedean term is `H^s` bounded for every `s>0`.

Hence the complete source-side Weil form extends continuously to `H_0^s((-L,L))` for every `s>0`. Relative to its ordinary positive Sobolev inner product, Riesz representation produces a bounded self-adjoint operator `A_(L,s)`.

This construction is unconditional at the level of form boundedness. It uses the explicit formula and digamma growth, not a positive zeta spectral measure.

## Compatibility and positivity gates

Different `s>0` produce different representing operators but the same form on the common smooth core. Nested support windows also agree on their shared core. To identify their completed quotients, one still needs closability/compatibility statements for the chosen embeddings; boundedness supplies these locally but not a global inductive Hilbert norm.

RH-bearing positivity remains

`A_(L,s)>=0 for every L`,

and is independent of the choice of positive `s` because all choices restrict to the same dense test core.

## Consequence

The common-domain blocker identified by Voevodsky can be resolved locally without RH. The remaining barrier is no longer existence of a completed form but positivity of the resulting bounded operators and coherent passage over increasing support.

## Disposition

Local Sobolev completion is established qualitatively for every `s>0`; `L^2` boundedness is rejected. A publication-grade version should record a numerical digamma constant, Fourier normalization, and the exact endpoint and prime coefficient constants.
