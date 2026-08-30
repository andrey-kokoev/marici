# The central concavity certificate has two remaining correlated remainders

The high-precision central scan uses the Euler transform for `eta(s)`, its
differentiated transform for `eta'(s)`, and the positive-real asymptotic
expansion for `digamma(s/2)` after recurrence.

For positive real `s`, the Euler-transformed eta-value terms satisfy

\[
 0\le\frac{\Delta^k(n^{-s})|_{n=1}}{2^{k+1}}\le2^{-k-1}.
\]

Hence truncation after depth `N` has remainder at most `2^-N`. At `N=120`
this is about `7.52e-37`. Even after a deliberately pessimistic amplification
combining `t=10^-8`, the central `1/sqrt(t)` factor, and the derivative stencil,
its budget is about `1.13e-21`, below the revised `3.4e-20` chord margin.

Recurrence originally moved the digamma argument to at least `20`. On the positive real
axis its Bernoulli asymptotic remainder is bounded by the first omitted term.
After retaining through `B_16`, the `B_18` value bound there is about
`1.16e-23`. Raising the recurrence target to `100` reduces it by `5^18`, to
about `3.05e-36`. Even independent propagation through the hostile boundary
stencil is then below the observed chord margin, so no delicate correlation
argument is needed.

The analytic transform truncations are therefore small enough. What remains is
implementation-level certification: outward-rounded propagation through the
complete nonlinear expression and a rigorous finite-difference truncation
bound. Until those are supplied, this is not an interval certificate and RH
remains unproved.

Finite differences have now been removed: analytic differentiation carries
`eta,eta',eta''` and `digamma,trigamma` through the exact source. A second
Laplace-tail split bounds the new eta-double-prime tail below `1.63e-37`.
Accordingly, only outward-rounded nonlinear propagation remains for the 21
finite chords. See `central-analytic-slope-and-eta-second-tail.md`.

The first item is now closed. A Laplace-integral split proves the uniform bound
`|d_k'(s)|<=3/k+1/k^2` on `1/2<=s<=3/5`, hence the depth-120 eta-prime tail is
below `1.90e-38`. See `eta-derivative-euler-tail-bound.md`. Together with the
recurrence-to-80 digamma budget, this closes the analytic transform tails.

## Durable verification

- Checker: `checkers/central_concavity_certification_error_budget.py`
- Result: `results/central-concavity-certification-error-budget.json`
