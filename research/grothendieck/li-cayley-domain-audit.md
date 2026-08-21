# Conditional Cayley-domain audit: dense operator, inadmissible cyclic vector

## Setup

In the conditional critical-line model, an ordinate `gamma` has phase

`u_gamma=1-1/(1/2+i gamma)`

and increment-measure weight

`w_gamma=|1-u_gamma|^2=1/(gamma^2+1/4)`

per divisor copy. The Cayley coordinate is `h(u_gamma)=gamma`.

## Domain theorem

On `L^2(mu)`, multiplication by the real measurable function

`h(u)=(1+u)/[2i(1-u)]`

is self-adjoint on its maximal domain

`Dom(H)={f: integral |h|^2 |f|^2 dmu < infinity}`.

If `mu` has no atom at `u=1`, finite-support spectral functions lie in this
domain and are dense. Thus accumulation of phases at `1` does not itself
destroy self-adjointness.

## The cyclic vector is not in the domain

For the constant GNS vector `1`, the domain sum is

`sum_gamma gamma^2/(gamma^2+1/4)`

with divisor multiplicities. Each summand tends to one. For an infinite
unbounded divisor this sum diverges, so the cyclic vector is not in
`Dom(H)`.

This is not a contradiction: the bounded unitary `U` acts on the cyclic
vector, while its unbounded Cayley transform need not. Li energies use
bounded phase polynomials and remain defined.

## Resolvent and compactness gate

In a discrete atomic realization with ordinates escaping to infinity, the
resolvent multiplier `(gamma-z)^(-1)` tends to zero. The Cayley operator then
has compact resolvent provided the amplified eigenspaces have finite
multiplicity and there is no finite accumulation of ordinates. These are
spectral-identification assumptions, not consequences of scalar positivity
alone.

## Prohibitions established by the audit

- Do not apply `H` or powers of `H` to the GNS cyclic vector without a
  separate domain proof.
- Do not treat the phase `1` as an ordinary eigenvalue.
- Do not infer compact resolvent from moment positivity alone.
- Do not infer divisor multiplicities from scalar atomic weights.

The correct order is: source positivity, GNS unitary, measure identification,
maximal Cayley domain, multiplicity amplification, then compact-resolvent
claims.
