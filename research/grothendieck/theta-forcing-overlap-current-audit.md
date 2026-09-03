# Audit of a current primitive for the theta forcing overlap

## Decision

The source derives partial current primitives, but none differentiates to the
complete antisymmetric forcing overlap without leaving a new mixed bulk term.
The forcing-overlap conservation law remains open.

## Exact unresolved density

For the centered doubled tails, the source identity is

`2 a N = -J' - 2 Fcal`,

where

`Fcal=Re(f_+ c_+ conjugate(G_+) - f_- c_- conjugate(G_-))`.

A confinement proof would require `2 Fcal=J_boundary'` for a current assembled
before zero restriction from all retained channels.

## Available primitives

### Continuous forcing reservoir

The seam--reservoir--Green compiler constructs

`J_f(q)=2 integral_q^infinity |f(v)|^2 dv`, so `J_f'=-2|f|^2`.

This exactly closes the continuous forcing-norm line exposed by the doubled
Clark--Green operation, and its construction is completion-stable under `L2`
cutoffs. It does not close the bilinear antisymmetric overlap `Re<f,Q>` and has
no primitive, square, or archimedean incidence capability.

### Primitive seam antiderivative

With `H'=F`, the local current

`J_H=2 sqrt(2) Re(H conjugate(d))`

cancels the explicit term `2 sqrt(2) Re(F conjugate(d))`. Differentiating it
also creates

`R_mix=-2 sqrt(2) delta Re(H conjugate(m))`
`      +2 sqrt(2) Re(i tau H conjugate(d))`.

This is generically nonzero both off the seam and on it. Primitive retention
therefore transports the obstruction into a mixed seam--bulk polarization; it
does not produce a conservation law.

## Source-authority boundary

Defining an integral of the already evaluated overlap would formally create an
antiderivative but would only rename the obstruction and would depend on the
response. The approved construction requires incidence from independent
source channels. Similarly, a moving adjoint covector solved backward from the
completed theta solution is tautological rather than source-derived.

No reviewed packet supplies square, Clark-shear, and archimedean currents whose
combined derivative is `-R_mix`, nor a cutoff-complete current packet proving
that cancellation. Thus `Re<f,Q>` has no authorized complete current primitive.

## First remaining finite test

Assemble the independently defined prime-square, Clark-shear, and
archimedean/modular boundary currents in the centered `(m,d,H)` frame and
compare their derivative coefficients against the two monomials
`delta Re(H conjugate(m))` and `Re(i tau H conjugate(d))`. Any surviving
coefficient is a decisive finite obstruction; scalar cancellation after
integration is insufficient.
